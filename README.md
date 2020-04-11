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
        ├── prometheus.yaml
        ├── requirements.txt
        ├── src
        │   ├── YamlOperations
        │   │   └── yaml_reader.py
        │   ├── config
        │   │   └── endpoints.yaml
        │   ├── main.py
        │   └── monitorURLs
        │       └── monitorURL.py
        └── tests
        ├── unitTests1.py
        └── unitTests2.py

## How to Use
### How to Run Locally
<img src='docs/run_locally.gif' title='Running Locally' width='' alt='Running Locally' />

### Authors
Santhosh Deepu Patrayuni
