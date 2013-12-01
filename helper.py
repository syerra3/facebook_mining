__name__= "helper"

import core
import connector
import datetime
class FacebookHelper:
    """ """
    def __init__(self):
        """ """
        try:
            self.connector = connector.FacebookConnector()
        except:
            ex = core.AppException("Error while creating Facebook connector")
            raise ex

    def get_facebook_user(self,id):
        """ """
        try:
            profile = self.connector.get_user(id)
            out = core.User()
            out.name = profile["name"]
            out.gender = profile["gender"]
            out.relationship_status = profile["relationship_status"]
            out.birthday = datetime.datetime.strptime(profile['birthday'], "%d/%m/%Y").date()
            return out
        except:
            ex = core.AppException("Error while geting Facebook user")
            raise ex 
        
    
