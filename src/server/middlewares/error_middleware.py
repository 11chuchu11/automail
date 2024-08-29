from flask import jsonify

class ErrorMiddleware:
    def __init__(self, app):
        self.app = app
        self.register_error_handlers()

    def register_error_handlers(self):
        @self.app.errorhandler(404)
        def not_found_error(error):
            return jsonify({
                'error': 'Not Found',
                'message': 'The requested resource could not be found'
            }), 404

        @self.app.errorhandler(500)
        def internal_server_error(error):
            return jsonify({
                'error': 'Internal Server Error',
                'message': 'An unexpected error occurred on the server'
            }), 500

        @self.app.errorhandler(Exception)
        def handle_exception(error):
            response = {
                'error': type(error).__name__,
                'message': str(error)
            }
            if isinstance(error, ValueError):
                response['message'] = 'A value error occurred'
            return jsonify(response), 500