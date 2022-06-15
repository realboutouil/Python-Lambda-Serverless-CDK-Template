from flask import Flask


def init_app(app: Flask):
    """ Register all blueprints to the app """
    from .root import ROOT_BLUEPRINT
    from .health import HEALTH_BLUEPRINT

    app.register_blueprint(ROOT_BLUEPRINT)
    app.register_blueprint(HEALTH_BLUEPRINT)
