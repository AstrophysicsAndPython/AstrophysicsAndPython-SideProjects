"""
Created on Feb 09 23:38:17 2022
"""

import conversion_error_base as ceb


class FromCelsius:
    """Conversion class from degree Celsius to one of Kelvin, degree Fahrenheit, or Rankine temperature scale.

    FUNCTIONS
    ----------
    __init__(temperature: float, convert_to: str = 'F')
        Class initializer function

    convert()
        Convert function to convert degree Celsius temperature.

    Examples
    ----------
    Convert 100 degree Celsius temperature to Kelvin, degree Fahrenheit, and Rankine scale.

    >>> FromCelsius(100, 'F').convert()

    >>> FromCelsius(100, 'Kelvin').convert()

    >>> FromCelsius(100, 'rankine').convert()
    """

    def __init__(self, temperature: float, convert_to: str = 'F') -> None:
        """

        Parameters
        ----------
        temperature :
            Measured temperature.
        convert_to :
            Scale indicator, which temperature scale you want to convert to.

        Returns
        -------
        object:
            Converted temperature from degree Celsius.

        Notes
        -------
            convert_to variable takes either

            - K, Kelvin
            - F, degree Fahrenheit
            - R, Rankine
            as valid inputs. However, the string literal check in case-insensitive.
        """
        self.temperature = temperature
        self.convert_to = convert_to

    def _to_kelvin(self):
        # C + 273.15
        return self.temperature + 273.15

    def _to_fahrenheit(self):
        # (C * 1.8) + 32
        return (self.temperature * 1.8) + 32  # 9/5 = 1.8

    def _to_rankine(self):
        # (C * 1.8) + 491.67
        return (self.temperature * 1.8) + 491.67

    def convert(self):
        sep, convertible, _c = ', ', ['f', 'k', 'r', 'fahrenheit', 'kelvin', 'rankine'], self.convert_to.lower()

        if _c not in convertible:
            ceb.raise_error(separator=sep, units=convertible)

        return self._to_fahrenheit() if _c in ['f', 'fahrenheit'] else self._to_kelvin() if _c in ['k', 'kelvin'] else self._to_rankine()


class FromKelvin:
    """Conversion class from Kelvin to one of degree Celsius, degree Fahrenheit, or Rankine temperature scale.

    FUNCTIONS
    ----------
    __init__(temperature: float, convert_to: str = 'C')
        Class initializer function

    convert()
        Convert function to convert Kelvin temperature.

    Examples
    ----------
    Convert 100 Kelvin temperature to degree Celsius, degree Fahrenheit, and Rankine scale.

    >>> FromKelvin(100, 'C').convert()

    >>> FromKelvin(100, 'f').convert()

    >>> FromKelvin(100, 'rankine').convert()
    """

    def __init__(self, temperature: float, convert_to: str = 'C'):
        """

        Parameters
        ----------
        temperature :
            Measured temperature.
        convert_to :
            Scale indicator, which temperature scale you want to convert to.

        Returns
        -------
        object:
            Converted temperature from Kelvin.

        Notes
        -------
            convert_to variable takes either

            - C, degree Celsius
            - F, degree Fahrenheit
            - R, Rankine
            as valid inputs. However, the string literal check in case-insensitive.
        """
        self.temperature = temperature
        self.convert_to = convert_to

    def _to_celsius(self):
        # K - 273.15
        return self.temperature - 273.15

    def _to_fahrenheit(self):
        # (K - 273.15) * 1.8 + 32
        return (self._to_celsius() * 1.8) + 32

    def _to_rankine(self):
        # K * 1.8
        return self.temperature * 1.8

    def convert(self):
        sep, convertible, _c = ', ', ['c', 'f', 'r', 'celsius', 'fahrenheit', 'rankine'], self.convert_to.lower()

        if _c not in convertible:
            ceb.raise_error(separator=sep, units=convertible)

        return self._to_celsius() if _c in ['c', 'celsius'] else self._to_fahrenheit() if _c in ['f', 'fahrenheit'] else self._to_rankine()


