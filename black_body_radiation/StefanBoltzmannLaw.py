"""
Created on Tue Aug  3 17:53:44 2021
"""

from typing import Optional

import numpy as np

sigma_sb = 5.67037e-8


class RadiantFlux:
    """
    Class to determine the radiant flux using Stefan-Boltzmann law. This class contains
    two methods,

    1- get_radiant_flux()

    2- solve()

    The get_radiant_flux() method requires two parameters,

    - temperature, and
    - emissivity.

    Although solve() method requires three parameters,

    - radiant flux,
    - temperature, and
    - emissivity.

    One of the three can be left unknown. However, two must be specified as float type
    arguments.
    """

    def __init__(self, temperature: Optional[float] = None,
                 emissivity: Optional[float] = 1):
        """
        Initializer method for RadiantFlux class for Stefan-Boltzmann Law.

        Parameters
        ----------
        temperature
            The temperature of the black body.
        emissivity
            The emissivity of the black body.
        """
        self.temperature = temperature
        self.emissivity = emissivity

    def get_radiant_flux(self) -> float:
        """
        Method to calculate the value for radiant flux from black body.

        Returns
        -------
        float:
            Value for radiant flux of the black body.

        """
        return self.emissivity * sigma_sb * self.temperature**4

    def solve(self, radiant_flux: Optional[float] = None) -> float:
        """
        Solver method of Stefan-Boltzmann law for one of the three unknown variables.

        Parameters
        ----------
        radiant_flux:
            The radiant flux of the black body.

        Returns
        -------
        float:
            One of the three unknown parameters for Stefan-Boltzmann law.
            
        Notes
        -------
        Takes the temperature and emissivity parameter from the __init__ function

        """
        r, s, t, e = radiant_flux, sigma_sb, self.temperature, self.emissivity

        # ensure we only have one unknown
        if [r, t, e].count(None) > 1:
            raise TypeError('Can\'t have more than one unknown variable.')

        return self.get_radiant_flux() if r is None else (r * (
                s * e)**-1)**0.25 if t is None else r * (s * t**4)**-1


class TotalPowerRadiated:
    """
    Class to determine the total power radiated using Stefan-Boltzmann law. This class
    contains two methods,

    1- get_total_power_radiated()

    2- solve()

    The get_total_power_radiated() method requires three parameters,

    - radius_of_the_object,
    - temperature, and
    - emissivity.

    Although solve() method requires four parameters,

    - total_power_radiated,
    - radius_of_the_object,
    - temperature, and
    - emissivity.

    One of the four can be left unknown. However, three must be specified as float type
    arguments.
    """

    def __init__(self, radius_of_the_object: Optional[float],
                 temperature: Optional[float] = None, emissivity: Optional[float] = 1):
        """
        Initializer method for TotalPowerRadiated class for Stefan-Boltzmann Law.

        Parameters
        ----------
        radius_of_the_object
            Radius of the emitting object/cavity. The object is assumed to be circular.
        temperature
            The temperature of the black body.
        emissivity
            The emissivity of the black body.
        """
        self.radius_of_the_object = radius_of_the_object
        self.temperature = temperature
        self.emissivity = emissivity

    def get_total_power_radiated(self) -> float:
        """
        Method to calculate the value for total radiated power from black body.

        Returns
        -------
        float:
            Value for radiant flux of the black body.
        """

        s_, e, t, r = (sigma_sb,
                       self.emissivity,
                       self.temperature,
                       self.radius_of_the_object)

        return 4 * np.pi * r**2 * s_ * t**4 * e

    def solve(self,
              total_power_radiated: Optional[float] = None,
              radius_of_object: Optional[float] = None,
              temperature: Optional[float] = None,
              emissivity: Optional[float] = 1) -> Optional[float]:
        """
        Method to get the radiant flux value from Stefan-Boltzmann Law.

        Parameters
        ----------
        total_power_radiated
            Total power radiated by the black body
        radius_of_object
            Radius of the emitting object/cavity. The object is assumed to be circular.
        temperature
            The temperature of the black body.
        emissivity
            The emissivity of the black body.

        Returns
        -------
        float:
            One of the four unknown parameters for Stefan-Boltzmann law.
        """

        # 0.25 * P * (pi * e * sigma_sb)**-1 * r**-2 * T**-4 = 0

        s_, e, t, r, tp = (sigma_sb,
                           emissivity,
                           temperature,
                           radius_of_object,
                           total_power_radiated)

        # ensure we only have one unknown
        if [tp, r, t, e].count(None) > 1:
            raise TypeError('Can\'t have more than one unknown variable.')

        _c = None if tp is None else 0.25 * tp * (np.pi * s_)**-1

        if tp is None:
            out = self.get_total_power_radiated()
        elif r is None:
            out = (_c * e**-1 * t**-4)**0.5
        elif t is None:
            out = (_c * e**-1 * r**-2)**0.25
        else:
            out = _c * r**-2 * t**-4

        return out
