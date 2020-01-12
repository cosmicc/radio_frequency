===============
Radio Frequency
===============

.. image:: https://img.shields.io/github/v/release/cosmicc/radio_frequency.svg?include_prereleases 
        :target: https://github.com/cosmicc/radio_frequency
        
.. image:: https://img.shields.io/pypi/v/radio_frequency.svg
        :target: https://pypi.python.org/pypi/radio_frequency

.. image:: https://pyup.io/repos/github/cosmicc/radio_frequency/python-3-shield.svg
        :target: https://pyup.io/repos/github/cosmicc/radio_frequency/
        :alt: Python 3
        
.. image:: https://img.shields.io/github/license/cosmicc/radio_frequency.svg
        :target: https://github.com/cosmicc/radio_frequency

.. image:: https://img.shields.io/travis/cosmicc/radio_frequency.svg
        :target: https://travis-ci.org/cosmicc/radio_frequency

.. image:: https://readthedocs.org/projects/radio-frequency/badge/?version=latest
        :target: https://radio-frequency.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/cosmicc/radio_frequency/shield.svg
     :target: https://pyup.io/repos/github/cosmicc/radio_frequency/
     :alt: Updates



Radio Frequency Information


* Free software: MIT license
* Documentation: https://radio-frequency.readthedocs.io.


Features
--------

Returns information about a radio frequency (US only for now)

Band Description__
Band Type__
ITU Abbreviation__
ITU Number__
IEEE Band Name__
NATO Band Name__
Broadcast__
Amateur Radio Details (Type, Class, Max Power), - Not yet Implimented__
Wavelength Range, - Not yet Implimented__
Meters__

Usage
-------
Frequency format examples:__
89.900.000, 89900000, 89,900,000__

Command Line:__
radio-frequency <frequency>__

Python:__
from radio_frequency import radio_frequency as rf

rf.frequency_info(frequency)

returns a dictionary:__
{ frequency: '89.900 Mhz', band_desc: 'Very High Frequency', band_type: None, meters: None, itu_abbr: 'VHF', itu_num: 8, ieee: 'VHF', nato: 'A', broadcast: 'FM Radio' }


Todo
-------

Convert to dictionary lookups instead of if/thens__
Amateur Radio Details__
Wavelength Range__
WIFI bandtypes__
Cellular bandtpes__
Sattelite bandtypes__
GMRS & CB Specific Channels__

Credits
-------

Ian Perry (ianperry99@gmail.com)
