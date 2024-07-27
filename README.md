This project is designed to provide a way to predict areas at high risk of flooding under an OpenScience framework.

The program uses elevation data from .csv, .tif, and .dem files. It interprets this data as a raster then applies a D8 flow analysis on the entire raster.
D8 flow is explained here: https://pro.arcgis.com/en/pro-app/latest/tool-reference/raster-analysis/flow-direction.htm

After applying the D8 raster analysis, the program runs a "flow_accumulation" function that determines, at each point, the amount of other cells that flow into that point.

This reveals specific points in a given topographical area that will accumulate water from the most unique sources from within the raster.

Although other D8 and flow accumulation plugins or instruments already exist such as the linked one from ArcGIS, the advantage of this project is that the code is completely open-source and easily adjustable.  It improves clarity as to how a D8 function is applied on an elevation raster and the methods used to predict areas of high flow accumulation.

Furthermore, this source can take any elevation data from around the world. Anyone concerned with flooding in their community can run this program over the area of interest (AOI) and be informed as to where it will flood.
