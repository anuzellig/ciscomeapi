# -*- coding: utf-8 -*-

"""
helpers
~~~~~~~~~~~~~~~~~~~

Helper functions used by the other modules
"""

import logging
from json.decoder import JSONDecodeError

import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from .exceptions import AuthenticationError, NotFoundError


def request(me, method: str, endpoint: str, parameters: dict={}, extra_params={}, json={}, data={}):
    url = me.base_url + endpoint
    all_params = {**parameters, **extra_params}
    if json:
        response = me.session.request(method, url, params=all_params, json=json)
    elif data:
        response = me.session.request(method, url, params=all_params, data=data)
    else:
        response = me.session.request(method, url, params=all_params)
    
    if response.status_code == 401:
            # For some reason you need to connect twice
            response = me.session.get(url)
            if response.status_code == 401:
                raise AuthenticationError('401 Invalid username or password', session=me.session)
    
    if response.status_code == 404:
        raise NotFoundError('404 Page not found', session=me.session)
    
    try:
        return response.json()
    except JSONDecodeError:
        return response.text