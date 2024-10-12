# HTML Parser - Part 2
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_comment(self, cmt):
        if '\n' in cmt:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        print(cmt)
    def handle_data(self, d):
        if d == '\n': return
        print('>>> Data')
        print(d)
html_content = ""
for _ in range(int(input())):
    html_content += input().rstrip() + '\n'
parser = MyHTMLParser()
parser.feed(html_content)
parser.close()
