=====
About
=====

This is an unofficial Cisco Mobility Express Python API which allows you to interact with a Cisco Mobility Express controller to retrieve data, make configuration changes, etc. 

 
Implementation Notes
--------------------

`gen-enpoints.py` programmatically generates the base functions for each API call in `_me_api.py` by interrogating the Mobility Express Web UI and identifying and parsing potential calls from the front-end to the back-end. Then these functions are front-ended by simple manually written-methods in `ciscomeapi.py` to provide more context and niceties like docstrings. So far just a few of these methods have been created, more coming soon. 

The API was generated from and tested against Mobility Express version 8.10.105.0. 

This project is not affiliated with or supported by Cisco Systems in any way. It uses private, undocumented, and unsupported web calls and therefore may not work as expected and may cease to function with a future update of Mobility Express. Caveat emptor!
