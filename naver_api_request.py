import requests
import pprint

my_request = requests.get('https://api.github.com/users/soongon')
menu_list = my_request.json()

pprint.pprint(menu_list)