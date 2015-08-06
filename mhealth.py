import base64
import requests
import uuid
import ast
import json
import sys

def make_login_request(username, password):
    """ Generate a post request to tidepool's login authentication API for a
        given username and password
        Return a session_token and user_id to use for note creation
    """
    login_in_bytes = str.encode("{:s}:{:s}".format(username, password)) 
    base64_login_string = base64.b64encode(login_in_bytes)
    url = 'https://devel-api.tidepool.io/auth/login'
    headers = {'Authorization': "Basic " + str(base64_login_string)[2:-1]}
    r = requests.post(url, headers=headers)
    session_token = r.headers['x-tidepool-session-token']
    text_to_object = ast.literal_eval(r.text)
    user_id = text_to_object['userid']
    return session_token, user_id

def post_note(session_token, user_id, note_text):
    """ Post a note to a specific user's devel API.
        session_token -- required by message API header
        user_id -- attached to the end of the url during each request
        note_text -- the body of the note
    """    
    headers = {
        'x-tidepool-session-token': session_token,
        'Content-Type':'application/json'
    }
    formated_note = format_note(user_id, note_text)    
    body = {'message': formated_note}
    
    url = 'https://devel-api.tidepool.io/message/send/' + user_id
    
    try:
        r = requests.post(url, headers=headers, data=json.dumps(body))
        str(r) == '<Response [201]>'
    except:
        print(r.text)
        sys.exit(1) 

def format_note(user_id, note_text):
    """ Format each note with required fields to post a request
    """
    note = {}
    note["guid"] = str(uuid.uuid4())
    note["userid"] = str(user_id)
    note["groupid"] = str(user_id)
    note["parentmessage"] = None,
    time_from_note = note_text["effective_time_frame"]["time_interval"]["start_date_time"]
    formated_time = time_from_note[:19] + '-' + time_from_note[24:]
    note["timestamp"] = formated_time
    note["messagetext"] = str(note_text)
    return note

session_token, user_id = make_login_request('karina@tidepool.org', 'Cokacola123')
note_text = {"activity_name": "Walking",
            "distance": {
              "value": 1668.16991784243,
              "unit": "m"
            },
            "effective_time_frame": {
                "time_interval": {
                    "start_date_time": "2015-08-04T15:58:21.000-07:00",
                    "duration": {
                        "value": 1179.089,
                        "unit": "sec"
                        }
                    }
                }
            }

post_note(session_token, user_id, note_text)



