import requests

compare_list = []


def request_superhero_stats(name):

    url = f'https://superheroapi.com/api/2619421814940190/search/{name}'
    resp = requests.get(url).json()

    compare_list.append(resp)


def compare_by_intellect(compare_list):
    if not compare_list:
        raise ValueError('empty')
    maximum_intellect = compare_list[0]['results'][0]['powerstats']['intelligence']
    maximum_name = compare_list[0]['results-for']

    for item in compare_list:
        if int(item['results'][0]['powerstats']['intelligence']) > int(maximum_intellect):
            maximum_intellect = item['results'][0]['powerstats']['intelligence']
            maximum_name = item['results-for']
    print(f'Самый умный супергерой - {maximum_name} с интеллектом {maximum_intellect}')


request_superhero_stats('Hulk')
request_superhero_stats('Captain America')
request_superhero_stats('Thanos')


compare_by_intellect(compare_list)
