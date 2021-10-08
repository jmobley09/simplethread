# Simple Thread
Technical Exercise for Simple Thread

## Prerequisites
### ENV
1. Code was developed on Ubuntu Linux Distro but in order to ensure that code could run anywhere no shebangs were added, just in case the python binary was located in a different location
2. Please ensure that you have python 3.8 and pip3 installed as a minimum on the system

### Pip
1. to install the needed dependencies for the app to run please run `pip3 install -r requirements.txt` from within the `src` folder

## Execution
### Start App
To run the app navigate to the `src` folder and run the following
```sh
python3 main.py
```
### Instructions
The app will ask for the following information:
1. project name
2. project start date (accepted format of mm/dd/yyyy)
3. project end date (accepted format of mm/dd/yyyy)
4. project city type (accepts `high` or `low`)

- After entering in this information it will ask if there additional projects
- A user may enter as many projects in as wanted as long as the start date of the next project is after the end date of the project before it. 