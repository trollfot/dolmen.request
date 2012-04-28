from cromlech.io.interfaces import IRequestType
from dolmen.request import register_request_type
from dolmen.request.interfaces import ISkin
from zope.interface.interfaces import IInterface


def request_type(name):
    """Class decorator to register an IRequestType under name
    """
    def decorate(iface):
        assert IInterface.providedBy(iface)
        assert iface.isOrExtends(IRequestType)
        register_request_type(iface, name)
        return iface

    return decorate


def skin(name):
    """Class decorator to register an ISkin under name
    """
    def decorate(iface):
        assert IInterface.providedBy(iface)
        assert iface.isOrExtends(ISkin)
        register_request_type(iface, name, provides=ISkin)
        return iface

    return decorate
