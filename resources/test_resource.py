from flask_restful import Resource
from flask import render_template, make_response


class TestResource(Resource):
    def get(self):
        return {'hello': 'world'}