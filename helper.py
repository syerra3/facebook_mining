__name__= "helper"

import core.connector as connector
import core.model as model
import datetime
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
            out.name = profile["name"]
            if "gender" in profile.keys():
                out.gender = profile["gender"]
            if "relationship_status" in profile.keys():
                out.relationship_status = profile["relationship_status"]
            if "religion" in profile.keys():
                out.religion = profile["religion"]
            if "birthday" in profile.keys():
                out.birthday = datetime.datetime.strptime(profile['birthday'], "%m/%d/%Y").date()
            if "hometown" in profile.keys():
                hometown = profile["hometown"]
                out.hometown = hometown["name"]
            if "favorite_athletes" in profile.keys():
                out.favorite_athletes = list()
                favorite_athletes = profile["favorite_athletes"]
                for athlet in favorite_athletes:
                    out.favorite_athletes.append(str(athlet["name"]))
            if "languages" in profile.keys():
                languages = profile["languages"]
                out.languages = list()
                for language in languages:
                    out.languages.append(str(language["name"]))
            if "sports" in profile.keys():
                sports = profile["sports"]
                out.sports = list()
                for sport in sports:
                    out.sports.append(str(sport["name"]))
            if "location" in profile.keys():
                location = profile["location"]
                out.location = location["name"]
            return out
        except Exception as e:
            ex = model.AppException('Error while geting Facebook user:'+e.message)
            raise ex

    def get_facebook_user_friends(self,id):
        """ """
        try:
            out = list()
            friends = self.connector.get_friends(id)
            for friend in friends["data"]:
                out.append(str(friend["id"]))
            return out
        except Exception as e:
            ex = model.AppException("Error while getting Facebook user's friends:"+e.message)
            raise ex
        
    
