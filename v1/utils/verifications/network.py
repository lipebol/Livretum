import requests


def network():
    #   Agent based on Device:"https://deviceatlas.com/blog/list-of-user-agent-strings"   
    headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"}
    try:
        URL = 'https://www.google.com/'
        r = requests.get(url=URL, headers=headers)
        if r.status_code == 200:
            status_net = 1
    except requests.exceptions.RequestException:
        status_net = 0

    return status_net
