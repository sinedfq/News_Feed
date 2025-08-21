from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Текст новости")
    date_pub = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    image = models.ImageField(upload_to="news_images/", blank=True, null=True, verbose_name="Картинка")


    class Meta:
        ordering = ["-date_pub"]
    
    def __str__(self):
        return self.title