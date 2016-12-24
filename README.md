# Project Title

In order to implement the web application for expense tracking, I am using Django which is a web framework in Python.

<!-- ## Code Example

Show what the library does as concisely as possible, developers should be able to figure out **how** your project solves their problem by looking at the code example. Make sure the API you are showing off is obvious, and that your code is short and concise. -->

## Prerequisites

* The setup guide provided in the next section is for Ubuntu 16.10
* Python 2.7 is used for all purposes

## Installation

* Install pip using the command below
```
sudo apt install python-pip
```
* We need virtual environment in order to run Django without any version issues
```
pip install virtualenv
```
* Change to suitable directory where you need to place virtual environment
```
cd /to/suitable/directory
```
* Install virtual environment with name *venv*
```
virtualenv venv
```
* Change directory to *venv*
```
cd venv
```
* Activate the virtual environment. This is necessary before starting installation of any softwares.
```
source bin/activate
```
Note that you can deactivate the environment using the command
```
deactivate
```
* Install MySQL server if it is not present already
```
sudo apt install mysql-server
```
* Requirements.txt file contains all relevant software installations for this project. You can install all at once using pip.
```
pip install -r requirements.txt
```

* Next step is to create user for our Django database.
```
mysql -u root -p
```
* In MySQL shell, type the following command:
```
CREATE USER 'dev_user'@'localhost' IDENTIFIED BY 'abcd1234';
```
Note that the password and username used here is the same as in django settings.py file and hence any changes to the same will make the software not function as desired.

* We grant all permissions to this user for creating, updating and deleting the database and records.
```
GRANT ALL PRIVILEGES ON * . * TO 'dev_user'@'localhost';
```
* Exit from the mysql shell
```
exit from the mysql shell
```
* Login to the created *dev_user* in mysql 
```
mysql -u dev_user -p
```
* Create database for our project.
```
create database gigster_db;
```
* Extract the contents of gigster-expense-tracker.zip in the virtual environment directory venv.
* Change to directory where the contents of the zip file are extracted.
* Perform initial migrations: 
```
python manager.py migrate --fake-initial
```
* Any other migrations afterwards will be reflected here.
```
python manage.py makemigrations
```
* Finally migrate all the changes.
```
python manage.py migrate
```
* Run the django server to start using the web app
```
python manage.py runserver 
```

* Open the Firefox Browser and type 127.0.0.1:8000 which is the localhost ip address. Note that I have not tested the UI on Chrome or other browsers.


## Tests

I was not able to perform any of the integration or unit tests because of lack of time and no prior experience in doing so.

## Tasks Completed
* Login, Register and Logout features are implemented properly.
* I was able to perform CRUD operations for managing the expenses.

## Tasks Incomplete
* Admin role not implemented
* Different report generation not implemented.
* No Integration or Unit testing performed.
* Interface not tested across web browsers.

## Project Folder Structure
* **gigster_core** contains all the core files for the project which includes base template
* **account** contains all the source code related to user accounts.
* **expenses** contains all the source code for performing CRUD operations.
* **gigster** is the main project and the above mentioned are the applications under this project.
