from django.db import models
from accounts.models import MyUser
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='post_user')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title}'
    
    @property
    def like_count(self):
        return PostLike.objects.filter(post=self).count()

class PostLike(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='like_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like')
    created_date = models.DateField(auto_now=True, verbose_name="Created Date")

    def __str__(self) -> str:
        return f'{self.post.title}'
    
    @classmethod
    def filter_by_date(cls, date_from, date_to):
        return cls.objects.filter(created_date__range=[date_from, date_to])