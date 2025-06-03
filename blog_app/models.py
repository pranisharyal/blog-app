from django.db import models

#make migrations=>track and generate migration file
#migrate=> run the generated migration file
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) #ahile ko date and time automatically halxa
    updated_at = models.DateTimeField(auto_now=True) #harek choti update hunxa
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
    ##1 -1 Relationship
#1 user can have only 1 profile => 1
# 1 profile is associated to only 1 user => 1
# OneToOneField() => Any Model

##1-M Relationship
# 1 user can add M post => M
#1 post is associated to only 1 user =>
#In django use foreignkey() => Use in many side Model

##M - M Relationship
# 1 student can learn from M teachers => M
#1 teacher can teach M students => M
#ManyTo =Manyfield() =>any place