from msal import ConfidentialClientApplication
from decouple import config

app = ConfidentialClientApplication(
    config('CLIENT_ID'),
    authority="https://login.microsoftonline.com/" + config('TENANT_ID'),
    client_credential=config('CLIENT_SECRET')
    )

token = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
print(token)