#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
"""Eliza Chat bot project"""
__author__ = 'Dimitri Papadakis'

import re
import random

def OkGoBa(r):
    l = ['good', 'ok', 'bad']
    rslt = ''
    isIt = False

    for wo in l:
        if re.search(fr'\b{wo}\b',r.lower()):
            if wo == 'good':
                ret= ['I am glad you are good, because I like happy people.', 'There is no better feeling than feeling good.', 'Great, happy people live longer.']
                isIt = True
            elif wo == 'ok':
                ret = ['Just ok?', 'What happened and you just feel ok?', 'Ok? Why?']
                isIt = True
            elif wo == "bad":
                ret = ['Why do you feel bad? Consider to go for a walk.', 'Why bad? What happened to you?', 'When I feel bad I like to read jokes in binary numbers while eating electrical cookies.\nTime to watch some funny YouTube videos.']
                isIt = True

    if not isIt:
        return rslt
    else:
        return random.choice(ret)

def emotions(r):
    l = ['very good', 'like you','very bad','sad','saddened']
    rslt = ''
    isIt = False

    for wo in l:
        if re.search(fr'\b{wo}\b',r.lower()):
            if wo == 'like':
                ret = ['Thank you for your like.']
                isIt = True

            elif wo == 'very good':
                ret = ['I sence good emotions. What a lovely day! Tell me more.', 'Good emotions, Nice! This is great. Stay happy.']
                isIt = True

            elif wo == 'very bad':
                ret = ['Do not let bad emotions fulfill your mind. Stay positive my friend.']
                isIt = True

            elif wo == 'sad':
                ret = ['I am sorry that you are sad. What happened?']
                isIt = True

            elif wo == 'saddened':
                ret = ['I am sorry that you are sad. What happened?\n']
                isIt = True
    if not isIt:
        return rslt
    else:
        return random.choice(ret)

def family(r):
    rslt1 = ''
    family = ['mother', 'mom', 'father', 'dad', 'sister', 'grandpa', 'grandma', 'uncle', 'aunt', 'brother','friend']

    for member in family:
        if re.search(fr'\b{member}\b',r.lower()):
            ret = ["That's interesting, talk to me about your familly.", "I see, it is good to be with family members.", "Always pleasure to be around familly."]
            rslt1 = random.choice(ret)

    return rslt1

def whatever(r):
    rslt1 = ''
    retur = ['hmmm, interesting. Tell me more.', 'Lets talk about something else. What interesting thing did you do today?',"Couldn't agree more."]
    rslt1 = random.choice(retur)

    return rslt1

def ed(r1):
    str = r1.split(" ")
    rslt = ''
    for w in str:
        rslt = ''
        remember=0
        for w in str:
            if 'ed' in w:
                if '.' in w:
                    rslt = f'Why did you {w[:-3]} '
                    remember = str.index(w)
                else:
                    rslt = f'Why did you {w[:-2]} '
                    remember = str.index(w)

        if rslt != '':
            for i in range(remember + 1, len(str)):
                rslt += str[i] + " "

            if '.' in rslt:
                rslt = rslt.replace('.', '')

            rslt += '?'
    return rslt

def answer(re1):
    re1 = re1.lower()

    fast = {'i am': 'you are',
            'i was': 'you were',
            'i': 'you',
            "i'm": 'you are',
            "i'd": 'you would',
            "i've": 'you have',
            "i'll": 'you will',
            'my': 'your',
            'you are': 'I am',
            'you were': 'I was',
            "you've": 'I have',
            "you'll": 'I will',
            'your': 'my',
            'yours': 'mine',
            'mine': 'yours',
            'you': 'me',
            'me': 'you',
            "you will": "I will"}

    sp = re1.split(" ")
    for i in range(len(sp)):
        if sp[i].lower() in fast.keys():
            sp[i] = sp[i].replace(sp[i], fast[sp[i]])

    re1 = " ".join(str(x) for x in sp)

    wentIn = False
    original = re1

    familyB = False
    emotionsB = False
    edB = False
    OkGoBaB = False

    temp2 = family(original)
    if temp2 != '':
        re1 = temp2 +"\n"
        familyB = True

    temp4 = emotions(original)
    if temp4 != '':
        if familyB:
            re1 += temp4 + "\n"
        else:
            re1 = temp4
            emotionsB = True

    temp5 = OkGoBa(original)
    if temp5 != '':
        if emotionsB==False and familyB:
            re1 += temp5 + "\n"
        elif not emotionsB:
            re1 = temp5
            OkGoBaB = True

    temp3 = ed(original)
    if temp3 != '':
        if emotionsB or familyB or OkGoBaB:
            re1 += temp3 + "\n"
        else:
            re1 = temp3
            edB = True

    temp6 = whatever(original)
    if temp6 != '':
        if not emotionsB and not familyB and not OkGoBaB and not edB:
            re1 = temp6

    return re1

exit1 = 'bye'
name = input("Hello, my name is Eliza. What is your name?\n")


person_Split = name.split(" ")
name1 = ""

if len(person_Split) > 1:
    name = person_Split[len(person_Split)-1]
    if name[len(name)-1]=='.':
        name = name[:-1]
     
print(f'Nice to meet you {name.title()}! What did you do today?')

out = " "
while(out.lower() != exit1 ):
    out = input()

    if out.lower() != 'bye':
        print(answer(out))
