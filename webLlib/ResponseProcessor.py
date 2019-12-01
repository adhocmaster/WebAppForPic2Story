from flask import jsonify
import logging

class ResponseProcessor:

    def __init__(self, debug=False):
        self.debug = debug


    def makeResponse(self, data, error=False):
        response = jsonify({
            'data': data,
            'error': error
        })

        if self.debug:
            logging.debug('ResponseProcessor: ' + str(response))
        return response