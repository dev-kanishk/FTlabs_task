# FTlabs task
This is a Production ready Django Web Application having Django-Rest API for displaying active periods of different users.

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

## For Hosting somewhere in a publicly accessible location like AWS or PythonAnywhere
* Make sure DEBUG is False 
* ALLOWED_HOST is configured according to usecase 
* command: `python manage.py collectstatic` for collecting all the static 
files in the folder mentioned in STATIC_ROOT, you can change it if want to server static from other location 

---
## High level overview:
This Django project consists of two Apps:
* account
* activityRecord

#### account
For User models and its related operations.
#### activityRecord
activityRecord APP is reponsible for serving the get request at the following mentioned API end-point by making queries to the database and performing serialization. This APP also stores the data related to the users active period like start time and end time.
#### Custom Management Command to populate the database
This command can be run by `python manage.py populate_UserRecord` .<br/>
Its code is present under activityRecord APP as follows `activityRecord/management/commands/populate_UserRecord.py`

---
## Rest-API end-point

For making get request to serve the list of members and their activity period. <br/>

* `/activity_record/members/` <br/>

Response:
* ok is a json boolean field.
* members is a json array of Users, each user having following fields id, real_name, tz(timezone) and activity_periods.
* activity_periods is again a json array of active time periods with start_time and end_time.
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

#### Users:<br/>
User models is an extention of AbstractUser model. <br/>
Having additional Fields as follow <br/>
* id as a primary key of fixed length 9 chars
* real_name simple character feild of max length 100
* tz for timezone, a character feild of max length 100 with default as Asia/kolkata


        class User(AbstractUser):
            id = models.CharField(primary_key=True ,max_length=9, validators=[MinLengthValidator(9)])
            real_name = models.CharField(max_length = 100)
            tz = models.CharField(max_length = 100, default="Asia/kolkata")

            def __str__(self):
                return self.real_name


#### Activity_period: <br/>
Activity_period is a simple Django model having:
* user as a Foreign Key to User model
* start_time and end_time are for storing user active time period both are DateTimeField type.


            class Activity_period(models.Model):
                start_time = models.DateTimeField()
                end_time = models.DateTimeField()
                user = models.ForeignKey(User, related_name='activity_periods',  on_delete=models.CASCADE)

                def __str__(self):
                    to_display = str(self.start_time) + " to " + str(self.end_time)
                    return to_display

## Serializers 

UserSerializer is a Model Based Nested Serializer, Nested because for every user object it calls for ActivityPeriodSerializer. 

    class UserSerializer(serializers.ModelSerializer):
        activity_periods = ActivityPeriodSerializer(many=True, read_only=True)

        class Meta:
            model = User
            fields = ['id', 'real_name', 'tz', 'activity_periods']


ActivityPeriodSerializer is a Model Based Serializer. Format of DateTimeField is explicity defined in the serializer

    class ActivityPeriodSerializer(serializers.ModelSerializer):
        start_time = serializers.DateTimeField(format='%b %e %Y %l:%M %p')
        end_time = serializers.DateTimeField(format='%b %e %Y %l:%M %p')

        class Meta:
            model = Activity_period
            fields = ['start_time', 'end_time'] 
        

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
Command will be creating 5 User objects and each user will have 5 activity periods




    class Command(BaseCommand):
        help = "Save randomly generated User record values."



        def get_dateTime(self):
            # Naively generating a random date
            day = random.randint(1, 28)
            month = random.randint(1, 12)
            year = random.randint(2014, 2017)
            hour = random.randint(0,23)
            min = random.randint(0,59)
            sec = random.randint(0,59)
            return datetime.datetime(year, month, day, hour, min, sec, tzinfo=pytz.UTC)

        def randomString(self, stringLength=8):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for i in range(stringLength))

        def get_id(self):
            random_char = random.choice(string.ascii_uppercase)
            random_num = random.randint(10000000,99999999)
            return random_char+str(random_num)

        def get_realName(self):
            return self.randomString(4) + " " + self.randomString(4)

        def get_Tz(self):
            timeZones = ["America/Denver", "America/Belize", "America/Cancun", "America/Chicago", "Chile/EasterIsland", "America/Bogota", "Europe/Belfast", "Europe/Dublin", "Europe/Lisbon"]
            random_index = random.randint(0,len(timeZones)-1)
            return timeZones[random_index]

        def get_password(self):
            return self.randomString(8)

        def get_username(self):
            return self.randomString(8)


        
        def handle(self, *args, **options):
            for _ in range(5):
                kwargs = {
                    'id': self.get_id(),
                    'username': self.get_username(),
                    'real_name': self.get_realName(),
                    'tz': self.get_Tz(),
                    'password': self.get_password()
                }
                # user object created
                user = User.objects.create(**kwargs)
                
                #list for storing all the activity_period objects that belongs one user
                activities = []
                for _ in range(5):
                    kwargs = {
                        'start_time': self.get_dateTime(),
                        'end_time': self.get_dateTime(),
                        'user': user
                    }

                    activity_obj = activity_period(**kwargs)
                    activities.append(activity_obj)
                    
                 #creating objects by bulk_create method
                activity_period.objects.bulk_create(activities)


            # if database populated successfully following string will be printed on the terminal
            self.stdout.write(self.style.SUCCESS('Database populated successfully.'))




