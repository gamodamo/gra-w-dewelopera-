#gra w dewelopera!
import random
import os
cash=0
actions=0
cena=1
tax=0
taxvalue=0
calculator=False
darkN=False
down_cours=False
up_cours=False
event=False
event_error=False
metatimer_up=0
metatimer_down=0
metatimer_error=0
metatimer_event=0

def kurs():
    global cena,down_cours,up_cours,event_error
    if event_error==True:
        cena=2137
    elif down_cours==True:
        cena=0.5*10
    elif up_cours==True:
        cena=2*10
    else:
        possible_odds=[0.5,0.5,0.5,0.7,0.7,0.7,0.9,0.9,1,1,1,1,1,1,1,1,1,1.1,1.1,1.2,1.2,1.5,1.7,1.8,2] 
        cena=random.choice(possible_odds)
        cena*=10

def robbed():
    global cash
    robbedd=cash*0.1
    cash-=robbedd
    print(f'Zostałeś okradziony na: {robbedd}$')
    t=input('')

def tip():
    global cash
    tipp=cash*0.1
    cash+=tipp
    print(f'Firma inwestycyjna przelała ci {tipp}$ za załugi ')
    t=input('')

def error_course():
    global event_error
    event_error=True
    print('Wystąpił błąd!')
    t=input('')

def wydarzenie():    
    if event==True:
        events=[1,2,3]
        eventchoice=random.choice(events)
        match eventchoice:
            case 1:
                robbed()
            case 2:
                tip()
            case 3:
                error_course()

def inwestycja():
    global cash,actions,cena
    if cash>=cena:
        try:
            if calculator==True:
                value=cash/cena
                value1=cena*value
                round(value,1)
                print(f'\nmożesz kupić {value} akcje za {value1}$\n')
            else:
                pass
            vaule=int(input(f'ile chcesz zainwestować?(koszt jednej akcji wynosi {cena}$) posiadasz {cash}$'))
            koszy=vaule*cena
            cash-=koszy
            actions+=vaule
        except ValueError:
            print('pomiń')
            d=input('')
    else:
        print('nie masz kasy')
        d=input('')

def sell():
    global cash,actions,cena
    if actions>=1:
        print(f'aktualna ilość akcji: {actions}\naktualna cena: {cena}')
        try:  
            if calculator==True:
                value1=cena*actions
                round(value1,1)
                print(f'\nmożesz sprzedać {actions} inwestycji za {value1}$')
            else:
                pass
            vaule=int(input('ile chcesz sprzedać?'))
            if vaule <= actions:
                koszt=cena*vaule
                cash+=koszt
                actions-=vaule
            else:
                print('nie posiadasz tyle akcji')
                d=input('')
        except ValueError:
            print('try again')
            d=input('')
    
def job(a):
    global cash
    match a:
        case 0:
            b=20
            win=10
            fail=5
        case 1:
            b=30
            win=20
            fail=10
        case 2:
            b=40
            win=25
            fail=17
        case _:
            print('błąd')
            pass
    list1=['0','1']
    string=''
    for _ in range(b):
        for x in list1:
            x=random.choice(list1)
            string+=x
    print(string)
    print('zrób kopie ręczną')
    jobvalue=input('')
    if jobvalue==string:
        print(f'dziękujemy!\ndodano {win}$')
        cash+=win
        v=input('')
    else:
        print(f'niestety odjęto z konta {fail}$')
        cash-=fail
        v=input('')
    
def choice_job():
    print('zrób zlecenie\ndostępne:Małe(0) Średnie(1) Duże(2)')
    choice=int(input('wybierz zlecenie: '))
    job(choice)

def taxx():
    global cash,tax,actions
    if cash<=2.5:
        tax_actions=actions*0.3
        tax_actions=int(tax_actions)
        tax_actions2=cena*tax_actions
        cash-=tax_actions2
        actions-=tax_actions
        tax=tax_actions2
    else:
        tax=cash*0.3
        cash-=tax
    print(f'zapłacono {tax}$')

def occurrence_of_tax():
    global taxvalue
    taxvalue+=1
    if taxvalue==10:
        taxx()
        taxvalue=0

