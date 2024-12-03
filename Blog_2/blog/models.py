from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    summary = models.CharField(max_length=300)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='img', default='placeholder.png')

    class Meta:
        ordering = ['-created']

        def __unicode__(self): #returns the Post object's title
            return u'%s'% self.title

    def get_absolute_url(self): # returns URL that doesnt change ?
        return reverse('blog.views.post', args=[self.slug])
