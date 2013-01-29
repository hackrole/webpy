#!/usr/bin/python2.7
#coding=utf-8

import web
import model
import markdown
from web.contrib.template import render_jinja

urls = (
    '/', 'Index',
    '/new', 'New',
    'edit/(\d+)', 'Edit',
    '/delete/(\d+)', 'Delete',
    '(.*)', 'Page',
    )

t_globals = {
    'datestr': web.datestr,
    'markdown': markdown.markdown,
}

render = render_jinja(
    'templates', # 模板路径
    encoding = 'utf-8', # 编码
)

class Index:
    def GET(self):
        """ show page"""
        pages = model.get_pages()
        return render.index(pages)

class Page:

    def GET(self, url):
        page = model.get_page_by_url(url)
        if not page:
            raise web.seeother('/new?url=%s' % web.websafe(url))
        return render.view(page)

class New:

    def not_page_exists(url):
        """
        Arguments:
        - `url`:
        """
        return not bool(model.get_page_by_url(url))

    page_exists_validator = web.form.Validator('Page already exists', not_page_exists)

    form = web.form.Form(
        web.form.Textbox('url', web.form.notnull, size=30, description="Location:"),
        web.form.Textbox('title', web.form.notnull, size=30, description="Page Title:"),
        web.form.Textarea('content', web.form.notnull, rows=30, cols=80, description="Page content:", post="use markdown syntax"),
        web.form.Button('Create Page')
        )
    def GET(self):
        url = web.input(url='').url
        form = self.form()
        return render.new(form)

    def POST(self):
        form = self.form()
        if not form.validates():
            return render.new(form)
        model.new_page(form.d.url, form.d.title, form.d.content)
        raise web.seeother('/' + form.d.url)

class Delete:
    """

    """

    def POST(self, id):
        model.del_page(int(id))
        raise web.seeother('/')

class Edit:
    form = web.form.Form(
        web.form.Textbox('url',web.form.notnull, description="Location:"),
        web.form.Textbox('title', web.form.notnull, size=30, description="Page Title:"),
        web.form.Textarea('content', web.form.notnull, rows=30, cols=80, description="Page content:", post="use markdown syntax"),
        web.form.Button('Update Page')
        )
    def GET(self, id):
        page = model.get_page_by_id(int(id))
        form = self.form()
        form.fill(page)
        return render.edit(page, form)

    def POST(self, id):
        form = self.form()
        page = model.get_page_by_id(int(id))
        if not form.validates():
            return render.edit(page, form)
        model.update_page(int(id), form.d.url, form.d.title, form.d.content)
        raise web.seeother('/')

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()




