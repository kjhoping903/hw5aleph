"""Small, offline Flask handover exercise."""
import os
from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)
    app.config['APP_PLACE'] = os.environ.get('APP_PLACE', 'UNKNOWN')

    @app.get('/api/hello')
    def hello():
        return jsonify(message='Hello', version='v2', place=app.config['APP_PLACE'])

    @app.get('/api/health')
    def health():
        return jsonify(status='ok', service='t05-stateless-handover')

    @app.get('/api/info')
    def info():
        return jsonify(project='T05 Stateless Handover Lab', runtime='Flask', handover=True)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify(error='not_found'), 404

    return app
