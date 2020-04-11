import time
import sys
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from prometheus_client import start_http_server, Counter

c = Counter('num_requests', 'The number of requests.')

class CustomCollector(object):
    def collect(self):
        endpoints = yaml_reader.readConfig()
        for endpoint in endpoints:
            startTime = time.time()
            http_status, response_latency = monitorURL.checkURL(endpoint)
            latencyTime = time.time() - startTime

            exportStatus = GaugeMetricFamily("sample_external_url_up", 'status Code', labels=['endpoint'])
            exportStatus.add_metric([endpoint], http_status)
            yield exportStatus

            exportLatency = GaugeMetricFamily("sample_external_url_response_ms", 'URl Response in ms', labels=['endpoint'])
            exportLatency.add_metric([endpoint], response_latency)
            yield exportLatency

            exportRTT = GaugeMetricFamily("sample_external_url_rtt_response_ms", 'URl Response in ms', labels=['endpoint'])
            exportRTT.add_metric([endpoint], latencyTime)
            yield exportRTT


if __name__ == '__main__':
    from monitorURLs import monitorURL
    from YamlOperations import yaml_reader
    try :
        start_http_server(8000)
        print("Site is up now at http://<ipaddress>:8000")
        REGISTRY.register(CustomCollector())
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('')
        print('\033[1m' + '\nKeyboard Interruption..Calm Down')
        print('\033[1m' + '\nExiting !!!!\n')
        print('\033[0m')
        sys.exit()
    except Exception as Error:
        print('')
        print('\033[1m' + f'\nReceived Error : {Error}')
        print('\033[1m' + '\nExiting !!!!\n')
        print('\033[0m')
        sys.exit()
else:
    from .monitorURLs import monitorURL
    from .YamlOperations import yaml_reader
