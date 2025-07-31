# Cloud segmentation
K Means clustering is used to separat clouds from land and/or water from satellite images. Chosen satellite image to test this out is a map of Sri Lanka.

[Link to code](3.Cloud-cover-K-means/main.py)
[Link to output](3.Cloud-cover-K-means/Output)

## Method
- Flattens RGB image into pixel rows
- Uses KMeans (n=2) to cluster pixels by color.
- Returns image to visualize segmentation
  
## What did I learn
- KMeans can easily segment images, especially when the regions are dominant.
- The alpha channel caused me some grief in this project, and I learnt this needs to be discarded sometimes for image analysis.
- Might be difficult using this method in snowy areas - would need a different system for this.
