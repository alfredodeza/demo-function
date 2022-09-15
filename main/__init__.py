import logging
from flask import Flask, redirect
import azure.functions as func

app = Flask(__name__)


# code from Azure functions
def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.WsgiMiddleware(app.wsgi_app).handle(req, context)

# code for Flask Application

@app.route("/")
def index():
    logging.info("flask app about to do a redirect")
    return redirect("https://portal.azure.com", code=301)
