from urllib import response
from xmlrpc.client import ResponseError
import requests


def get_pokemon_info(name):

    """
    Gets a dictionary of information from the PokeApi for a specified Pokemon

    :param name: Pokemon's name (or Poke index) 
    :returns: Dictionary of Pokemon Information if successful; none if unsuccessful
    """

    print("Getting Pokemon information...", end='')
    if name is None:
        print('error: Missing name parameter')
        return


    name = name.strip().lower()

    if name == '':
        print('error: Empty name parameter')
        return
    URL = 'https://pokeapi.co/api/v2/pokemon/' + str(name)
    response = requests.get(URL)

    if response.status_code == 200:
        print('success')
        return response.json()
    else: 
        print('failed. Response code:', response.status_code)
        return

#Connecting the the website in which I'll get my pokemon from, and getting a limit of 2000
def get_pokemon_list(limit=2000, offset=0):
    print("Getting list of pokemon...", end='')
    URL = 'https://pokeapi.co/api/v2/pokemon/'
    params = {
        'offset': offset,
        'limit': limit
    }

    #Code to test connection
    response = requests.get(URL, params=params)

    if response.status_code == 200:
        print('success')
        poke_dict = response.json() 

        return [p['name'] for p in poke_dict['results']]
    else: 
        print('failed. Response code:', response.status_code)


#Code to get pokemon names
def get_pokemon_image_url(name):
    poke_dict = get_pokemon_info(name)

    if poke_dict:
        poke_url = poke_dict['sprites']['other']['official-artwork']['front_default']
        return poke_url