"""
Created on Tue Aug  3 17:29:13 2021
"""

from typing import Optional

wien_constant = 0.0028977729


def get_peak_wavelength(temperature: float) -> float:
    """
    Method to determine the peak wavelength for a black body given its temperature.

    Parameters
    ----------
    temperature:
        The temperature of the black body (in Kelvin).

    Returns
    -------
    float:
        wavelength - The wavelength (in nanometer) corresponding to the temperature of the black body.

    """
    return wien_constant * temperature**-1


def solve(wavelength: Optional[float] = None,
          temperature: Optional[float] = None) -> float:
    """
    Method to solve the Wien displacement law given one unknown.

    Parameters
    ----------
    wavelength:
        Wavelength of the object (in nanometer).
    temperature:
        Temperature of the object (in Kelvin).

    Returns
    -------
    object:
        Either the temperature of the black body or the wavelength of emission depending upon the unknown parameter.

    """
    w, w_, t = wavelength, wien_constant, temperature

    return get_peak_wavelength(t) if w is None else w_ * w**-1
