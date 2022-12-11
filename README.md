# Objective
This project is implemented to touch and feel Django Web Application.

# Overview
* Contains all the topis related to pytest and had fewer examples on
  * confest
  * Fixtures
  * Markers
  * Options
  * Parameterization
  * pytest_ini
  * Pytest_pass_fail_skip 
  * Report_Generation
  * Sample Test Case
  * Mock


# Pre-Requisites
```
sudo yum install git -t
sudo yum install python3-pip -y
sudo pip3 install django
sudo pip3 install djangorestframework
sudo pip install guniucorn
```




# Execution Flow

# Django CRUD App
```
git clone https://github.com/naveenreddymanukonda/pytest_django_crud.git
cd pytest_django_crud
pip3 install -r requirements.txt
python manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
```


# pytest_django_crud
To demonstrate pytest for django rest framework
## How to run project?

* Clone this repository.
* Create virtualenv with Python 3.
* Install dependences.
* Run the migrations.


```git clone https://github.com/naveenreddymanukonda/pytest_django_crud.git
cd pytest_django_crud
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
pytest```



# Issues
```sudo pip3 install requests
https://stackoverflow.com/questions/64634674/django-typeerror-argument-of-type-posixpath-is-not-iterable```
