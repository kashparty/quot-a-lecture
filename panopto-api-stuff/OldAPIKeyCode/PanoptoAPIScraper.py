from bs4 import BeautifulSoup
import requests
from http.cookiejar import MozillaCookieJar
import webbrowser
import json
from urllib.request import urlopen
from panopto_oauth2 import PanoptoOAuth2
from base64 import b64encode
from hashlib import sha256

def main():
    password = getPassword()
    url = "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#isSharedWithMe=true"

    client_name = "AnaLecture"
    client_id = "4697ef53-d3fe-4bf0-8c13-ae3300dc1f6e"
    client_secret = "54ENB734CHapmulZdgNcBoIZzVZU+nHXszY+cZxBytg="
    username = "nrb21"
    server = "imperial.cloud.panopto.eu"
    base_url = "https://{0}/Panopto/api/".format(server)
    application_key = client_id

    username = "nrb21"



    oauth2 = PanoptoOAuth2(server, client_id, client_secret, False)
    requests_session = requests.Session()
    #authcode = b64encode(sha256((username.lower() + '|' + application_key.lower()).encode('utf-8')).digest())
    # requests_session.headers.update({"Authorization": "Bearer"+oath2.get_access_token_resource_owner_grant(username,authcode)})
    access_token = oauth2.get_access_token_authorization_code_grant()
    #requests_session.headers.update({"Authorization": "Bearer"+oath2.get_access_token_authorization_code_grant()})





































def getPassword():
    return "Haha nice try - I would never put my password in plaintext in a public GitHub repo, who do you think I am?"
try:
    main()
except Exception as e:
    print(e)
input("End of program!")
