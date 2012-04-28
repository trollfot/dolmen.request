from cromlech.io.interfaces import IRequestType
from dolmen.request.interfaces import ISkin
from cromlech.browser.interfaces import IHTTPException
from zope.component import provideUtility
from zope.interface.interfaces import IInterface


def register_request_type(iface, name, provides=IRequestType):
    """Declare that interface iface as name
    """
    provideUtility(iface, provides=provides, name=name)


def request_type(name):
    """Class decorator to register an IRequestType under name
    """
    def decorate(iface):
        assert IInterface.providedBy(iface)
        assert iface.isOrExtends(IRequestType)
        register_request_type(iface, name)

    return decorate


def skin(name):
    """Class decorator to register an ISkin under name
    """
    def decorate(iface):
        assert IInterface.providedBy(iface)
        assert iface.isOrExtends(ISkin)
        register_request_type(iface, name, provides=ISkin)

    return decorate
