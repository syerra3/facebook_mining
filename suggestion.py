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
            #print user
            for fid in fids:
                friend = self.h.get_facebook_user(fid)
                scores[friend.name] = algorithms.get_name_compatibility(user.name,friend.name)    
            return scores
        except Exception as e:
            ex = model.AppException(e.message)
            raise ex
        
    def get_suggestions(self, id):
        return dict()

    def get_best_match(self, id, n=1):
        return list()
    
    
    
