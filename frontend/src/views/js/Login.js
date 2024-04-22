import { openToast } from "../../common/js/toast";
import loginService from "../../services/login.service";
import { isEmptyOrNull, setLocalStorage } from "../../utils/utils";

export async function onClickSignIn() {
  let email = document.getElementById('email').value;
  let password = document.getElementById('password').value;
  
  if(isEmptyOrNull(email) || isEmptyOrNull(password)) {
    openToast('warn', "Please fill all the fields before continue.")
    return;
  }

  let user = {
    email: email,
    password: password
  }

  let response = await loginService.login(user)
  if(response.statusCode === 200){
    setLocalStorage('token',response.obj.token)
    document.location.href = '/home'
  }else{
    openToast('error', response.description)
  }
}
