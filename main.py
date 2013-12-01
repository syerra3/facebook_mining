import core
import algorithms
import helper

__name__ = "main"
try:
    h = helper.FacebookHelper()
    user = h.get_facebook_user("me")
    print user
except core.AppException as ex:
    print ex
    

