import requests
import json
import time
import datetime

CLIENT_ID = '8dda116418894e0895884c99d106ce92'
CLIENT_SECRET = 'cae4026256d5468e84851f58ccf5aed0'
SPOTIFY_USER = 'sillybearbuddy'

GRANT_TYPE = 'client_credentials'
body_params = {'grant_type' : GRANT_TYPE}

url = 'https://accounts.spotify.com/api/token'
response = requests.post(url, data=body_params, auth = (CLIENT_ID, CLIENT_SECRET))

token_raw = json.loads(response.text)
token = token_raw["access_token"]

headers = {"Authorization" : "Bearer {}".format(token)}

testurl = f'https://api.spotify.com/v1/users/{SPOTIFY_USER}/playlists'
r = requests.get(url=testurl, headers=headers)

print (r.text)

def StringStrength(the_string):
    """Determines a value in range [1, 100] after evaluating the string.
    """
    # TODO: Add some RegEx here to see if input matches an easy pattern.
    return 50

def ValidateID(id_string):
    """Validates an ID in three phases.

        1) Compares the string with commonly used "fake" string samples.

        2) Measures the strength of the input.

        3) Seen unfit, defaults the ID value into an empty string.

        It is assumed that the endpoint handles requests with invalid parameters.
        Common passwords (taken from wikipedia) are stored locally in a json file for the following reasons:
            a. Security
            b. Delay
            c. There simply is no API online that compares a string that is supposed
            to be secret without raising concerns regarding a and b. See the link:
            https://github.com/danielmiessler/SecLists/issues/132
    """
    allowed_string = id_string
    # Phase 1: Checking if the input string is too common, possibly invalid.
    # https://en.wikipedia.org/wiki/List_of_the_most_common_passwords
    is_common = False
    with open('blacklist.json') as json_file:
        phrase_list = json.load(json_file)["phrases"]
        if id_string in phrase_list:
            is_common = True

    # Phase 2: Checking if the string is too easy to predict.
    is_weak = False
    if StringStrength(id_string) < 50:
        is_weak = True
    
    # Phase 3: Checking if the input requires to be defaulted to empty string.
    if is_common or is_weak:
        allowed_string = ""
    
    return id_string

def UpdateGetURL(url_suffix, validated_params):
    # TODO: Basically parse url_suffix and replace invalid parts with validated parts.
    pass

class Btac:
    """Example usage::
        
        import btac

        bt = btac.Btac()
        
        oid = "s0m30rg4n1z4t10nid"

        did = "s0m3d3v1c31d"        
        device_info = bt.detailed(oid, did)
        print(device_info)

        id = "s0m31d3nt1ty1d"
        identity = bt.identity_detailed(oid, id)
        print(identity)

    """
    # Completely making up the base URL, since the address provided in the swagger page was localhost.
    base_url = "https://www.armongate.com/api"

    # One of to 2-3 requirements, there you have it.
    headers = {"Authorization" : "Bearer {}".format(token)}
    def __init__(
            self,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET):
        """ The constructor provides default keys. """

    def GetRequest(self, url_suffix, parameters):
        """ Sends a GET request to Armon API.

            Parameters are passed on url, still taken as input here for validation.
        """
        # Expecting parameters argument to be a dictionary.
        
        # This loop populates a new dictionary with "validated" parameters.
        validated_params = {}
        for key in parameters:
            # Here, we basically add key:value pairs with validated values.
            validated_params[key] = ValidateID(parameters[key])
        
        # This function will update invalid ID strings in the URL.
        # Potentially, before: "/111111/system/accesscontrolpoint/123456/markasfavorite/true"
        # Potentially, after: "//system/accesscontrolpoint//markasfavorite/true"
        # Obviously, empty spots might be problematic, but not going to dig for now.

        # base_url doesn't change, so we just concatenate updated GET url to end of it.
        updated_url = base_url + UpdateGetURL(url_suffix, validated_params)
        # Finally we are ready to shoot our rock.. request.
        response = requests.get(url=updated_url, headers=headers)
        return response

    def PostRequest(self, url_suffix, body):
        """ Sends a GET request to Armon API.

            Some parameters are passed on body, some on url. So updating both body and 
            url will be necessary, but the process for validating IDs will be almost same here.
        """
        # Expecting body argument to be a json, but it shouldn't matter.

        # This loop also populates a new dictionary with "validated" parameters.
        validated_params = {}
        for key in body:
            # Here, we basically add key:value pairs with validated values.
            validated_params[key] = ValidateID(body[key])

        # base_url doesn't changehere either, so we just concatenate updated POST url to end of it.
        updated_url = base_url + UpdateGetURL(url_suffix, validated_params)
        response = requests.post(url=base_url+url_suffix, headers=headers)
        return response

