import os
import sys
import logging
from flask import Flask
from klue_microservice import API, letsgo


log = logging.getLogger(__name__)

app = Flask(__name__)

def start(port, debug):

    here = os.path.dirname(os.path.realpath(__file__))
    path_apis = os.path.join(here, "apis")

    api = API(
        app,
        port=port,
        debug=debug,
    )
    api.load_apis(path_apis)
    api.start(serve="helloworld")


letsgo(__name__, callback=start)
