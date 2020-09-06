import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url, headers = kv,timeout = 50)
        r.raise_for_status
        r.encoding = 'utf-8'
        return r.text
    except:
        return ' '

def fillMoviesList(mlist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for ol in soup.find('ol'):
        if isinstance(ol, bs4.element.Tag):
            ols = ol('span')
            mlist.append([ols[0].string, ols[1].string, ols[2].string])

def printMoviesList(mlist, num):
    print('名次', '电影名')
    for i in range(num):
        m = mlist[i]
        print(str(i)+'.', '{:^10}\t{:^10}'.format(m[0], m[1]))

def main():
    minfo = []
    try:
        max_number = int(input('How many movies do you want to show (Maximum 25):'))
        url = "https://movie.douban.com/top250"
        html = getHTMLText(url)
        fillMoviesList(minfo, html)
        printMoviesList(minfo, max_number)
    except:
        print("I want NUMBEWR, not any things else !!!")
main()