class ControlPanel(Btac):
    """Contains methods relevant to an organization's control panel.
    
    """
    def __init__(
            self,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET):
        super().__init__(client_id=client_id, client_secret=client_secret)
    
    def set_emergency_state(self, oid, body):
        """Sets emergency state for a control panel or organization as true or false.

            The parameter body should have the following format:
            {
                "state": 0
            }
        """
        route = f"/{oid}/system/emergencystate"
        return super.PostRequest(route, body)
        
    def update_wiegrad_reader(self, oid, did, wid, body):
        """Updates wiegand reader's name and location information.

            The parameter body should have the following format:
            {
                "name": "string",
                "location": "string",
                "recurrentAttemptTimeout": 0
            }
        """
        route = f"/{oid}/configuration/armoncontrolpanel/{did}/wiegandreader/{wid}"
        return super.PostRequest(route, body)
        

    def update_counter_sensor(self, oid, did, ccid, body):
        """Updates counter sensors' countsTo where information.

            The parameter body should have the following format:
            {
                "name": "string"
            }
        """
        route = f"/{oid}/configuration/armoncontrolpanel/{did}/countersensor/{ccid}"
        return super.PostRequest(route, body)

    def update_status_sensor(self, oid, did, sid, body):
        """Updates status sensor's timeout and sense to where information.

            The parameter body should have the following format:
            {
                "name": "string",
                "timeOut": 0
            }
        """
        route = f"/{oid}/configuration/armoncontrolpanel/{did}/statussensor/{sid}"
        return super.PostRequest(route, body)
    
    def update_relay(self, oid, did, rid, body):
        """Update relay's manages to where and drive duration information.

            The parameter body should have the following format:
            {
                "name": "string",
                "driveDuration": 0
            }
        """
        route = f"/{oid}/configuration/armoncontrolpanel/{did}/relay/{rid}"
        return super.PostRequest(route, body)
    
    def update_hikvision_lprc(self, oid, did, id, body):
        """Updates a hikvision license plate reader camera's name,number, recurrentAttemptTimeout.

            The parameter body should have the following format:
            {
                "name": "string",
                "number": 0,
                "recurrentAttemptTimeout": 0
            }
        """
        route = f"/{oid}/configuration/armoncontrolpanel/{did}/hikvisionlicenseplatecameralanes/{id}"
        return super.PostRequest(route, body)

    def update_impinj_sga(self, oid, did, id, body):
        """Updates an impinj speedway gateway antenna's name, number, recurrentAttemptTimeout.

            The parameter body should have the following format:
            {
                "name": "string",
                "number": 0,
                "recurrentAttemptTimeout": 0
            }
        """
        route = f"/{oid}/configuration/armoncontrolpanel/{did}/impinjspeedwaygatewayantennas/{id}"
        return super.PostRequest(route, body)

