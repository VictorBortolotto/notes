from service import user_service

class UserController():
  def __init__(self):
    self.user_service = user_service.UserService()

  def create_user(self,user):
    return self.user_service.create_user(user)

  def update_password(self,new_password,id):
    return self.user_service.update_user_password(new_password,id)