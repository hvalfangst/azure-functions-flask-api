import azure.functions as func
from flask_api import app


def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    """Each request is redirected to the WSGI handler, which serves our Flask API.
    """
    return func.WsgiMiddleware(app.wsgi_app).handle(req, context)
