# -*- coding: utf-8 -*-

from dolmen.request.interfaces import ITypedHTTPRequest
from zope.component import provideUtility


def register_request_type(iface, name, provides=ITypedHTTPRequest):
    """Declare that interface iface as name
    """
    provideUtility(iface, provides=provides, name=name)
