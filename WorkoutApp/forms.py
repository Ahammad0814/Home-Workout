from django import forms
from .models import BeginnersAbs,BeginnersChest,BeginnersArm,BeginnersBack,BeginnersLeg,IntermediateAbs,IntermediateChest,IntermediateArm,IntermediateBack,IntermediateLeg

class BaseDataForm(forms.ModelForm):
    class Meta:
        abstract = True
        fields = '__all__'

# Beginners Data Form

class BeginnerAbsForm(BaseDataForm):
    class Meta(BaseDataForm.Meta):
        model = BeginnersAbs

class BeginnerChestForm(BaseDataForm):
    class Meta(BaseDataForm.Meta):
        model = BeginnersChest

class BeginnerArmForm(BaseDataForm):
    class Meta(BaseDataForm.Meta):
        model = BeginnersArm
        
class BeginnerBackForm(BaseDataForm):
    class Meta(BaseDataForm.Meta):
        model = BeginnersBack

class BeginnerLegForm(BaseDataForm):
    class Meta(BaseDataForm.Meta):
        model = BeginnersLeg

# Intermediate Data Form

class intermediateAbsForm(BaseDataForm):
    class Meta(BaseDataForm.Meta):
        model = IntermediateAbs
        
class intermediateChestForm(BaseDataForm):
    class Meta(BaseDataForm.Meta):
        model = IntermediateChest

class intermediateArmForm(BaseDataForm):
    class Meta(BaseDataForm.Meta):
        model = IntermediateArm

class intermediateBackForm(BaseDataForm):
    class Meta(BaseDataForm.Meta):
        model = IntermediateBack
        
class intermediateLegForm(BaseDataForm):
    class Meta(BaseDataForm.Meta):
        model = IntermediateLeg