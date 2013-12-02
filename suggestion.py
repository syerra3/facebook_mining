__name__ = "suggestion"
import core.model as model
import core.algorithms as algorithms
import helper

class SuggestionManager:
    """ """
    def __init__(self):
        """ """
        try:
            self.h = helper.FacebookHelper()
        except Exception as e:
            ex = model.AppException(e.message)
            raise ex

    def get_best_friends(self, id, n=1):
        """ """
        try:
            scores = dict()
            friends, user, fids = list(), self.h.get_facebook_user(id),self.h.get_facebook_user_friends(id)
            print user
            for fid in fids:
                friend = self.h.get_facebook_user(fid)
                scores[friend.name] = algorithms.get_name_compatibility(user.name,friend.name)
                if friend.birthday is not None:
                    #print friend.birthday
                    scores[friend.name] += algorithms.get_zodiac_compatibility(user.birthday,friend.birthday)
            return scores
        except Exception as e:
            ex = model.AppException('Exception occured at get_best_friends:'+e.message)
            raise ex
        
    def get_suggestions(self, id):
        return dict()

    def get_best_match(self, id, n=1):
        """ """
        try:
            scores = dict()
            friends, user, fids = list(), self.h.get_facebook_user(id),self.h.get_facebook_user_friends(id)
            print user
            for fid in fids:
                friend = self.h.get_facebook_user(fid)
                if friend.gender == 'female' and (friend.relationship_status == 'Single' or friend.relationship_status == ''):
                    print friend.name, 'Name compatibility :',algorithms.get_name_compatibility(user.name,friend.name)
            return scores
        except Exception as e:
            ex = model.AppException('Exception occured at get_best_friends:'+e.message)
            raise ex
        
    
    
