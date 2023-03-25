import requests
import pandas as pd
from alive_progress import alive_bar

def get_manor_ids(placeId):
    "Returns the list of manors from a place"
    res = requests.get('https://opendomesday.org/api/1.0/place/'+str(placeId))
    data = res.json()
    if  'manors'  in data.keys():
        return data['manors']
    else:
        return []

def get_all_manors(county):
    '''Returns the list of manos from a county (by checking each place of the county)'''
    res = requests.get('https://opendomesday.org/api/1.0/county/'+county)
    data = res.json()

    manorIds = []
    places = data['places_in_county']
    with alive_bar(len(places)) as bar:
        for place in places:
            manorIds.extend(get_manor_ids(place['id']))
            bar()
    return manorIds

def get_manors_info(county):
    "Returns a DataFrame containing 'geld/totalploughs' values for each manor of a county"
    manorIds = get_all_manors(county)
    df = pd.DataFrame()
    with alive_bar(len(manorIds)) as bar:
        for manor in manorIds:
            res = requests.get("https://opendomesday.org/api/1.0/manor/"+str(manor['id']))
            data = res.json()
            manorInfo = pd.DataFrame({
                "geld": data['geld'],
                "totalploughs": data['totalploughs']
            }, index=[manor['id']])
            df = pd.concat([df, manorInfo])
            bar()
    return df


