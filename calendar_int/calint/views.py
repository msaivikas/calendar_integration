from django.shortcuts import render
from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'calint'

# Create your views here.
# def main():
#     creds = None
#     if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json', SCOPES)
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         with open('token.json', 'w') as token:
#             token.write(creds.to_json())
#     # now = datetime.date.today()
#     service = build('calendar', 'v3', credentials=creds)
#     events = service.events().list(calendarId='primary', singleEvents=True, orderBy = 'startTime').execute()
#     all_events.append(events)
#     pprint(events)
#     # print(*all_events, sep='\n')

