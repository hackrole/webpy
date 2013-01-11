#!/usr/bin/python2.7
#coding=utf-8

import web, datetime

db = web.database(dbn="mysql", db="blog", user="root", passwd='root')

def get_posts():
    return db.select('entries', order='id DESC')

def get_post(id):
    try:
        return db.select('entries', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def new_post(title, text):
    db.insert('entries', where='id=$id', vars=locals())

def del_post(id):
    db.delete('entries', where='id=$id', vars=locals())
    
def update_post(id, title, text):
    db.update('entries', where='id=$id', vars=locals(), title=title, context=text)



