from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

SAMPLE_SPREADSHEET_ID = '1Y0mSqV5uCWjqg1l8FZZT2lQxBc2cJNxQonDWm-rC7wc'

table_range = {"Timing": "A:Q",
               "Data":"A:W",
               "Информация по иону": "A:O"}


credentials = service_account.Credentials.from_service_account_file('credentials.json', scopes=SCOPES)
service = build('sheets', 'v4', credentials=credentials)
sheet = service.spreadsheets()

def GetRangeByName(NameList, Range: list = None):
    if Range == None:
        range = table_range[NameList]
    else:
        range = ":".join(Range)
    return NameList + "!" + range

def GetPieceTable(List:str, Range: list):
    try:
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=GetRangeByName(List, Range)).execute()
        values = result.get('values')

        if not values:
            print('No data found.')
            return

        return values
    except Exception as e:
        print(e)

def GetValuesFromList(NameList):
    try:
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=GetRangeByName(NameList)).execute()
        values = result.get('values')

        if not values:
            print('No data found.')
            return

        return values
    except Exception as e:
        print(e)


