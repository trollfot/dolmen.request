# -*- coding: utf-8 -*-

import grokcore.component as grok

from cromlech.browser import ITraverser
from cromlech.io import IRequest
from dolmen.request.interfaces import ITypedHTTPRequest, RequestTypedEvent
from zope.component import queryUtility
from zope.event import notify
from zope.interface import alsoProvides, Interface


class RequestTypeTraverser(grok.MultiAdapter):
    grok.provides(ITraverser)
    grok.name('request_type')
    grok.adapts(Interface, IRequest)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def traverse(self, ns, name):
        request_type = queryUtility(ITypedHTTPRequest, name=name)
        if request_type is not None:
            alsoProvides(self.request, request_type)
            notify(RequestTypedEvent(self.request))
            return self.context
        return None
