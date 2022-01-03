
# ИУ5-55 Турчин Денис. лаб-5. 27.12.2021. Предметная область 14: CD-диск (класс-1) и Библиотека CD-дисков (класс-2). Запросы Д:
# 
# 
#   «Библиотека CD-дисков» и «CD-диск» связаны соотношением многие-ко-многим.                                                    <-- сделал многие-ко-многим
#     Выведите список всех библиотек, у которых название начинается с буквы «А», и список хранящихся в них CD-дисков.
#

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models import Count

class Disk(models.Model):
  class Meta:
    db_table = 'Disks'
    managed = True
    verbose_name = 'диск'
    verbose_name_plural = 'диски'

  title = models.CharField(max_length=200)
  format = models.CharField(max_length=10)
  size = models.IntegerField(default = 0)

  @property 
  def description(self):
    return self.title + '(' + str(self.size) + ' MB, ' + self.format + ')'

  def __str__(self):
    return self.title

class Library(models.Model):
  class Meta:
    db_table = 'Libraries'
    managed = True
    verbose_name = 'библиотека'
    verbose_name_plural = 'библиотеки'

  fk_storedDisks = models.ManyToManyField(Disk)
  title = models.CharField(max_length=200)
  owner = models.CharField(max_length=80)

  @property
  def disks_num(self):
    _disks_num = self.fk_storedDisks.all().count()
    return _disks_num
  
  @property 
  def description(self):
    return str(self.disks_num) + ' disks | owner: , ' + self.owner

  def __str__(self):
    return self.title
