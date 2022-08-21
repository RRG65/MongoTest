import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from pymongo import MongoClient
import pandas as pd 
import numpy as np 

def plotMap(lon,lat,imd):
    ax=plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines()
    c=ax.scatter(lon,lat,c=imd,transform=ccrs.PlateCarree())
    plt.show()

def main():
    c=MongoClient()
    db=c.bufrdb
    lstData=[ (d['longitude'],d['latitude'],d['#1#integratedOzoneDensity']) for d in db.ozone.find()]
    alon=np.array([])
    alat=np.array([])
    aimd=np.array([])
    for d in db.ozone.find():
        alon=np.hstack((alon,d['longitude']))
        alat=np.hstack((alat,d['latitude']))
        aimd=np.hstack((aimd,d['#1#integratedOzoneDensity']))
    

    plotMap(alon,alat,aimd)
    

if __name__=="__main__":
    main()
    
