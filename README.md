# MonitorURLs
Using this script we will be able to MonitorURLs and export the metrics to Prometheus


- [Setup](#Setup)
    - [Softwares Used](#softwares-used)
    - [Prerequisites](#prerequisites)
    - [For Mac Users](#for-mac-users)
- [How to Use](#how-to-use)
    - 1. [Check Current Status](#check-current-status)  
    - 2. [Failover or Disable a Region](#failover-or-disable-a-region)  
    - 3. [Failback or Enable a Region](#failback-or-enable-a-region)


## Setup
### Dev
Setup your virutal env:

```shell
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

### Test

```
pip3 install -r requirements.txt
python3 -m unittest tests.unitTests1
python3 -m unittest tests.unitTests2
```

## Project Structure

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

### How to Use

# Dev
Setup your virutal env:

```shell
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

## Test

```
pip3 install -r requirements.txt
python3 -m unittest tests.unitTests1
python3 -m unittest tests.unitTests2
```

## Authors
Santhosh Deepu Patrayuni
