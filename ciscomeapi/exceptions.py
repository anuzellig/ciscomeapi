# -*- coding: utf-8 -*-

"""
exceptions
~~~~~~~~~~~~~~~~~~~

This module contains CiscoMobilityExpressSDK exceptions
"""

class CiscoMobilityExpressAPIException(Exception):
    def __init__(self, *args, **kwargs):
        self.session = kwargs.pop('session', None)
        Exception.__init__(self,*args,**kwargs)


class AuthenticationError(CiscoMobilityExpressAPIException):
    """An HTTP authentication error occurred."""

class NotFoundError(CiscoMobilityExpressAPIException):
    """An HTTP authentication error occurred."""