export function isEmptyOrNull(value) {
  return value === null || value === undefined || value === '';
}

export function isPasswordsEquals(password, confirmPassword) {
  return password === confirmPassword;
}
