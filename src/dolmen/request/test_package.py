# -*- coding: utf-8 -*-

from cromlech.browser.interfaces import ITypedRequest
from dolmen.request import register_request_type
from dolmen.request.decorators import request_type, skin
from dolmen.request.interfaces import ISkin
from zope.component import getUtility
from zope.interface.interfaces import IInterface


def test_decorators():

    @request_type('spam')
    class ISpamRequest(ITypedRequest):
        pass

    assert IInterface.providedBy(ISpamRequest)
    assert ISpamRequest.isOrExtends(ITypedRequest)
    assert getUtility(ITypedRequest, name='spam') == ISpamRequest

    @skin('foo')
    class IFooSkin(ISkin):
        pass

    assert IInterface.providedBy(IFooSkin)
    assert IFooSkin.isOrExtends(ITypedRequest)
    assert getUtility(ISkin, name='foo') == IFooSkin
    assert getUtility(ITypedRequest, name='foo') == IFooSkin

    register_request_type(ISpamRequest, 'other')
    assert getUtility(ITypedRequest, name='other') == ISpamRequest
    register_request_type(IFooSkin, 'other')
    assert getUtility(ITypedRequest, name='other') == IFooSkin


def test_interfaces():
    assert ISkin.isOrExtends(ITypedRequest)
