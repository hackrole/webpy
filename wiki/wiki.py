import web
import model
import markdown

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

render = web.template.render('templates', base='base', globals=t_globals)

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
    
    def GET(self):
        
        import time
        import re
