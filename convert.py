from markdown import markdown, markdownFromFile
import sys
import os
import os.path as path

ext = ['codehilite', 'extra']

# args
rev = True
if 'reverse' in sys.argv:
  rev = False

markdown_files = []
markdown_path = path.join(path.abspath('.'), 'markdown')
html_path = path.join(path.abspath('.'), 'html')

template = open('template.html', 'ru').read()
index = open('index.html', 'ru').read()
lst = open('list.html', 'ru').read()

for root, dirs, files in os.walk(path.join(path.abspath('.'), 'markdown')):
  d = path.basename(root)
  markdown_files.extend((d, f) for f in files if not f.endswith('swp'))

markdown_files.sort(key=lambda x: x[1], reverse=rev)

for d, fi in markdown_files:
  print 'writing', fi + '.html'
  md = open(path.join(markdown_path, fi), 'r').read().decode('utf-8')
  title = md.split('#')[1].split('\n')[0][1:]
  html = markdown(md, extensions=ext).encode('utf-8')
  html += '<div class="footer"><a href="/blog">Back</a></div>'
  open(path.join(html_path, fi + '.html'), 'w').write(template.format(title, html))
  index += lst.format('<a href="{}.html">{}</a>'.format(fi, title))

open(path.join(html_path, 'index.html'), 'w').write(template.format('index', index))
