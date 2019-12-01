from flask import json, make_response
import logging

class ResponseProcessor:

    def __init__(self, debug=False):
        self.debug = debug


    def makeResponse(self, data, error=False):
        responseStr = json.dumps({
            'data': data,
            'error': error
        })

        if self.debug:
            logging.debug('ResponseProcessor: ' + responseStr)

        response = make_response(responseStr)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response