#http testing

import requests


response = requests.get('https://discord.com')

if response.status_code == 200:
    cf_cache_status = response.headers.get('CF-Cache Status')
    cf_ray = response.headers.get('CF Ray')

    print('CF-Cache-Status:', cf_cache_status)
    print('CF Ray', cf_ray) 
else:
    print(f'failed to retrieve response: {response.status_code}')

