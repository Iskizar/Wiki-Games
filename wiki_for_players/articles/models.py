from django.db import models


class Articles(models.Model):
    objects = None
    title = models.CharField('Название', max_length=50)
    logo = models.ImageField(upload_to='./main/static/main/img'
                            , null=True, max_length=255)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __repr__(self):
        return 'Image(%s, %s)' % (self.title, self.logo)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/hollow_knight_characters{self.id}'

    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'
