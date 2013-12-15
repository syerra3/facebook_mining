import core.model as model
import suggestion 
__name__ = "main"
try:
    """ main module """
    manager = suggestion.SuggestionManager()
    scores,suggestions = manager.get_compatibility("me",threshold = 60)
    if len(scores) > 0:
        print 'Most compatible people for you:'
        for k,v in scores.iteritems():
            print k,' (',v,')'
        print '---------------------------------'
        if len(suggestions['sports']) > 0:
            print 'Sports suggested for you:'
            for sport in suggestions['sports']:
                print sport
            print '---------------------------------'
        if len(suggestions['teams']) > 0:
            print 'Teams suggested for you:'
            for team in suggestions['teams']:
                print team
            print '---------------------------------'
        if len(suggestions['athlets']) > 0:
            print 'Athlets suggested for you:'
            for athlet in suggestions['athlets']:
                print athlet        
            print '---------------------------------'
    else:
        print 'No compatible person found for given threshold'
except model.AppException as ex:
    print ex
    
