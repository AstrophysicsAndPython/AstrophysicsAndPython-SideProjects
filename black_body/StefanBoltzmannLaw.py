"""
Created on Tue Aug  3 17:53:44 2021
"""

from typing import Optional

import numpy as np

sigma_sb = 5.67037e-8


class RadiantFlux:
    """
    Class to determine the radiant flux from Stefan-Boltzmann law. This class contains two methods,

    1- get_radiant_flux()

    2- solve()

    The get_radiant_flux() method requires two float/int type arguments,

    - temperature, and
    - emissivity.

    Although solve() method requires three parameters,

    - radiant flux,
    - temperature, and
    - emissivity.

    One of the three can be left unknown. However, two must be specified as float/int type arguments.
    """

    def __init__(self):
        pass

    @staticmethod
    def get_radiant_flux(temperature: float, emissivity: float) -> float:
        """
        Method to get the radiant flux value from Stefan-Boltzmann Law.

        Parameters
        ----------
        temperature
            The temperature of the black body.
        emissivity
            The emissivity of the black body.

        Returns
        -------
        float:
            Radiant flux of the black body.

        """

        e, s, t = emissivity, sigma_sb, temperature

        return e * s * t**4

    def solve(self,
              radiant_flux: Optional[float] = None,
              temperature: Optional[float] = None,
              emissivity: Optional[float] = None) -> Optional[float]:
        """
        Method to solve the Stefan-Boltzmann law for one of the three unknown variables.

        Parameters
        ----------
        radiant_flux:
            The radiant flux of the black body.
        temperature:
            The temperature of the black body
        emissivity:
            The emissivity parameter for the black body.

        Returns
        -------
        object:
            One of the three unknown parameters for Stefan-Boltzmann law.

        """
        r, s, t, e = radiant_flux, sigma_sb, temperature, emissivity

        return self.get_radiant_flux(t, e) if r is None else (r * (s * e)**-1)**0.25 if t is None else r * (s * t**4)**-1 if e is None else None


class TotalPowerRadiated:

    def __init__(self):
        pass

    @staticmethod
    def get_total_power_radiated(radius_of_the_object: float,
                                 temperature: float,
                                 emissivity: float) -> float:
        return 4 * np.pi * radius_of_the_object**2 * sigma_sb * temperature**4 * emissivity

    def solve(self,
              total_power_radiated: Optional[float] = None,
              radius_of_object: Optional[float] = None,
              temperature: Optional[float] = None,
              emissivity: Optional[float] = None) -> Optional[float]:
        # 0.25 * P * (pi * e * sigma_sb)**-1 * r**-2 * T**-4 = 0

        tp, r, t, e, s = total_power_radiated, radius_of_object, temperature, emissivity, sigma_sb

        _constants = None if tp is None else 0.25 * tp * (np.pi * s)**-1

        return self.get_total_power_radiated(r, t, e) if tp is None else (_constants * e**-1 * t**-4)**0.5 if r is None else (_constants * e**-1 * r**-2)**0.25 if t is None else \
            _constants * r**-2 * t**-4 if e is None else None
