import base64
import requests
import uuid
import ast

def make_login_request(username, password):
    base64_login_string = base64.b64encode(b'karina@tidepool.org:Cokacola123')
    url = 'https://devel-api.tidepool.io/auth/login'
    headers = {'Authorization': "Basic " + str(base64_login_string)[2:-1]}
    r = requests.post(url, headers=headers)
    session_token = r.headers['x-tidepool-session-token']
    text_to_object = ast.literal_eval(r.text)
    user_id = text_to_object['userid']
    return session_token, user_id

def make_note_request(session_token, user_id, note_text):
    """ session_token goes in header and is required for every note request
        user_id goes in the end of the url
        note goes in the body
    """
   # formated_note = format_note(user_id, note_text)
    
    #body = {"message": formated_note}
    headers = {'x-tidepool-session-token': session_token}
    url = 'https://devel-api.tidepool.io/message/send/' + user_id
    body = {
        'guid': 'abcde',
        'parentmessage' : 'null', #None,
        'userid': user_id,
        'groupid': user_id,
        'timestamp': '2013-11-28T23:07:40+00:00',
        'createdtime': '2013-11-28T23:07:40+00:00',
        'messagetext': 'In three words I can sum up everything I have learned about life: it goes on.'
        }
    r = requests.post(url, headers=headers, data=body)
    print(r.headers)
    print(r)
    print(r.text)

def format_note(user_id, note_text):
    note = {}
    note["guid"] = str(uuid.uuid4())
    note["userid"] = user_id
    note["groupid"] = user_id
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
                    "start_date_time": "2015-08-02T15:58:21.000-07:00",
                    "duration": {
                        "value": 1179.089,
                        "unit": "sec"
                        }
                    }
                }
            }

make_note_request(session_token, user_id, note_text)



