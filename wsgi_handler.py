# wsgi_handler.py
from app import app
from serverless_wsgi import handle

def handler(event, context):
    return handle(event, context, app)
