__name__= "helper"

import core.connector as connector
import core.model as model
import datetime
import unicodedata


def get_zodiac_sign(day, month):
    """ """
    if month == 3: #March
        if day <= 20:
            return 'Pisces'
        else:
            return 'Aries'
    if month == 4: #April
        if day <=19:
            return 'Aries'
        else:
            return 'Taurus'
    if month == 5: #May
        if day <=20:
            return 'Taurus'
        else:
            return 'Gemini'
    if month == 6: #June
        if day <= 20:
            return 'Gemini'
        else:
            return 'Cancer'
    if month == 7: #July
        if day <= 22:
            return 'Cancer'
        else:
            return 'Leo'
    if month == 8: #August
        if day <= 22:
            return 'Leo'
        else:
            return 'Virgo'
    if month == 9: #September
        if day <= 22:
            return 'Virgo'
        else:
            return 'Libra'
    if month == 10: #October
        if day <= 22:
            return 'Libra'
        else:
            return 'Scorpio'
    if month == 11: #November
        if day <= 21:
            return 'Scorpio'
        else:
            return 'Sagittarius'
    if month == 12: #December
        if day <= 21:
            return 'Sagittarius'
        else:
            return 'Capricorn'
    if month == 1: #January
        if day <= 19:
            return 'Capricorn'
        else:
            return 'Aquarius'
    if month == 2: #Feb
        if day <= 18:
            return 'Aquarius'
        else:
            return 'Pisces'

class FacebookHelper:
    """ """
    def __init__(self):
        """ """
        try:
            self.connector = connector.FacebookConnector()
        except:
            ex = model.AppException("Error while creating Facebook connector")
            raise ex

    def get_facebook_user(self,id):
        """ """
        try:
            profile = self.connector.get_user(id)
            out = model.User()
            out.name = unicodedata.normalize('NFKD', profile["name"]).encode('ascii','ignore')
            if "gender" in profile.keys():
                out.gender = unicodedata.normalize('NFKD', profile["gender"]).encode('ascii','ignore')
            if "relationship_status" in profile.keys():
                out.relationship_status =  unicodedata.normalize('NFKD', profile["relationship_status"]).encode('ascii','ignore')
            if "religion" in profile.keys():
                out.religion = unicodedata.normalize('NFKD', profile["religion"]).encode('ascii','ignore')
            if "birthday" in profile.keys():
                tokens = profile['birthday'].split('/',3) #m/d/Y
                out.zodiac = get_zodiac_sign(int(tokens[1]),int(tokens[0]))
            if "hometown" in profile.keys():
                hometown = profile["hometown"]
                out.hometown = unicodedata.normalize('NFKD', hometown["name"]).encode('ascii','ignore')
            if "favorite_athletes" in profile.keys():
                out.favorite_athletes = list()
                favorite_athletes = profile["favorite_athletes"]
                for athlet in favorite_athletes:
                    out.favorite_athletes.append(unicodedata.normalize('NFKD', athlet["name"]).encode('ascii','ignore'))
            if "languages" in profile.keys():
                languages = profile["languages"]
                out.languages = list()
                for language in languages:
                    out.languages.append(unicodedata.normalize('NFKD', language["name"]).encode('ascii','ignore'))
            if "sports" in profile.keys():
                sports = profile["sports"]
                out.sports = list()
                for sport in sports:
                    out.sports.append(unicodedata.normalize('NFKD', sport["name"]).encode('ascii','ignore'))
            if "location" in profile.keys():
                location = profile["location"]
                out.location = unicodedata.normalize('NFKD', location["name"]).encode('ascii','ignore')
            if "favorite_teams" in profile.keys():
                favorite_teams = profile["favorite_teams"]
                out.favorite_teams = list()
                for team in favorite_teams:
                    out.favorite_teams.append(unicodedata.normalize('NFKD', team["name"]).encode('ascii','ignore'))
            return out
        except Exception as e:
            ex = model.AppException('Error while geting Facebook user:'+e.message)
            raise ex

    def get_facebook_user_friends(self,id):
        """ """
        try:
            out = list()
            friends = self.connector.get_friends(id)
            #print friends 
            for friend in friends["data"]:
                out.append(str(friend["id"]))
            return out
        except Exception as e:
            ex = model.AppException("Error while getting Facebook user's friends:"+e.message)
            raise ex
        
