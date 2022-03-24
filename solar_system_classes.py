"""
Solar System Classes
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.animation as animation

""" CONSTANTS """
# Gravitational Constant in (AU)^3*(yr)^-2*(M_sun)^-1
G = 4*np.pi**2/332946

""" CLASSES """ 
class SolarSystemBody():
    """ For creating any body to be included in a Solar System.
    Position and vector parameters are 2D vectors. 
    """

    def __init__(self, solar_system, name, mass, diameter, position, 
                velocity, color):
        self.solar_system = solar_system
        self.name = name
        self.mass = mass
        self.diameter = diameter
        self.position = position 
        self.velocity = velocity
        self.color = color
        
    def get_name(self):
        return self.name
    
    def get_mass(self):
        return self.mass
    
    def get_diameter(self):
        return self.diameter

    def get_position(self):
        return self.position
    
    def get_velocity(self):
        return self.velocity

    def get_color(self):
        return self.color

class SolarSystem:
    """ For creating the Solar System environment. """
    def __init__(self):
        self.bodies = []
        
    def add_body(self, body):
        self.bodies.append(body)
    
    def get_bodies(self):
        return self.bodies
        
    def states_init(self):
        """ Put initial states of positions and velocities of
        each SolarSystemBody object into a single array for odeint.
        Array format: [x, y, dx/dt, dy/dt] 
        """
        bodies = self.bodies
        states = np.array([])

        for body in bodies:
            states = np.append(states, body.get_position()[0]) # x
            states = np.append(states, body.get_position()[1]) # y
            states = np.append(states, body.get_velocity()[0]) # dx/dt
            states = np.append(states, body.get_velocity()[1]) # dy/dt

        states = np.reshape(states, -1)

        return states

    def dv_dt(self, states, t):
        """ Function for calculating acceleration in x and y. 
        The solution of Newton's equation of gravity for 3+
        bodies is calculated using odeint.
        Returns derivatives in an array:
        [dx/dt, dy/dt, d2x/d2t, d2y/d2t]
        """

        # Total number of SolarSystemBody objects
        M = int(len(self.bodies))

        # Total number of states [x, y, dx/dt, dy/dt]
        N = int(len(states))
        
        # Put the mass values of all SolarSystemBody objects
        M_array = np.array([])

        for body in self.bodies:
            M_array = np.append(M_array, body.get_mass())
        
        # Separate states into their respective categories
        x_init = states[[k for k in range(N) if (k % 4 == 0)]]
        y_init = states[[k for k in range(N) if ((k-1) % 4 == 0)]]
        vx_init = states[[k for k in range(N) if ((k-2) % 4 == 0)]]
        vy_init = states[[k for k in range(N) if ((k-3) % 4 == 0)]]

        v_init = np.transpose(np.vstack((vx_init, vy_init)))

        # Instantiate acceleration arrays
        d2x_dt2 = np.array([])
        d2y_dt2 = np.array([])

        # Calculation for acceleration according to Newton's Law of Gravity
        for i in range(M):
            xi = x_init[i]
            yi = y_init[i]

            # Instantiate vx and vy component arrays for summation later
            vx_comp = np.array([])
            vy_comp = np.array([])

            for j in range(M):

                # Calculate force of other bodies acting on body i
                if i != j:
                    Mj = M_array[j]

                    xj = x_init[j]
                    yj = y_init[j]

                    rij_x = xj - xi
                    rij_y = yj - yi
                    rij = np.sqrt(rij_x**2 + rij_y**2)

                    vx_comp = np.append(vx_comp, Mj*rij_x/rij**3)
                    vy_comp = np.append(vy_comp, Mj*rij_y/rij**3)

            d2x_dt2 = np.append(d2x_dt2, G*np.sum(vx_comp))
            d2y_dt2 = np.append(d2y_dt2, G*np.sum(vy_comp))

        d2r_dt2 = np.transpose(np.vstack((d2x_dt2, d2y_dt2)))

        derivs = np.hstack((v_init, d2r_dt2))
        derivs = np.reshape(derivs, -1) # reshape array for odeint

        return derivs

    def animate(self, t, frames):
        """ 2D Animation for the simulation of the gravitational interactions
        of the SolarSystemBody objects within the SolarSystem.
        t = range of time over which to perform odeint calculations.
        frames = each day to animate.
        """

        # Get initial states of each SolarSystemBody
        states = self.states_init()
        
        # Total number of SolarSystemBody objects
        M = int(len(self.bodies))

        # Total number of states [x, y, dx/dt, dy/dt]
        N = int(len(states))

        # Solve Newton's Equation of Gravity given initial states and t
        solution = odeint(self.dv_dt, states, t)
        x_pos = solution[:, [k for k in range(N) if (k % 4 == 0)]]
        y_pos = solution[:, [k for k in range(N) if ((k-1) % 4 == 0)]]

        # Instantiate figure for animation
        fig = plt.figure(figsize=(12, 9))
        ax = fig.add_subplot(1,1,1)
        ax.set_facecolor("black")
        ax.set_xlabel("x [AU]")
        ax.set_ylabel("y [AU]")

        # Set limits for SolarSystem coordinates
        lim = np.max(x_pos)*1.2
        plt.xlim(-lim, lim)
        plt.ylim(-lim, lim)

        for i in range(M):
            plt.plot(x_pos[:,i], y_pos[:,i], "-", linewidth=1, color="white")
        
        # Display passage of time in days
        text_x = np.max(x_pos)*0.70
        text_y = np.max(y_pos)*0.95
        time_text = plt.text(text_x, text_y, '', fontsize=15, color='white')
        
        # Instantiate SolarSystemBody objects
        # The diameters of each SolarSystemBody are scaled up for visibility
        body_list = np.array([])
        for body in self.bodies:
            ss_body = ax.plot(body.get_position()[0], 
                              body.get_position()[1], 
                              'o', 
                              ms=body.get_diameter()*20,
                              color=body.get_color())
            body_list = np.append(body_list, ss_body)

        def update_anim(i):
            """ Animation function for FuncAnimation! """
            for k, ss_body in enumerate(body_list):

                # Position update
                ss_body = ss_body.set_data(x_pos[i,k], y_pos[i,k])

                # Time display update
                time_text.set_text("{} Earth days".format(str(i)))

        animation_2d = animation.FuncAnimation(fig, update_anim, frames, 
                                             interval=50, repeat=False)

        #animation_2d.save("solar_system_real_2d.mp4")
        plt.show()