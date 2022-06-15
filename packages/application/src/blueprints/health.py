from flask import Blueprint

HEALTH_BLUEPRINT = Blueprint("root", __name__)


@HEALTH_BLUEPRINT.route("/health", )
def health_check():
    """ A simple check to see if the application is running """
    return {"status": "UP"}
