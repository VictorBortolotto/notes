from flask import Flask, request, Response
app = Flask(__name__)
from controller import user_controller, note_list_controller
from utils import routes

@app.route(routes.Routes.NEW_USER.value, methods=['POST'])
def signup():
  new_user = request.get_json()
  response = user_controller.UserController().create_user(new_user)
  return Response(response.response_to_json(),mimetype='application/json')

@app.route(routes.Routes.UPDATE_USER_PASSWORD.value, methods=['PATCH'])
def update_password(id):
  new_password = request.get_json()
  response = user_controller.UserController().update_password(new_password,id)
  return Response(response.response_to_json(),mimetype='application/json')

@app.route(routes.Routes.NEW_NOTE_LIST.value, methods=['POST'])
def new_note_list():
  new_note_list = request.get_json()
  response = note_list_controller.NoteListController().create_note_list(new_note_list)
  return Response(response.response_to_json(),mimetype='application/json')

@app.route(routes.Routes.DELETE_NOTE_LIST.value, methods=['DELETE'])
def delete_note_list(id):
  response = note_list_controller.NoteListController().delete_note_list(id)
  return Response(response.response_to_json(),mimetype='application/json')

@app.route(routes.Routes.UPDATE_NOTE_LIST_NAME.value, methods=['PATCH'])
def update_note_list_name(id):
  new_name = request.get_json()
  response = note_list_controller.NoteListController().update_note_list_name(new_name,id)
  return Response(response.response_to_json(),mimetype='application/json')