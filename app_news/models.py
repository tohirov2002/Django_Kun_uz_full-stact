from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories'
        db_table = 'categories'


class News(models.Model):
    news_title = models.CharField(max_length=255)
    news_description = RichTextField()
    news_image = models.ImageField(upload_to='news/')
    news_content = RichTextField()
    news_pub_date = models.DateTimeField(auto_now_add=True)
    news_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    news_view = models.IntegerField(default=0)

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name_plural = 'News'
        db_table = 'news'



