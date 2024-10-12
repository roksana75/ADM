# HTML Parser - Part 1
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, t, a):
        print('Start :', t)
        for e in a:
            print('->', e[0], '>', e[1])
    def handle_endtag(self, t):
        print('End   :', t)
    def handle_startendtag(self, t, a):
        print('Empty :', t)
        for e in a:
            print('->', e[0], '>', e[1])
parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())