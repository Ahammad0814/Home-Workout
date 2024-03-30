from django.urls import path
from . import views

urlpatterns = [
    path('',views.SelectFunction,name='WebStartPage'),
    path('home/',views.WorkoutHome,name='HomePage' ),
    # Beginner Pages
    path('beginner/abs/',views.Beginner,name='BeginnerAbsPage'),
    path('beginner/chest/',views.Beginner,name='BeginnerChestPage'),
    path('beginner/arm/',views.Beginner,name='BeginnerArmPage'),
    path('beginner/back/',views.Beginner,name='BeginnerBackPage'),
    path('beginner/leg/',views.Beginner,name='BeginnerLegPage'),
    # Intermediate Pages
    path('intermediate/abs/',views.Beginner,name='IntermediateAbsPage'),
    path('intermediate/chest/',views.Beginner,name='IntermediateChestPage'),
    path('intermediate/arm/',views.Beginner,name='IntermediateArmPage'),
    path('intermediate/back/',views.Beginner,name='IntermediateBackPage'),
    path('intermediate/leg/',views.Beginner,name='IntermediateLegPage'),
    # Advanced Pages
    path('advanced/abs/',views.Beginner,name='AdvancedAbsPage'),
    path('advanced/chest/',views.Beginner,name='AdvancedChestPage'),
    path('advanced/arm/',views.Beginner,name='AdvancedArmPage'),
    path('advanced/back/',views.Beginner,name='AdvancedBackPage'),
    path('advanced/leg/',views.Beginner,name='AdvancedLegPage'),
]

