from lambdarado import start


def get_app():
    # this function must return WSGI app, e.g. Flask
    from src import create_app
    return create_app()


start(get_app)
