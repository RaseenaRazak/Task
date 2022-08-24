from django.db import models


# Create your models here.
class district(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class branch(models.Model):
    district = models.ForeignKey(district, on_delete=models.CASCADE)
    branch = models.CharField(max_length=250)

    def __str__(self):
        return self.branch


class person_info(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField(auto_now_add=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    mail_id = models.CharField(max_length=250)
    address = models.TextField()
    dist = models.ForeignKey(district, on_delete=models.CASCADE)
    branch = models.CharField(max_length=250)
    account_type = models.CharField(max_length=250)
    debit = models.CharField(max_length=200)
    credit = models.CharField(max_length=200)
    checkbook = models.CharField(max_length=200)

    def __str__(self):
        return self.name
