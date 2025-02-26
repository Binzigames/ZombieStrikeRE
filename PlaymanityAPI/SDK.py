import API
#---------------------------------> strings and bools for use
photoURL = None
ADinfo = None
Isactive = False
ADurl = None
#---------------------------------> functions to use (this one load the strings and bools)
#start api (+check files, if game_uuid or device_id = 0, it will be changed for basic (debug))
def init_api():
    API.check_sdk()
    API.main(0, 0)
#get functions (load for user information)
def get_photoURL():
    global photoURL
    response = API.get_ad()
    if response and "media" in response:
        photoURL = response
    return

def get_ad_info():
    global ADinfo
    response = API.get_ad()
    if response:
        ADinfo = response
    return
def get_url():
    global ADurl
    response = API.get_ad()
    if response and "url" in response:
        ADurl = response
    return
def get_IsActive():
    global Isactive
    response = API.get_ad()
    if response and "isActive" in response:
        Isactive = response
    return
#---------------------------------> debug
#if __name__ == "__main__":
    #init_api()
