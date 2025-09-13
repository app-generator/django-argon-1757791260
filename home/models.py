# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    image = models.TextField(max_length=255, null=True, blank=True)
    customer_id = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Weight(models.Model):

    #__Weight_FIELDS__
    id_user = models.ForeignKey(user, on_delete=models.CASCADE)
    weight = models.IntegerField(null=True, blank=True)
    date = models.TextField(max_length=255, null=True, blank=True)
    time = models.TextField(max_length=255, null=True, blank=True)

    #__Weight_FIELDS__END

    class Meta:
        verbose_name        = _("Weight")
        verbose_name_plural = _("Weight")


class Metrics(models.Model):

    #__Metrics_FIELDS__
    birthday = models.TextField(max_length=255, null=True, blank=True)
    gender = models.TextField(max_length=255, null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    goal = models.TextField(max_length=255, null=True, blank=True)
    activitylevel = models.IntegerField(null=True, blank=True)
    caloriesadjustment = models.IntegerField(null=True, blank=True)
    proteindistribution = models.IntegerField(null=True, blank=True)
    fatdistribution = models.IntegerField(null=True, blank=True)
    carbsdistribution = models.IntegerField(null=True, blank=True)
    id_user = models.ForeignKey(user, on_delete=models.CASCADE)

    #__Metrics_FIELDS__END

    class Meta:
        verbose_name        = _("Metrics")
        verbose_name_plural = _("Metrics")


class Diary(models.Model):

    #__Diary_FIELDS__
    id_user = models.ForeignKey(user, on_delete=models.CASCADE)
    date = models.TextField(max_length=255, null=True, blank=True)
    target_calories = models.IntegerField(null=True, blank=True)
    target_protein = models.IntegerField(null=True, blank=True)
    target_fat = models.IntegerField(null=True, blank=True)
    target_carbs = models.IntegerField(null=True, blank=True)
    consumed_calories = models.IntegerField(null=True, blank=True)
    consumed_protein = models.IntegerField(null=True, blank=True)
    consumed_fat = models.IntegerField(null=True, blank=True)
    consumed_carbs = models.IntegerField(null=True, blank=True)

    #__Diary_FIELDS__END

    class Meta:
        verbose_name        = _("Diary")
        verbose_name_plural = _("Diary")


class User(models.Model):

    #__User_FIELDS__

    #__User_FIELDS__END

    class Meta:
        verbose_name        = _("User")
        verbose_name_plural = _("User")


class Meal(models.Model):

    #__Meal_FIELDS__
    id_user = models.ForeignKey(user, on_delete=models.CASCADE)
    id_diary = models.ForeignKey(diary, on_delete=models.CASCADE)
    time = models.TextField(max_length=255, null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    image = models.TextField(max_length=255, null=True, blank=True)
    type = models.TextField(max_length=255, null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    portion = models.IntegerField(null=True, blank=True)
    nvt_energy = models.IntegerField(null=True, blank=True)
    nvt_fat = models.IntegerField(null=True, blank=True)
    nvt_saturated_fat = models.IntegerField(null=True, blank=True)
    nvt_carbohydrates = models.IntegerField(null=True, blank=True)
    nvt_sugar = models.IntegerField(null=True, blank=True)
    nvt_fiber = models.IntegerField(null=True, blank=True)
    nvt_protein = models.IntegerField(null=True, blank=True)
    nvpc_energy = models.IntegerField(null=True, blank=True)
    nvpc_fat = models.IntegerField(null=True, blank=True)
    nvpc_saturated_fat = models.IntegerField(null=True, blank=True)
    nvpc_carbohydrates = models.IntegerField(null=True, blank=True)
    nvpc_sugar = models.IntegerField(null=True, blank=True)
    nvpc_fiber = models.IntegerField(null=True, blank=True)
    nvpc_protein = models.IntegerField(null=True, blank=True)
    calories = models.IntegerField(null=True, blank=True)
    reasoning = models.TextField(max_length=255, null=True, blank=True)

    #__Meal_FIELDS__END

    class Meta:
        verbose_name        = _("Meal")
        verbose_name_plural = _("Meal")


class Note(models.Model):

    #__Note_FIELDS__
    id_user = models.ForeignKey(user, on_delete=models.CASCADE)
    type = models.TextField(max_length=255, null=True, blank=True)
    content = models.TextField(max_length=255, null=True, blank=True)

    #__Note_FIELDS__END

    class Meta:
        verbose_name        = _("Note")
        verbose_name_plural = _("Note")



#__MODELS__END
