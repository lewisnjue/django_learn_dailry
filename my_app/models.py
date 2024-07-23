from django.db import models # any of my model calss will need to 
""" 
subclass the class django.db.models.models -> donf forget this 

 """

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
       abstract = True


class Post(BaseModel):
    title = models.CharField(max_length=30,verbose_name='Title Of Post')
    comment = models.TextField()
    class Meta:
        ordering =['title']
        verbose_name_plural ='posts'
