# An Unofficial Cisco Mobility Express Python API
This Python API allows you to interact with a Cisco Mobility Express controller to retrieve data, make configuration changes, etc. 

## Installation
`pip install git+https://github.com/anuzellig/cisco-mobility-express-python-api.git`

## Example Usage
To retrieve system information about the controller (platform, version, etc.):

```python
from ciscomeapi import CiscoME
me = CiscoME(host='controller IP', username='username', password='password')
info = me.system_information()
for key, value in info.items():
    print(f'{key}: {value}')
``` 
 See the `examples` directory for more code samples.
 
## Documentation
[https://cisco-mobility-express-python-api.readthedocs.io](https://cisco-mobility-express-python-api.readthedocs.io/en/latest/)
 
## Requirements
The library has been tested with Python 3.5 and later. Although some of the examples require Python 3.6 or later because of the use of f-strings. 

## Implementation Notes
`gen-enpoints.py` programmatically generates the base functions for each API call in `_me_api.py` by interrogating the Mobility Express Web UI and identifying and parsing potential calls from the front-end to the back-end. Then these functions are front-ended by simple manually written-methods in `ciscomeapi.py` to provide more context and niceties like docstrings. So far just a few of these methods have been created, more coming soon. 

The API was generated from and tested against Mobility Express version 8.10.105.0. 

This project is not affiliated with or supported by Cisco Systems in any way. It uses private, undocumented, and unsupported web calls and therefore may not work as expected and may cease to function with a future update of Mobility Express. Caveat emptor!