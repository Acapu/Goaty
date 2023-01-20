from flask import request, jsonify, Blueprint
from proj.views.goaty import auth
from proj.views import func

import json
bp_auth = Blueprint('bp_auth', __name__, url_prefix='/auth')



@bp_auth.route('/login', methods=['POST'])
def login():
    params = request.form['data']
    params = json.loads(params)
    status = func.generate_status()
    try:
        status = auth.login(params)
    except:
        status['message'] = func.error_log()
        status['code'] = 'error'

    return jsonify(status)

@bp_auth.route('/register', methods=["POST"])
def register():
    params = request.form['data']
    params = json.loads(params)
    status = func.generate_status()
    try:
        status = auth.register(params)
    except:
        status['message'] = func.error_log()
        status['code'] = 'error'

    return jsonify(status)


