import urllib
from bs4 import BeautifulSoup

titles = []
images = []

r = urllib.urlopen('https://www.open2study.com/courses').read()
soup = BeautifulSoup(r)

for i in soup.find_all('div', {'class': "courses_adblock_rollover"}):
    titles.append(i.h2.text)

for i in soup.find_all(
    'img', {
        'class': "image-style-course-logo-subjects-block"}):
    images.append(i.get('src'))

with open('test.txt', "w") as f:
    for i in zip(titles, images):
        f.write(i[0].encode('ascii', 'ignore') +
                '\n'+i[1].encode('ascii', 'ignore') +
                '\n\n')