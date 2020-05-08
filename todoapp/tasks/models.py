from django.db import models


# Create your models here.

class Department(models.Model):
    name = models.CharField("Название подразделения", max_length=100)
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name='Подразделение'
        verbose_name_plural='Подразделения'
        
        
class Importance(models.Model):
    name = models.CharField("Имя", max_length=100)
    color = models.CharField("Цвет", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Важность'
        verbose_name_plural = 'Важность'

class Task(models.Model):
    title = models.CharField("Задача", max_length=200)
    complete = models.BooleanField("Выполнено", default=False)
    created = models.DateTimeField(auto_now_add=True)
    from_devision = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    importance = models.ForeignKey(Importance, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = "Задачи"
