from django.db import models, transaction


class City(models.Model):
    name = models.TextField()
    population = models.BigIntegerField()

    def set_population_to_zero(self):
        with transaction.atomic():
            self.population = 0
            self.save()
            transaction.on_commit(self.set_name_to_died)

    def set_name_to_died(self):
        self.name = "Died"
        self.save()


class School(models.Model):
    name = models.TextField()
    number = models.SmallIntegerField()
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)


class Student(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
