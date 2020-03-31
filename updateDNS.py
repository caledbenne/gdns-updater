import json
import http.client
from base64 import b64encode
def get_ip_address():
    h = http.client.HTTPSConnection('ipv4bot.whatismyipaddress.com', 443)
    h.request('GET', '/')
    response = h.getresponse()
    return str(response.read(), "UTF-8")
def set_ip_address(username, password, hostname, ip_address, email):
    h = http.client.HTTPSConnection('domains.google.com', 443)
    user_pass = b64encode(bytes('%s:%s' % (username, password), "UTF-8")).decode("UTF-8")
    headers = {'Authorization': 'Basic %s' % user_pass, 'User-Agent': 'GoogleDynamicUpdater/1.0', 'accept': 'text/html'}
    h.request("POST", '/nic/update?hostname=%s&myip=%s' % (hostname, ip_address), email, headers)
    response = h.getresponse()
    return str(response.read(), "UTF-8")


def work():
    conf_file = open('./data/options.json')
    config = json.load(conf_file)
    n_minutes = int(config["interval"] * 60)
    check = {'good %s' % ip, 'nochg %s' % ip}
    old_ip = ""
    while (true):
        ip = get_ip_address()
        if old_ip != ip:
            for domain in config['domains']:
                ret = set_ip_address(domain['username'], domain['password'], domain['hostname'], ip, config['email'])
                if ret not in check:
                    print('Error: no good  - %s' % ret)
            old_ip = ip
        time.sleep(n_minutes)

work()
