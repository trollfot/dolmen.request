from dolmen.request.interfaces import IRequestType
from zope.component import provideUtility


def register_request_type(iface, name, provides=IRequestType):
    """Declare that interface iface as name
    """
    provideUtility(iface, provides=provides, name=name)
