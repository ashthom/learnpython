import urllib
from BeautifulSoup import *

#url2 = raw_input('Enter URL: ')

url2 = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Alaska.html'#tags[2].get('href', None)
count = raw_input('Enter count: ')
count = int(count)+1;

position = raw_input('Enter position: ')
position = int(position) - 1

while (count > 0):
    if count == 1:
        print 'Last Url:', url2
    else:
        print 'Retrieving:',url2

    html = urllib.urlopen(url2).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    url2 = tags[position].get('href', None)
    print tags[position].contents
    count = count - 1;
