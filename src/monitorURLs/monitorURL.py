'''
Using HTTPAdapter as I need to retry the connection at least twice/n number of times before error handling it
Using ConnectionError for catching any connection Errors
'''

#Importing the required libraries
import requests
from requests.exceptions import ConnectionError
from requests.adapters import HTTPAdapter

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

def main():
    url = "https://httpstat.us/503"
    print(checkURL(url))

if __name__ == '__main__':
    main()
