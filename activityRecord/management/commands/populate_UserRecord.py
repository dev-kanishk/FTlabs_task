import datetime
import random
import string
import pytz

from django.core.management.base import BaseCommand

from activityRecord.models import activity_period
from accounts.models import User 





class Command(BaseCommand):
    help = "Save randomly generated stock record values."
 
        

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
            user = User.objects.create(**kwargs)
            activities = []
            for _ in range(5):
                kwargs = {
                    'start_time': self.get_dateTime(),
                    'end_time': self.get_dateTime(),
                    'user': user
                }

                activity_obj = activity_period(**kwargs)
                activities.append(activity_obj)

            activity_period.objects.bulk_create(activities)


         
        self.stdout.write(self.style.SUCCESS('Database populated successfully.'))