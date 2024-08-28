from flask import Blueprint
from src.injection.dependency_injection import container
from src.controllers.user_type_controller import User_Type_Controller

user_type_controller:User_Type_Controller = container.User_Type_Controller()
user_type_route = Blueprint("user-type", __name__)

@user_type_route.route('/all', methods=['GET'])
def find_all():
  return user_type_controller.find_all()

@user_type_route.route('/<id>', methods=['GET'])
def find_by_id(id):
  return user_type_controller.find_by_id(id)

@user_type_route.route('/', methods=['POST'])
def add():
    return user_type_controller.add()

@user_type_route.route('/<id>', methods=['PUT'])
def update(id):
    return user_type_controller.update(id)

@user_type_route.route('/<id>', methods=['DELETE'])
def delete(id):
    return user_type_controller.delete(id)