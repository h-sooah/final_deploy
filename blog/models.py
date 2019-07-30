from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]

class Sell_list(models.Model):
    name = models.CharField(max_length = 200)
    phone_number = models.CharField(max_length = 30)
    account_number = models.CharField(max_length = 30)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    method = models.CharField(max_length = 30)
    country = models.CharField(max_length = 30)
    start_date = models.DateField()
    end_date = models.DateField()

class Buy_list(models.Model):
    buy_name = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    amount = models.IntegerField()
    price = models.IntegerField()
    body = models.TextField()
    request_country = models.CharField(max_length = 50)
    end_date = models.DateField()
    size = models.CharField(max_length = 30)
    request_text = models.CharField(max_length = 400)
