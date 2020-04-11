import yaml
import os

current_path = os.getcwd()
if 'src' in current_path:
    file_name = current_path + "/config/endpoints.yaml"
elif 'tests' in current_path:
    file_name = os.path.normpath(os.getcwd() + os.sep + os.pardir) + "/src/config/endpoints.yaml"
elif 'app' in current_path:
    file_name = "config/endpoints.yaml"
else:
    file_name = "src/config/endpoints.yaml"

def readConfig(filename = file_name):
    #filename = "config/endpoints.yaml"
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
