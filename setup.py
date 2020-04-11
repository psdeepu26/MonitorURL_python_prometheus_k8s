import os
import re
from setuptools import setup

with open('README.md') as f:
    readme = f.read()


setup(
      name='MonitorURL_python_prometheus_k8s',
      version='0.1.0',
      description='Python Script to monitor URLs and export metrics to Prometheus',
      long_description=readme,
      url='https://github.com/psdeepu26/MonitorURL_python_prometheus_k8s',
      author='Santhosh Deepu Patrayuni',
      author_email='deepu4social@gmail.com',
      install_requires=['prometheus_client'],
      packages=['requests', 'pyyaml'],
      zip_safe=False
)
