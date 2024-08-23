from flask import Blueprint
from src.injection.dependency_injection import container
from src.controllers.test_controller import Test_controller


test_controller:Test_controller = container.Test_controller()

test_route = Blueprint('test',__name__)

@test_route.route('/all', methods=['GET'])
def find_all():
    return test_controller.find_all()

@test_route.route('/<id>', methods=['GET'])
def find_by_id(id):
    return test_controller.find_by_id(id)

@test_route.route('/', methods=['POST'])
def add():
    return test_controller.add()

@test_route.route('/<id>', methods=['PUT'])
def update(id):
    return test_controller.update(id)

@test_route.route('/<id>', methods=['DELETE'])
def delete(id):
    return test_controller.delete(id)