class FromFahrenheit:
    """Conversion class from degree Fahrenheit to one of degree Celsius, Kelvin, or Rankine temperature scale.

    FUNCTIONS
    ----------
    __init__(temperature: float, convert_to: str = 'C')
        Class initializer function

    convert()
        Convert function to convert degree Fahrenheit temperature.

    Examples
    ----------
    Convert 100 degree Fahrenheit temperature to degree Celsius, Kelvin, and Rankine scale.

    >>> FromFahrenheit(100, 'C').convert()

    >>> FromFahrenheit(100, 'Kelvin').convert()

    >>> FromFahrenheit(100, 'rankine').convert()
    """

    def __init__(self, temperature: float, convert_to: str = 'C'):
        """

        Parameters
        ----------
        temperature :
            Measured temperature.
        convert_to :
            Scale indicator, which temperature scale you want to convert to.

        Returns
        -------
        object:
            Converted temperature from degree Fahrenheit.

        Notes
        -------
            convert_to variable takes either

            - C, degree Celsius
            - K, Kelvin
            - R, Rankine
            as valid inputs. However, the string literal check in case-insensitive.
        """
        self.temperature = temperature
        self.convert_to = convert_to

    def _to_celsius(self):
        # (F - 32) / 1.8
        return (self.temperature - 32) / 1.8

    def _to_kelvin(self):
        # ((F - 32) / 1.8) + 273.15
        return self._to_celsius() + 273.15

    def _to_rankine(self):
        # F + 459.67
        return self.temperature + 459.67

    def convert(self):
        sep, convertible, _c = ', ', ['c', 'k', 'r', 'celsius', 'kelvin', 'rankine'], self.convert_to.lower()

        if _c not in convertible:
            ceb.raise_error(separator=sep, units=convertible)

        return self._to_celsius() if _c in ['c', 'celsius'] else self._to_kelvin() if _c in ['k', 'kelvin'] else self._to_rankine()


class FromRankine:
    """Conversion class from Rankine to one of degree Celsius, degree Fahrenheit, or Kelvin temperature scale.

    FUNCTIONS
    ----------
    __init__(temperature: float, convert_to: str = 'C')
        Class initializer function

    convert()
        Convert function to convert Rankine temperature.

    Examples
    ----------
    Convert 100 Rankine temperature to degree Celsius, degree Fahrenheit, and Kelvin scale.

    >>> FromRankine(100, 'C').convert()

    >>> FromRankine(100, 'F').convert()

    >>> FromRankine(100, 'Kevlin').convert()
    """

    def __init__(self, temperature: float, convert_to: str = 'C'):
        """

        Parameters
        ----------
        temperature :
            Measured temperature.
        convert_to :
            Scale indicator, which temperature scale you want to convert to.

        Returns
        -------
        object:
            Converted temperature from Rankine.

        Notes
        -------
            convert_to variable takes either

            - C, degree Celsius
            - K, Kelvin
            - F, degree Fahrenheit
            as valid inputs. However, the string literal check in case-insensitive.
        """
        self.temperature = temperature
        self.convert_to = convert_to

    def _to_fahrenheit(self):
        # R - 459.67
        return self.temperature - 459.67

    def _to_celsius(self):
        # (R - 391.67) / 1.8
        return (self.temperature - 491.67) / 1.8

    def _to_kelvin(self):

        return self.temperature / 1.8

    def convert(self):
        sep, convertible, _c = ', ', ['c', 'k', 'f', 'celsius', 'kelvin', 'fahrenheit'], self.convert_to.lower()

        if _c not in convertible:
            ceb.raise_error(separator=sep, units=convertible)

        return self._to_celsius() if _c in ['c', 'celsius'] else self._to_kelvin() if _c in ['k', 'kelvin'] else self._to_fahrenheit()
