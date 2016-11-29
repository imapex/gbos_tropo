import requests
import os
from requests.auth import HTTPBasicAuth

"""
Utilities for installing a tropo application using the Tropo REST API
"""


CONTENT_HEADER = {'Content-Type': "application/json"}
TROPO_URL = "https://api.tropo.com/v1"



def get_applications():
    url = TROPO_URL + "/applications"
    resp = requests.get(url,
                        headers=CONTENT_HEADER,
                        auth=HTTPBasicAuth(TROPO_USER, TROPO_PASS))
    applications = resp.json()
    return applications



def create_application(name, url):
    """

    :param name: str name of the application
    :param url: str url for the application
    :return: str url for application endpoint

    """
    tropo_url = TROPO_URL + '/applications'
    data = {
    "name": name,
    "voiceUrl": url,
    "messagingUrl": url,
    "platform":"webapi",
    "partition":"staging"
    }
    resp = requests.post(tropo_url,
                         headers=CONTENT_HEADER,
                         auth=HTTPBasicAuth(TROPO_USER, TROPO_PASS),
                         json=data)
    appurl = resp.json()["href"]
    page = requests.get(appurl,
                        headers=CONTENT_HEADER,
                        auth=HTTPBasicAuth(TROPO_USER, TROPO_PASS))
    app = page.json()
    return app

def add_number(application, prefix):
    data = {
    "type":"number",
    "prefix":prefix
    }

    tropo_u = TROPO_URL + "/applications/%s/addresses" % (application["id"])
    page = requests.post(tropo_u,
                         headers=CONTENT_HEADER,
                         auth=HTTPBasicAuth(TROPO_USER, TROPO_PASS),
                         json=data)
    if page.status_code == 200:
        # Success

        addressurl = page.json()["href"]
        page = requests.get(addressurl,
                            headers=CONTENT_HEADER,
                            auth=HTTPBasicAuth(TROPO_USER, TROPO_PASS))
        address = page.json()
        return address
    else:
        return "Error: Failed to add number to application"


def add_token(application, type="messaging"):
    data = {
    "type":"token",
    "channel": type
    }

    tropo_u = TROPO_URL + "/applications/%s/addresses" % (application["id"])
    page = requests.post(tropo_u,
                         headers=CONTENT_HEADER,
                         auth=HTTPBasicAuth(TROPO_USER, TROPO_PASS),
                         json=data)

    # {"href":"https://api.tropo.com/v1/applications/123456/addresses/token/12345679f90bac47a05b178c37d3c68aaf38d5bdbc5aba0c7abb12345d8a9fd13f1234c1234567dbe2c6f63b"}
    if page.status_code == 200:
        # Success
        # print page
        addressurl = page.json()["href"]
        page = requests.get(addressurl,
                            headers = CONTENT_HEADER,
                            auth=HTTPBasicAuth(TROPO_USER, TROPO_PASS))
        address = page.json()
        return address
    else:
        return "Error: Failed to add number to application"





if __name__ == '__main__':
    from argparse import ArgumentParser
    import os, sys
    from pprint import pprint
    # Setup and parse command line arguments
    parser = ArgumentParser("GBOS Tropo Interaction Bot")
    parser.add_argument(
        "-n", "--name", help="Name of the Tropo application", required=True
    )
    parser.add_argument(
        "-a", "--app", help="Address for this tropo apps scripts", required=True
    )
    parser.add_argument(
        "-u", "--user", help="Tropo Username", required=True
    )
    parser.add_argument(
        "-p", "--tropopass", help="Tropo Password", required=True
    )
    parser.add_argument(
        "--tropoprefix", help="Tropo Number Prefix", required=False
    )

    args = parser.parse_args()
    TROPO_USER = args.user
    TROPO_PASS = args.tropopass
    # Create new app in tropo only if it does not already exist

    tropo_apps = [a['name'] for a in get_applications()]

    if args.name not in tropo_apps:
        print "Creating New tropo application for {}".format(args.name)
        app = create_application(args.name, args.app)
        token = add_token(app)['token']
        number = add_number(app, args.tropoprefix)

    else:
        print "Tropo Application already exists"
        app = [item for item in get_applications() if item['name'] == args.name][0]
        app = requests.get(app['href'],
                               headers=CONTENT_HEADER,
                               auth=HTTPBasicAuth(TROPO_USER, TROPO_PASS)).json()
        if 'token' not in app.keys():
            print "Creating Token for existing tropo application"
            token = add_token(app)['token']

    print "Your Application Token is: {}".format(token)
