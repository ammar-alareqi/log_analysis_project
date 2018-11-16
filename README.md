# Log Analysis
This is the first project solution for the udacity course FSND.

## Overview
This project aims to help students applying SQL knowledge they get through the course. Students are asked to use SQL statements to observe data from a database and apply some aggregations. 

## Requirements
To run this project you need to have:
* Python 3.
* VirtualBox.
* Vagrant.
* Git.

## How to run this project
To run the code you need to:
1. Install **Python 3**.
2. Install **VirtualBox**.
3. Install **Vagrant**.
4. Download and install [Udacity Virtual Machine](https://github.com/udacity/fullstack-nanodegree-vm).
5. Download the [database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdat
a.zip).
6. Move the database file to the **Udacity Virtual Machine** forlder and unzip it. 
7. Open **Git Bash** termial and launch the vagrant using the following command:
```
 $ vagrant up
```
8. Log into the system using:
```
$ vagrant ssh
```
9. Load the data from the database using:
```
 psql -d news -f newsdata.sql
```
10. Connect to the database using:
```
psql -d news -f newsdata.sql
```
11. Run the code file using **Python 3**:
```
python3 log-analysis.py
```