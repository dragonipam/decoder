##created by Neprav_Enot

alp_rus=['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з',
         'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
         'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ',
         'ъ', 'ы', 'ь', 'э', 'ю', 'я']
number=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
global output
def split(sentence):
    return [char for char in sentence]

def printOutput(out):
    print("*"*21)        
    print("Зашифрованное сообщение:", out)
    print("*"*21)

def decode_c(shift, sentence):
    out=""
    sent=[]
    sent=split(sentence.lower())
    for k in range(0,len(sent)):
            try:
                indexLetter=alp_rus.index(sent[k])-shift
                while (indexLetter<=0):
                    indexLetter= indexLetter + len(alp_rus)
                while (indexLetter>=len(alp_rus)):
                    indexLetter= indexLetter - len(alp_rus)
                    
                out+=alp_rus[indexLetter]
            except ValueError:
                out+=sent[k]
    return out

def caesar_decoder():
    print("Введите строку:")
    sentence = input()
    print("Если вам известен сдвиг, то введите его, иначе оставьте пустым:")
    shift=input()
    if (shift in number):
        shift = int(shift)
        output=decode_c(shift, sentence)
        printOutput(output)
    else:
        for shift in range(1,33):
            output=decode_c(shift, sentence)
            print("Предпологаемое сообщение:", output)
            print("Это предложение имеет смысл? 1-да/2-нет")
            f1=True
            while f1==True:
                ch3=input()
                if (ch3=='1'):
                    print("Сдвиг =",shift)
                    printOutput(output)
                    chooseCrypto()
                elif (ch3=='2'):
                    output=""
                    indexLetter=0
                    f1=False
                else:
                    print("Введены неверные данные")
    
    
def caesar():
    print("Введите строку:")
    sentence = input()
    sent=[]
    sent=split(sentence.lower())
    
    print("Введите сдвиг:")
    try:
        shift=int(input())
    except ValueError:
        print("Необходимо вводить цифры")
        caesar()
        
    output=""
    for k in range(0,len(sent)):
            try:
                indexLetter=alp_rus.index(sent[k])+shift
                while (indexLetter>=len(alp_rus)):
                    indexLetter= indexLetter - len(alp_rus)
                output+=alp_rus[indexLetter]
            except ValueError:
                output+=sent[k]

    print("*"*21)        
    print("Зашифрованное сообщение:", output)
    print("*"*21)
    
def printArray(array=[]): ##Вывод массива
    for i in range(i:=0, len(array)):
        print(array[i])

def chooseCrypto():
    while True:
        name_crypro=['1 - Шифр Цезаря','2 - Шифр Вижинера (На данный момент не работает)','- скоро будет ещё что-нибудь','0-Выход']
        print("Ave, Caesar, morituri te salutant! Выбери метод шифрования:")
        printArray(name_crypro)
        
        try:
            ch=int(input())
        except ValueError: 
            print("Введены неверные данные")
            chooseCrypto()
        
        if (ch==1):
            print("1-зашифровать сообщение / 2-дешифровать сообщение / 0-вернуться в меню")
            ch2=input()
            if(ch2=='1'):
                caesar()
            elif(ch2=='2'):
                caesar_decoder()
            elif(ch2=='0'):
                chooseCrypto()
            else:
                print("Неизвестное значение, проверьте данные и повторите ввод")
                
        elif(ch==2):
            print("1-зашифровать сообщение / 2-дешифровать сообщение / 0-вернуться в меню")
            ch2=input()
            if(ch2=='1'):
                pass
            elif(ch2=='2'):
                pass
            elif(ch2=='0'):
                chooseCrypto()
            else:
                print("Неизвестное значение, проверьте данные и повторите ввод")
            
        elif(ch==0):
            print("Выход...")
            return 0
        
        else:
            print("Неизвестное значение")
chooseCrypto()
##ё тезте хтлюсъ