def view_wallet():
    global cash,actions
    breaki='=========================================='
    print(f'{breaki}\nposiadasz {cash}$ oraz {actions} inwestycji\n{breaki}')
    d=input('')

def kalkulator():
    global cena,cash,calculator
    
    print('price: 5000$')
    try:
        value=int(input('Yes(1)/No(0): '))
        if cash>=5000:
            if value==1:
                calculator=True
                cash-=5000
            else:
                pass
        else:
            print('masz za mało kasy')
    except ValueError:
        print('')

def metatimer_for_all():
    global down_cours, up_cours, metatimer_up, metatimer_down,event_error,metatimer_error,event,metatimer_event,cash
    if down_cours:
        metatimer_down += 1
        if metatimer_down == 3:
            down_cours = False
            metatimer_down = 0
    elif up_cours:
        metatimer_up += 1
        if metatimer_up == 3:
            up_cours = False
            metatimer_up = 0
    elif event_error:
        metatimer_error += 1
        if metatimer_error == 3:
            event_error = False
            metatimer_error = 0
    if cash==1000:
        event=True
        if event:
            metatimer_event+=1
            if metatimer_event==10:
                wydarzenie()
                metatimer_event=0
    else:
        pass


def Dark_Net_Shop():
    global cash,up_cours,down_cours
    choice=int(input('Zwiększ Kurs(0)/Zmniejsz Kurs(1): '))
    match choice:
        case 0:
            if cash>=5000:
                choice2=int(input('Price: 5000$ Yes(1)/No(0)'))
                match choice2:
                    case 1:
                        cash-=5000
                        up_cours=True
                    case _:
                        pass
            else:
                pass
        case 1:
            if cash>=5000:
                choice2=int(input('Price: 5000$ Yes(1)/No(0)'))
                match choice2:
                    case 1:
                        cash-=5000
                        down_cours=True
                    case _:
                        pass
            else:
                pass

def Dark_Net(a):
    global cash,darkN
    try:
        match a:
            case 1:
                print('kup dostęp za: 5000$')
                value=int(input('Yes(1)/No(0): '))
                if cash>=5000:
                    if value==1:
                        darkN=True
                        cash-=5000
                    else:
                        pass
                else:
                    print('masz za mało kasy')
            case 2:
                print('=====W|tamψy W DarKK NΔEcie')
                choice=int(input('złóż łapówki firmie inwestycyjnej YES(1)/NO(0): '))
                match choice:
                    case 1: 
                        Dark_Net_Shop()      

    except ValueError:
        print('')

def shop():
    breek='==================='
    print(f'{breek}\n1.Kalkulator\n{breek}\n2.Dostęp do Dark Netu\n{breek}\n')
    value=int(input('wybierz przedmiot:'))
    if value==1:
        kalkulator()
    elif value==2:
        Dark_Net(1)

def start_game():
    global cena,cash,darkN
    round(cash,1)
    occurrence_of_tax()    
    print(f'=====aktualna cena {cena}$ =====')
    try:
        if darkN==True:
            choice=int(input('wybierz opcje: 1(inwestuj) 2(sprzedaj) 3(sprawdź swój portfel) 4(Wejdź do sklepu) 5(wykonaj prace) 6(We!dx D0 D@rKK NqTu) : '))
            match choice:
                case 1:
                    inwestycja()
                case 2:
                    sell()
                case 3:
                    view_wallet()
                case 4:
                    shop()
                case 5:
                    choice_job()
                case 6:
                    Dark_Net(2)
                case _:
                    pass
        else:
            choice=int(input('wybierz opcje: 1(inwestuj) 2(sprzedaj) 3(sprawdź swój portfel) 4(Wejdź do sklepu) 5(wykonaj prace) : '))
            match choice:
                case 1:
                    inwestycja()
                case 2:
                    sell()
                case 3:
                    view_wallet()
                case 4:
                    shop()
                case 5:
                    choice_job()
                case _:
                    pass
    except ValueError:
        print('try again')
        d=input('')

kurs()
while True:
    print(f'{cash}  {actions}')
    start_game()
    metatimer_for_all()
    kurs()
    os.system('cls')
