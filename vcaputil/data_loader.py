import os
import json


def get_vcap():
    if 'VCAP_SERVICES' in os.environ:
        vcap = json.loads(os.getenv('VCAP_SERVICES'))
        print('VCAP_SERVICES found')
        return vcap
    else:
        print('VCAP_SERVICES not found')
        return None


def get_user_provided(vcap):
    if 'user-provided' in vcap:
        print('user-provided found in vcap')
        creds = vcap['user-provided'][0]['credentials']
        secret_key = creds['SECRET_KEY']
        print(secret_key)
        return secret_key
    else:
        print('user-provided not found in vcap')
        return None


def get_secret_key():
    vcap = get_vcap()
    if vcap is not None:
        return get_user_provided(vcap)
