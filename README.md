[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/anuzellig/ciscomeapi)
# An Unofficial Cisco Mobility Express Python Module
This Python module allows you to interact with a [Cisco Mobility Express](https://www.cisco.com/c/en/us/solutions/enterprise-networks/mobility-express/index.html) controller to retrieve data, make configuration changes, etc. Features currently include:

* Getting information about associated clients, such as a list of clients with details, connection scores, and connection speeds
* Getting a list of and details about registered APs
* Restarting APs
* Blinking or toggling AP LEDs
* System information, such as the Mobility Express version, platforms, etc. 



## Installation
`pip install ciscomeapi`

## Quickstart
To retrieve system information about the controller (platform, version, etc.):

```python
from ciscomeapi import CiscoME
me = CiscoME(host='controller IP', username='username', password='password')
info = me.system_information()
for key, value in info.items():
    print(f'{key}: {value}')
``` 

## Examples
To use these examples, first clone the repo:

    git clone https://github.com/anuzellig/ciscomeapi.git
Then install the Python modules used by the example, ideally after creating a [virtual environment](https://docs.python.org/3/tutorial/venv.html):

	cd examples/<example dir>
	pip install requirements.txt
    

### monitor_clients
Continuously polls the Mobility Express client table and sends a text message when a previously unseen client has joined. This script uses [Twilio](https://www.twilio.com) to send texts. Sign up for a free Twilio account [here](https://www.twilio.com/try-twilio). Then go to the [Twilio console](https://www.twilio.com/console) to get your unique Account SID and Auth Token. 

The configuration parameters are read from environment variables by the script. On Linux/macOS you can launch the script from the shell like this:

	TWILIO_SID=<Twilio account SID> TWILIO_TOKEN=<Twilio auth token> FROM_NUMBER=<Twilio phone number> TO_NUMBER =<phone number to sent the text to> ME_HOST =<Mobility Express hostname or IP> USERNAME=<Mobility Express username> PASSWORD=<Mobility Express password> python monitor-clients.py
	
Or on Windows:

	cmd /C "set TWILIO_SID=<Twilio account SID> && set TWILIO_TOKEN=<Twilio auth token> && set FROM_NUMBER=<Twilio phone number> && set TO_NUMBER=<phone number to sent the text to> && set ME_HOST =<Mobility Express hostname or IP> && set USERNAME=<Mobility Express username> && set PASSWORD=<Mobility Express password> python monitor-clients.py"

### which_ap
A simple Flask-based app that shows connectivity info about the client that the app is accessed from, e.g. which AP the client is connected to, client IP addresses, signal strength and quality, connection speed, frequency, etc. This can be very handy when troubleshooting connectivity issues as you can browse to the site from a mobile phone or other device to see these details, change location, and refresh the page to see updated info. 

<div style="text-align: center;">
<img src="https://github.com/anuzellig/ciscomeapi/blob/master/examples/which_ap/screenshots/screenshot.png?raw=true" width="500" >
</div>

The configuration parameters are read from environment variables by the script. On Linux/macOS you can launch the script from the shell like this:

	ME_HOST=<Mobility Express hostname or IP> USERNAME=<Mobility Express username> PASSWORD=<Mobility Express password> python which-ap.py
	
Or on Windows:

	cmd /C "ME_HOST =<Mobility Express hostname or IP> && set USERNAME=<Mobility Express username> && set PASSWORD=<Mobility Express password> python monitor-which-ap.py"

And then from your wireless client browse to the IP address of the host that is running the script on port 5000. I.e. `http://<ip>:5000`

### reboot_aps
Reboots all the APs sequentially, waiting for each one to come back up before moving on to the next. The hostname, username, and password are read from environment variables by the script (see the `which_ap` example above).

 
## Documentation
[https://cisco-mobility-express-python-api.readthedocs.io](https://cisco-mobility-express-python-api.readthedocs.io/en/latest/)
 
## Requirements
The library has been tested with Python 3.5 and later. Although some of the examples require Python 3.6 or later because of the use of f-strings. 

## Implementation Notes
`gen-enpoints.py` programmatically generates the base functions for each API call in `_me_api.py` by interrogating the Mobility Express Web UI and identifying and parsing potential calls from the front-end to the back-end. Then these functions are front-ended by simple manually written-methods in `ciscomeapi.py` to provide more context and niceties like docstrings. So far just a few of these methods have been created, more coming soon. 

This project is not affiliated with or supported by Cisco Systems in any way. It uses private, undocumented, and unsupported web calls and therefore may not work as expected and may cease to function with a future update of Mobility Express. Caveat emptor!
