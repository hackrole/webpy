import web

db = web.database(dbn='sqlite', db='sql/main.db')

def get_pages():
    return db.select('pages', order='id DESC')

def get_page_by_url(url):
    """
    
    Arguments:
    - `url`:
    """
    try:
        return db.select('pages', where='url=$url', vars=locals())[0]
    except IndexError:
        return None

def get_page_by_id(id):
    """
    
    Arguments:
    - `id`:
    """
    try:
        return db.select('pages', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def new_page(url, title, text):
    db.insert('pages', url=url, title=title, content=text)
    
def del_page(id):
    """
    
    Arguments:
    - `id`:
    """
    db.delete('pages', where='id=$id', vars=locals())

def update_page(id, url, title, text):
    """
    
    Arguments:
    - `id`:
    - `url`:
    
    """
    db.update('pages', where='id=$id', vars=locals(), url=url, title=title, content=text)
