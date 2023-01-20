from flask import request, jsonify, Blueprint
from proj.views.goaty import diary
from proj.views import func
import json

bp_diary = Blueprint('bp_diary', __name__, url_prefix="/diary")

@bp_diary.route('/getDetail', methods=['POST'])
def getDiaryDetails():
    params = request.form['data']
    params = json.loads(params)
    # params = {"range": "20.1.23",
    #         "time": "9:00-10:00"}
    status = func.generate_status()
    try:
        status = diary.getDiaryDetails(params)
    except:
        status['message'] = func.error_log()
        status['code'] = 'error'

    return jsonify(status)

@bp_diary.route('/getTitle', methods=['POST'])
def getTitle():
    # params = request.form['data']
    # params = json.loads(params)
    params = {"range": "20.1.23"}
    status = func.generate_status()
    try:
        status = diary.getTitle(params)
    except:
        status['message'] = func.error_log()
        status['code'] = 'error'

    return jsonify(status)

@bp_diary.route('/updateDiary', methods=['POST'])
def updateDiary():
    params = request.form['data']
    params = json.loads(params)
    # params = {"range": "20.1.23",
    #         "time": "9:00-10:00"}
    status = func.generate_status()
    try:
        status = diary.updateDiary(params)
    except:
        status['message'] = func.error_log()
        status['code'] = 'error'

    return jsonify(status)

@bp_diary.route('/new', methods=['POST'])
def createNewDiary():
    # params = request.form['data']
    # params = json.loads(params)
    # params = {"range": "20.1.23",
    #         "time": "9:00-10:00"}
    status = func.generate_status()
    try:
        status = diary.createNewDiary()
    except:
        status['message'] = func.error_log()
        status['code'] = 'error'

    return jsonify(status)
