#!/usr/bin/python2.7
#coding=utf-8

from jinja2 import *
import sys,traceback
import time

def fileSystem_try(f, path, **kargs):

    env = Environment(loader=FileSystemLoader(path)))
    try:
        template = env.get_template(file)
        template.render(**kargs)
    except TemplateNotFound:
        print "tempalte %s under %s not found" % (file, path)
        sys.exit()
    except TemplateError:
        print "tempalte %s under %s is error" % (file, path)
        print traceback.print_stack()
        
if __name__ == "__main__":
    path = raw_input('please entry the template dir path:')
    f = raw_input('please enter the file name:')
    b = raw_input('if write the result to file:')
    while b not in ['Y', 'N', 'y', 'n']:
        b = raw_input('you must entry y or n:')

    result = fileSystem_try(f, path)
    if b in ['Y', 'y']:
        tmp = '/tmp/%s' % (time.now()+f)
    open(tmp, 'w').write(result)
