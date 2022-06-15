#!/usr/bin/env python3

from src import create_app

flask_app = create_app()
flask_app.run(host='0.0.0.0', port=5500)
