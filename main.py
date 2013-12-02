import core.model as model
import suggestion 
__name__ = "main"
try:
    manager = suggestion.SuggestionManager()
    print manager.get_best_friends("me")
except model.AppException as ex:
    print ex
    

