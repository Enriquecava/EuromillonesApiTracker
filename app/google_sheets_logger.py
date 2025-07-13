import datetime
import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), 'credentials.json')

# TODO: Put your actual Google Sheet ID here
SPREADSHEET_ID = 'YOUR_GOOGLE_SHEET_ID_HERE'
RANGE_NAME = 'Logs!A:C'  # Sheet named "Logs" with columns: Timestamp | Path | Error

credentials = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=credentials)

def log_error(path, error_text):
    now = datetime.datetime.utcnow().isoformat()
    values = [[now, path, error_text]]
    body = {'values': values}
    try:
        result = service.spreadsheets().values().append(
            spreadsheetId=SPREADSHEET_ID,
            range=RANGE_NAME,
            valueInputOption='RAW',
            insertDataOption='INSERT_ROWS',
            body=body
        ).execute()
        return result
    except Exception as e:
        print(f"Failed to log to Google Sheets: {e}")
        return None
