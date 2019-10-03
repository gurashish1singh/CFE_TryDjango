from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 50)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to = 'pics')
    content = models.TextField()
    updated = models.DateTimeField(auto_now = True, auto_now_add = False)
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail',kwargs = {'slug': self.slug})
        # return '/posts/%s' %(self.id)
    
    class Meta:
        ordering = ['-timestamp','-updated']

# Slug as URL(Cleaning up the URL) - This is called before saving every element

# Recurssive Function to slugify the title, also checking for if the slug exists. If it exists, then we run through the function again
def create_slug(instance, new_slug=None):
    slug=slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' %(slug,qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)