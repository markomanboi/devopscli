from logging import error
import subprocess, json, sys

from jsonschema import ValidationError

def get_credentials(role_arn, role_name):
    print('Retrieving Role Keys...')
    creds = ''
    try:
        creds = subprocess.check_output(["aws","sts","assume-role","--role-arn",role_arn,"--role-session-name",role_name])
    except subprocess.CalledProcessError:
        print('Error: role input is invalid')
        sys.exit()
    return creds

def get_role_keys(json_role):
    creds = json.loads(json_role)
    print('Initializing Role Keys...')
    access_key = creds['Credentials']['AccessKeyId']
    secret_key = creds['Credentials']['SecretAccessKey']
    session_token = creds['Credentials']['SessionToken']
    return access_key, secret_key, session_token

def export_role(json_role):
    access_key, secret_key, session_token = get_role_keys(json_role)
    print('Setting the Role Keys...')
    subprocess.call(["aws","configure","set","aws_access_key_id",access_key])
    subprocess.call(["aws","configure","set","aws_secret_access_key",secret_key])
    subprocess.call(["aws","configure","set","aws_session_token",session_token])
    print('Role Assumed')
    
if __name__ == '__main__':
    input_stream = sys.argv
    main_cmd = input_stream[1]
    if main_cmd == 'assume':
        try:
            role_arn = input_stream[2]
            role_name = input_stream[3]
        except IndexError:
            print('Error: no role parameter provided')
            sys.exit()
    
        creds = get_credentials(role_arn, role_name)
        export_role(creds)
    
    elif main_cmd == 'version':
        print('DevOpsCLI Version - 0.0.0')
    
    else:
        print('That is not a valid command')



    