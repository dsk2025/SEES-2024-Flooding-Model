2024 SEES Flood Model

This project is designed to provide a way to predict areas at high risk of flooding under an OpenScience framework.

The program uses elevation data from .csv, .tif, and .dem files. It interprets this data as a raster then applies a D8 flow analysis on the entire raster.
D8 flow is explained here: https://pro.arcgis.com/en/pro-app/latest/tool-reference/raster-analysis/flow-direction.htm

After applying the D8 raster analysis, the program runs a "flow_accumulation" function that determines, at each point, the amount of other cells that flow into that point.

This reveals specific points in a given topographical area that will accumulate water from the most unique sources from within the raster.

Although other D8 and flow accumulation plugins or instruments already exist such as the linked one from ArcGIS, the advantage of this project is that the code is completely open-source and easily adjustable.  It improves clarity as to how a D8 function is applied on an elevation raster and the methods used to predict areas of high flow accumulation.

Replication of Houston AOIs

1. Download the given notebook "SEES_Flood_Traker.ipynb" in Colab or other medium
2. Copy the GitHub link of the TIF file in the DEM Data folder
3. Scroll down to the "main" function in the notebook
4. Replace the old link "tif_url" with the new link (from 2.)
5. Run all

Alternatively, you can upload your own .dem, .csv, or .tif file to a unique Colab session:

1) Click on files on the left sidebar
2) Press "Upload to session storage"
3) Upload your file
4) Comment out the "tif_url" to the "urlretrieve" lines.
5) Replace "tif_name" in main(tif_name) with your file's directory


