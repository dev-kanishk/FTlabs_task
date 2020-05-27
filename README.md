# FullThrottle Labs - Backend Intern Assignment
This is a Production ready Django Web Application having Django-Rest API that serves a list of members(users) and their respective active periods. Active period basically includes the time at which member logs into the system(start_time) and logs out of the system(end_time). Custom management command to populate the database is also included.

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
Currently Hosted at PythonAnywhere server: https://kanishkftltask.pythonanywhere.com/activity_record/members/ . <br />

![](https://github.com/dev-kanishk/FTlabs_task/blob/master/Screenshot%20from%202020-05-26%2020-22-29.png)
<br/>
<br/>



---
## High level overview:
This Django project consists of two Apps:
* activityRecord
* account


#### activityRecord
activityRecord APP is reponsible for serving the get request at the following mentioned API end-point by making queries to the database and performing serialization. This APP also stores the data related to the users active period like start time and end time.

#### account
For User models and its related operations.

#### Custom Management Command to populate the database
This command can be run by `python manage.py populate_UserRecord` .<br/>
Its code is present under activityRecord APP as follows `activityRecord/management/commands/populate_UserRecord.py`

---
## Rest-API end-point

Get request for the list of members and their respective activity periods. <br/>

* `/activity_record/members/` <br/>

Response:
* ok is a json boolean field.
* members is a json array of Users
* Each User object has following fields id, real_name, tz(timezone) and activity_periods.
* activity_periods is again a json array of active time period.
* Each active time period has start_time and end_time fields.
```json
{
    "ok": true,
    "members": [
        {
            "id": "A15472216",
            "real_name": "skus kfpj",
            "tz": "Europe/Dublin",
            "activity_periods": [
                {
                    "start_time": "Nov 27 2017 10:12 PM",
                    "end_time": "Oct  5 2017  4:37 PM"
                },
                {
                    "start_time": "Apr 14 2015 12:46 PM",
                    "end_time": "May  4 2017  3:23 PM"
                }
            ]
        },
        {
            "id": "Y37307426",
            "real_name": "eukb lssk",
            "tz": "Europe/Belfast",
            "activity_periods": [
                {
                    "start_time": "Dec  3 2016 10:33 PM",
                    "end_time": "Sep  4 2016 10:02 PM"
                },
                {
                    "start_time": "Jan 15 2015  8:21 AM",
                    "end_time": "Jun 23 2017 10:43 PM"
                },
                {
                    "start_time": "Mar 15 2015  3:27 PM",
                    "end_time": "Aug 22 2016  3:29 PM"
                }
            ]
        }
    ]
}
```



## Database Models used

#### User:<br/>
User models is an extention of AbstractUser model. <br/>
Having additional Fields as follow <br/>
* id  (primary key, Char-field, fixed length 9) 
* real_name (Char-field, max length 100)
* tz for timezone (Char-field, max length 100, default Asia/kolkata)



#### Activity_period: <br/>
Activity_period is a simple Django model having:
* user (Foreign Key User model)
* start_time (DateTimeField)
* end_time (DateTimeField)


          
## Hosting locally:
**Step-1:** Clone the repo to your system.

**Step-2:** Download and install a PostgreSQL server, for ubuntu/debian users https://www.youtube.com/watch?v=M4RDizdaO9U  

**Step-3:** Create new user and database in Postgres.

**Step-4:** Find evn_example.txt in the repo you just cloned, copy all text present in it to a new file, change all the fields in the text according to your Postgres setup and save this file as .env.<br/>
Make sure DEBUG is True for running locally.

**Step-5:** Find local_settings.example rename it as local_settings.py 

**Step-6:** Run command: `pip install -r requirements.txt`

**Step-7** Run command: `python manage.py makemigrations`

**Step-8** Run command: `python manage.py migrate`

**Step-9** Run command: `python manage.py populate_UserRecord`

**Step-10** Run command: `python manage.py runserver`
<br/>

## Using Cloud services like AWS or PythonAnywhere
* Make sure DEBUG is False 
* ALLOWED_HOST is configured according to usecase 
* command: `python manage.py collectstatic` for collecting all the static 
files in the folder mentioned in STATIC_ROOT, you can change it if want to server static from other location 

---

## API View

Class based API for serving get request. Here get function first makes a query to database for all the User model and than pass the List of all Users to the the UserSerializer

    class UsersList(APIView):

        def get(self, request, format=None):
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response({
                'ok': True,
                'members': serializer.data
                })


## Custom Management Command to populate the database
This command fills the database with the dummy data.<br/>
command: `python manage.py populate_UserRecord` <br/>
Command will be creating 5 User objects and each user will have 5 activity periods.<br/>
For random string generation, I have used 'random.choice(string.ascii_lowercase)'<br/>
For integers `random.randint()`<br/>
TimeZone(tz) by a List having number of TimeZone which are Hard coded <br/>
Code is present under activityRecord APP as follows `activityRecord/management/commands/populate_UserRecord.py`








