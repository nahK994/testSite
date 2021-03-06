from django.views import generic
from . models import Categories, CardsInfo, Codes, References, The_All_New_Images_From_GoogleDrive
from django.shortcuts import render

class View(generic.ListView):
    template_name = 'index.html'

    model = CardsInfo
    viewType = ''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.viewType == 'Intro':
            context['title'] = 'Introduction - BanglayML'
        elif self.viewType == 'SL':
            context['title'] = 'Supervised Learning - BanglayML'
        elif self.viewType == 'UL':
            context['title'] = 'Unsupervised Learning - BanglayML'
        elif self.viewType == 'RL':
            context['title'] = 'Reinforcement Learning - BanglayML'
        elif self.viewType == 'RNN':
            context['title'] = 'Deep Learning: RNN - BanglayML'
    
        context['querySet'] = super().get_queryset().filter(category_title = self.viewType).order_by('card_serial_NO')
        return context

def Text(request, cardID_for_txt=1):

    context = {}
    context['title'] = str(CardsInfo.objects.get(card_info_ID = cardID_for_txt).card_title)
    context['card_info_ID'] = cardID_for_txt
        
    imageObj = The_All_New_Images_From_GoogleDrive.objects.filter(card_info_ID = cardID_for_txt).order_by('Serial_NO')
    imageObjIndex = 0
    # {{i.1.image_upload.url}}
    codeObj = Codes.objects.filter(card_info_ID = cardID_for_txt).order_by('code_serial_NO')
    codeObjIndex = 0

    recommendationObj = References.objects.filter(card_info_ID = cardID_for_txt).order_by('reference_serial_NO')
    context['recommendationList'] = recommendationObj

    a = str(CardsInfo.objects.get(card_info_ID = cardID_for_txt).card_text)
    ans = []
    aa = a.split('<br><br>')
    if aa[0] != '':
        ans.append(aa[0])
    i = 1
    while i<len(aa):
        ans.append('<br><br>')
        if aa[i] != '':
            ans.append(aa[i])
        i = i+1

    Ans = []
    i = 0
    while i<len(ans):
        aa = ans[i].split('<br>')
        if aa[0] != '':
            Ans.append(aa[0])
        j = 1
        while j<len(aa):
            Ans.append('<br>')
            if aa[j] != '':
                Ans.append(aa[j])
            j = j+1
        i = i+1

    while len(Ans[len(Ans)-1])==1 and (Ans[len(Ans)-1] == '<br>' or Ans[len(Ans)-1] == ''):
        Ans = Ans[:-1]

    while len(Ans[0])==1 and Ans[0] == '':
        Ans = Ans[1:]

    ANS = []
    i = 0
    while i<len(Ans):
        aa = Ans[i].split('<img>')
        ANS.append(aa[0])
        j = 1
        while j<len(aa):
            ANS.append(['<img>', imageObj[imageObjIndex]])
            imageObjIndex = imageObjIndex +1
            if len(imageObj) == imageObjIndex:
               imageObjIndex = 0
                
            ANS.append(aa[j])
            j = j+1
        i = i+1

    answer = []
    i = 0
    while i<len(ANS):
        if len(ANS[i]) == 2:
            answer.append(ANS[i])
            i = i+1
            continue
        aa = ANS[i].split('<code>')
        answer.append(aa[0])
        j = 1
        while j<len(aa):
            answer.append(['<code>', codeObj[codeObjIndex]])
            codeObjIndex = codeObjIndex +1
            if len(codeObj) == codeObjIndex:
                codeObjIndex = 0 
                
            answer.append(aa[j])
            j = j+1
        i = i+1
     
    Answer=[]
    i = 0
    while i<len(answer):
        if len(answer[i]) == 2:
            Answer.append(answer[i])
            i = i + 1
            continue

        aa = answer[i].split('<span>')
        j = 0
        while j<len(aa):
            if j%2 == 0:
                if aa[j] != '':
                    Answer.append(aa[j])
            else:
                Answer.append(['<span>', aa[j]])
            j = j + 1

        i = i + 1
    
    ANSWER =[]
    i = 0
    while i<len(Answer):
        if len(Answer[i]) == 2:
            ANSWER.append(Answer[i])
            i = i + 1
            continue

        aa = Answer[i].split('<blockquote>')
        j = 0
        while j<len(aa):
            if j%2 == 0:
                if aa[j] != '':
                    ANSWER.append(aa[j])
            else:
                ANSWER.append(['<blockquote>', aa[j]])
            j = j + 1

        i = i + 1

    context['list'] = ANSWER

    return render(request, 'Text.html', context=context)