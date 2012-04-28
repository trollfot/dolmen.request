from cromlech.browser.interfaces import ITypedHTTPRequest
from dolmen.request import register_request_type
from dolmen.request.decorators import request_type, skin
from dolmen.request.interfaces import ISkin
from zope.component import getUtility
from zope.interface.interfaces import IInterface


def test_decorators():
    @request_type('spam')
    class ISpamRequest(ITypedHTTPRequest):
        pass

    assert IInterface.providedBy(ISpamRequest)
    assert ISpamRequest.isOrExtends(ITypedHTTPRequest)
    assert getUtility(ITypedHTTPRequest, name='spam') == ISpamRequest

    @skin('foo')
    class IFooSkin(ISkin):
        pass

    assert IInterface.providedBy(IFooSkin)
    assert IFooSkin.isOrExtends(ITypedHTTPRequest)
    assert getUtility(ISkin, name='foo') == IFooSkin
    assert getUtility(ITypedHTTPRequest, name='foo') == IFooSkin

    register_request_type(ISpamRequest, 'other')
    assert getUtility(ITypedHTTPRequest, name='other') == ISpamRequest
    register_request_type(IFooSkin, 'other')
    assert getUtility(ITypedHTTPRequest, name='other') == IFooSkin
    

def test_interfaces():
    assert ISkin.isOrExtends(ITypedHTTPRequest)


