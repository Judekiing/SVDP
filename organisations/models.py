from django.db import models
from django.db.models.fields import DurationField
from django.urls import reverse
from django.db.models.deletion import CASCADE


# Create your models here.
class Organ(models.Model):
    orgTitle = models.CharField(max_length=120)
    # orgCount = 
    orgDescription = models.TextField(max_length=300)
    orgLogo = models.ImageField
    orgAnthem =models.TextField(max_length=300)
    orgPurse = models.ForeignKey( 
        'Finance.purse', on_delete=CASCADE,
    )
    orgGroups = models.CharField(max_length=120)
    orgPrerequisite = models.CharField(max_length=120)
    orgnMeetLoc = models.CharField(max_length=120)
    author = models.ForeignKey(
        'auth.User', on_delete=CASCADE,
    )
    # office = models.ForeignKey(
    #     'auth.office', on_delete=CASCADE,
    # )
    orgMeetTime = models.TimeField
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=False, auto_now_add=True)
    created_at = models.DateField

    def __str__(self):
        return self.orgTitle
    
    def get_absolute_url(self):
        return reverse('org_detail', args=[self.id])

class Meeting(models.Model):
    meetingMinute = models.TextField(max_length=300)
    meetingAgenda = models.TextField(max_length=250)
    meetingAOB = models.TextField(max_length=250)
    # meetFinReport
    # meetingAttendance =models.
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=False, auto_now_add=True)
    created_at = models.DateField
    author = models.ForeignKey(
        'auth.User', on_delete=CASCADE,
    )


class Finace(models.Model):
    title = models.CharField(max_length=200)
    report =models.CharField(max_length=500)
    timeframe = models.DurationField
    created_at = models.DateField
    income = models.IntegerField
    expenses = models.IntegerField
    net_profit = models.IntegerField
    bank = models.IntegerField
    cash = models.IntegerField
    purse = models.IntegerField
    udated_at = models.DateTimeField(auto_now=False, auto_now_add=True)

class ProjectReport(models.Model):
    title = models.CharField(max_length=200)
    report =models.CharField(max_length=500)
    timeframe = models.DurationField()
    created_at = models.DateField
    income = models.IntegerField
    expenses = models.IntegerField
    net_profit = models.IntegerField
    bank = models.IntegerField
    cash = models.IntegerField
    purse = models.IntegerField
    udated_at = models.DateTimeField(auto_now=False, auto_now_add=True)





# class Welfare(models.Model):
# new_users
# active_users
# inactive_users
# check_up
# sick users
# Diseased_users


# class Sports(models.Model):

# class Spritual(models.Model):

# class Group(models.Model):
