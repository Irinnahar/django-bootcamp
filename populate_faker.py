import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_bootcamp.settings')

import django
django.setup()

# fake pop script
import random
from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

fake = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
  t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
  t.save()
  return t

def populate( N=20 ):
  for entry in range(N):
    top = add_topic()
    fake_url = fake.url()
    fake_date = fake.date()
    fake_name = fake.name()

    webpage = Webpage.objects.get_or_create(topic= top, url= fake_url, name= fake_name)[0]
    acc_rec = AccessRecord.objects.get_or_create(name=webpage, date= fake_date)[0]

if __name__ == "__main__":
    populate(20)

