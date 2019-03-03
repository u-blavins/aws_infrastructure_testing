# AWS Infrastructure Testing
Scripts to test AWS services infrastructure. Testing that is to be conducted before setting up infrastructure.

## Branching
When adding a feature, branch off the develop branch by switching from `master` to `develop` and then creating a feature branch.

## Prerequisites
- Python 3.x
- Pip
- Virtualenv
- AWS Account

## Setup
```
> virutalenv -p Python3 venv
> source venv/bin/activate
> pip install -r requirements.txt
```
> This setup is for local testing, you will not need to setup a virtual enviornment if using Jenkins.

## Usage
To be included...

## Testing
To run the pytests locally, enter the following command in a terminal:
```$xslt
> python -m pytest
```
To run a test coverage report, use this:
```$xslt
> python -m --cov-report html --cov {package/file}
```
