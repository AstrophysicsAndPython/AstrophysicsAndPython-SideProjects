"""
Created on Mon Aug 16 00:40:21 2021
"""

from typing import Union, List

import numpy as np

h, c, kB = 6.62607004e-34, 299792458, 1.38064852e-23


def power_radiated(wavelength: Union[List[float], float],
                   temperature: Union[List[float], float]) -> Union[List[float], float]:
    """
    Get the value of power radiated per unit area by a black body given its wavelength and temperature.

    Parameters
    ----------
    wavelength:
        Wavelength of emission of black body (in nanometer).
    temperature:
        Temperature of the black body (in Kelvin).

    Returns
    -------
    float:
        Power radiated by the black body.

    """
    l, t = wavelength, temperature

    p1 = 2 * np.pi * h * c**2 * l**-5
    p2 = np.exp(h * c * (l * kB * t)**-1) - 1
    return p1 * p2**-1 * 1e-10
