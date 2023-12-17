from django.db import models
import uuid
from django.db.models import Manager,Model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ObjectDoesNotExist
# Create your models here.


class AbstractManager(models.Manager):
    def get_object_by_public_id(self, id):
        try:
            instance = self.get(id=id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            raise ValueError(_("ID Cannot be found"))

class TimeStampedUUIDModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = AbstractManager()
 
    class Meta:
        abstract = True
        ordering = ["-created_at", "-updated_at"]
        get_latest_by = 'created_at'


class Booking(TimeStampedUUIDModel):
    id =models.IntegerField(db_index=True)
    name=models.CharField(max_length=255)
    No_of_guests=models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    BookingDate=models.DateField()

    def __str__(self):
        return f"{self.name} - {self.BookingDate}"

class Category(TimeStampedUUIDModel):
    slug=models.SlugField()
    title=models.CharField(max_length=255, db_index=True)

class Menu(TimeStampedUUIDModel):
    id=models.IntegerField(db_index=True)
    Title=models.CharField(max_length=50)
    Price=models.DecimalField(max_digits=6, decimal_places=2)
    Inventory=models.PositiveSmallIntegerField(default=0, help_text="In Stock")

class MenuItem(models.Model):
    title=models.CharField(max_length=255, db_index=True)
    price=models.DecimalField(max_digits=6, decimal_places=2)
    featured=models.BooleanField(db_index=True, default=None)
    category=models.ForeignKey(Category, related_name='Title', on_delete=models.PROTECT)

