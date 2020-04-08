import yaml
import os

def readConfig():
    filename = "config/endpoints.yaml"
    file_details = {}

    if os.path.exists(filename) and os.access(filename, os.R_OK):
        try:
            file_details = yaml.safe_load(open(filename))
        except Exception as exception:
            print("Unable to retrieve because of the reason : {}".format(exception))
        return file_details['URLS']

def main():
    file_details = readConfig()
    print(file_details)

if __name__ == '__main__':
    main()
