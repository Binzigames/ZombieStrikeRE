import PlaymanityAPI.API as API

#---------------------------------> Strings and bools for use
photoURL = None
ADinfo = None
Isactive = False
ADurl = None

gUUID = None
dID = None

#---------------------------------> Functions to use
def init_api(global_gUUID, global_dID):
    global gUUID, dID
    gUUID, dID = global_gUUID, global_dID
    API.check_sdk()
    API.main(gUUID, dID)

def get_ad_data():
    response = API.get_ad(gUUID , dID)
    if response and isinstance(response, dict):
        return response
    return {}

def get_photoURL():
    global photoURL
    response = get_ad_data()
    photoURL = response.get("media", None)
    return photoURL

def get_ad_info():
    global ADinfo
    ADinfo = get_ad_data()
    return ADinfo

def get_url():
    global ADurl
    response = get_ad_data()
    ADurl = response.get("url", None)
    return ADurl

def get_IsActive():
    global Isactive
    response = get_ad_data()
    Isactive = response.get("isActive", False)
    return Isactive

#---------------------------------> Debug
#if __name__ == "__main__":
    #test_gUUID = "test_uuid"
    #test_dID = "test_did"
    #init_api(test_gUUID, test_dID)
    #print("Photo URL:", get_photoURL())
    #print("Ad Info:", get_ad_info())
    #print("Ad URL:", get_url())
    #print("Is Active:", get_IsActive())