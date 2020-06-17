from django.db import models

# Create your models here.
class App(models.Model):
    id = models.CharField(max_length=70, blank=False, default='', primary_key=True)
    title = models.CharField(max_length=70, blank=False, default='')
    advertiser_id = models.CharField(max_length=200, blank=False, default='')
    startdate = models.CharField(max_length=200, blank=False, default='')
    enddate = models.CharField(max_length=200, blank=False, default='')
    type = models.CharField(max_length=200, blank=False, default='')
    created_at = models.CharField(max_length=200, blank=False, default='')

    class Meta:
        db_table = 'campaign'