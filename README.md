# MonitorURLs
A Simple HTTP Service Application which monitors a set of URLs/Endpoints and outputs a Prometheus format metrics for consumption
**Functional Requirements:**
* Using this script we will be able to MonitorURLs and export the metrics to Prometheus
* A Service which monitors URLs like (https://httpstat.us/503 & https://httpstat.us/200)
  * Service should query and get HTTP Status Code and Response Time in milliseconds
  * Service should run a Simple HTTP Service that produces metrics (/metrics) output to a Prometheus format for consumption
**Non-Functional Requirements:**
  * Dockerfile to build image
  * Kubernetes files to Deploy the Application and expose it as a Service
  * Unit Tests to test each module


## Contents
- [Setup](#Setup)
    - [Dev](#Dev)
    - [Test](#Test)
    - [Project Structure](#Project-Structure)
- [How to Use](#how-to-use)
    - 1. [Run Locally](#Run-Locally)  
    - 2. [Run using Docker](#Run-using-Docker)  
    - 3. [Run using Kubernetes](#Run-using-Kubernetes)
- [Unit Tests](#Unit-Tests)


## Setup
#### Dev
```shell
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Test
```
pip3 install -r requirements.txt
python3 -m unittest tests.unitTests1
python3 -m unittest tests.unitTests2
```

#### Project Structure
      .
      ├── Architecture.txt
      ├── Dockerfile
      ├── README.md
      ├── docs
      │   ├── docker_run.gif
      │   ├── k8s_run.gif
      │   └── run_locally.gif
      ├── k8s_src
      │   ├── app_namespace.yaml
      │   ├── monitorurls-app.yaml
      │   └── monitorurls-service.yaml
      ├── prometheus.yaml
      ├── requirements.txt
      ├── src
      │   ├── YamlOperations
      │   │   ├── __init__.py
      │   │   └── yaml_reader.py
      │   ├── __init__.py
      │   ├── config
      │   │   └── endpoints.yaml
      │   ├── main.py
      │   └── monitorURLs
      │       ├── __init__.py
      │       └── monitorURL.py
      └── tests
          ├── __init__.py
          ├── unitTests1.py
          ├── unitTests2.py
          └── unitTests3.py

## How to Use
### Run Locally
<img src='docs/run_locally.gif' title='Running Locally' width='' alt='Running Locally' />

### Run using Docker
<img src='docs/docker_run.gif' title='Running App using Docker' width='' alt='Running App using Docker' />

### Run using Kubernetes
<img src='docs/k8s_run.gif' title='Running App using Kubernetes' width='' alt='Running App using Kubernetes' />

## Unit Tests
```bash
 python -m unittest tests/unitTest_main.py
 python -m unittest tests/unitTest_helpers.py
```

### Author
Santhosh Deepu Patrayuni
