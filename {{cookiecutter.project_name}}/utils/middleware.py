import logging
logger = logging.getLogger('utils.middleware')


class LoggingMiddleWare(object):
    """
    Used to log usefull things about request and session
    """

    def process_request(self, request):
        
        logger.critical("LoggingMiddleWare|user|%s" % request.user)
        if request.user.is_authenticated():
            logger.debug("LoggingMiddleWare|user|member_type_display|%s" % request.user.get_member_type_display())
            logger.debug("LoggingMiddleWare|user|is_company|%s" % request.user.is_company)
        logger.debug("LoggingMiddleWare|request|method|%s" % request.method)


class CookieMiddleWare(object):
    """
    Used to log usefull things about request and session
    """

    def process_request(self, request):
        if not hasattr(request.session, 'cookie'):
            request.session['cookie'] = True
        if request.user.is_authenticated:
            request.session['cookie'] = False
