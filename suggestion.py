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
            print user.name, user.zodiac, user.id
            print user.sports
            print user.favorite_athletes
            print user.favorite_teams
            print user.education, user.work
            #self.h.execute_facebook_fql('SELECT user_id FROM like')
            print '------------------'
            #for fid in fids:
            #    friend = self.h.get_facebook_user(fid)
            #    print friend.name,friend.gender, friend.relationship_status, friend.religion, friend.hometown, friend.location, friend.zodiac
            #    print friend.birthday
            #    print friend.favorite_athletes
            #    print friend.favorite_teams
            #    print friend.languages
            #    print friend.education, friend.work
            #    print 'Name compatibility: ',algorithms.get_name_compatibility(user.name,friend.name)
            #    if user.zodiac is not None and friend.zodiac is not None:
            #        print 'Zodiac compatibility: ',algorithms.get_zodiac_compatibility(user.zodiac,friend.zodiac)
            #    if user.sports is not None and friend.sports is not None:
            #        print 'Sports compatibility: ',algorithms.get_similarity(user.sports, friend.sports)
            #    if user.favorite_athletes is not None and friend.favorite_athletes is not None:
            #        print 'Athlet compatibility: ',algorithms.get_similarity(user.favorite_athletes, friend.favorite_athletes)
            #    if user.favorite_teams is not None and friend.favorite_teams is not None:
            #        print 'Favorite teams compatibility: ',algorithms.get_similarity(user.favorite_teams, friend.favorite_teams)
            #    if user.languages is not None and friend.languages is not None:
            #        print 'Language compatibility: ',algorithms.get_similarity(user.languages, friend.languages)
            #    print '----------------------'
                #if friend.gender == 'female' and (friend.relationship_status == 'Single' or friend.relationship_status == ''):
                #    print friend.name, '(Name compatibility :',algorithms.get_name_compatibility(user.name,friend.name),')'
            return scores
        except Exception as e:
            
            ex = model.AppException('Exception occured at get_best_match:'+e.message)
            raise ex
  
    
    
