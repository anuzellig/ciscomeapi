# -*- coding: utf-8 -*-

"""
monitor-clients
~~~~~~~~~~~~~~~~~~~

Poll Cisco Mobility express and send a text alert when a previously unknown client joins the network
"""

import time
import os

from twilio.rest import Client

from ciscomeapi import CiscoME


# Get Twilio account SID, auth token, and the phone number to send texts to from environment variables
account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['TWILIO_TOKEN']
from_number = os.environ['FROM_NUMBER']
to_number = os.environ['TO_NUMBER']

host = os.environ['ME_HOST']
username = os.environ['USERNAME']
password = os.environ['PASSWORD']

def send_text(client):
    twilio = Client(account_sid, auth_token)

    message = twilio.messages \
                .create(
                    body=f'New client detected: {client["HN"]} {client["devtype"]}',
                    from_=from_number,
                    to=to_number
                    )


if __name__ == '__main__':
    seen_clients = []

    me = CiscoME(host=host, username=username, password=password)
    first_run = True
    while True:
        print('Checking clients...')
        clients = me.client_table()
        for client in clients['data']:
            mac = client['macaddr']
            if mac not in seen_clients:
                seen_clients.append(client['macaddr'])
                if not first_run:
                    print(f'New client detected: {client["HN"]}')
                    send_text(client)
        
        first_run=False
        time.sleep(5)