from markdown import markdown, markdownFromFile
import sys
import os
import os.path as path
import codecs
from string import Template

ext = ['codehilite', 'extra']

# args
rev = True
if 'reverse' in sys.argv:
  rev = False

markdown_files = []
markdown_path = path.join(path.abspath('.'), 'markdown')
html_path = path.join(path.abspath('.'), 'html')

template = Template(codecs.open('template.html', 'r' ,'utf-8').read())
index    = Template(codecs.open('index.html', 'r', 'utf-8').read())
post     = Template(codecs.open('post.html', 'r' ,'utf-8').read())
lst      = Template(codecs.open('list.html', 'r', 'utf-8').read())

for root, dirs, files in os.walk(path.join(path.abspath('.'), 'markdown')):
  d = path.basename(root)
  markdown_files.extend((d, f) for f in files if not f.endswith('swp'))

markdown_files.sort(key=lambda x: x[1], reverse=rev)

index_list = ''
for d, fi in markdown_files:
  print 'writing', fi + '.html'
  mapping = {}
  md = codecs.open(path.join(markdown_path, fi), 'r', 'utf-8').read()
  html = markdown(md, extensions=ext)

  mapping['title'] = md.split('#')[1].split('\n')[0][1:]
  mapping['body'] = html
  mapping['date'] = fi[:10]
  mapping['url'] = fi + '.html'

  post_html = template.substitute(title=mapping['title'], body=post.substitute(mapping))
  codecs.open(path.join(html_path, fi + '.html'), 'w', 'utf-8').write(post_html)
  if not fi.endswith('.draft'):
    index_list += lst.substitute(mapping)

codecs.open(path.join(html_path, 'index.html'), 'w', 'utf-8').write(template.substitute(title='index', body=index.substitute({'list':index_list})))
