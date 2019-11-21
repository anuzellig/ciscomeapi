=====
Usage
=====

To retrieve system information about the controller (platform, version, etc.)::

    from ciscomeapi import CiscoME
    me = CiscoME(host='controller IP', username='username', password='password')
    info = me.system_information()
    for key, value in info.items():
        print(f'{key}: {value}')

See the examples directory for more code samples.
