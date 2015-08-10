import json
import getpass
import api

def main():

    #replace file_name with desired .json file
    with open('fitness-data.json') as data_file:    
        data = json.load(data_file)

    #change username and password here for a different user
    session_token, user_id = api.login(input("Email: "), getpass.getpass())

    #format specific for runkeeper, may need to be changed for other API's
    physical_activity = data['body']['physical_activity']

    for note in physical_activity:
        api.post_note(session_token, user_id, note)

if __name__ == '__main__':
    main()
