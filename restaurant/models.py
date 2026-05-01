from django.db import models







class Booking(models.Model):
    
    
    name = models.CharField(max_length=255)
    num_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()


    def __str__(self):
        return self.name



class Menu(models.Model):
    
    
    item_title  = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()




    def __str__(self):
        return f'{self.item_title} : {str(self.price)}'