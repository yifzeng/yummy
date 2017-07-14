from django.db import models
from django.forms import ModelForm
# Create your models here.



class Person(models.Model):
    volume = models.CharField(max_length=50,verbose_name=u'期数')
    postdate = models.DateTimeField(blank=True, null=True,verbose_name=u'投稿日')
    gender = models.CharField(verbose_name=u'性别', max_length=2, choices=((u'男', u'男'), (u'女', u'女')))
    idnum = models.IntegerField(verbose_name=u'序号')
    city = models.CharField(max_length=50,verbose_name=u'城市')
    dec = models.TextField(verbose_name=u'自我介绍')
    image_urls = models.TextField(verbose_name=u'图片地址')

    def __str__(self):              # __unicode__ on Python 2
        return self.idnum
    def __unicode__(self):
        return u'%s %s' %(self.idnum,self.gender)
    class Meta:
        ordering = ['-postdate']


# class PersonForm(ModelForm):
#      class Meta:
#          model = Person
#          fields = ['gender', 'city', 'postdate', 'volume']
