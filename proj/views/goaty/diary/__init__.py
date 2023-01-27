from googleapiclient.discovery import build

from google.oauth2 import service_account
from proj.views import func
import datetime

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'secret.json'
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# # If modifying these scopes, delete the file token.json.
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1nxFrY_lfi844vnZjieDeNLQqsd9vZWekOjG5ZZ6SlLk'
RANGE_NAME = '18.1.23!C5'

rangeColumn = {"9:00-10:00": "!C5:F5",
                "10:00-11:00": "!C6:F6",
                "11:00-12:00": "!C7:F7",
                "12:00-1:00": "!C8:F8",
                "1:00-2:00": "!C9:F9",
                "2:00-3:00": "!C10:F10",
                "3:00-4:00": "!C11:F11",
                "4:00-5:00": "!C12:F12"}

def getDiaryDetails(params):
    status = func.generate_status()
    try:
        RANGE_NAME = params['range'] + rangeColumn[params['time']]
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                    range=RANGE_NAME).execute()
        values = result.get('values', [])
        status['data'] = values
    except:
        status['message'] = func.error_log()
        status['code'] = 'error'

    return status

def getTitle(params):
    status = func.generate_status()
    try:
        RANGE_NAME = params['range'] + "!C2"
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID, 
                                            includeGridData=False).execute()
        # values = result.get('values', [])
        status['data'] = result
    except:
        status['message'] = func.error_log()
        status['code'] = 'error'

    return status

def updateDiary(params):
    status = func.generate_status()
    try:
        RANGE_NAME = params['range'] + rangeColumn[params['time']]
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        updateValue = [
            [params['activity'], params['objective'], params['result'], params['note']]
        ]
        request = sheet.values().update(
            spreadsheetId=SPREADSHEET_ID,
            range=RANGE_NAME, 
            valueInputOption="USER_ENTERED", 
            body={"values": updateValue}).execute()

        status['data'] = request
    except:
        status['message'] = func.error_log()
        status['code'] = 'error'

    return status


def createNewDiary():
    status = func.generate_status()
    try:
        # RANGE_NAME = params['range'] + rangeColumn[params['time']]
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        
        rangeExist = None
        try:
            rangeExist = sheet.values().get(spreadsheetId=SPREADSHEET_ID, 
                                                        range=datetime.datetime.now().strftime("%d.%m.%y"), 
                                                        valueRenderOption="FORMATTED_VALUE", 
                                                        dateTimeRenderOption="FORMATTED_STRING").execute()
        except:
            print("range doesnt exist")

        if rangeExist:
            raise Exception("Range already exist")
        
        request = sheet.sheets().copyTo(
            spreadsheetId=SPREADSHEET_ID, 
            sheetId=1904020906, 
            body={'destination_spreadsheet_id' : SPREADSHEET_ID}).execute()
        
        # update sheet title
        newSheetName = {
            "requests" : [{
                "updateSheetProperties" : {
                    "properties" : {
                        "title": datetime.datetime.now().strftime("%d.%m.%y"),
                        "sheetId": request['sheetId']
                    },
                    "fields": "Title"
                }
            }]
        }
        update = sheet.batchUpdate(spreadsheetId=SPREADSHEET_ID, body=newSheetName).execute()


        # update title in the sheet
        RANGE_NAME = str(datetime.datetime.now().strftime("%d.%m.%y")) + "!C2"
        updateValue = [
            [datetime.datetime.now().strftime("%d.%m.%y")]
        ]
        request = sheet.values().update(
            spreadsheetId=SPREADSHEET_ID,
            range=RANGE_NAME, 
            valueInputOption="USER_ENTERED", 
            body={"values": updateValue}).execute()

        status['data'] = [request, update]
    except:
        status['message'] = func.error_log()
        status['code'] = 'error'

    return status