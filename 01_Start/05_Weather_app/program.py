import requests
import bs4


def main():
    print_the_header()
    city = input('What city do you want the wether for: ')
    html = get_html_from_web(city)
    report = get_weather_from_html(html)
    print(f'The temp in {city} is {report} F')

def print_the_header():
    print('------------------------------')
    print('       WEATHER APP')
    print('------------------------------')


def get_html_from_web(city):
    url = f'https://www.wunderground.com/weather/ru/{city}/'
    response = requests.get(url)
    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    temp = soup.find('span', {'class':'wu-value wu-value-to'}).get_text()
    return temp

if __name__ == '__main__':
    main()
