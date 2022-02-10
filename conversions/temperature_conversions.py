"""
Created on Feb 09 23:38:17 2022
"""

import conversion_error_base as ceb


class FromCelsius:

    def __init__(self, temperature: float, convert_to: str = 'F') -> None:
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

    def __init__(self, temperature: float, convert_to: str = 'C'):
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

    def __init__(self, temperature: float, convert_to: str = 'C'):
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

    def __init__(self, temperature: float, convert_to: str = 'C'):
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
