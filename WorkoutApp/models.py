from django.db import models

# Create your models here.

class WorkoutBaseData(models.Model):
    MainImage = models.ImageField(upload_to='images/')
    MainTitle = models.CharField(max_length=255)
    Text1 = models.TextField()
    Text2 = models.TextField()
    Image = models.ImageField(upload_to='images/')
    FocusFields = models.CharField(max_length=255,null=True)
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.MainTitle

class BeginnersAbs(WorkoutBaseData):
    pass
    
class BeginnersChest(WorkoutBaseData):
    pass

class BeginnersArm(WorkoutBaseData):
    pass

class BeginnersBack(WorkoutBaseData):
    pass

class BeginnersLeg(WorkoutBaseData):
    pass

class IntermediateAbs(WorkoutBaseData):
    pass
    
class IntermediateChest(WorkoutBaseData):
    pass

class IntermediateArm(WorkoutBaseData):
    pass

class IntermediateBack(WorkoutBaseData):
    pass

class IntermediateLeg(WorkoutBaseData):
    pass