import core.model as model
import suggestion 
__name__ = "main"
try:
    manager = suggestion.SuggestionManager()
    #print manager.get_best_friends("me")
    #print manager.get_best_match("me")
    print manager.get_suggestions("me", threshold = 35)
except model.AppException as ex:
    print ex
    

