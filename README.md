# CSCI4560
 External Database application for CSCI4560 Assignment 5


Author: John Lasseter
CSCI 4560 Assignment 5
Due: Nov. 25 2019

**Description**: Manipulate the SUPPLIER-PART-SHIPMENT database programmatically

**Video of execution**: https://www.cs.mtsu.edu/~c8070423/CSCI4560_P5.mp4

**Setup instructions**: 

Executed in an Ubuntu 18.04 VM

Developed on OSX with PyCharm, but it's not needed for execution

SQL: MySQL

Python: 3.6, but 3+ should work

MySQL admin obtained from: https://dev.mysql.com/downloads/mysql/
MySQL connector obtained from: https://dev.mysql.com/downloads/connector/python/

Installed with:

`sudo apt install ./mysql-apt-config_0.8.14-1_all.deb`

Then setup a root user, with highly secure password 'password'. 
Created database named "CSCI4560"

`sudo apt install ./mysql-connector-python-py3_8.0.18-1ubuntu18.04_all.deb`

All other python sql connectors had to be pip uninstalled before correct connection.

To run (see video): `python3.6 main.py`