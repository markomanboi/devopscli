import subprocess, json, sys

def get_credentials(role_arn, role_name):
    return subprocess.check_output(["aws","sts","assume-role","--role-arn",role_arn,"--role-session-name",role_name])

def get_role_keys(json_role):
    creds = json.loads(json_role)
    access_key = creds['Credentials']['AccessKeyId']
    secret_key = creds['Credentials']['SecretAccessKey']
    session_token = creds['Credentials']['SessionToken']
    return access_key, secret_key, session_token

def export_role(json_role):
    print("Assuming Role...")
    access_key, secret_key, session_token = get_role_keys(json_role)
    subprocess.call(["aws","configure","set","aws_access_key_id",access_key])
    subprocess.call(["aws","configure","set","aws_secret_access_key",secret_key])
    subprocess.call(["aws","configure","set","aws_session_token",session_token])

if __name__ == '__main__':
    input_stream = sys.argv
    if input_stream[1] == 'test':
        print('Testing Goods')
    elif input_stream[1] == 'exit':
        print('Exit')

    