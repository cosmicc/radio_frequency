#!/usr/bin/env python3

"""Tests for `radio_frequency` package."""

import pytest
from radio_frequency import radio_frequency

# from radio_frequency import radio_frequency

TEST_BROADCAST = (
         ('89.900.000', 'FM Radio'),
         ('155.500', 'Longwave AM'),
         ('55.500.000', 'VHF TV'),
         ('510.000.000', 'UHF TV'),
         )


TEST_IEEE = (
         ('1.525.500.000', 'L'),
         ('17.155.000.000', 'Ku'),
         ('34.567.121.000', 'Ka'),
         ('105.157.100.000', 'W'),
         )


TEST_BANDTYPE = (
         ('132.000.000', 'Air Band'),
         ('166.580.000', 'Marine VHF'),
         ('27.405.000', 'CB'),
         ('462.562.500', 'GMRS'),
         )


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_types():
    result = radio_frequency.frequency_info('89.900.000')
    assert isinstance(result, dict)
    result = radio_frequency.frequency_info(900.000)
    assert isinstance(result, dict)
    result = radio_frequency.frequency_info(1000000)
    assert isinstance(result, dict)


def test_broadcast():
    template = '{0:20s} | {1:20s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'BROADCAST', '=='))
    for (freq, expected) in TEST_BROADCAST:
        result = radio_frequency.frequency_info(freq)
        ok = 'OK' if result['broadcast'] == expected else 'XX'
        print(template.format(str(freq), str(result['broadcast']), ok))
        assert result['broadcast'] == expected


def test_ieee():
    template = '{0:20s} | {1:20s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'IEEE', '=='))
    for (freq, expected) in TEST_IEEE:
        result = radio_frequency.frequency_info(freq)
        ok = 'OK' if result['ieee'] == expected else 'XX'
        print(template.format(str(freq), str(result['ieee']), ok))
        assert result['ieee'] == expected


def test_bandtype():
    template = '{0:20s} | {1:20s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'BANDTYPE', '=='))
    for (freq, expected) in TEST_BANDTYPE:
        result = radio_frequency.frequency_info(freq)
        ok = 'OK' if result['band_type'] == expected else 'XX'
        print(template.format(str(freq), str(result['band_type']), ok))
        assert result['band_type'] == expected
