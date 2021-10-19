import os
import sys
import time

from ciscomeapi import CiscoME


def main():
    host = os.getenv('ME_HOST')
    username = os.getenv('ME_USERNAME')
    password = os.getenv('ME_PASSWORD')
    if not all([host, username, password]):
        print('Missing environment variables')
        sys.exit(1)

    me = CiscoME(host=str(host), username=str(username), password=str(password))
    aps = me.aps()['data']
    aps_by_mac = dict(zip([x['macaddr'] for x in aps], [x for x in aps]))
    for mac, ap in aps_by_mac.items():
        ap_name = ap['name']
        # Skip the ISR
        if ap_name == 'Basement-ISR1111':
            continue

        me.restart_ap(mac)

        # Wait for AP to vanish from the list of APs
        # TODO: add a timeout
        while True:
            aps_alive = [x['macaddr'] for x in me.aps()['data']]
            if mac in aps_alive:
                print(f'Waiting for AP to go down: {ap_name}')
                time.sleep(5)
            else:
                print(f'AP has gone down: {ap_name}')
                break

        # Wait for AP to come back up
        # TODO: add a timeout
        while True:
            aps_alive = [x['macaddr'] for x in me.aps()['data']]
            if mac not in aps_alive:
                print(f'Waiting for AP to come back: {ap_name}')
                time.sleep(5)
            else:
                print(f'AP has come back: {ap_name}')
                print('Delaying 30 seconds for it to become operational')
                time.sleep(30)
                break

    print('Done!')

if __name__ == '__main__':
    main()
