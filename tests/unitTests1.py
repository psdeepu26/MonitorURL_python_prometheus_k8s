import unittest
import sys
import requests
import warnings
from itertools import islice

from http_server_mock import HttpServerMock

from src import main as source_code
testObject = source_code.CustomCollector

class Test_MainProgram(unittest.TestCase):
    def test_http_server_mock(self):
        print("------------------ Test Case : HTTP Server Mock ------------------")
        app = HttpServerMock(__name__, is_alive_route="/metrics")

        @app.route("/", methods=["GET"])
        def index():
            return "Prometheus Metrics"

        with app.run("localhost", 8000):
            r = requests.get("http://localhost:8000/")
        print("------------------------ Test Case : Completed ------------------\n")

    def test_customcollector_instantiation(self):
        print("------------------------ Test Case : Custom Collector Instantiation ------------------")
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        try:
            source_code.REGISTRY.register(source_code.CustomCollector())
            print("Collector Class Instantiated Successfully")
        except Exception as Error:
            print(f"Collector Class Couldn't Instantiated with {Error}")
        print("------------------------ Test Case : Completed ------------------\n")

    def test_GaugeMetricFamily_single_output(self):
        print("------------ Test Case : GaugeMetricFamily Single Output ----------")
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        values = testObject.collect(self)
        self.assertIn(str(type(tuple(islice(values, 1))[0])), "<class 'prometheus_client.metrics_core.GaugeMetricFamily'>")
        print(f"prometheus_client metrics_core GaugeMetricFamily Output: {tuple(islice(values, 1))}")
        print("------------------------ Test Case : Completed ------------------\n")

    def test_GaugeMetricFamily_complete_output (self):
        print("------------ Test Case : GaugeMetricFamily Complete Output ----------")
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        values = testObject.collect(self)
        self.assertIn(str(type(tuple(islice(values, 3))[0])), "<class 'prometheus_client.metrics_core.GaugeMetricFamily'>")
        print(f"prometheus_client metrics_core GaugeMetricFamily Output: {tuple(islice(values, 3))}")
        print("------------------------ Test Case : Completed ------------------\n")

if __name__ == '__main__':
    unittest.main()
