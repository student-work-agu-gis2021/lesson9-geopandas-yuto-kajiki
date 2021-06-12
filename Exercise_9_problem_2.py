#!/usr/bin/env python
# coding: utf-8

# ## Problem 2: Points to map
#  
# In this problem we continue to learn how to turn latitude and longitude coordinates in to geometries.
# 


import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
# YOUR CODE HERE 1 to read data
data = None
 #read csv_file
data = pd.read_csv('data/some_posts.csv')
Points = lambda row:Point(row['lat'],row['lon'])
 #I'll use hint2 apply metod
data['geometry'] = data.apply(Points, axis=1)
# CODE FOR TESTING YOUR SOLUTION

# Check the result
print("Number of rows:", len(data))


# CODE FOR TESTING YOUR SOLUTION

# Check the result
print(data['geometry'].head())


# YOUR CODE HERE 2
import geopandas as gpd
from pyproj import CRS

# Convert DataFrame into a GeoDataFrame
geo=None
#converted DataFrame into GeoDataFrame
geo = gpd.GeoDataFrame(data, geometry='geometry',crs=CRS.from_epsg(4326).to_wkt())
# CODE FOR TESTING YOUR SOLUTION

# Check the geodataframe head
print("Number of rows:", len(geo))
print(geo.head())


# CODE FOR TESTING YOUR SOLUTION
fp = 'Kruger_posts.shp'

geo.to_file(fp)
# Check that the output file exists
import os
assert os.path.isfile(fp), "output shapefile does not exist"


# **Finally:** 
# - **Create a simple map of the points** using the `plot()` -funtion. 
geo.plot()
# YOUR CODE HERE 3

# Well done! Now you can move on to Exercise_9_problem_3.

def func5():
    return data

def func6():
    return geo
