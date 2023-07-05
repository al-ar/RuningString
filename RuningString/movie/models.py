from django.db import models




class Text(models.Model):
    text = models.CharField(max_length=255, verbose_name='текст',
                            help_text='Здесь должен быть текст')
    files = models.FileField(upload_to='../tempVideo/')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='дата публикации')

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-pub_date']