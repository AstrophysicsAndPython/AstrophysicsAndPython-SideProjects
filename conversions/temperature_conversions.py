"""
Created on Feb 09 23:38:17 2022
"""

from typing import Union

import numpy as np


class FromCelsius:
    """Conversion class from degree Celsius to one of degree Fahrenheit, Rankine, or Kelvin temperature scale.

    Parameters
    ----------
    temperature : float or list or ndarray
        Measured temperature in degree Celsius.
    convert_to : str, optional
        Scale indicator, which temperature scale you want to convert to.
        Valid inputs are 'F' (degree Fahrenheit), 'R' (Rankine), and 'K' (Kelvin).
        Default is 'F'.

    Attributes
    ----------
    temperature : float or ndarray
        Measured temperature in degree Celsius.
    convert_to : str
        Scale indicator, which temperature scale you want to convert to.

    Examples
    --------
    Convert 100 degree Celsius temperature to degree Fahrenheit, Rankine, and Kelvin scale.

    >>> FromCelsius(100, 'F').convert()
    212.0

    >>> FromCelsius(100, 'R').convert()
    671.67

    >>> FromCelsius(100, 'K').convert()
    373.15
    """

    def __init__(self, temperature: Union[float, list, np.ndarray], convert_to: str = 'F'):
        """Initialize the class."""
        self.temperature = temperature
        self.convert_to = convert_to

    def check_input_type(self):
        """Convert input temperature to a NumPy array if necessary."""
        if isinstance(self.temperature, float):
            self.temperature = np.array([self.temperature])
        elif isinstance(self.temperature, list):
            self.temperature = np.array(self.temperature)

    def convert(self) -> Union[float, int, list, np.ndarray]:
        """Convert the temperature from degree Celsius to the specified scale.

        Returns
        -------
        float or int or ndarray
            Converted temperature.
        """
        self.check_input_type()
        c = self.convert_to.lower()

        if c not in ['f', 'r', 'k']:
            raise ValueError(f"Invalid temperature scale: {c}. Valid scales are 'F', 'R', and 'K'.")

        func_map = {'f': (self.temperature * 1.8) + 32,
                    'r': (self.temperature * 1.8) + 491.67,
                    'k': self.temperature + 273.15}

        return func_map[c]


class FromKelvin:
    """Conversion class from Kelvin to one of degree Celsius, degree Fahrenheit, or Rankine temperature scale.

    Parameters
    ----------
    temperature : float or list or ndarray
        Measured temperature in Kelvin.
    convert_to : str, optional
        Scale indicator, which temperature scale you want to convert to.
        Valid inputs are 'C' (degree Celsius), 'F' (degree Fahrenheit), and 'R' (Rankine).
        Default is 'C'.

    Attributes
    ----------
    temperature : float or ndarray
        Measured temperature in Kelvin.
    convert_to : str
        Scale indicator, which temperature scale you want to convert to.

    Examples
    --------
    Convert 100 Kelvin temperature to degree Celsius, degree Fahrenheit, and Rankine scale.

    >>> FromKelvin(100, 'C').convert()
    -173.15

    >>> FromKelvin(100, 'f').convert()
    -279.67

    >>> FromKelvin(100, 'rankine').convert()
    180.0
    """

    def __init__(self, temperature: Union[float, list, np.ndarray], convert_to: str = 'C'):
        """Initialize the class."""
        self.temperature = temperature
        self.convert_to = convert_to

    def check_input_type(self):
        """Convert input temperature to a NumPy array if necessary."""
        if isinstance(self.temperature, float):
            self.temperature = np.array([self.temperature])
        elif isinstance(self.temperature, list):
            self.temperature = np.array(self.temperature)

    def convert(self) -> np.ndarray:
        """Convert the temperature from Kelvin to the specified scale.

        Returns
        -------
        ndarray
            Converted temperature.
        """
        self.check_input_type()
        k = self.convert_to.lower()

        if k not in ['c', 'f', 'r']:
            raise ValueError(f"Invalid temperature scale: {k.upper()}. Valid scales are 'C', 'F', and 'R'.")

        func_map = {'c': self.temperature - 273.15,
                    'f': (self.temperature - 273.15) * 1.8 + 32,
                    'r': self.temperature * 1.8}

        return func_map[k]


