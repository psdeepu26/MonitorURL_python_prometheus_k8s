import unittest
import os
import sys
import requests
import warnings
from pathlib import Path

from src.monitorURLs import monitorURL
from src.YamlOperations import yaml_reader

class Test_YamlOperations(unittest.TestCase):
    def test_yaml_exists(self):
        print("--------------- Test Case : Endpoints File Exists ------------")
        self.yaml_file = os.getcwd() + "/src/config/endpoints.yaml"
        print(f"File Path : {self.yaml_file}")
        assert os.path.exists(self.yaml_file)
        print("------------------------ Test Case : Completed ------------------\n")

    def test_yaml_reader(self):
        print("--------------- Test Case : Return Endpoints details ------------")
        self.yaml_file = os.getcwd() + "/src/config/endpoints.yaml"
        endpoints = yaml_reader.readConfig(self.yaml_file)
        print(f"Endpoint Details : {endpoints}")
        self.assertEqual(endpoints, ['https://httpstat.us/503', 'https://httpstat.us/200'])
        print("------------------------ Test Case : Completed ------------------\n")

class Test_MonitorURL(unittest.TestCase):
    def test_success(self):
        print("----------- Test Case : Status Code for Success Test ------------")
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        http_response, response_latency = monitorURL.checkURL("https://httpstat.us/200")
        print(f"HTTP Status Code for \"https://httpstat.us/200\" : {http_response}")
        self.assertEqual(http_response, 1)
        print("------------------------ Test Case : Completed ------------------\n")

    def test_failure(self):
        print("----------- Test Case : Status Code for Failure Test -------------")
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        http_response, response_latency = monitorURL.checkURL("https://httpstat.us/503")
        print(f"HTTP Status Code for \"https://httpstat.us/503\" : {http_response}")
        self.assertEqual(http_response, 0)
        print("------------------------ Test Case : Completed ------------------\n")

if __name__ == '__main__':
    unittest.main()
