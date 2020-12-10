# Examples
To use these examples, first clone the repo:

    git clone https://github.com/anuzellig/ciscomeapi.git
Then install the Python modules used by the example, ideally after creating a [virtual environment](https://docs.python.org/3/tutorial/venv.html):

	cd examples/<example dir>
	pip install requirements.txt
    

## monitor_clients
Continuously polls the Mobility Express client table and sends a text message when a previously unseen client has joined. This script uses [Twilio](https://www.twilio.com) to send texts. Sign up for a free Twilio account [here](https://www.twilio.com/try-twilio). Then go to the [Twilio console](https://www.twilio.com/console) to get your unique Account SID and Auth Token. 

The configuration parameters are read from environment variables by the script. On Linux/macOS you can launch the script from the shell like this:

	TWILIO_SID=<Twilio account SID> TWILIO_TOKEN=<Twilio auth token> FROM_NUMBER=<Twilio phone number> TO_NUMBER =<phone number to sent the text to> ME_HOST =<Mobility Express hostname or IP> USERNAME=<Mobility Express username> PASSWORD=<Mobility Express password> python monitor-clients.py
	
Or on Windows:

	cmd /C "set TWILIO_SID=<Twilio account SID> && set TWILIO_TOKEN=<Twilio auth token> && set FROM_NUMBER=<Twilio phone number> && set TO_NUMBER=<phone number to sent the text to> && set ME_HOST =<Mobility Express hostname or IP> && set USERNAME=<Mobility Express username> && set PASSWORD=<Mobility Express password> python monitor-clients.py"

## which_ap
A simple Flask-based app that shows connectivity info about the client that the app is accessed from, e.g. which AP the client is connected to, client IP addresses, signal strength and quality, connection speed, frequency, etc. This can be very handy when troubleshooting connectivity issues as you can browse to the site from a mobile phone or other device to see these details, change location, and refresh the page to see updated info. 

![Image](https://github.com/anuzellig/ciscomeapi/blob/master/examples/which_ap/screenshots/screenshot.png?raw=true)

The configuration parameters are read from environment variables by the script. On Linux/macOS you can launch the script from the shell like this:

	ME_HOST=<Mobility Express hostname or IP> USERNAME=<Mobility Express username> PASSWORD=<Mobility Express password> python which-ap.py
	
Or on Windows:

	cmd /C "ME_HOST =<Mobility Express hostname or IP> && set USERNAME=<Mobility Express username> && set PASSWORD=<Mobility Express password> python monitor-which-ap.py"

And then from your wireless client browse to the IP address of the host that is running the script on port 5000. I.e. `http://<ip>:5000`