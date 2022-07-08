import subprocess, json, sys

def get_credentials(role_arn, role_name):
    print('Retrieving Role Keys...')
    creds = ''
    try:
        creds = subprocess.check_output(["aws","sts","assume-role","--role-arn",role_arn,"--role-session-name",role_name])
    except subprocess.CalledProcessError:
        print('Error: role input is invalid or you are not permitted to assume this role')
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

def get_app_details():
    app_details = {}
    try:
        with open('./app.json') as app_json:
            app_details = json.load(app_json)
    except FileNotFoundError:
        print('Error: app.json not found in directory')
        sys.exit()
    return app_details
    
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
        app_details = get_app_details()
        app_name = app_details['app-name']
        version = app_details['version']
        print(f'{app_name}: {version}')

    else:
        print('Error: invalid command')



    