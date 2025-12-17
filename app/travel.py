<<<<<<< HEAD
import urllib.request
import urllib.parse
import json
from flask import Flask

def getCommon(key):
    url = "https://restcountries.com/v3.1/alpha/" + key
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
    common = data[0]['name']['common']
    #print(common)
    return(common)

def getPop(key):
    url = "https://restcountries.com/v3.1/alpha/" + key
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
    pop = data[0]['maps']['population']
    #print(pop)
    return(pop)

def getList():
    url = "https://restcountries.com/v3.1/alpha/" + curKey
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
    list = data[0]['borders']
    #print(list)
    return(list)

def getCommonList():
    list = []
    for country in getList():
        list.append(getCommon(country));
    #print(list)
    return list

def getPopList():
    list = []
    for country in getList():
        list.append(getPop(country));
    #print(list)
=======
import utility

def get_common(key):
    data = utility.call_api("Countries", "/" + key)
    common = data[0]['name']['common']
    return common

def get_pop(key):
    data = utility.call_api("Countries", "/" + key)
    pop = data[0]['maps']['population']
    return pop

def get_list(username):
    country = utility.get_user(username)
    data = utility.call_api("Countries", "/" + country)
    list = data[0]['borders']
    return list

def get_common_list():
    list = []
    for country in get_list():
        list.append(get_common(country))
    return list

def get_pop_list():
    list = []
    for country in get_list():
        list.append(get_pop_list(country))
>>>>>>> b56faa36c925bfc6a66116878d45ad8af05f0797
    return list

def make_numbers(p):
    nums = []
    current = p
<<<<<<< HEAD

=======
>>>>>>> b56faa36c925bfc6a66116878d45ad8af05f0797
    for times in range(13):
        current = (current * 1103515245 + 12345) % 2**31
        nums.append((current % 1000000) / 1000000)
    total = sum(nums)
    scale = 100 / total
    return [n * scale for n in nums]

<<<<<<< HEAD
def getChanceList():
    list = []
    for pop in getPopList():
        list.append(make_numbers(pop));
    #print(list)
=======
def get_chance_list():
    list = []
    for pop in get_pop_list():
        list.append(make_numbers(pop))
>>>>>>> b56faa36c925bfc6a66116878d45ad8af05f0797
    return list
