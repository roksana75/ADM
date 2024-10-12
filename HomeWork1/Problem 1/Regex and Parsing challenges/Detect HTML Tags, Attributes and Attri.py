# Detect HTML Tags, Attributes and Attribute Values
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, t, a):
        print(t)
        [print('-> {} > {}'.format(*attr)) for attr in a]
html_input = '\n'.join([input() for _ in range(int(input()))])
parser = MyHTMLParser()
parser.feed(html_input)
parser.close()