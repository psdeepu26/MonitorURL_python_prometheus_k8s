import yaml
import os
#Importing the required libraries
import requests
from requests.exceptions import ConnectionError
from requests.adapters import HTTPAdapter

def readConfig(filename = "endpoints.yaml"):
    #filename = "config/endpoints.yaml"
    file_details = {}

    if os.path.exists(filename) and os.access(filename, os.R_OK):
        try:
            file_details = yaml.safe_load(open(filename))
        except Exception as exception:
            print("Unable to retrieve because of the reason : {}".format(exception))
        return file_details['URLS']


'''
Using HTTPAdapter as I need to retry the connection at least twice/n number of times before error handling it
Using ConnectionError for catching any connection Errors
'''
def checkURL(url):
    #create a HTTPAdapter (Transport Adapter) for the retries
    github_adapter = HTTPAdapter(max_retries=2)

    #Create a session to put persistence across retries/requests
    session = requests.Session()

    #Mounting the session with required parameters before requesting GET
    session.mount(url,github_adapter)

    try:
        #GET request to the site
        response = session.get(url=url)
    except ConnectionError as ce:
        print("Connection error found {}".format(ce))

    if response.status_code == 200:
        return (1, (response.elapsed.seconds)/1000)
    elif response.status_code == 503:
        return (0, (response.elapsed.seconds)/1000)
