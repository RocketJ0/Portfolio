# Humidity-temperature relationship

This project tries to figure out whether there’s a measurable connection between humidity and temperature using two different methods. The goal is to take a humidity map, with the output being the corresponding temperature map. I did this project to get an understanding on regression. The humidity and temperature images come from https://zoom.earth/maps/.

[Link to code](./main.py)

[Link to output](./Output)

## Methods
Two methods are used:

1. Naive method
   Both humidity and temperature have scales at the bottom of the map. This method samples both scales and tries to pair each humidity value with a corresponding temperature value. Called the naive method because it is a simple method of regression, with no training image data needed.

2. Image method
   Samples a region from actual images (not just the color scale) to learn a relationship between the map’s humidity and temperature pixels.

## Tools used
Python with numpy and pandas, as well as two ML algorithms: linear regression and nearest neighbour.

## What did I learn?
- Application of the nearest neighbour algorithm
- R^2 values don't tell the whole story: The R^2 value on naive methods were, well, appalling (around -35). However, looking at the image that while the colors are different, the naive method tends to capture better detail when it comes to regions. The image method has more accurate colors, but there is not as much detail present in the picture. Visual analysis is still useful to get insights. 
