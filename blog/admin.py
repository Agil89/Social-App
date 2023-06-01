from django.contrib import admin
from .models import Post, PostLike
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'created_date')
    fields = ('user', 'post', 'created_date')