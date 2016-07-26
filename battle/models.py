from django.db import models
# from django.db.models import Q, F

# Create your models here.


class Authors(models.Model):
    name = models.CharField(max_length=100)


class Books(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    # автоматически добавит id к названию поля
    # author = models.ForeignKey(Author, on_delete='Cascade')
    # создается авт. таблица
    author = models.ManyToManyField(Authors, through='Books_Authors')

    # @python2_unicode_compatible  # for python2
    def __str__(self):
        return self.name


class Books_Authors(models.Model):
    class Meta:
        # проверить
        # уникальность значений
        unique_together = (("book", "author"), )
        # сортировка (- сортировка по убыванию)
        ordering = ['-user', ]
        # наше название таблицы
        # db_table = 'Books_Authors'

    book = models.ForeignKey(Books)
    author = models.ForeignKey(Authors)
    user = models.CharField(max_length=100)


# создание дерева
class Tree(models.Model):
    node = models.ForeignKey('self')
    # работа с объектом перед тем, как он создался
    # .ForeignKey('app.models.TreeNode')
