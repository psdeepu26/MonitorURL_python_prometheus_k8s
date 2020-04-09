import unittest
import os
import sys
import requests
import warnings
from pathlib import Path

from src.monitorURLs import monitorURL
from src.YamlOperations import yaml_reader
from src import main as source_code
my_obj = source_code.CustomCollector


if __name__ == '__main__':
    unittest.main()
