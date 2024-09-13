from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from user_service import UserService
from models_user import User


app = Flask(__name__)
api = Api(app, version='1.0', title='Notification Service API',
          description='A simple Notification Service API')

ns_notifications = api.namespace('notifications', description='Notification operations')

user_service = UserService()

# Models for Swagger
user_model = api.model('User', {
    'email': fields.String(required=True, description='The user email'),
    'frequency': fields.String(required=True, description='Notification frequency', enum=['weekly', 'biweekly', 'monthly', 'semiannual'])
})

# New Notification Endpoints
@ns_notifications.route('/register')
class Register(Resource):
    @ns_notifications.expect(user_model)
    @ns_notifications.response(201, 'User registered successfully')
    @ns_notifications.response(400, 'Invalid input')
    def post(self):
        data = request.get_json()
        email = data.get('email')
        frequency = data.get('frequency')

        if not email or frequency not in ['weekly', 'biweekly', 'monthly', 'semiannual']:
            return {"error": "Invalid input"}, 400

        user = user_service.register_user(email, frequency)
        return {"message": "User registered successfully", "user": user.email}, 201

@ns_notifications.route('/unsubscribe')
class Unsubscribe(Resource):
    @ns_notifications.param('email', 'The user email')
    @ns_notifications.response(200, 'User unsubscribed successfully')
    @ns_notifications.response(400, 'Invalid input')
    def delete(self):
        email = request.args.get('email')

        if not email:
            return {"error": "Invalid input"}, 400

        success = user_service.unsubscribe_user(email)
        if success:
            return {"message": "User unsubscribed successfully"}, 200
        return {"error": "User not found"}, 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)
