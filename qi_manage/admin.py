from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(PlasterRetrofit)
admin.site.register(InsulationRetrofit)
admin.site.register(GlazingRetrofit)
admin.site.register(GlazingRetrofitSingle)
admin.site.register(GlazingRetrofitDouble)
admin.site.register(GlazingRetrofitDynamic)
admin.site.register(RoofRetrofit)
admin.site.register(RooftopFinish)
admin.site.register(SkylightRetrofit)
admin.site.register(SolarEnergy)
admin.site.register(ElevatorEscalator)

admin.site.register(HVACSystem)
admin.site.register(LightType)
admin.site.register(LightControl)
