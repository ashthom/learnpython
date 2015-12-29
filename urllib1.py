import urllib
from BeautifulSoup import *
#fhand = urllib.urlopen('http://www.dr-chuck.com/page1.htm')

#for line in fhand:
#    print line.strip()

#url = raw_input('Enter - ')
url='http://python-data.dr-chuck.net/comments_212026.html'
pagecontents = urllib.urlopen(url).read()
soup = BeautifulSoup(pagecontents)

tags = soup('span');
span_list = list();

for tag in tags:
    span_list.extend(map(int,tag.contents))
    print 'contents:', tag, map(int,tag.contents)

print 'sum', sum(span_list)
