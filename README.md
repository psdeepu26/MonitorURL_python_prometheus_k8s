# MonitorURLs
Using this script we will be able to MonitorURLs and export the metrics to Prometheus


- [Setup](#Setup)
    - [Dev](#Dev)
    - [Test](#Test)
    - [Project Structure](#Project-Structure)
- [How to Use](#how-to-use)
    - 1. [Locally](#Locally)  
    - 2. [Using Docker](#Using-Docker)  
    - 3. [Using Kubernetes](#Using-Kubernetes)


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
### How to Run Locally
<img src='docs/run_locally.gif' title='Running Locally' width='' alt='Running Locally' />

### How to Run using Docker
<img src='docs/docker_run.gif' title='Running App using Docker' width='' alt='Running App using Docker' />

### How to Run using Kubernetes
<img src='docs/k8s_run.gif' title='Running App using Kubernetes' width='' alt='Running App using Kubernetes' />

### Authors
Santhosh Deepu Patrayuni
