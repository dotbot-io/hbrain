from flask import Flask, current_app, g, jsonify, Response, request, current_app, redirect, url_for
from . import api_2_0 as api

from flask_cors import CORS, cross_origin
from flask_json import JsonError, json_response, as_json
from flask_restful import Api, Resource, reqparse

from ..tasks.ros import run_shell

rest_api = Api(api)

@api.before_request
def option_autoreply():
    if request.method == 'OPTIONS':
        resp = current_app.make_default_options_response()

        headers = None
        if 'ACCESS_CONTROL_REQUEST_HEADERS' in request.headers:
            headers = request.headers['ACCESS_CONTROL_REQUEST_HEADERS']

        h = resp.headers

        # Allow the origin which made the XHR
        h['Access-Control-Allow-Origin'] = '*'
        # Allow the actual method
        h['Access-Control-Allow-Methods'] = h['Allow']
        # Allow for 10 seconds
        h['Access-Control-Max-Age'] = 86400

        h["Access-Control-Allow-Credentials"] = False;
        h["Access-Control-Allow-Headers"] = "X-Requested-With, X-HTTP-Method-Override, Content-Type, Accept";
        h["Access-Control-Allow-Content-Type"] = "text/event-stream; charset=utf-8"
        # We also keep current headers
        if headers is not None:
            h['Access-Control-Allow-Headers'] = headers

        return resp

class HBRProcess(Resource):
    decorators = [cross_origin(origin="*", headers=["content-type", "autorization"], methods=['GET', 'PUT'])]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('cmd')
        args = parser.parse_args()

        cmd = args['cmd'].split()
        proc = run_shell.delay(cmd)
        return 'ok'

rest_api.add_resource(HBRProcess, '/shell_cmd')
