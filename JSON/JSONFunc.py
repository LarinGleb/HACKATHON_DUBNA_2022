import json
from . import ConfigJSON
from . import ErrorsJSON

def LoadData(PATH = ConfigJSON.PATH_USERS):
    try:
        with open(PATH) as Users:
            data = json.load(Users)
            Users.close()
        return data
    except Exception as ex:
        print(ex)
    
def GetUserConfigDict(TelegaID: int = -1):
    if type(TelegaID) != int:
        raise ErrorsJSON.InvalidID(f"ID {TelegaID} isn't integer. Please check type of ID")
    try:
        configUser = None

        for userID, settings in LoadData().items():
            if int(userID) == TelegaID:
                configUser = settings
                break
                
        if configUser == None:
            raise ErrorsJSON.UnavailabilityID(f"This ID not in Users: {TelegaID}")

        return configUser
    except Exception as ex:
        print(ex)

def GetUserConfig(TelegaID: int = -1):
    try:
        configUser = GetUserConfigDict(TelegaID)
        return list(configUser.values())

    except Exception as ex:
        print(ex)

def AddUser(TelegaID: int):
    configUser = LoadData()
    configUser[TelegaID] = LoadData(ConfigJSON.PATH_DEFAULT_USER)

    with open(ConfigJSON.PATH_USERS, 'w') as Users:
        json.dump(configUser, Users, indent=4)
        Users.close()

def SetPropertyUser(TelegaID: int = -1, Property: str = "", IndexProperty: int = -1, value = None):
    if type(TelegaID) != int:
        raise ErrorsJSON.InvalidID(f"ID {TelegaID} isn't integer. Please check type of ID")

    try:
        configUser = GetUserConfigDict(TelegaID)
        if (IndexProperty != -1): 
            configUser[list(configUser.keys())[IndexProperty]] = value
        else:
            configUser[Property] = value
    
        dataUsers = LoadData()
        dataUsers[str(TelegaID)] = configUser

        with open(ConfigJSON.PATH_USERS, 'w') as Users:
            json.dump(dataUsers, Users, indent=4)
            Users.close()

    except Exception as ex:
        print(ex)

def CheckUser(TelegaID: int):
    data = LoadData()
    return str(TelegaID) in data.keys()