class FromFahrenheit:
    """Conversion class from degree Fahrenheit to one of degree Celsius, Rankine, or Kelvin temperature scale.

    Parameters
    ----------
    temperature : float or list or ndarray
        Measured temperature in degree Fahrenheit.
    convert_to : str, optional
        Scale indicator, which temperature scale you want to convert to.
        Valid inputs are 'C' (degree Celsius), 'R' (Rankine), and 'K' (Kelvin).
        Default is 'C'.

    Attributes
    ----------
    temperature : float or ndarray
        Measured temperature in degree Fahrenheit.
    convert_to : str
        Scale indicator, which temperature scale you want to convert to.

    Examples
    --------
    Convert 100 degree Fahrenheit temperature to degree Celsius, Rankine, and Kelvin scale.

    >>> FromFahrenheit(100, 'C').convert()
    37.78

    >>> FromFahrenheit(100, 'R').convert()
    559.67

    >>> FromFahrenheit(100, 'K').convert()
    310.928
    """

    def __init__(self, temperature: Union[float, list, np.ndarray], convert_to: str = 'C'):
        """Initialize the class."""
        self.temperature = temperature
        self.convert_to = convert_to

    def check_input_type(self):
        """Convert input temperature to a NumPy array if necessary."""
        if isinstance(self.temperature, float):
            self.temperature = np.array([self.temperature])
        elif isinstance(self.temperature, list):
            self.temperature = np.array(self.temperature)

    def convert(self) -> np.ndarray:
        """Convert the temperature from degree Fahrenheit to the specified scale.

        Returns
        -------
        ndarray
            Converted temperature.
        """
        self.check_input_type()
        f = self.convert_to.lower()

        if f not in ['c', 'k', 'r']:
            raise ValueError(f"Invalid temperature scale: {f.upper()}. Valid scales are 'C', 'K', and 'R'.")

        func_map = {'c': (self.temperature - 32) * 1.8,
                    'k': (self.temperature - 32) * 1.8 + 273.15,
                    'r': self.temperature + 459.67}

        return func_map[f]


class FromRankine:
    """Conversion class from Rankine to one of degree Fahrenheit, degree Celsius, or Kelvin temperature scale.

    Parameters
    ----------
    temperature : float or list or ndarray
        Measured temperature in Rankine.
    convert_to : str, optional
        Scale indicator, which temperature scale you want to convert to.
        Valid inputs are 'F' (degree Fahrenheit), 'C' (degree Celsius), and 'K' (Kelvin).
        Default is 'F'.

    Attributes
    ----------
    temperature : float or ndarray
        Measured temperature in Rankine.
    convert_to : str
        Scale indicator, which temperature scale you want to convert to.

    Examples
    --------
    Convert 100 Rankine temperature to degree Fahrenheit, degree Celsius, and Kelvin scale.

    >>> FromRankine(100, 'F').convert()
    180.0

    >>> FromRankine(100, 'C').convert()
    -272.594

    >>> FromRankine(100, 'K').convert()
    55.56
    """

    def __init__(self, temperature: Union[float, list, np.ndarray], convert_to: str = 'F'):
        """Initialize the class."""
        self.temperature = temperature
        self.convert_to = convert_to

    def check_input_type(self):
        """Convert input temperature to a NumPy array if necessary."""
        if isinstance(self.temperature, float):
            self.temperature = np.array([self.temperature])
        elif isinstance(self.temperature, list):
            self.temperature = np.array(self.temperature)

    def convert(self) -> np.ndarray:
        """Convert the temperature from Rankine to the specified scale.

        Returns
        -------
        ndarray
            Converted temperature.
        """
        self.check_input_type()
        r = self.convert_to.lower()

        if r not in ['c', 'f', 'k']:
            raise ValueError(f"Invalid temperature scale: {r.upper()}. Valid scales are 'C', 'F', and 'K'.")

        func_map = {'c': (self.temperature - 491.67) * 1.8,
                    'f': self.temperature - 459.67,
                    'k': self.temperature * 1.8}

        return func_map[r]
