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


class HVACSystem(models.Model):
    hvac_system = models.CharField(null=True, blank=True, max_length=127)
    hvac_cop = models.DecimalField(max_digits=4, decimal_places=1, default=None)
    hvac_system_cost = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    hvac_savings_perc = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    system_status = models.SmallIntegerField(blank=True, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hvac_system


class LightType(models.Model):
    light_type = models.CharField(null=True, blank=True, max_length=127)
    efficacy = models.IntegerField(null=True, blank=True, default=0)
    light_cost = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    light_is_auto = models.SmallIntegerField(blank=True, default=0)
    light_status = models.SmallIntegerField(blank=True, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class LightControl(models.Model):
    light_control = models.CharField(null=True, blank=True, max_length=127)
    light_sqm_area = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    light_sensor_factor = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    control_status = models.SmallIntegerField(blank=True, default=1)
    control_is_auto = models.SmallIntegerField(blank=True, default=0)
    control_cost = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class LightRetrofit(models.Model):
    retrofit_type = models.CharField(null=True, blank=True, max_length=127)
    saving_factor = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    cost = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)

    status = models.SmallIntegerField(blank=True, default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
