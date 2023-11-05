from django.db import models


class Record(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    rollno = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    CPI = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    CSE_205 = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    ME_102 = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    CSO_204 = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    CSO_211 = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    DOS = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    MA_202 = models.DecimalField(max_digits=10, decimal_places=0, default=0)

    def __str__(self) -> str:
        return (f"{self.first_name} {self.last_name} {self.rollno}")
