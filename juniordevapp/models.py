from django.db import models

class Content(models.Model):
    content = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    
    @classmethod
    def get_comment(cls,id):
       Content.objects.all()

