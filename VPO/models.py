from django.db import models


# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class User_member(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    json = models.TextField(default="Individual")

    def __str__(self):
        return self.email


class User_organizer(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    json = models.TextField(default="Individual")

    def __str__(self):
        return self.email


class Organizer_project(models.Model):
    id_organizer = models.CharField(max_length=255)
    json = models.TextField(default="Individual")
    json_data = models.TextField(default="Individual")

    def __str__(self):
        return self.id_organizer


class Project(models.Model):
    id_organizer = models.CharField(max_length=255)
    title = models.TextField(null=True)
    short_description = models.TextField(null=True)
    big_description = models.TextField(null=True)
    category_vpo = models.TextField(null=True)
    category_help = models.TextField(null=True)
    data_create = models.DateTimeField(null=True)
    permission = models.BooleanField(null=True)


    def __str__(self):
        return self.id_organizer


# class User_VPO(models.Model):
#     nickname = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     surname = models.CharField(max_length=255)
#     birth = models.CharField(max_length=255)
#     local_birth = models.CharField(max_length=255)
#     rnokpp = models.CharField(max_length=255)
#     passport = models.CharField(max_length=255)
#     room_number = models.CharField(max_length=255)
#     date_of_issue_vpo =  models.CharField(max_length=255)
#     registered_place = models.CharField(max_length=255)
#     actual_place = models.CharField(max_length=255)
#     contact = models.CharField(max_length=255)
#     information_about = models.CharField(max_length=255)
#     sex = models.CharField(max_length=255)
#     pensioner = models.CharField(max_length=255)
#     invalidity = models.CharField(max_length=255)
#     UBD = models.CharField(max_length=255)
#     invalidity_var = models.CharField(max_length=255)
#     has_state_awards = models.CharField(max_length=255)
#     family_member_of_a_deceased_serviceman = models.CharField(max_length=255)

def __str__(self):
    return self.name
