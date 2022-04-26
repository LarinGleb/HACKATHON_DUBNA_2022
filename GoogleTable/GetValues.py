from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

SPREADSHEET_ID = '1Y0mSqV5uCWjqg1l8FZZT2lQxBc2cJNxQonDWm-rC7wc'

table_range = {"Информация по иону": "A:O", 
                "Timing": "A:R",
               "Data":"A:AH",
               }


credentials = service_account.Credentials.from_service_account_file('credentials.json', scopes=SCOPES)
service = build('sheets', 'v4', credentials=credentials)
sheet = service.spreadsheets()

def GetValuesByValue(Value):
    information = []
    for list in table_range.keys():
        for values in GetValuesFromList(list):
            if values[0] == Value:
                information.extend(values)
                break
    return information


def GetRangeByName(NameList, Range: list = None):
    if Range == None:
        range = table_range[NameList]
    else:
        range = ":".join(Range)
    return NameList + "!" + range

def GetPieceTable(List:str, Range: list):
    try:
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=GetRangeByName(List, Range)).execute()
        values = result.get('values')
        if not values:
            print('No data found.')
            return

        return values
    except Exception as e:
        print(e)

def GetValuesFromList(NameList):
    try:
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=GetRangeByName(NameList)).execute()
        values = result.get('values')

        if not values:
            print('No data found.')
            return

        return values
    except Exception as e:
        print(e)


