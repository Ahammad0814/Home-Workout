from django.shortcuts import render
from .models import BeginnersAbs,BeginnersChest,BeginnersArm,BeginnersBack,BeginnersLeg,IntermediateAbs,IntermediateChest,IntermediateArm,IntermediateBack,IntermediateLeg
from django.urls import reverse
from itertools import chain


# Create your views here.

def get_main_data(request):
    # Beginner Object
    if request.resolver_match.url_name == 'BeginnerAbsPage':
        Data = BeginnersAbs.objects.all()
        Final_Data = list(chain(Data[:7], Data[1:]))
        Main = Final_Data
        Name = 'ABS BEGINNER'
    elif request.resolver_match.url_name == 'BeginnerChestPage':
        FirstData = BeginnersAbs.objects.all()
        Data = BeginnersChest.objects.all()
        Final_Data = list(chain(FirstData[:1], Data[:4], Data[:4], Data[4:]))
        Main = Final_Data
        Name = 'CHEST BEGINNER'
    elif request.resolver_match.url_name == 'BeginnerArmPage':
        Data1 = BeginnersArm.objects.all()
        Data2 = IntermediateArm.objects.all()
        Final_Data = list(chain(Data1[:9], Data2[:4], Data1[9:]))
        Main = Final_Data
        Name = 'ARM BEGINNER'
    elif request.resolver_match.url_name == 'BeginnerBackPage':
        FirstData = BeginnersArm.objects.all()
        Data1 = BeginnersBack.objects.all()
        Data2 = IntermediateBack.objects.all()
        Final_Data = list(chain(FirstData[:1], Data1, Data2[1:2], Data1[1:4], Data1[7:], Data2[8:9]))
        Main = Final_Data
        Name = 'SHOULDER & BACK BEGINNER'
    elif request.resolver_match.url_name == 'BeginnerLegPage':
        Main = BeginnersLeg.objects.all()
        Name = 'LEG BEGINNER'
        
    # Intermediate Object
    
    elif request.resolver_match.url_name == 'IntermediateAbsPage':
        FirstData = BeginnersAbs.objects.all()
        Data = IntermediateAbs.objects.all()
        Final_Data = list(chain(FirstData[:1], Data[:5], FirstData[1:7], Data, FirstData[7:]))
        Main = Final_Data
        Name = 'ABS INTERMEDIATE'
    elif request.resolver_match.url_name == 'IntermediateChestPage':
        FirstData = BeginnersAbs.objects.all()
        Data1 = BeginnersChest.objects.all()
        Data2 = IntermediateChest.objects.all()
        Final_Data = list(chain(FirstData[:1], Data1[:4], Data2[:4], Data2[:2], Data2[4:], Data1[4:]))
        Main = Final_Data
        Name = 'CHEST INTERMEDIATE'
    elif request.resolver_match.url_name == 'IntermediateArmPage':
        FirstData = BeginnersAbs.objects.all()
        Data1 = BeginnersArm.objects.all()
        Data2 = IntermediateArm.objects.all()
        Final_Data = list(chain(FirstData[:1], Data1[:9], Data2, Data2[:2], Data1[9:]))
        Main = Final_Data
        Name = 'ARM INTERMEDIATE'
    elif request.resolver_match.url_name == 'IntermediateBackPage':
        FirstData = BeginnersAbs.objects.all()
        Data1 = BeginnersBack.objects.all()
        Data2 = IntermediateBack.objects.all()
        Final_Data = list(chain(FirstData[:1], Data1[:1], Data1[2:6], Data1[7:], Data2))
        Main = Final_Data
        Name = 'SHOULDER & BACK INTERMEDIATE'
    elif request.resolver_match.url_name == 'IntermediateLegPage':
        I_Data = BeginnersLeg.objects.all()
        A_Data = IntermediateLeg.objects.all()
        Main = list(chain(A_Data[:1], I_Data[:7], A_Data[1:], I_Data[7:]))
        Name = 'LEG INTERMEDIATE'
        
    #Advanced Object
    
    elif request.resolver_match.url_name == 'AdvancedAbsPage':
        FirstData = BeginnersAbs.objects.all()
        Data = IntermediateAbs.objects.all()
        Final_Data = list(chain(FirstData[:1], Data[:5], FirstData[1:7], Data, FirstData[7:]))
        Main = Final_Data
        Name = 'ABS ADVANCED'
    elif request.resolver_match.url_name == 'AdvancedChestPage':
        FirstData = BeginnersAbs.objects.all()
        Data1 = BeginnersChest.objects.all()
        Data2 = IntermediateChest.objects.all()
        Final_Data = list(chain(FirstData[:1], Data1[:4], Data2[:4], Data2[:2], Data2[4:], Data1[4:]))
        Main = Final_Data
        Name = 'CHEST ADVANCED'
    elif request.resolver_match.url_name == 'AdvancedArmPage':
        FirstData = BeginnersAbs.objects.all()
        Data1 = BeginnersArm.objects.all()
        Data2 = IntermediateArm.objects.all()
        Final_Data = list(chain(FirstData[:1], Data1[:9], Data2, Data2[:2], Data1[9:]))
        Main = Final_Data
        Name = 'ARM ADVANCED'
    elif request.resolver_match.url_name == 'AdvancedBackPage':
        FirstData = BeginnersAbs.objects.all()
        Data1 = BeginnersBack.objects.all()
        Data2 = IntermediateBack.objects.all()
        Final_Data = list(chain(FirstData[:1], Data1[:1], Data1[2:6], Data1[7:], Data2))
        Main = Final_Data
        Name = 'SHOULDER & BACK ADVANCED'
    elif request.resolver_match.url_name == 'AdvancedLegPage':
        I_Data = BeginnersLeg.objects.all()
        A_Data = IntermediateLeg.objects.all()
        Final_Data = list(chain(A_Data[:1], I_Data[:7], A_Data[1:], I_Data[7:]))
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
