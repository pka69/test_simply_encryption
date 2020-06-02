import os
import web

URLS = (
    '/', 'HashKey',
    '/tconvert', 'TextConvert',
)

render = web.template.render('templates/')

PassKey=''
PassKeyTab=[
['','']
]
message=''
Pary=''

def removeAccents(input_text): #zwraza tekst odfiltrowany ze znaków diakrytycznych
    strange='ŮôῡΒძěἊἦëĐᾇόἶἧзвŅῑἼźἓŉἐÿἈΌἢὶЁϋυŕŽŎŃğûλВὦėἜŤŨîᾪĝžἙâᾣÚκὔჯᾏᾢĠфĞὝŲŊŁČῐЙῤŌὭŏყἀхῦЧĎὍОуνἱῺèᾒῘᾘὨШūლἚύсÁóĒἍŷöὄЗὤἥბĔõὅῥŋБщἝξĢюᾫაπჟῸდΓÕűřἅгἰშΨńģὌΥÒᾬÏἴქὀῖὣᾙῶŠὟὁἵÖἕΕῨčᾈķЭτἻůᾕἫжΩᾶŇᾁἣჩαἄἹΖеУŹἃἠᾞåᾄГΠКíōĪὮϊὂᾱიżŦИὙἮὖÛĮἳφᾖἋΎΰῩŚἷРῈĲἁéὃσňİΙῠΚĸὛΪᾝᾯψÄᾭêὠÀღЫĩĈμΆᾌἨÑἑïოĵÃŒŸζჭᾼőΣŻçųøΤΑËņĭῙŘАдὗპŰἤცᾓήἯΐÎეὊὼΘЖᾜὢĚἩħĂыῳὧďТΗἺĬὰὡὬὫÇЩᾧñῢĻᾅÆßшδòÂчῌᾃΉᾑΦÍīМƒÜἒĴἿťᾴĶÊΊȘῃΟúχΔὋŴćŔῴῆЦЮΝΛῪŢὯнῬũãáἽĕᾗნᾳἆᾥйᾡὒსᾎĆрĀüСὕÅýფᾺῲšŵкἎἇὑЛვёἂΏθĘэᾋΧĉᾐĤὐὴιăąäὺÈФĺῇἘſგŜæῼῄĊἏØÉПяწДĿᾮἭĜХῂᾦωთĦлðὩზკίᾂᾆἪпἸиᾠώᾀŪāоÙἉἾρаđἌΞļÔβĖÝᾔĨНŀęᾤÓцЕĽŞὈÞუтΈέıàᾍἛśìŶŬȚĳῧῊᾟάεŖᾨᾉςΡმᾊᾸįᾚὥηᾛġÐὓłγľмþᾹἲἔбċῗჰხοἬŗŐἡὲῷῚΫŭᾩὸùᾷĹēრЯĄὉὪῒᾲΜᾰÌœĥტ'
    ascii_replacements='UoyBdeAieDaoiiZVNiIzeneyAOiiEyyrZONgulVoeETUiOgzEaoUkyjAoGFGYUNLCiIrOOoqaKyCDOOUniOeiIIOSulEySAoEAyooZoibEoornBSEkGYOapzOdGOuraGisPngOYOOIikoioIoSYoiOeEYcAkEtIuiIZOaNaicaaIZEUZaiIaaGPKioIOioaizTIYIyUIifiAYyYSiREIaeosnIIyKkYIIOpAOeoAgYiCmAAINeiojAOYzcAoSZcuoTAEniIRADypUitiiIiIeOoTZIoEIhAYoodTIIIaoOOCSonyKaAsSdoACIaIiFIiMfUeJItaKEISiOuxDOWcRoiTYNLYTONRuaaIeinaaoIoysACRAuSyAypAoswKAayLvEaOtEEAXciHyiiaaayEFliEsgSaOiCAOEPYtDKOIGKiootHLdOzkiaaIPIIooaUaOUAIrAdAKlObEYiINleoOTEKSOTuTEeiaAEsiYUTiyIIaeROAsRmAAiIoiIgDylglMtAieBcihkoIrOieoIYuOouaKerYAOOiaMaIoht'
    translator=str.maketrans(strange,ascii_replacements)
    return input_text.translate(translator)
    
def Get_Key ( PassKey, PassKeyTab ): #zwraca komunikat błędu (lub pusty łańcuch)
    message=''
    
    #PassKey= input("Podaj klucz (bez cyfr, polskich znaków, spacji powtórzeń):")
    PassKey=removeAccents(PassKey)
    PassKey=PassKey.upper()
    isDouble =  [ i for i in PassKey if PassKey.count(i)>1]
    if len(PassKey)%2==1:
        message = "błędna ilość znaków. \n Spróbuj jeszcze raz"
    elif len(PassKey)<10:
        message = "Klucz za krótki. \n Spróbuj jeszcze raz"
    elif PassKey.count(' ')>0:
        message = "musi być tekst bez spacji. \n Spróbuj jeszcze raz"
    elif not PassKey.isalpha():
        message = "nie moze być cyfr i znaków specjalnych. \n Spróbuj jeszcze raz"
    elif len(isDouble)>0:
        message = "litery nie moga się powtarzać. \n Spróbuj jeszcze raz"
    else:
        PassKeyTab[0][0]=PassKey[0]
        PassKeyTab[0][1]=PassKey[1]
        for i in range(1,len(PassKey)//2):
            PassKeyTab.append([PassKey[i*2],PassKey[i*2+1]])

    return message

def Get_Kode_S(S, PassKey): # zwraca zaszyfrowany tekst

    CopyS=removeAccents(S.upper())

    Final=""
    for i in range(len(S)):
        if CopyS[i] in PassKey: #PassKey.count(CopyS[i])>0
            j=PassKey.index(CopyS[i])
            if j%2==0:
                Temp=PassKey[j+1]
            else:
                Temp=PassKey[j-1]

            if S[i].islower():
                Temp=Temp.lower()
            Final+=Temp
        else:
            Final+=S[i]
    return Final
    
#-----------------------------------------------------------------------------------------------
#------------------main program-----------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
'''
Get_Key()
S=input("podaj tekst do zaszyfrowania(gwiazdka jeśli chcesz zakończyć):")
while S!="*":
    print(Get_Kode_S(S, PassKey, PassKeyTab))
    S=input("podaj tekst do zaszyfrowania(gwiazdka jeśli chcesz zakończyć):")
'''
class HashKey:
    def GET(self):
        return render.szyfr()

    def POST(self):  
        global PassKey
        global Pary
        global message
        data = web.input()
        if len(data) == 0:
            return render.szyfr()
        try:
            PassKey = data["HashKey"]
        except:
            pass
        else:
            PassKey = PassKey.upper()
            message=Get_Key(PassKey, PassKeyTab)
            if message=="":
                Pary=str(PassKeyTab)
                Pary=Pary.replace("[[","[")
                Pary=Pary.replace("]]","]")
                Pary=Pary.replace(", ","")
                Pary=Pary.replace("'","")
                ToConvert = ""
                Converted=""
                return render.szyfr(PassKey, message, Pary, ToConvert,Converted)
            else:
                return render.szyfr("", message, "", "","")
        try:
            ToConvert=data["ToTranslate"]
        except:
            pass
        else:
            Converted=Get_Kode_S(ToConvert, PassKey)
            return render.szyfr(PassKey, message, Pary, ToConvert,Converted)

if __name__ == "__main__":
    app = web.application(URLS, globals())
    app.run()
