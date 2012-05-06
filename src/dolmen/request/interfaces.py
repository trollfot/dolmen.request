# -*- coding: utf-8 -*-

from cromlech.browser.interfaces import ITypedRequest
from zope.component.interfaces import IObjectEvent, ObjectEvent
from zope.interface import implements


class ISkin(ITypedRequest):
    """Base interface for marker interfaces that define a skin

    by skin we mean different CSS or html layout...
    This is mainly for sematic purpose
    """


class IRequestTypedEvent(IObjectEvent):
    """Event triggered when request is typed with a new IRequestType
    """


class RequestTypedEvent(ObjectEvent):
    """IRequestTypedEvent implementation
    """
    implements(IRequestTypedEvent)
