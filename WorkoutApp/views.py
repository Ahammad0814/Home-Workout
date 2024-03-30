from django.shortcuts import render
from .models import BeginnersAbs,BeginnersChest,BeginnersArm,BeginnersBack,BeginnersLeg,IntermediateAbs,IntermediateChest,IntermediateArm,IntermediateBack,IntermediateLeg
from django.urls import reverse
from itertools import chain


# Create your views here.

def get_main_data(request):
    # Beginner Object
    if request.resolver_match.url_name == 'BeginnerAbsPage':
        Main = BeginnersAbs.objects.all()
        Name = 'ABS BEGINNER'
    elif request.resolver_match.url_name == 'BeginnerChestPage':
        Main = BeginnersChest.objects.all()
        Name = 'CHEST BEGINNER'
    elif request.resolver_match.url_name == 'BeginnerArmPage':
        Main = BeginnersArm.objects.all()
        Name = 'ARM BEGINNER'
    elif request.resolver_match.url_name == 'BeginnerBackPage':
        Main = BeginnersBack.objects.all()
        Name = 'SHOULDER & BACK BEGINNER'
    elif request.resolver_match.url_name == 'BeginnerLegPage':
        Main = BeginnersLeg.objects.all()
        Name = 'LEG BEGINNER'
    # Intermediate Object
    elif request.resolver_match.url_name == 'IntermediateAbsPage':
        Main = IntermediateAbs.objects.all()
        Name = 'ABS INTERMEDIATE'
    elif request.resolver_match.url_name == 'IntermediateChestPage':
        Main = IntermediateChest.objects.all()
        Name = 'CHEST INTERMEDIATE'
    elif request.resolver_match.url_name == 'IntermediateArmPage':
        Main = IntermediateArm.objects.all()
        Name = 'ARM INTERMEDIATE'
    elif request.resolver_match.url_name == 'IntermediateBackPage':
        Main = IntermediateBack.objects.all()
        Name = 'SHOULDER & BACK INTERMEDIATE'
    elif request.resolver_match.url_name == 'IntermediateLegPage':
        I_Data = BeginnersLeg.objects.all()
        A_Data = IntermediateLeg.objects.all()
        I_Data1 = I_Data[:7]
        I_Data2 = I_Data[7:]
        A_Data1 = A_Data[:1]
        A_Data2 = A_Data[1:]
        Main = list(chain(A_Data1, I_Data1, A_Data2, I_Data2))
        Name = 'LEG INTERMEDIATE'
    #Advanced Object
    elif request.resolver_match.url_name == 'AdvancedAbsPage':
        Main = IntermediateAbs.objects.all()
        Name = 'ABS ADVANCED'
    elif request.resolver_match.url_name == 'AdvancedChestPage':
        Main = IntermediateChest.objects.all()
        Name = 'CHEST ADVANCED'
    elif request.resolver_match.url_name == 'AdvancedArmPage':
        Main = IntermediateArm.objects.all()
        Name = 'ARM ADVANCED'
    elif request.resolver_match.url_name == 'AdvancedBackPage':
        Main = IntermediateBack.objects.all()
        Name = 'SHOULDER & BACK ADVANCED'
    elif request.resolver_match.url_name == 'AdvancedLegPage':
        I_Data = BeginnersLeg.objects.all()
        A_Data = IntermediateLeg.objects.all()
        I_Data1 = I_Data[:7]
        I_Data2 = I_Data[7:]
        A_Data1 = A_Data[:1]
        A_Data2 = A_Data[1:]
        Final_Data = list(chain(A_Data1, I_Data1, A_Data2, I_Data2))
        Main = list(chain(Final_Data[:2], Final_Data[2:20], Final_Data[2:20], Final_Data[20:]))
        Name = 'LEG ADVANCED'
    return Main,Name

cnt = 0
Data  = ''
def Beginner(request):
    global cnt,Data
    Main_Data, Name = get_main_data(request)
    Data_Length = len(Main_Data)
    if Data_Length > 0:
        if cnt < Data_Length:
            Data = Main_Data[cnt]
            element = None
            focus_fields = Main_Data[cnt].FocusFields
            
            if request.method == 'POST':
                if 'Forward' in request.POST:
                    element = 'Forward'
                elif 'Backward' in request.POST:
                    element = 'Backward'
                    
                if element == 'Forward':
                    if cnt < Data_Length - 1:
                        cnt += 1
                        Data = Main_Data[cnt]
                    else:
                        Data = Main_Data[cnt]
                    
                elif element == 'Backward':
                    if cnt > 0:
                        cnt -= 1
                        Data = Main_Data[cnt]
                    else:
                        Data = Main_Data[cnt]
                focus_fields = Main_Data[cnt].FocusFields
            return render(request, 'excercises.html', {'Data': Data, 'Main_Data': Main_Data, 'Name': Name, 'Count': cnt, 'FocusFields': focus_fields})
    if Data != Main_Data:
        cnt = 0
        Data = Main_Data
    Data = None
    focus_fields = None
    return render(request, 'excercises.html', {'Data': Data, 'Main_Data': Main_Data, 'Name': Name, 'Count': cnt, 'FocusFields': focus_fields})

def SelectFunction(request):
    return render(request, 'index.html')

def WorkoutHome(request):
    global cnt
    cnt = 0
    MainUrls = {'BeginnerAbsPage' : reverse('BeginnerAbsPage'),'BeginnerChestPage' : reverse('BeginnerChestPage'),'BeginnerArmPage' : reverse('BeginnerArmPage'),'BeginnerBackPage' : reverse('BeginnerBackPage'),'BeginnerLegPage' : reverse('BeginnerLegPage'),
                'IntermediateAbsPage' : reverse('IntermediateAbsPage'),'IntermediateChestPage' : reverse('IntermediateChestPage'),'IntermediateArmPage' : reverse('IntermediateArmPage'),'IntermediateBackPage' : reverse('IntermediateBackPage'),'IntermediateLegPage' : reverse('IntermediateLegPage'),
                'AdvancedAbsPage' : reverse('AdvancedAbsPage'),'AdvancedChestPage' : reverse('AdvancedChestPage'),'AdvancedArmPage' : reverse('AdvancedArmPage'),'AdvancedBackPage' : reverse('AdvancedBackPage'),'AdvancedLegPage' : reverse('AdvancedLegPage')}

    return render(request, 'home.html', {'Main_Urls_Data': MainUrls})