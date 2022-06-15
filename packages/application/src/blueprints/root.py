from flask import Blueprint, Response

ROOT_BLUEPRINT = Blueprint("root_blueprint", __name__)


@ROOT_BLUEPRINT.route("/hello", methods=['GET', 'POST'])
def hello_world():
    """ A simple check to see if the application is running """
    return Response('hello world!', status=200)
