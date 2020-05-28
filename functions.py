from secrets import token_hex
from random import choice, randint
from db import create_connection, namelist, entry, increment, findhex

def registration(name, link, promo ):
    r = open('lencheck.txt','r')
    lencheck = r.read()
    dictionary={'name':name,'link':link, 'hex':token_hex(5), 'balance':800}
    if len(str(lencheck))<=10:
        dictionary['balance']=1000
        r = open('lencheck.txt','a')
        r.write('1')
    elif promo in ['SLYTHERIN','faa31489']:
        r = open('validity.txt', 'r')
        validity = r.read()
        if 'faa31489'*15 not in validity:
           dictionary['balance']=1000
        elif promo == "SLYTHERIN":
            dictionary['balance']=1000
    return dictionary

def data_entry(dictionary):
    r = open('existense.txt','r')
    existense = r.read()
    if dictionary['link'] not in existense:
        conn = create_connection('riches.db')
        r = open('existense.txt','a')
        r.write(dictionary['link'])
        with conn:
            if len(dictionary)==4:
                names=(dictionary['name'],dictionary['link'],dictionary['balance'],dictionary['hex'])
                entry(names)
                return "SUCCESS!"
    else:
        return "Already exists"

def coinflip_func(supply):
    if findhex(supply['id_num'])[0]['balance']<supply['amount']:
        supply['answer']="Not enough balance"
        supply['amount']=findhex(supply['id_num'])[0]['balance']
        supply['id_num']=f"{findhex(supply['id_num'])[0]['name']}"
        return supply
    else:
        cpu=randint(1,2)
        if int(supply['prediction'])==cpu:
            supply['amount']= round(supply['amount']*0.5)

        else:
            supply['amount']=(-supply['amount'])
        if cpu==1:
            supply['answer']="Heads"
        elif cpu==2: 
            supply['answer']="Tails"
        result = increment(supply['id_num'], supply['amount'])
        supply['amount']=result[0]['balance']
        supply['id_num']=f"{findhex(supply['id_num'])[0]['name']}"
    return(supply)

def dice_func(supply):
    if findhex(supply['id_num'])[0]['balance']<supply['amount']:
        supply['user']='N/A'
        supply['cpu']='N/A'
        supply['answer']="Not enough balance"
        supply['amount']=findhex(supply['id_num'])[0]['balance']
        supply['id_num']=f"{findhex(supply['id_num'])[0]['name']}"
        return(supply)
    else:
        supply['user']=randint(1,6)
        supply['cpu']=randint(1,6)
        if supply['user']>supply['cpu']:
            supply['answer']='USER Wins'
            result = increment(supply['id_num'], supply['amount'])
            supply['amount']=result[0]['balance']
        elif supply['user']<supply['cpu']:
            supply['answer']='CPU Wins'
            supply['amount']=(-supply['amount'])
            result = increment(supply['id_num'], supply['amount'])
            supply['amount']=result[0]['balance']
        else:
            supply['answer']='Draw'
            supply['amount']=findhex(supply['id_num'])[0]['balance']
        supply['id_num']=f"{findhex(supply['id_num'])[0]['name']}"
        return(supply)

def slots_func(supply):
    if findhex(supply['id_num'])[0]['balance']<supply['amount']:
        supply['display']="N/A"
        supply['answer']="Not enough balance"
        supply['amount']=findhex(supply['id_num'])[0]['balance']
        supply['id_num']=f"{findhex(supply['id_num'])[0]['name']}"
        return(supply)
    else:
        supply['display']=f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        display=[i for i in supply['display']]
        if len(set(display))==1:
            supply['answer']='All matched'
            result = increment(supply['id_num'], supply['amount'])
            supply['amount']=result[0]['balance']
        elif len(set(display))==2:
            supply['answer']='Two matched'
            result = increment(supply['id_num'], supply['amount']*.5)
            supply['amount']=result[0]['balance']
        else:
            supply['answer']='No match'
            supply['amount']=(-supply['amount'])
            result = increment(supply['id_num'], supply['amount'])
            supply['amount']=result[0]['balance']
            supply['id_num']=f"{findhex(supply['id_num'])[0]['name']}"
        return(supply)

def roulette_func(supply):
    if findhex(supply['id_num'])[0]['balance']<supply['amount']:
        supply['display']="N/A"
        supply['answer']="Not enough balance"
        supply['amount']=findhex(supply['id_num'])[0]['balance']
        supply['id_num']=f"{findhex(supply['id_num'])[0]['name']}"
        return(supply)
    else:
        cpu_num=randint(1,50)
        cpu_color=randint(1,2)
        if cpu_color==1:
            cpu_color_name='Black'
        else:
            cpu_color_name='White'
        supply['result']=f"{cpu_num} of {cpu_color_name}"
        if supply['prediction']==cpu_num and int(supply['color'])==cpu_color:
            supply['answer']='3x'
            result = increment(supply['id_num'], supply['amount']*2)
            supply['amount']=result[0]['balance']
        elif supply['prediction']==cpu_num:
            supply['answer']='2x'
            result = increment(supply['id_num'], supply['amount'])
            supply['amount']=result[0]['balance']
        elif int(supply['color'])==cpu_color and supply['prediction']%2==cpu_num%2:
            supply['answer']='1.5x'
            result = increment(supply['id_num'], supply['amount']*.5)
            supply['amount']=result[0]['balance']
        elif int(supply['color'])==cpu_color or supply['prediction']%2==cpu_num%2:
            supply['answer']='0.5x'
            supply['amount']=(-supply['amount']*.5)
            result = increment(supply['id_num'], supply['amount'])
            supply['amount']=result[0]['balance']
        else:
            supply['answer']='No match'
            supply['amount']=(-supply['amount'])
            result = increment(supply['id_num'], supply['amount'])
            supply['amount']=result[0]['balance']
        supply['id_num']=f"{findhex(supply['id_num'])[0]['name']}"
        return(supply)

def ludo_func(supply):
    if findhex(supply['id1'])[0]['balance']<supply['amount'] or findhex(supply['id2'])[0]['balance']<supply['amount'] or findhex(supply['id3'])[0]['balance']<supply['amount'] or findhex(supply['id4'])[0]['balance']<supply['amount']:
        supply['answer']="One of you doesn't meet the amount"
        supply['id1']=f"{findhex(supply['id1'])[0]['name']}: {findhex(supply['id1'])[0]['balance']}"
        supply['id2']=f"{findhex(supply['id2'])[0]['name']}: {findhex(supply['id2'])[0]['balance']}"
        supply['id3']=f"{findhex(supply['id3'])[0]['name']}: {findhex(supply['id3'])[0]['balance']}"
        supply['id4']=f"{findhex(supply['id4'])[0]['name']}: {findhex(supply['id4'])[0]['balance']}"
        return(supply)
    else:
        supply['answer']='Success'
        increment(supply['id1'], supply['amount']*1.5)
        increment(supply['id2'], supply['amount']*1)
        increment(supply['id3'], 0)
        increment(supply['id4'], supply['amount']*(-1))
        supply['id1']=f"{findhex(supply['id1'])[0]['name']}: {findhex(supply['id1'])[0]['balance']}"
        supply['id2']=f"{findhex(supply['id2'])[0]['name']}: {findhex(supply['id2'])[0]['balance']}"
        supply['id3']=f"{findhex(supply['id3'])[0]['name']}: {findhex(supply['id3'])[0]['balance']}"
        supply['id4']=f"{findhex(supply['id4'])[0]['name']}: {findhex(supply['id4'])[0]['balance']}"
    return(supply)