from django.db import models

# Create your models here.
class PizzaSize(models.Model):
    ps_id=models.AutoField(primary_key=True)
    size=models.CharField(max_length=100)

    def __str__(self):
        return self.size

class PizzaTopping(models.Model):
    pt_id=models.AutoField(primary_key=True)
    topping=models.CharField(max_length=100)

    def __str__(self):
        return self.topping

class Pizza(models.Model):
    p_type=(
        ('Regular','Regular'),
        ('Square','Square'),
    )
    pid=models.AutoField(primary_key=True)
    types=models.CharField(max_length=100,choices=p_type)
    sizes=models.ForeignKey(PizzaSize,related_name='pizza_size',on_delete=models.CASCADE)
    toppings=models.ForeignKey(PizzaTopping,related_name='pizza_topping',on_delete=models.CASCADE)



