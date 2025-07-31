# tries to identify a relationship between humidity, pressure, and temperature

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score


# Tries to establish a relationship between humidity and temperature. Two methods are used:
# 1. Naive method: Samples key of temperature and humidity (found at the bottom of respective images) and establishes a relationship directly from this. 
# 2. Image method: Samples test temperature and humidity images and establishes a relationship between these.
#
# In both methods, the colors are converted to values, linear regression is calculated with the values, and the values are converted back to color


def color_maps_to_values(input_map: np.ndarray, min_value:int, max_value:int, scale_name:str) -> pd.DataFrame:
    scaling = pd.DataFrame(input_map.reshape(-1,3), columns=["R","G","B"])
    scaling[scale_name] = np.linspace(min_value, max_value, len(scaling))
    return scaling


def map_to_values(map_type: np.ndarray, scale:pd.DataFrame, desired_column: str) -> np.ndarray:
    """Uses the Nearest Neighbour algorithm to find corresponding values based on the colors"""
    nn_mtv = NearestNeighbors(n_neighbors=1)

    img_rgb = map_type.reshape(-1,3)

    # Filters the scale so that only rgb colors also present in the image are taken. Ensures the Nearest Neighbour Algorithm 
    # doesn't take too wide a range of values
    img_rgb_df = pd.DataFrame(np.unique(img_rgb,axis=0), columns=["R","G","B"])
    new_scale = pd.merge(scale, img_rgb_df, on=["R","G","B"], how="inner")


    nn_mtv.fit(new_scale[["R","G","B"]].to_numpy())
    _, indices = nn_mtv.kneighbors(img_rgb)
    scale_values = new_scale[desired_column].to_numpy()
    new_values = scale_values[indices.flatten()]

    return new_values[:, np.newaxis]

def values_to_map(vals: np.ndarray,scale:pd.DataFrame, new_shape, merge_column: str) -> np.ndarray:
    nn_vtm = NearestNeighbors(n_neighbors=1)
    nn_vtm.fit(scale[merge_column].to_numpy()[:,np.newaxis])


    _, indices = nn_vtm.kneighbors(vals.reshape(-1,1))

    scale_rgb = scale[["R", "G", "B"]].to_numpy()
    new_rgb = scale_rgb[indices.flatten()]
    return new_rgb.reshape(new_shape)

humidity_maps = [
    plt.imread("Src/Humidity.png")[:,:,:3],
    plt.imread("Src/Humidity_test.png")[:,:,:3],
    plt.imread("Src/Humidity test 2.png")[:,:,:3]
]

temperature_maps = [
    plt.imread("Src/Temperature.png")[:,:,:3],
    plt.imread("Src/Temperature_test.png")[:,:,:3],
    plt.imread("Src/Temperature_test 2.png")[:,:,:3]
]

color_maps = {
    "humidity": humidity_maps[0][1915:1916,100:650,:3][:, ::-1, :],
    "temperature": temperature_maps[0][1915:1916,100:650,:3]
}

temp = "temperature (T)"
humi = "humidity (%)"



# changes the color map to a numerical values of shape(n,1) for Regression testing
X = color_maps_to_values(color_maps["humidity"], 0, 100, humi)
y = color_maps_to_values(color_maps["temperature"], -30, 50, temp)

# Naive method
model_naive = LinearRegression(fit_intercept=True)
model_naive.fit(X[[humi]],y[temp])

def naive_method(humidity, temperature):
    X_fit = map_to_values(humidity,X,humi)
    y_test = temperature
    y_fit_raw = model_naive.predict(X_fit)

    y_fit1 = values_to_map(y_fit_raw,y,y_test.shape, temp)

    fig, ax = plt.subplots(2,2)
    ax[0,0].imshow(humidity)
    ax[0,0].set_title("Humidity Map")
    ax[1,0].imshow(y_test)
    ax[1,0].set_title("True temperature map")
    ax[1,1].imshow(y_fit1)
    ax[1,1].set_title("Fitted map")
    plt.show()

    naive_r2 = r2_score(map_to_values(y_test.flatten(),y,temp),y_fit_raw)
    return naive_r2



print("naive classification completed")

# Image method
image_model = LinearRegression(fit_intercept=True)
X_image = map_to_values(humidity_maps[0][400:1700,500:2900,:3],X,humi)
y_image = map_to_values(temperature_maps[0][400:1700,500:2900,:3],y,temp)

image_model.fit(X_image,y_image)

def image_method(humidity, temperature):
    X_fit = map_to_values(humidity,X,humi)
    y_test = temperature
    y_fit_raw = image_model.predict(X_fit)

    y_fit = values_to_map(y_fit_raw,y,y_test.shape, temp)

    fig, ax = plt.subplots(2,2)
    ax[0,0].imshow(humidity)
    ax[0,0].set_title("Humidity Map")
    ax[1,0].imshow(y_test)
    ax[1,0].set_title("True map")
    ax[1,1].imshow(y_fit)
    ax[1,1].set_title("Fitted map")
    plt.show()

    return r2_score(map_to_values(y_test.flatten(),y,temp),y_fit_raw)


for i in range(3):
    naive_method(humidity_maps[i][400:1700,500:2900,:3],temperature_maps[i][400:1700,500:2900,:3])
    image_method(humidity_maps[i][400:1700,500:2900,:3],temperature_maps[i][400:1700,500:2900,:3])

# conclusion - doing a direct comparision shows naive_r2 having a much worse score than image_r2 (-35.92330997030965 vs 0.3929131664680334). but looking at the graphs shows that
# the naive_r2 has more nuanced analysis, altho the temperature is off. It classifies data better together.
# The image_r2 produces more accurate colors, but all the colors are similar to each other and does not produce as much detail.



# to continue:

# some other model for better data
# check if the naive classification can somehow be improved
# take away sea areas and only have land to see if there is any difference in classification
# add in more factors than just humidity to see if it changes anything