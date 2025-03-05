# banksystem django

Azat Gainolla
Alikhan Nassikhov


HOW TO RUN LOCALLY

clone repository git clone https://github.com/azatgainolla026/banksystem.git


1)install venv

python -m venv venv #to create venv

cd banking_system

source venv/bin/activate # For macOS/Linux

venv\Scripts\activate # For Windows

pip install django

python manage.py migrate

python manage.py runserver
