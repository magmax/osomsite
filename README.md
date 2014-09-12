# OsomSite

The faster way to create a blog. Just write your posts in [Jekyll] YAML/Markdown format and generate automatically all indexes. 


## Current status

**Under development.**

To be done:

- retrieve a post.
- render it.
- add tag list.


# Contributing

- Download the repository: `git clone https://github.com/magmax/osomsite.git`
- Create a couple of posts in **"site/app/post"**. Example:

```yaml
    ---
    layout: post
    title: "title1"
    description: "description1"
    lang: en
    tags:
    - tag1
    - tag2
    ---
    This is the post content
```

- Run the `osomsite.py` script. This will generate all the needed indexes.
- Download the Javascript dependencies. Just enter in **"site"** directory and execute `bower install`. You can install [bower] with [npm].
- Configure any web server to serve **"site/app"**. The easiest way is to enter in that directory and execute one of these::

    python -m http.server 8080      # for python 3.X
    python -m SimpleHTTPServer 8080 # for python 2.X

Now you can see your site in http://localhost:8080



[Jekyll]: http://jekyllrb.com/
[bower]: http://bower.io/
[npm]: https://www.npmjs.org/
