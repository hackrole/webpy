#!/usr/bin/python2.7
#coding=utf-8

from jinja2 import *
import sys,traceback

def fileSystem_try(file, path, **kargs):
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
        

