import subprocess, json, sys

def get_role(role):
    role_arn = 'arn:aws:iam::933594548532:role/DevOpsPHIntern'
    role_name = 'AWSInternRole'
    if role == 'prod':
        role_arn = 'arn:aws:iam::170785246738:role/OrganizationAccountAccessRole'
        role_name = 'AWSProd'
    return role_arn, role_name

def get_credentials(role_arn, role_name):
    return subprocess.check_output(["aws","sts","assume-role","--role-arn",role_arn,"--role-session-name",role_name])

def get_role_keys(json_role):
    creds = json.loads(json_role)
    access_key = creds['Credentials']['AccessKeyId']
    secret_key = creds['Credentials']['SecretAccessKey']
    session_token = creds['Credentials']['SessionToken']
    return access_key, secret_key, session_token

def export_role(json_role):
    access_key, secret_key, session_token = get_role_keys(json_role)
    subprocess.call(["aws","configure","set","aws_access_key_id",access_key])
    subprocess.call(["aws","configure","set","aws_secret_access_key",secret_key])
    subprocess.call(["aws","configure","set","aws_session_token",session_token])
    print('Role Assumed')
    
if __name__ == '__main__':
    input_stream = sys.argv
    main_cmd = input_stream[1]
    if main_cmd == 'assume':
        params = input_stream[2]
        role_arn, role_name = get_role(params)
    
        creds = get_credentials(role_arn, role_name)
        export_role(creds)
    
    elif main_cmd == 'version':
        print('DevOpsCLI Version - 0.0.0')
    
    else:
        print('That is not a valid command')



    