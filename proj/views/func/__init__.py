import os, sys
from colorama import Fore, Back, Style
from proj.models import db

def generate_status():
    return {
        "code": "ok",
        "message" : "",
        "data" : []
    }

def error_log() -> str:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    msg = exc_obj, fname, "Line number : ", exc_tb.tb_lineno
    print(Back.LIGHTRED_EX + "\n############################")
    print(Back.LIGHTRED_EX + "############################")
    print(msg)
    print("############################")
    print("############################\n")
    print(Style.RESET_ALL)
    db.session.rollback()
    return str(msg)