from django.db import models

# Create your models here.
class Metadata(models.Model):
    company_id=models.AutoField(primary_key=True)
    key_word_conf =models.CharField(max_length=100)
    weightage=models.FloatField(max_length=100)
    about=models.TextField()
    category=models.CharField(max_length=100,choices=(('NDA','NDA'),
                                                      ('SLA','SLA'),))