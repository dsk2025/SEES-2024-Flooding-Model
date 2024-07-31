2024 SEES Flood Model

This project is designed to provide a way to predict areas at high risk of flooding under an OpenScience framework.

The program uses elevation data from .csv, .tif, and .dem files. It interprets this data as a raster then applies a D8 flow analysis on the entire raster.
D8 flow is explained here: https://pro.arcgis.com/en/pro-app/latest/tool-reference/raster-analysis/flow-direction.htm

After applying the D8 raster analysis, the program runs a "flow_accumulation" function that determines, at each point, the amount of other cells that flow into that point.

This reveals specific points in a given topographical area that will accumulate water from the most unique sources from within the raster.

Although other D8 and flow accumulation plugins or instruments already exist such as the linked one from ArcGIS, the advantage of this project is that the code is completely open-source and easily adjustable.  It improves clarity as to how a D8 function is applied on an elevation raster and the methods used to predict areas of high flow accumulation.

Replication of Houston AOIs

1. Download the given notebook "SEES_Flood_Traker.ipynb" in Colab
2. Download the TIFs in the "DEM Data" folder and save them to Google Drive
3. Scroll down to the "main" function in Colab
4. Replace the line tif_file = '...' with tif_file = '(directory of one of the Houston TIFs)'
5. Run all

For other elevation datasets, save them to Google Drive and replace the tif_file line with tif_file = '(your other elevation file directory)'

