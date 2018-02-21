try:
    from zope.i18nmessageid import MessageFactory
    _ = MessageFactory('dynamore.policy')
except ImportError:
    _ = None
