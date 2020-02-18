from __future__ import unicode_literals
from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["title"]) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData["network"]) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if len(postData["desc"]) < 10:
            errors["desc"] = "Show description should be at least 10 characters"
        return errors 

    def edit_validator(self,postData):
        errors = {}
        if len(postData["editTitle"]) < 2:
            errors["editTitle"] = "Title should be at least 2 characters"
        if len(postData["editNetwork"]) < 3:
            errors["editNetwork"] = "Network should be at least 3 characters"
        if len (postData["editDesc"]) < 10:
            errors["editDesc"] = "Description should be at least 10 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    def __repr__ (self):
        return f"Title: {self.title} Network: {self.network} Release Date: {self.release_date}"
