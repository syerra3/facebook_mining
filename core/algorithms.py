__name__ = "algorithms"

import datetime
import string

zodiac_signs = { 'Aquarius':0,'Pisces':1,'Aries':2,'Taurus':3,'Gemini':4,'Cancer':5,'Leo':6,'Virgo':7,'Libra':8,'Scorpio':9,'Sagittarius':10,'Capricorn':11} 
zodiac_scores = list()
zodiac_scores.append([9.4,4  ,7  ,1  ,9  ,3  ,5  ,3  ,9  ,7  ,7  ,4  ]) #Aquarius
zodiac_scores.append([4  ,9.5,4  ,8  ,2  ,8  ,3  ,5  ,3  ,7  ,6  ,8  ]) #Pisces
zodiac_scores.append([7  ,4  ,9.5,3  ,8  ,2  ,9  ,3  ,5  ,3  ,8  ,2  ]) #Aries
zodiac_scores.append([1  ,8  ,3  ,9.5,4  ,8  ,1  ,10 ,3  ,5  ,3  ,10 ]) #Taurus
zodiac_scores.append([9  ,2  ,8  ,4  ,9.5,4  ,8  ,1  ,10 ,3  ,5  ,3  ]) #Gemini
zodiac_scores.append([3  ,8  ,2  ,8  ,4  ,9.5,4  ,6  ,2  ,9  ,3  ,5  ]) #Cancer
zodiac_scores.append([5  ,3  ,9  ,1  ,8  ,4  ,9.5,4  ,7  ,2  ,10 ,3  ]) #Leo
zodiac_scores.append([3  ,5  ,3  ,10 ,1  ,6  ,4  ,9.5,4  ,8  ,2  ,10 ]) #Virgo
zodiac_scores.append([9  ,3  ,5  ,3  ,10 ,2  ,7  ,4  ,9.5,4  ,8  ,1  ]) #Libra
zodiac_scores.append([7  ,7  ,3  ,5  ,3  ,9  ,2  ,8  ,4  ,9.5,4  ,6  ]) #Scorpio
zodiac_scores.append([7  ,6  ,8  ,3  ,5  ,3  ,9  ,2  ,8  ,4  ,9.5,5  ]) #Sagittarius
zodiac_scores.append([4  ,8  ,2  ,10 ,3  ,5  ,3  ,10 ,1  ,6  ,5  ,9.5]) #capricorn


chaldean_numerology = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':8,'g':3,'h':5,'i':1,'j':1,'k':2,'l':3,'m':4,'n':5,'o':7,'p':8,'q':1,'r':2,'s':3,'t':4,'u':6,'v':6,
                       'w':6,'x':5,'y':1,'z':7}
chaldean_scores = list()
chaldean_scores.append([0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ]) #0
chaldean_scores.append([0  ,6  ,7  ,6.5,1  ,4  ,9  ,8  ,7.5,2  ]) #1
chaldean_scores.append([0  ,8  ,6.5,2  ,8  ,6.5,6  ,9  ,10 ,0  ]) #2
chaldean_scores.append([0  ,9.5,2  ,6  ,1  ,5  ,8  ,0  ,5  ,7  ]) #3
chaldean_scores.append([0  ,0  ,8  ,0  ,10 ,0  ,10 ,0  ,9  ,9  ]) #4
chaldean_scores.append([0  ,3  ,7  ,5  ,0  ,7  ,0  ,8  ,9  ,6.5]) #5
chaldean_scores.append([0  ,8  ,6.5,8.5,10 ,0  ,9  ,3  ,8  ,7.5]) #6
chaldean_scores.append([0  ,6  ,9  ,0  ,0  ,8  ,2  ,0  ,5.5,10 ]) #7
chaldean_scores.append([0  ,7.5,9  ,5  ,9  ,10 ,10 ,6.5,9  ,6  ]) #8
chaldean_scores.append([0  ,0  ,0  ,7  ,0  ,6  ,8  ,10 ,6  ,10 ]) #9

def sum_digits(n):
    """ """
    s = 0
    while n:
        s += n % 10
        n /= 10
    return s

def get_chaldean_score(name):
    """ """
    if name == None:
        return 0
    score = 0
    for c in name.lower():
        if c.isalpha():
            score += chaldean_numerology[c]
    while score >=10:
        score = sum_digits(score)
    return score

            
def get_zodiac_sign(date):
    """ """
    if date == None:
        return ''
    if date.month == 3: #March
        if date.day <= 20:
            return 'Pisces'
        else:
            return 'Aries'
    if date.month == 4: #April
        if date.day <=19:
            return 'Aries'
        else:
            return 'Taurus'
    if date.month == 5: #May
        if date.day <=20:
            return 'Taurus'
        else:
            return 'Gemini'
    if date.month == 6: #June
        if date.day <= 20:
            return 'Gemini'
        else:
            return 'Cancer'
    if date.month == 7: #July
        if date.day <= 22:
            return 'Cancer'
        else:
            return 'Leo'
    if date.month == 8: #August
        if date.day <= 22:
            return 'Leo'
        else:
            return 'Virgo'
    if date.month == 9: #September
        if date.day <= 22:
            return 'Virgo'
        else:
            return 'Libra'
    if date.month == 10: #October
        if date.day <= 22:
            return 'Libra'
        else:
            return 'Scorpio'
    if date.month == 11: #November
        if date.day <= 21:
            return 'Scorpio'
        else:
            return 'Sagittarius'
    if date.month == 12: #December
        if date.day <= 21:
            return 'Sagittarius'
        else:
            return 'Capricorn'
    if date.month == 1: #January
        if date.day <= 19:
            return 'Capricorn'
        else:
            return 'Aquarius'
    if date.month == 2: #Feb
        if date.day <= 18:
            return 'Aquarius'
        else:
            return 'Pisces'

def get_zodiac_compatibility(sign1 ,sign2):
    """ """
    scores = zodiac_scores[zodiac_signs[sign1]]
    return scores[zodiac_signs[sign2]]

def get_name_compatibility(name1 , name2):
    """ """
    scores = chaldean_scores[get_chaldean_score(name1)]
    return scores[get_chaldean_score(name2)]
    

#print zodiac_signs['Pisces'],zodiac_signs['Aries'],zodiac_signs['Aquarius'],zodiac_signs['Capricorn'],zodiac_signs['Sagittarius'],zodiac_signs['Scorpio']
#print get_zodiac_compatibility('Pisces','Aries')
#print get_name_compatibility('Adam','Eve')
