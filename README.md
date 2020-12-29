# Python-CRUD

## About

Python-CRUD is a simple CRUD (eureka!) application used for storing people (relax, only their `name`s and `surname`s).
Basic functionality covers then:

- **C**reating new record
- **R**eading all existing records
- **U**pdating existing record
- **D**eleting existing record

## Branches

This repository stores multiple versions of application. For CLI versions release tags are prefixed as marked below:

- CLI application (local)
  - using CSV file as database (`cc` - CLI CSV)
  - using MySQL database (`cs` - CLI SQL)
- API using MySQL database (no version prefix)

## Prerequisites (API version)

Application requires the following installed on you machine:

- Python3
- mysql-connector-python
- flask
- flask_cors
- [flask_api](https://www.flaskapi.org/)

## How to run

- make sure you fulfill all the prerequisites
- create `credentials.py` file (based on `.example` file)
- start app via command:

```
python3 src/main.py
```
