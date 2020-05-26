# FTlabs task
This is a Production ready Django Web Application having Django-Rest API for displaying activity periods of different users.

---

## Tech/framework used
* Python 3.8
* Django 3.0.6
* Postgres
* Django Rest Framework 3.11
* Markdown 3.2.2
* Django-Filter 2.2.0
* Psycopg2 2.8.5
* Python-decopule 3.2
* Pytz 2020.1
* sqlparse 0.3.1

<br/>

## Demo
Currently Hosted at PythonAnywhere server: http://kanishkftltask.pythonanywhere.com/activity_record/members/ . <br />

![](https://github.com/dev-kanishk/FTlabs_task/blob/master/Screenshot%20from%202020-05-26%2020-22-29.png)
<br/>
<br/>

## For running locally:
**Step-1:** Clone the repo to your system.

**Step-2:** Download and install a PostgreSQL server, for ubuntu/debian users https://www.youtube.com/watch?v=M4RDizdaO9U  

**Step-3:** Create new user and database in Postgres.

**Step-4:** Find evn_example.txt in the repo you just cloned copy all those fields in a new file, save this file as .env and change all the fields according to Postgres setup.
Make sure DEBUG is True for running locally.

**Step-5:** Find local_settings.example rename it as local_settings.py 

**Step-6:** Run command: `pip install -r requirements.txt`

**Step-7** Run command: `python manage.py makemigrations`

**Step-8** Run command: `python manage.py migrate`

**Step-9** Run command: `python manage.py populate_UserRecord`

**Step-10** Run command: `python manage.py runserver`
<br/>

## For running on some server:
* Make sure DEBUG is True 
* ALLOWED_HOST is configured according to usecase 
* command: `python manage.py collectstatic` for collecting all the static 
files in the folder mentioned in STATIC_ROOT, you can change it if want to server static from other location 

---

## Rest-API end-point

For making get request to serve the list of members and there activity period. <br/>

/activity_record/members/ <br/>




