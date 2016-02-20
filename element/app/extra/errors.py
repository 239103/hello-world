from . import extra

@extra.app_errorhandler(404)
def page_not_found(e):
    return "404\n"

@extra.app_errorhandler(500)
def internal_server_error(e):
    return "500\n"