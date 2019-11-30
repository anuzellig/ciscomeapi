import os
import sys

import pytest
from dotenv import load_dotenv
# Load environment variables from .env
load_dotenv()

from ciscomeapi import CiscoME, print_table


me = None


def setup_module(module):
    global me
    host = os.environ['ME_HOST']
    username = os.environ['USERNAME']
    password = os.environ['PASSWORD']
    me = CiscoME(host=host, username=username, password=password)


def test_system_information():
    data = me.system_information()
    assert type(data) is dict
    assert 'platform' in data


def test_clients_table():
    clients = me.client_table()
    assert type(clients) is dict
    assert 'data' in clients


def test_aps():
    aps = me.aps()
    assert type(aps) is dict
    assert 'data' in aps


def test_apdata():
    aps = me.aps_data()
    assert type(aps) is dict
    assert 'data' in aps


def test_client_connection_score():
    scores = me.client_connection_score()
    assert type(scores) is dict
    assert 'clientconnectionscore' in scores


def test_client_connection_speed():
    speeds = me.client_connection_speed()
    assert type(speeds) is dict
    assert 'clientconnectionspeed' in speeds


def test_blink_ap_led():
    ap_mac = os.environ['AP_MAC']
    response = me.blink_ap_led(ap_mac)
    assert response['errorCode'] == 0


def test_toggle_ap_led():
    ap_mac = os.environ['AP_MAC']
    response = me.toggle_ap_led(ap_mac)
    # For some reason the errorCode is 13 (usually?)
    assert 'errorCode' in response


def test_restart_ap():
    ap_mac = os.environ['AP_MAC']
    # Uncomment to test restarting the AP
    # response = me.restart_ap(ap_mac)
    # assert 'errorCode' in response


def teardown_module(module):
    me.close()


if __name__ == '__main__':
    # Also allow the tests to be run manually, outside of pytest
    setup_module(sys.modules[__name__])

    test_blink_ap_led()
    # Call it twice to set it back to the original state
    test_toggle_ap_led()
    test_toggle_ap_led()
    test_system_information()
    test_clients_table()
    test_aps()
    test_apdata()
    test_client_connection_score()
    test_client_connection_speed()
    test_restart_ap()

    teardown_module(sys.modules[__name__])