class Settings(Btac):
    """Sets the organization settings

    """
    def __init__(
            self,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET):
        super().__init__(client_id=client_id, client_secret=client_secret)
    
    def update_org_settings(self, oid, body):
        """Sets the organization settings.

            The parameter body should have the following format:
            {
                "name": "string",
                "userAccountAllowed": true,
                "languageCode": 0
            }
        """
        route = f"/{oid}/system/remotecontrol"
        return super.PostRequest(route, body)

class RemoteControl(Btac):

    def __init__(
            self,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET):
        super().__init__(client_id=client_id, client_secret=client_secret)

    def manage_acp(self, oid, body):
        """Manages access control point remotely.

            {
                "accessControlPointId": "string",
                "direction": 0
            }
        """
        route = f"/{oid}/system/remotecontrol"
        return super.PostRequest(route, body)

    def mark_acp_favorite(self, oid, id, option):
        """Marks an access control point as favorite.

            The parameter body should have the following format:
            {
                "name": "string",
                "userAccountAllowed": true,
                "languageCode": 0
            }
        """
        parameters = {"oid": oid, "id": id, "option": option}
        route = f"/{oid}/system/accesscontrolpoint/{id}/markasfavorite/{option}"
        return super.GetRequest(route, parameters)




"""
These should be more than enough, I will probably skip rest of the subclasses
and their methods.
"""


class Camera(Btac):
    def __init__(
            self,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET):
        super().__init__(client_id=client_id, client_secret=client_secret)

class Feedback(Btac):
    def __init__(
            self,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET):
        super().__init__(client_id=client_id, client_secret=client_secret)

class Notifications(Btac):
    def __init__(
            self,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET):
        super().__init__(client_id=client_id, client_secret=client_secret)

class UserGroup(Btac):
    def __init__(
            self,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET):
        super().__init__(client_id=client_id, client_secret=client_secret)

class User(Btac):
    def __init__(
            self,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET):
        super().__init__(client_id=client_id, client_secret=client_secret)

class System(Btac):
    def __init__(
            self,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET):
        super().__init__(client_id=client_id, client_secret=client_secret)

class OrganizationUnit(Btac):
    def __init__(
            self,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET):
        super().__init__(client_id=client_id, client_secret=client_secret)

class AccessControlPoint(Btac):
    def __init__(
            self,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET):
        super().__init__(client_id=client_id, client_secret=client_secret)

class Organization(Btac):
    def __init__(
            self,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET):
        super().__init__(client_id=client_id, client_secret=client_secret)

class Report(Btac):
    def __init__(
            self,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET):
        super().__init__(client_id=client_id, client_secret=client_secret)
        
class UserProfile(Btac):
    def __init__(
            self,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET):
        super().__init__(client_id=client_id, client_secret=client_secret)

class Rregion(Btac):
    def __init__(
            self,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET):
        super().__init__(client_id=client_id, client_secret=client_secret)

class FloorPlan(Btac):
    def __init__(
            self,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET):
        super().__init__(client_id=client_id, client_secret=client_secret)

class Role(Btac):
    def __init__(
            self,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET):
        super().__init__(client_id=client_id, client_secret=client_secret)

class Device(Btac):
    def __init__(
            self,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET):
        super().__init__(client_id=client_id, client_secret=client_secret)

class Credential(Btac):
    def __init__(
            self,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET):
        super().__init__(client_id=client_id, client_secret=client_secret)

class AccessControlPoint(Btac):
    def __init__(
            self,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET):
        super().__init__(client_id=client_id, client_secret=client_secret)
class UserSelection(Btac):
    def __init__(
            self,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET):
        super().__init__(client_id=client_id, client_secret=client_secret)

class ClientApplication(Btac):
    def __init__(
            self,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET):
        super().__init__(client_id=client_id, client_secret=client_secret)

class AccessRules(Btac):
    def __init__(
            self,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET):
        super().__init__(client_id=client_id, client_secret=client_secret)

class Identity(Btac):
    def __init__(
            self,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET):
        super().__init__(client_id=client_id, client_secret=client_secret)