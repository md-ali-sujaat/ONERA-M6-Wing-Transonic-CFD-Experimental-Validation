# Data availability and figure provenance

The project presentation contains plotted CFD/experimental comparisons, but the uploaded sources do **not** include digitized curve points, export CSV files, or ANSYS Fluent case/data files. The figures in ../figures were extracted directly from the source PowerPoint.

To reproduce the line plots quantitatively, acquire original simulation surface-pressure exports and corresponding reference measurements. NASA maintains the Schmitt and Charpin (1979) reference Cp data at: https://www.grc.nasa.gov/www/wind/valid/m6wing/m6wing.html

For the optional plotting script, a normalized CSV must contain these columns:

`mach,station,dataset,x_c,cp`

Where:
- `mach` is numeric (for example 0.84 or 0.88)
- `station` is an integer station index (for example 1, 3, 6)
- `dataset` is a descriptive series label such as `Experiment`, `Hybrid + SST`, or `Hexahedral + SA`
- `x_c` is chord-normalized streamwise position in [0,1]
- `cp` is nondimensional surface pressure coefficient

Do not assemble upper and lower surface points into a single sorted curve without separating surfaces; distinguish the branches with a separate dataset label when exporting data. Do not infer numeric error bars from figure screenshots.
