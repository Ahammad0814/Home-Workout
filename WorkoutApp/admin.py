from django.contrib import admin
from .models import BeginnersAbs,BeginnersChest,BeginnersArm,BeginnersBack,BeginnersLeg,IntermediateAbs,IntermediateChest,IntermediateArm,IntermediateBack,IntermediateLeg

# Register your models here.

# Beginner Model

class BeginnerAbsAdmin(admin.ModelAdmin):
    pass
admin.site.register(BeginnersAbs, BeginnerAbsAdmin)

class BeginnerChestAdmin(admin.ModelAdmin):
    pass
admin.site.register(BeginnersChest, BeginnerChestAdmin)

class BeginnerArmAdmin(admin.ModelAdmin):
    pass
admin.site.register(BeginnersArm, BeginnerArmAdmin)

class BeginnerBackAdmin(admin.ModelAdmin):
    pass
admin.site.register(BeginnersBack, BeginnerBackAdmin)

class BeginnerLegAdmin(admin.ModelAdmin):
    pass
admin.site.register(BeginnersLeg, BeginnerBackAdmin)

# Intermediate Model

class IntermediateAbsAdmin(admin.ModelAdmin):
    pass
admin.site.register(IntermediateAbs, BeginnerAbsAdmin)

class IntermediateChestAdmin(admin.ModelAdmin):
    pass
admin.site.register(IntermediateChest, BeginnerChestAdmin)

class IntermediateArmAdmin(admin.ModelAdmin):
    pass
admin.site.register(IntermediateArm, BeginnerArmAdmin)

class IntermediateBackAdmin(admin.ModelAdmin):
    pass
admin.site.register(IntermediateBack, BeginnerBackAdmin)

class IntermediateLegAdmin(admin.ModelAdmin):
    pass
admin.site.register(IntermediateLeg, BeginnerBackAdmin)