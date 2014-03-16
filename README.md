# white noise
hello this is a static blog type thing generator i wrote because i couldn't
find one simple enough. not intended for anyone elses use really.

it is braindead simple and will prboably break if you try to do anything that
isn't the following:

install [python markdown](http://pythonhosted.org//Markdown)

edit the ext variable at the top of convert.py to include the extenions you
want. see
[here](http://pythonhosted.org//Markdown/extensions/index.html#officially-supported-extensions).
the default is ['extra', 'codehilite']

set up your directory structure like this:

    convert.py          the actual program
    template.html       your main page template
    index.html          your index template
    list.html           your post list template
    markdown/           your markdown files
      2014-03-16-hello
      2014-02-16-why-would-you-do-this
    html/               where the final html files will go. symlink/upload this
                        to your web directory or whatever.

run

    python convert.py

## the main page template
add one python string formatting thingy where you want the output from your
markdown/the index stuff to go. for example:

    <html>
      <body>
        <div class="content">
          {}
        </div>
      </body>
    </html>

on each post a back link is automatically added in a div with the 'footer'
class.

## the index template
this is what goes before the post list on the index. example:

    <h1>welcome to my web site am i internet famous yet?</h1>

## the list template
this is what goes around each post link on the index page. example:
    
    <div class="post-link">{}</div>

the complete anchor tag with the url is inserted into this.

## ordering
the post list on the index page is ordered by the original filenames. by
default this is in reverse order, so prefixing ISO dates (2014-03-16 for
example) will cause the posts to be ordered newest to oldest. if you want to
reverse this run convert like this:

    python convert.py reverse
