class AkiyoshiException(Exception):
    """Base Exception
    """
    pass
class AkiyoshiDbException(AkiyoshiException):
    """Database Exception
    """
    pass
class AkiyoshiLibException(AkiyoshiException):
    """Lib Exception
    """
    pass
class AkiyoshiServiceException(AkiyoshiException):
    """Service Exception
    """
    pass
class AkiyoshiControllerException(AkiyoshiException):
    """Controller Exception
    """
    pass
class AkiyoshiTemplateException(AkiyoshiException):
    """Template Exception
    """
    pass

