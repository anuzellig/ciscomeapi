import os

import pytest

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

def teardown_module(module):
    me.close()
