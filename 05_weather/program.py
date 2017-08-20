import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                                       'cond, temp, scale, loc')

def print_header():
    print('------------------------')
    print('       WEATHER APP')
    print('------------------------')


def get_zip_code():
    print('What zip code? (97201)')
    return 97201


def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    return response.text


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


def parse_location(loc):
    parts = loc.split('\n')
    return parts[0].strip()


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')

    raw_location = soup.find(id='location').find('h1').get_text()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    temp = soup.find(id='curTemp').find(class_='wx-value').get_text()
    unit = soup.find(id='curTemp').find(class_='wx-unit').get_text()

    raw_location = cleanup_text(raw_location)
    loc = parse_location(raw_location)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    unit = cleanup_text(unit)

    # print(condition, temp, unit, loc)
    return WeatherReport(cond=condition, temp=temp, scale=unit, loc=loc)

if __name__ == '__main__':
    print_header()
    zipcode = get_zip_code()
    html = get_html_from_web(zipcode)
    weather = get_weather_from_html(html)

    print('The temperature in {} is {} {}, {}'.format(weather.loc, weather.temp, weather.scale, weather.cond))