# -*- coding: utf-8 -*-
"""
Solar System Simulation in 2D
"""
import numpy as np
import solar_system_classes as ss_class
import solar_system_dicts as ss_dict

def createSS():
    """ Builds a SolarSystem consisting of the Sun and rocky planets.
    The coordinates of the gas planets are far away enough that the
    sizes and distances would need to be scaled to still look presentable.
    The attributes of each SolarSystemBody is loaded from a dictionary.
    """

    # Class definitions
    ss = ss_class.SolarSystem()
    
    sun = ss_class.SolarSystemBody(ss, 
                        ss_dict.sun.get("name"), 
                        ss_dict.sun.get("mass"), 
                        ss_dict.sun.get("diameter"), 
                        ss_dict.sun.get("position"),
                        ss_dict.sun.get("velocity"),
                        ss_dict.sun.get("color"))

    mercury = ss_class.SolarSystemBody(ss, 
                            ss_dict.mercury.get("name"), 
                            ss_dict.mercury.get("mass"),
                            ss_dict.mercury.get("diameter"),
                            ss_dict.mercury.get("position"),
                            ss_dict.mercury.get("velocity"),
                            ss_dict.mercury.get("color"))

    venus = ss_class.SolarSystemBody(ss, 
                            ss_dict.venus.get("name"), 
                            ss_dict.venus.get("mass"),
                            ss_dict.venus.get("diameter"),
                            ss_dict.venus.get("position"),
                            ss_dict.venus.get("velocity"),
                            ss_dict.venus.get("color"))

    earth = ss_class.SolarSystemBody(ss, 
                            ss_dict.earth.get("name"), 
                            ss_dict.earth.get("mass"),
                            ss_dict.earth.get("diameter"),
                            ss_dict.earth.get("position"),
                            ss_dict.earth.get("velocity"),
                            ss_dict.earth.get("color"))

    mars = ss_class.SolarSystemBody(ss, 
                            ss_dict.mars.get("name"), 
                            ss_dict.mars.get("mass"),
                            ss_dict.mars.get("diameter"),
                            ss_dict.mars.get("position"),
                            ss_dict.mars.get("velocity"),
                            ss_dict.mars.get("color"))
    
    # Add SolarSystemBody objects to SolarSystem
    ss.add_body(sun)
    ss.add_body(mercury)
    ss.add_body(venus)
    ss.add_body(earth)
    ss.add_body(mars)

    # Set up time range to simulate
    years = 5
    days = years*365

    # Account for leap years
    for i in range(years):
        if ((i+1) % 4 == 0):
            days+=1

    t_range = np.linspace(0, years, days)

    ss.animate(t_range, days)

# Create Solar System Simulation
ss_2d = createSS()