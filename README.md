# MonitorURLs
Using this script we will be able to MonitorURLs and export the metrics to Prometheus


- [Installation](#installation)
    - [Softwares Used](#softwares-used)
    - [Prerequisites](#prerequisites)
    - [For Mac Users](#for-mac-users)
- [How to Use](#how-to-use)
    - 1. [Check Current Status](#check-current-status)  
    - 2. [Failover or Disable a Region](#failover-or-disable-a-region)  
    - 3. [Failback or Enable a Region](#failback-or-enable-a-region)


## Installation
### Softwares Used

* **Programming Language** - Python 3.*
* **Python Libraries
* ***prometheus_client
* ***requests
* ***pyyaml

### Prerequisites

* Check your current Python version
* eiamCli (https://github.intuit.com/EIAM/eiamCLI)
* prometheus_client (https://pypi.org/project/prometheus_client/)
* pyyaml (https://pypi.org/project/PyYAML/)

```
python --version
```

### For Mac Users:
These instructions can be used under a Virtual environment or even under your mac.

Please refer **requirements.txt** in this Github repository

```
pip3 install -r requirements.txt
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

Run the below command to get the basic script usage

```
python3 Failover_v5.0.py -h
usage: Failover_v5.0.py [-h] -s {sms,voice} -e {d2d,qal,prf,e2e,prd} -r
                        {west,east} [-enable | -disable | -status]

Enable/Disable Regions

optional arguments:
  -h, --help            show this help message and exit
  -s {sms,voice}, --service {sms,voice}
                        Provide the Service Name
  -e {d2d,qal,prf,e2e,prd}, --env {d2d,qal,prf,e2e,prd}
                        Provide the Environment
  -r {west,east}, --region {west,east}
                        Provide Region (west/east)
  -enable               To Enable Health Check
  -disable              To Disable Health Check
  -status               To Check the current status of Health Check

```


### Check Current Status

It provides the current state of the Route53 Endpoints along with Health checks and their status (Success/Failure). Subsequently it will also provide information

To get Current State for one of our service on a specific region to a particular environement, you can do following
```
	Failover_v5.0.py -s [SERVICE NAME] -e [ENVIRONMENT NAME] -r [REGION] -status
```

Sample Command: python3 Failover_v5.0.py -s voice -e prf -r west -status

<img src='resources/current_status.gif' title='current status' width='' alt='Current Status' />

### Failover or Disable a Region

<img src='resources/prod-change-1.gif' title='prod-change-1' width='' alt='prod-change-1' />

It gives the ability to Disable a Health check for a given service on a particular enivorment to a said reagion (which we are currently doing using manually)

To get Current State for one of our service on a specific region to a particular environement, you can do following
```
	Failover_v5.0.py -s [SERVICE NAME] -e [ENVIRONMENT NAME] -r [REGION] -disable
```

Sample Command: python3 Failover_v5.0.py -s voice -e prf -r west -disable

<img src='resources/disable_region.gif' title='disable region' width='' alt='Disable Region' />

### Failback or Enable a Region

<img src='resources/prod-change-1.gif' title='prod-change-1' width='' alt='prod-change-1' />

It gives the ability to Enable a Health check for a given service on a particular enivorment to a said reagion (which we are currently doing using manually)

To get Current State for one of our service on a specific region to a particular environement, you can do following
```
	Failover_v5.0.py -s [SERVICE NAME] -e [ENVIRONMENT NAME] -r [REGION] -enable
```

Sample Command: python3 Failover_v5.0.py -s voice -e prf -r west -enable

<img src='resources/enable_region.gif' title='enable region' width='' alt='Enable Region' />

## Authors
Santhosh Deepu Patrayuni
