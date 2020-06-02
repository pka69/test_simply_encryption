import os

PassKey=''
PassKeyTab=[
['','']
]

def removeAccents(input_text):
    strange='ŮôῡΒძěἊἦëĐᾇόἶἧзвŅῑἼźἓŉἐÿἈΌἢὶЁϋυŕŽŎŃğûλВὦėἜŤŨîᾪĝžἙâᾣÚκὔჯᾏᾢĠфĞὝŲŊŁČῐЙῤŌὭŏყἀхῦЧĎὍОуνἱῺèᾒῘᾘὨШūლἚύсÁóĒἍŷöὄЗὤἥბĔõὅῥŋБщἝξĢюᾫაπჟῸდΓÕűřἅгἰშΨńģὌΥÒᾬÏἴქὀῖὣᾙῶŠὟὁἵÖἕΕῨčᾈķЭτἻůᾕἫжΩᾶŇᾁἣჩαἄἹΖеУŹἃἠᾞåᾄГΠКíōĪὮϊὂᾱიżŦИὙἮὖÛĮἳφᾖἋΎΰῩŚἷРῈĲἁéὃσňİΙῠΚĸὛΪᾝᾯψÄᾭêὠÀღЫĩĈμΆᾌἨÑἑïოĵÃŒŸζჭᾼőΣŻçųøΤΑËņĭῙŘАдὗპŰἤცᾓήἯΐÎეὊὼΘЖᾜὢĚἩħĂыῳὧďТΗἺĬὰὡὬὫÇЩᾧñῢĻᾅÆßшδòÂчῌᾃΉᾑΦÍīМƒÜἒĴἿťᾴĶÊΊȘῃΟúχΔὋŴćŔῴῆЦЮΝΛῪŢὯнῬũãáἽĕᾗნᾳἆᾥйᾡὒსᾎĆрĀüСὕÅýფᾺῲšŵкἎἇὑЛვёἂΏθĘэᾋΧĉᾐĤὐὴιăąäὺÈФĺῇἘſგŜæῼῄĊἏØÉПяწДĿᾮἭĜХῂᾦωთĦлðὩზკίᾂᾆἪпἸиᾠώᾀŪāоÙἉἾρаđἌΞļÔβĖÝᾔĨНŀęᾤÓцЕĽŞὈÞუтΈέıàᾍἛśìŶŬȚĳῧῊᾟάεŖᾨᾉςΡმᾊᾸįᾚὥηᾛġÐὓłγľмþᾹἲἔбċῗჰხοἬŗŐἡὲῷῚΫŭᾩὸùᾷĹēრЯĄὉὪῒᾲΜᾰÌœĥტ'
    ascii_replacements='UoyBdeAieDaoiiZVNiIzeneyAOiiEyyrZONgulVoeETUiOgzEaoUkyjAoGFGYUNLCiIrOOoqaKyCDOOUniOeiIIOSulEySAoEAyooZoibEoornBSEkGYOapzOdGOuraGisPngOYOOIikoioIoSYoiOeEYcAkEtIuiIZOaNaicaaIZEUZaiIaaGPKioIOioaizTIYIyUIifiAYyYSiREIaeosnIIyKkYIIOpAOeoAgYiCmAAINeiojAOYzcAoSZcuoTAEniIRADypUitiiIiIeOoTZIoEIhAYoodTIIIaoOOCSonyKaAsSdoACIaIiFIiMfUeJItaKEISiOuxDOWcRoiTYNLYTONRuaaIeinaaoIoysACRAuSyAypAoswKAayLvEaOtEEAXciHyiiaaayEFliEsgSaOiCAOEPYtDKOIGKiootHLdOzkiaaIPIIooaUaOUAIrAdAKlObEYiINleoOTEKSOTuTEeiaAEsiYUTiyIIaeROAsRmAAiIoiIgDylglMtAieBcihkoIrOieoIYuOouaKerYAOOiaMaIoht'
    translator=str.maketrans(strange,ascii_replacements)
    return input_text.translate(translator)

def clear():
    """Clear screen."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def Get_Key():
    global PassKey
    global PassKeyTab
    
    isCorrect = False
    
    while not isCorrect:
        PassKey= input("Podaj klucz (bez cyfr, polskich znaków, spacji powtórzeń):")
        PassKey=removeAccents(PassKey)
        PassKey=PassKey.upper()
        isDouble =  [ i for i in PassKey if PassKey.count(i)>1]
        if len(PassKey)%2==1:
            print("błędna ilość znaków.")
        elif len(PassKey)<10:
            print("Klucz za krótki")
        elif PassKey.count(' ')>0:
            print("musi być tekst bez spacji")
        elif len(isDouble)>0:
            print("litery nie moga się powtarzać")
        elif not PassKey.isalpha():
            print("nie moze być cyfr i znaków specjalnych")
        else:
            isCorrect=True
    print("Hasło-klucz:",PassKey)            
    
    PassKeyTab[0][0]=PassKey[0]
    PassKeyTab[0][1]=PassKey[1]
    
    for i in range(1,len(PassKey)//2):
        PassKeyTab.append([PassKey[i*2],PassKey[i*2+1]])
    print("Pary zamienne:")
    print (PassKeyTab)

def Get_Kode_S(S, PassKey, PassKeyTab):

    CopyS=removeAccents(S.upper())

    Final=""
    for i in range(len(S)):
        if CopyS[i] in PassKey: #PassKey.count(CopyS[i])>0
            j=PassKey.index(CopyS[i])
            if j%2==0:
                Temp=PassKeyTab[j//2][1]
            else:
                Temp=PassKeyTab[j//2][0]

            if S[i].islower():
                Temp=Temp.lower()
            Final+=Temp
        else:
            Final+=S[i]
    return Final
    
#-----------------------------------------------------------------------------------------------
#------------------main program-----------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
clear()


Get_Key()
S=input("podaj tekst do zaszyfrowania(gwiazdka jeśli chcesz zakończyć):")
while S!="*":
    print(Get_Kode_S(S, PassKey, PassKeyTab))
    S=input("podaj tekst do zaszyfrowania(gwiazdka jeśli chcesz zakończyć):")

