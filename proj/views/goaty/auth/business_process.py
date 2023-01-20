from proj.views.goaty.auth import business_rules
from proj.views import func
from proj.models import model, db

def login_user(params):
    status = func.generate_status()
    try:
        validEmailUser = business_rules.check_email(params['email'])
        if validEmailUser:
            validPass = business_rules.check_password(validEmailUser, params['password'])
            if not validPass:
                raise Exception("Wrong password")

        status['message'] = "user validated"
    except:
        status['message'] = func.error_log()
        status['code'] = 'error'

    return status

def register_user(params):
    status = func.generate_status()
    try:
        user = model.User(username=params['username'],
                        email=params['email'],
                        password=params['password'])
        db.session.add(user)
        db.session.commit()
    except:
        status['message'] = func.error_log()
        status['code'] = 'error'

    return status