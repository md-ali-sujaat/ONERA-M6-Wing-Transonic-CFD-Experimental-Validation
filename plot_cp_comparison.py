#!/usr/bin/env python3
"""Generate Cp validation plots from externally supplied machine-readable data.

This is a plotting utility only. It does not contain CFD or experimental samples.
CSV header: mach,station,dataset,x_c,cp
Usage: python scripts/plot_cp_comparison.py data/curves.csv --out figures/recomputed
"""
import argparse
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('csv',type=Path)
    p.add_argument('--out',type=Path,default=Path('figures/recomputed'))
    args=p.parse_args()
    df=pd.read_csv(args.csv)
    expected={'mach','station','dataset','x_c','cp'}
    missing=expected-set(df.columns)
    if missing: p.error('Missing columns: '+', '.join(sorted(missing)))
    args.out.mkdir(parents=True,exist_ok=True)
    for (mach,station), grp in df.groupby(['mach','station'],sort=True):
        fig,ax=plt.subplots(figsize=(8,5),layout='constrained')
        for label,subset in grp.groupby('dataset',sort=True):
            subset=subset.sort_values('x_c')
            if 'experiment' in str(label).lower():
                ax.scatter(subset.x_c,subset.cp,s=13,label=label,zorder=3)
            else:
                ax.plot(subset.x_c,subset.cp,label=label,linewidth=1.7)
        ax.invert_yaxis() # aerodynamic convention
        ax.set(xlabel='x/c',ylabel=r'$C_p$',title=f'ONERA M6 — Mach {mach:g}, station {station}')
        ax.legend(fontsize=8,frameon=False)
        ax.grid(alpha=0.25)
        file=args.out/f'cp_m{float(mach):.2f}_station{station}.png'
        fig.savefig(file,dpi=180)
        plt.close(fig)
        print(file)

if __name__=='__main__': main()
