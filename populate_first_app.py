import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()


## FAKE POP SCRIPT
import random
from first_app.models import AccessRecord,Topic,Webpage,User
from faker import Faker

fakegen = Faker()
topics= ['Search','Social','Marketplace','News','Game']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t
def populate(N=5):
    for entry in range(N):
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]
def populateUser(N=5):
    for entry in range(N):
        fake_name= fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email= fakegen.email()
        users = User.objects.get_or_create(Last_Name=fake_last_name,Email=fake_email,First_Name=fake_first_name)[0]
if __name__ == '__main__':
    print("populating scripts!")
    populateUser(20)
    print("populating complete!")
