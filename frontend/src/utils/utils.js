export function isEmptyOrNull(value) {
  return value === null || value === undefined || value === '';
}

export function isPasswordsEquals(password, confirmPassword) {
  return password === confirmPassword;
}


export function setLocalStorage(key,value){
  localStorage.setItem(key,value)
}

export function getLocalStorage(key){
  return localStorage.getItem(key)
}