"""
Created on Mar 10 13:06:50 2022
"""

import numpy as np


def lightcurve_data(dat_file: str, energy_low: float, energy_high: float, errors=False):
    """
    Get the time, rate, and background from the RMFIT .dat file within a specific energy boundary.

    Parameters
    ----------
    dat_file: str
        RMFIT .dat file.
    energy_low: float
        The lower bound on energy.
    energy_high: float
        The upper bound on energy.
    errors: bool

    Returns
    -------
    time:
        Time measurements for the burst duration.
    data_rate:
        Rate of data accumulation within the energy bounds for the burst duration
    data_background:
        Estimated background for the energy bounds specified.
    errs:
        Errors on data_rate, and data_background

    """

    # Initialization
    data_rate, data_background, channel_number = 0, 0, 128
    data_rate_error, data_background_error = 0, 0
    detector_file, detector_data, low_energy_channel, high_energy_channel = [], [], [], []

    # reading the detector data
    with open(dat_file) as f:
        detector_file.append(f.readlines())

    detector_file = detector_file[0]

    # separating energy data from real data
    energy_channels, data = detector_file[11:11 + channel_number], detector_file[12 + channel_number:]

    for data_item in data:
        detector_data.append(np.genfromtxt(data_item.split()))

    detector_data = np.array(detector_data)

    # getting time data
    time = detector_data[:, 0]

    # separating low and high energy channel
    for iterator in energy_channels:
        low_channel, high_channel = iterator.split()
        low_energy_channel.append(float(low_channel))
        high_energy_channel.append(float(high_channel))

    low_energy_channel, high_energy_channel = np.array(low_energy_channel), np.array(high_energy_channel)

    number_of_low_energy_channels = len(np.where(low_energy_channel < energy_low)[0])
    number_of_high_energy_channels = len(np.where(high_energy_channel < energy_high)[0]) + 1

    # getting the data
    for x in range(number_of_low_energy_channels, number_of_high_energy_channels):
        data_rate += detector_data[:, 4 * x + 2]
        data_background += detector_data[:, 4 * x + 4]
        if errors:
            data_rate_error += detector_data[:, 4 * x + 3]
            data_background_error += detector_data[:, 4 * x * 5]

    # return
    return time, data_rate, data_background if not errors else time, data_rate, data_background, (data_rate_error, data_background_error)
