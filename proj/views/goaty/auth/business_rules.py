from proj.models import model
import bcrypt

def check_email(email):
    emailValid = model.User.query.filter(model.User.email==email).first()
    return emailValid

def check_password(user, password):
    passValid = bcrypt.checkpw(password.encode(), user.password.encode())
    return passValid