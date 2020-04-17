"""
This script runs the BackendWebAPI application using a development server.
"""

from os import environ
from __init__ import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'https://health-tracker.azurewebsites.net')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
