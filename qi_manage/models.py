from django.db import models


# Create your models here.
class PlasterRetrofit(models.Model):
    plaster_name = models.CharField(max_length=100)
    wmk = models.DecimalField(max_digits=6, decimal_places=2)
    cost = models.DecimalField(max_digits=6, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.plaster_name


class InsulationRetrofit(models.Model):
    insulation_name = models.CharField(max_length=100)
    wmk = models.DecimalField(max_digits=6, decimal_places=2)
    cost = models.DecimalField(max_digits=6, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.insulation_name


class GlazingRetrofitBase(models.Model):
    glazing_name = models.CharField(max_length=100)
    u_value = models.DecimalField(max_digits=6, decimal_places=2)
    shgc = models.DecimalField(max_digits=6, decimal_places=2)
    cost = models.DecimalField(max_digits=6, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.glazing_name


class GlazingRetrofit(GlazingRetrofitBase):
    pass


class GlazingRetrofitSingle(GlazingRetrofitBase):
    pass


class GlazingRetrofitDouble(GlazingRetrofitBase):
    pass


class GlazingRetrofitDynamic(GlazingRetrofitBase):
    pass


class RoofRetrofit(models.Model):
    roof = models.CharField(max_length=255)
    wmk = models.DecimalField(max_digits=6, decimal_places=2)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.roof


class RooftopFinish(models.Model):
    name = models.CharField(max_length=255)
    sri = models.DecimalField(max_digits=6, decimal_places=2)
    savings = models.DecimalField(max_digits=6, decimal_places=2)
    cost = models.DecimalField(max_digits=6, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class SkylightRetrofit(models.Model):
    name = models.CharField(max_length=255)
    u_value = models.DecimalField(max_digits=6, decimal_places=2)
    shgc = models.DecimalField(max_digits=6, decimal_places=2)
    cost = models.DecimalField(max_digits=6, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class SolarEnergy(models.Model):
    category_name = models.CharField(max_length=255)
    sg = models.DecimalField(max_digits=6, decimal_places=2)
    cost = models.DecimalField(max_digits=6, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.category_name


class ElevatorEscalator(models.Model):
    system_name = models.CharField(max_length=255)
    system_sgd = models.DecimalField(max_digits=6, decimal_places=2)
    system_savings = models.DecimalField(max_digits=6, decimal_places=2)
    comments = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.system_name
