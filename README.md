## QA-DCFP
# DevOps Core Fundamental Project


This is a simple web application that an end user can interact with via their browser in order to to manage a cloud-hosted database of gardens and plants. It allows the user to create, read, update and delete entries for both of these categories as well as adding and removing plants from individual gardens.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Software:

-Linux system (Ubuntu 18.04 or similar)
    https://releases.ubuntu.com/18.04/

-MySQL installed either locally or on a cloud hosting service



### Installing


-Clone the repository to the machine you wish to run it on:
    git clone https://github.com/laportag/QA-DCFP.git

-Move into the QA-DCFP directory and run these commands to install python, python pip package installer and the python virtual environment venv: \
    > cd QA-DCFP/ \
    > sudo apt update \
    > sudo apt install python3 \
    > sudo apt install python3-venv  \
    > sudo apt install python3-pip 

-Run these commands to install and run the virtual environment: \
    > python3 -m venv venv \
    > source venv/bin/activate 

-Run these commands to install required packages to the virtual environment: \
    > pip3 install -r requirements.txt \
    > pip install gunicorn 

-Run the create.py file to initialise the database:
    > python3 create.py

-Create a user for the systemd service to run the webserver in the background:
    > sudo useradd --system garden

-Create a file called crud-garden.service containing the following:

    [Unit]
    Description=CRUD-Garden app
    After=network.target

    [Service]
    User=garden
    Type=Simple
    ExecStart=/[path to your repo]/venv/bin/gunicorn --chdir /[path to your repo] --workers=4 --bind=0.0.0.0:5000 app:app
    Environment=DATABASE_URI=mysql+pymysql://root:root@[your_database_ip]:3306/[your_database_name]
    Environment=SECRET_KEY=[your_secret_key]
    Restart=on-failure

    [Install]
    WantedBy=multi-user.target

- Copy the crud-garden.service to /etc/systemd/system/crud-garden.service

- Change the file permissions of the service file:
    > sudo chmod 777 /etc/systemd/system/crud-garden.service

## Start the service:  
    > sudo systemctl daemon-reload   
    > sudo systemctl start crud-garden 

-Open the webapp by entering the ip of the machine into a browser with the port 5000:  \
    [your_ip_address:5000] 


## Running the tests

Move into the QA-DCFP folder and run: \
    > python3 -m pytest --cov --cov-report term-missing \

### Unit Tests 

The Unit tests test the functions in the routes.py file. There is 99% coverage testing the entire app and 98% of the routes.py file. Pytest was used for the unit tests. The tests for creating and updating also work as integration testing due to the intrinsic nature of Flask microframework.


## Built With

-Flask \
-Python \
-Jenkins 

## Versioning

Git was used for version control.

## Author

Gregory Laporta  

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details 

## Acknowledgments

Thanks to the QA training team for imparting the requisite knowlegde to build this app.
