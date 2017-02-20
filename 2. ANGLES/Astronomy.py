
from pysolar.solar import *
import datetime

def GetAxialTilt():
    Axial_Tilt = {}
    Axial_Tilt["Sun"] =  7.25
    Axial_Tilt["Mercury"] =  0.01
    Axial_Tilt["Venus"] =   177.4
    Axial_Tilt["Earth"] =   23.439281
    Axial_Tilt["Moon"] =   1.5424
    Axial_Tilt["Mars"] =   25.19
    Axial_Tilt["Ceres"] =   4
    Axial_Tilt["Jupiter"] =   3.13
    Axial_Tilt["Saturn"] =   26.73
    Axial_Tilt["Uranus"] =   97.77
    Axial_Tilt["Neptune"] =   28.32
    Axial_Tilt["Pluto"] =   119.61
    return Axial_Tilt
    
def GetAxialTiltForSolarSystemPlanet(planet):
    dic = dict (GetAxialTilt())
    if planet in dic.keys():
        return dic[planet]
    return None

def GetSolarPosition(Latitude,Longitude,datetime):
    if datetime is None:
        d = datetime.datetime.now()
    else:
        d = datetime
    return (get_altitude(Latitude, Longitude, d),get_azimuth(Latitude, Longitude, d) % 360)
 
 def GetSolarPositionErrors():
    ret = {}
    Azimuth = {}
    Azimuth["Mean"] =0.00463
    Azimuth["Standard deviation"] =0.00550
    Azimuth["Minimum"] = 6.10 * 10e-6
    Azimuth["Maximum"] =0.176
    ret["Azimuth"] = Azimuth
    Elevation = {}
    Elevation["Mean"] =0.0379
    Elevation["Standard deviation"] =0.0795
    Elevation["Minimum"] = 1.04  * 10e-6
    Elevation["Maximum"] = 0.604
    ret["Elevation"] = Azimuth
    return (ret)
