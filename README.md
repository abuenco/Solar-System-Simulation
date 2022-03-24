# Solar System Simulation

## About the Project

The project creates a simplified 2D simulation of the motion of bodies in a Solar System resulting from the gravitational forces acting them. 
The position of each body can be calculated by numerically integrating the acceleration component from the summation of the forces 
acting on it based on Newton's equation of gravity. 

By expressing the gravitational forces acting on each body as a differential equation, the position solutions for each planet were calculated
using Scipy's odeint package. The simulation is presented in a 2D Matplotlib animation to display the orbital motion of each body. 

## Simulation Details

The simulation only includes the Sun and the rocky planets as the distances between the gas planets from each other and from the rocky planets are
much larger than the distances between the rocky planets. If the gas planets were to be included in the simulation, their locations in space
would need to be scaled down in the animation, but this would result in a loss of accuracy in presentation.

The size of the Sun is *not* to scale in the animation to make it easier to see the planets orbiting around it...!

The masses, diameters, initial positions, and initial velocities of each Solar System body re expressed in Astronomical Units (AU) relative to 
Earth. This system of measurement was selected to handle computing limitations (I tried using SI values but the values were too big for 
my computer). The initial position and velocity states are defined for odeint's calculations.
    
![SS simulation 2d Screenshot](https://user-images.githubusercontent.com/25872191/159993390-1c848d95-5be2-4966-8d51-c79bf7460a26.png)

### Simplifications
- The initial positions of each planet are defined to be their average distance away from the Sun. They all start in line with each other
along the y-axis as well. 
- The initial velocities of each planet are approximated by assuming a circular orbit and dividing its circumference by the orbital period.

### Sources
The astronomical data is sourced from HyperPhysics:
- [Sun](http://hyperphysics.phy-astr.gsu.edu/hbase/Solar/sun.html)
- [Planets](http://hyperphysics.phy-astr.gsu.edu/hbase/Solar/soldata2.html)

The names of the colors assigned to each Solar System body are sourced from 
[Matplotlib](https://matplotlib.org/stable/gallery/color/named_colors.html)

## Software
- [Python](https://www.python.org/)
- [Numpy](https://numpy.org/)
- [Scipy](https://scipy.org/)
  - [odeint](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html)
- [Matplotlib](https://matplotlib.org/)

  ## Contact
  Andie Buenconsejo  
  Email: al.buenco@gmail.com  
  [Project Link](https://github.com/abuenco/Solar-System-Simulation)
