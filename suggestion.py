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
        
    def get_suggestions(self, id, threshold = 30):
        """ """
        try:
            suggestions = dict()
            suggestions['sports'] = set()
            suggestions['athlets'] = set()
            suggestions['teams'] = set()
            suggestions['languages'] = set()
            friends, user, fids = list(), self.h.get_facebook_user(id),self.h.get_facebook_user_friends(id)
            for fid in fids:
                score = 0
                friend = self.h.get_facebook_user(fid)
                score += algorithms.get_name_compatibility(user.name,friend.name)
                if user.zodiac is not None and friend.zodiac is not None:
                    score += algorithms.get_zodiac_compatibility(user.zodiac,friend.zodiac)
                if user.sports is not None and friend.sports is not None:
                    score += algorithms.get_similarity(user.sports, friend.sports)
                if user.favorite_athletes is not None and friend.favorite_athletes is not None:
                    score += algorithms.get_similarity(user.favorite_athletes, friend.favorite_athletes)
                if user.favorite_teams is not None and friend.favorite_teams is not None:
                    score += algorithms.get_similarity(user.favorite_teams, friend.favorite_teams)
                if user.languages is not None and friend.languages is not None:
                    score += algorithms.get_similarity(user.languages, friend.languages)
                if user.hometown is not None and friend.hometown is not None:
                    score += algorithms.get_similarity(user.hometown.split(","),friend.hometown.split(","))
                if user.location is not None and friend.location is not None:
                    score += algorithms.get_similarity(user.location.split(","),friend.location.split(","))         
                #print score, friend.name
                if score >= threshold:
                    if friend.sports is not None:
                        for sport in friend.sports:
                            suggestions['sports'].add(sport)
                    if friend.favorite_teams is not None:
                        for team in friend.favorite_teams:
                            suggestions['teams'].add(team)
                    if friend.favorite_athletes is not None:
                        for athlet in friend.favorite_athletes:
                            suggestions['athlets'].add(athlet)
                    if friend.languages is not None:
                        for language in friend.languages:
                            suggestions['languages'].add(language)

            if user.sports is not None:
                suggestions['sports'] = suggestions['sports'].difference(set(user.sports))
            if user.favorite_teams is not None:
                suggestions['teams'] = suggestions['teams'].difference(set(user.favorite_teams))
            if user.favorite_athletes is not None:
                suggestions['athlets'] = suggestions['athlets'].difference(set(user.favorite_athletes))
            if user.languages is not None:
                suggestions['languages'] = suggestions['languages'].difference(set(user.languages))
            return suggestions
        except Exception as e:
            ex = model.AppException('Exception occured at get_suggestions: '+e.message)
            raise ex

    def get_best_match(self, id, n=1, gender = 'female'):
        """ """
        try:
            scores = dict()
            friends, user, fids = list(), self.h.get_facebook_user(id),self.h.get_facebook_user_friends(id)
            #print user.name, user.zodiac, user.id, user.age
            #print user.sports
            #print user.favorite_athletes
            #print user.favorite_teams
            #print user.education, user.work
            #print user.hometown.split(",")
            #print '------------------'
            for fid in fids:
                friend = self.h.get_facebook_user(fid)
                #print friend.name,friend.gender, friend.relationship_status, friend.religion, friend.hometown, friend.location, friend.zodiac
                #print friend.age
                #print friend.favorite_athletes
                #print friend.favorite_teams
                #print friend.languages
                #print friend.education, friend.work
                #print 'Name compatibility: ',algorithms.get_name_compatibility(user.name,friend.name)
                if user.zodiac is not None and friend.zodiac is not None:
                    print 'Zodiac compatibility: ',algorithms.get_zodiac_compatibility(user.zodiac,friend.zodiac)
                if user.sports is not None and friend.sports is not None:
                    print 'Sports compatibility: ',algorithms.get_similarity(user.sports, friend.sports)
                if user.favorite_athletes is not None and friend.favorite_athletes is not None:
                    print 'Athlet compatibility: ',algorithms.get_similarity(user.favorite_athletes, friend.favorite_athletes)
                if user.favorite_teams is not None and friend.favorite_teams is not None:
                    print 'Favorite teams compatibility: ',algorithms.get_similarity(user.favorite_teams, friend.favorite_teams)
                if user.languages is not None and friend.languages is not None:
                    print 'Language compatibility: ',algorithms.get_similarity(user.languages, friend.languages)
                if user.hometown is not None and friend.hometown is not None:
                    print 'Hometown compatibility: ',algorithms.get_similarity(user.hometown.split(","),friend.hometown.split(","))
                if user.location is not None and friend.location is not None:
                    print 'Location compatibility: ',algorithms.get_similarity(user.location.split(","),friend.location.split(","))
                print '----------------------'
                
                #if friend.gender != 'female' and (friend.relationship_status == 'Single' or friend.relationship_status == ''):
                #    print friend.name, '(Name compatibility :',algorithms.get_name_compatibility(user.name,friend.name),')'
            return scores
        except Exception as e:
            
            ex = model.AppException('Exception occured at get_best_match:'+e.message)
            raise ex
  
    
    
