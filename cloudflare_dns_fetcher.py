import requests

api_key = 'API_KEY'
email = 'EMAIL_ADDRESS'
domain = 'DOMAIN_NAME'

def get_zone_id(domain):
    endpoint = f'https://api.cloudflare.com/client/v4/zones?name={domain}'
    headers = {
        'X-Auth-Email': email,
        'X-Auth-Key': api_key,
        'Content-Type': 'application/json'
    }

    response = requests.get(endpoint, headers=headers)
    response_data = response.json()
    zone_id = response_data['result'][0]['id']
    return zone_id

def get_dns_records(domain):
    zone_id = get_zone_id(domain)
    endpoint = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records'
    headers = {
        'X-Auth-Email': email,
        'X-Auth-Key': api_key,
        'Content-Type': 'application/json'
    }

    response = requests.get(endpoint, headers=headers)
    response_data = response.json()
    dns_records = response_data['result']
    return dns_records

dns_records = get_dns_records(domain)

for record in dns_records:
    record_type = record['type']
    record_name = record['name']
    record_content = record['content']
    print(f'Type: {record_type}, Name: {record_name}, Content: {record_content}')
