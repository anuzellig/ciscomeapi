from ciscomeapi import CiscoME
import os
from flask import Flask, render_template, request
import humanfriendly


app = Flask(__name__)

host = os.environ['ME_HOST']
username = os.environ['USERNAME']
password = os.environ['PASSWORD']

@app.route('/')
def hello():
    client_ip = request.environ['REMOTE_ADDR']
    print(client_ip)
    me = CiscoME(host=host, username=username, password=password)
    clients = me.client_table()   
    client_info = {}
    for client in clients['data']:
        if client['IP'] == client_ip:
            client_info['AP'] = client['AP']
            client_info['IPv4'] = client['IP']
            try:
                client_info['IPv6'] = client['I6']
            except KeyError:
                pass
            client_info['Signal Strength'] = str(client['SS']) + ' dBm'
            client_info['Signal Quality'] = str(client['SG']) + ' db'
            client_info['Connection Speed'] = str(client['SD']) + ' Mbps'
            client_info['Frequency'] = client['FB']
            client_info['Capabilitiy'] = client['PT']
            client_info['Device Type'] = client['devtype']
            client_info['SSID'] = client['SSID']
            client_info['AP Group'] = client['AG']
            client_info['Bytes Total'] = humanfriendly.format_size(client['bytes_total'], binary=True)
    
    return render_template('client_info.html', client_info=client_info)
            

if __name__ == '__main__':
    app.run(host='0.0.0.0')
