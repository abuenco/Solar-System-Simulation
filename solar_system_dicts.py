"""
Dictionaries for Sun and rocky planets in a simplified Solar System.

The masses, diameters, positions, and velocities of the SolarSystem objects
are expressed in Astronomical Units (AU) relative to Earth. This system of
measurement was selected to handle computing limitations.

The position and velocity attributes of each body are 2D vectors expressing
their initial states. The initial vy values are expressed in
vy_0 = 2*pi*R/(planet's orbit in Earth days/Number of Earth days).

Data is sourced from HyperPhysics:
http://hyperphysics.phy-astr.gsu.edu/hbase/hframe.html
http://hyperphysics.phy-astr.gsu.edu/hbase/Solar/soldata2.html

Assigned colors are sourced from Matplotlib:
https://matplotlib.org/stable/gallery/color/named_colors.html
"""

import numpy as np

sun = {
  "name": "Sun", 
  "mass": 332800,
  "diameter": 2.5,
  "position": [0.0, 0.0],
  "velocity": [0.0, 0.0],
  "color": "gold"
}

mercury = {
  "name": "Mercury",
  "mass": 0.055,
  "diameter": 0.382,
  "position": [0.387, 0.0],
  "velocity": [0.0, 2*np.pi*0.387/(88/365)],
  "color": "gray"
}

venus = {
  "name": "Venus",
  "mass": 0.815,
  "diameter": 0.949,
  "position": [0.723, 0.0],
  "velocity": [0.0, 2*np.pi*0.723/(243/365)],
  "color": "goldenrod"
}
        
earth = {
  "name": "Earth",
  "mass": 1.00,
  "diameter": 1.00,
  "position": [1.00, 0.0],
  "velocity": [0.0, 2*np.pi],
  "color": "darkturquoise"
}

mars = {
  "name": "Mars",
  "mass": 0.107,
  "diameter": 0.532,
  "position": [1.524, 0.0],
  "velocity": [0.0, 2*np.pi*1.524/(687/365)],
  "color": "firebrick"
}