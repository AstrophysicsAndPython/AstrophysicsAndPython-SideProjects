#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 17:53:44 2021

@author: astrophysics and python
"""

from numpy import pi


class StefanBoltzamnnLaw:

    def __init__(self):
        self.sigma_sb = 5.67037e-8

    class RadianFlux:

        def __init__(self):
            self.sigma_sb = StefanBoltzamnnLaw().sigma_sb

        def radiant_flux(self, temperature, emissivity):
            return emissivity * self.sigma_sb * temperature**4

        def solve(self, radiant_flux=None, temperature=None, emissivity=None):
            if radiant_flux is None:
                out = self.radiant_flux(temperature, emissivity)
            elif temperature is None:
                out = radiant_flux * (self.sigma_sb * emissivity)**-1
                out = pow(out, 1/4)
            elif emissivity is None:
                out = radiant_flux * (self.sigma_sb * temperature**4)**-1

            return out

    class TotalPowerRadiated:

        def __init__(self):
            self.sigma_sb = StefanBoltzamnnLaw().sigma_sb

        def total_power_radiated(self, radius_of_the_object, temperature, emissivity):
            return 4 * pi * radius_of_the_object**2 * self.sigma_sb * temperature**4

        def solve(self, total_power_radiated=None, radius_of_object=None, temperature=None, emissivity=None):
            # 0.25 * P * (pi * e * sigma_sb)**-1 * r**-2 * T**-4 = 0

            pre_calculated_terms = [None if total_power_radiated is None else 0.25 * total_power_radiated * (pi * self.sigma_sb)**-1][0]

            if total_power_radiated is None:
                out = self.total_power_radiated(radius_of_object, temperature, emissivity)
            elif radius_of_object is None:
                out = (pre_calculated_terms * emissivity**-1 * temperature**-4)**0.5
            elif temperature is None:
                out = (pre_calculated_terms * emissivity**-1 * radius_of_object**-2)**0.25
            elif emissivity is None:
                out = pre_calculated_terms * radius_of_object**-2 * temperature**-4
            else:
                out = None

            return out
