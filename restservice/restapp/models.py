from django.db import models


# class Folder(models.Model):
#     name = models.CharField(max_length=50)
#     time_create = models.DateTimeField(auto_now_add=True)
#     time_update = models.DateTimeField(auto_now=True)
#     type = models.ForeignKey()
#
#     def __str__(self):
#         return self.name
#
#
# class Type1(models.Model):
#     name = models.CharField(max_length=50)
#     type = models.ForeignKey(Folder, on_delete=models.PROTECT)
#     time_create = models.DateTimeField(auto_now_add=True)
#     time_update = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Type2(models.Model):
#     name = models.CharField(max_length=50)
#     time_create = models.DateTimeField(auto_now_add=True)
#     time_update = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name


class Type(models.Model):
    type = models.CharField(primary_key=True, max_length=50, unique=True, verbose_name='Тип объекта')

    def __str__(self):
        return self.type


class Object(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, )
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


