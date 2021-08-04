#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 17:29:13 2021

@author: astrophysics and python
"""


class WienDisplacementLaw:

    def __init__(self):
        self.wien_constant = 0.0028977729

    def peak_wavelength(self, temperature):
        return self.wien_constant * temperature**-1

    def solve(self, wavelength=None, temperature=None):
        return [self.peak_wavelength(temperature) if wavelength is None else self.wien_constant * wavelength**-1][0]
