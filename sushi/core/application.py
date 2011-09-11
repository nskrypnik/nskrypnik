# -*- coding: utf-8 -*-

'''

@author: Niko Skrypnik
Created: 6-09-2011
filedescr: Base sushi application

'''

def load_middleware(self):
    """
    Populate middleware lists from settings.MIDDLEWARE_CLASSES.

    Must be called after the environment is fixed (see __call__ in subclasses).
    """
    from django.conf import settings
    from django.core import exceptions
    self._view_middleware = []
    self._template_response_middleware = []
    self._response_middleware = []
    self._exception_middleware = []

    request_middleware = []
    for middleware_path in settings.MIDDLEWARE_CLASSES:
        try:
            mw_module, mw_classname = middleware_path.rsplit('.', 1)
        except ValueError:
            raise exceptions.ImproperlyConfigured('%s isn\'t a middleware module' % middleware_path)
        try:
            mod = import_module(mw_module)
        except ImportError, e:
            raise exceptions.ImproperlyConfigured('Error importing middleware %s: "%s"' % (mw_module, e))
        try:
            mw_class = getattr(mod, mw_classname)
        except AttributeError:
            raise exceptions.ImproperlyConfigured('Middleware module "%s" does not define a "%s" class' % (mw_module, mw_classname))
        try:
            mw_instance = mw_class()
        except exceptions.MiddlewareNotUsed:
            continue

        if hasattr(mw_instance, 'process_request'):
            request_middleware.append(mw_instance.process_request)
        if hasattr(mw_instance, 'process_view'):
            self._view_middleware.append(mw_instance.process_view)
        if hasattr(mw_instance, 'process_template_response'):
            self._template_response_middleware.insert(0, mw_instance.process_template_response)
        if hasattr(mw_instance, 'process_response'):
            self._response_middleware.insert(0, mw_instance.process_response)
        if hasattr(mw_instance, 'process_exception'):
            self._exception_middleware.insert(0, mw_instance.process_exception)

    # We only assign to this when initialization is complete as it is used
    # as a flag for initialization being complete.
    self._request_middleware = request_middleware

from django.core.handlers.wsgi import WSGIHandler



class Application(WSGIHandler):
    pass
    
