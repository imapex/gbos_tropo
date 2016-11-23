import requests
import os
from requests.auth import HTTPBasicAuth
CONTENT_HEADER = {'Content-Type': "application/json"}
TROPO_URL = "https://api.tropo.com/v1"

def get_applications():
    tropo_u = TROPO_URL + "/applications"
    resp = requests.get(tropo_u,
                        headers=CONTENT_HEADER,
                        auth=HTTPBasicAuth(os.getenv("TROPO_USER"), os.getenv("TROPO_PASS")))
    applications = page.json()
    return applications

print get_applications()

def create_application(name, voiceurl=None, messagingurl=None):
    """

    :param name: str name of the application
    :param voiceurl: str url for voice requests
    :param messagingurl: str url for SMS requests
    :return: str url for application endpoint

    """