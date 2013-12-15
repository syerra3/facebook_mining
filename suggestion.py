__name__ = "suggestion"
import core.model as model
import core.algorithms as algorithms
import helper

class SuggestionManager:
    """ encapsulates business logic """
    
    def __init__(self):
        """ constructor """
        try:
            self.h = helper.FacebookHelper()
        except Exception as e:
            ex = model.AppException(e.message)
            raise ex

    def get_best_match(self, id, n=1):
        """ return best match from friend's for the given user """
        try:
            scores = dict()
            friends, user, fids = list(), self.h.get_facebook_user(id),self.h.get_facebook_user_friends(id)
            return scores
        except Exception as e:
            ex = model.AppException('Exception occured at get_best_friends:'+e.message)
            raise ex
        
    def get_compatibility(self, id, threshold = 60):
        """ returns friend's compatibility scores for  the given user"""
        try:
            friends, user, fids = list(), self.h.get_facebook_user(id),self.h.get_facebook_user_friends(id)
            scores, suggestions = dict(), dict()
            suggestions['sports'] = set()
            suggestions['athlets'] = set()
            suggestions['teams'] = set()
            suggestions['languages'] = set()
            for fid in fids:
                score ,friend = 0, self.h.get_facebook_user(fid)
                score += algorithms.get_name_compatibility(user.name,friend.name)
                #Zodiac compatibility
                if user.zodiac is not None and friend.zodiac is not None:
                    score += algorithms.get_zodiac_compatibility(user.zodiac,friend.zodiac)
                else:
                    score += 3
                #language compatibility
                if user.languages is not None and friend.languages is not None:
                    score += algorithms.get_similarity(user.languages, friend.languages)
                else:
                    score += 3
                #Hometown
                if user.hometown is not None and friend.hometown is not None:
                    score += algorithms.get_similarity(user.hometown.split(","),friend.hometown.split(","))
                else:
                    score += 3
                #Location
                if user.location is not None and friend.location is not None:
                    score += algorithms.get_similarity(user.location.split(","),friend.location.split(","))
                else:
                    score += 3
                #Education
                if user.education is not None and friend.education is not None:
                    score += algorithms.get_education_compatibility(user.education, friend.education )
                else:
                    score += 3
                #Sports
                if user.sports is not None and friend.sports is not None:
                    score += algorithms.get_similarity(user.sports, friend.sports)
                else:
                    score += 3
                score = (score * 100.0)/70
                print friend.name,friend.education, friend.work, friend.age, score
                if score >= threshold:
                    scores[friend.name] = score 
                    if friend.sports is not None:
                        for sport in friend.sports:
                            suggestions['sports'].add(sport)
                    if friend.favorite_teams is not None:
                        for team in friend.favorite_teams:
                            suggestions['teams'].add(team)
                    if friend.favorite_athletes is not None:
                        for athlet in friend.favorite_athletes:
                            suggestions['athlets'].add(athlet)
            if user.sports is not None:
                suggestions['sports'] = suggestions['sports'].difference(set(user.sports))
            if user.favorite_teams is not None:
                suggestions['teams'] = suggestions['teams'].difference(set(user.favorite_teams))
            if user.favorite_athletes is not None:
                suggestions['athlets'] = suggestions['athlets'].difference(set(user.favorite_athletes))
            return scores, suggestions 
        except Exception as e:            
            ex = model.AppException('Exception occured at get_best_match:'+e.message)
            raise ex
  
    
    
