import requests
import collections


search = 'capital'
url = f'http://www.omdbapi.com/?s={search}&y=&plot=short&r=json'

r = requests.get(url)
data = r.json()

results = data['Search']

print(results[0])


def main():
    pass


if __name__ == '__main__':
    main()
