from proj.views.goaty.auth import business_process

def login(params):
    status = business_process.login_user(params)
    return status

def register(params):
    status = business_process.register_user(params)
    return status