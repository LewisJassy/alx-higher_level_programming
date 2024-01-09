#!/usr/bin/python3

def lookup(obj):
    if isinstance(obj, dict):
        return dict((lookup(k), lookup(v)) for k, v in obj.items())
    elif isinstance(obj, list):
        return [lookup(x) for x in obj]
    else:
        return obj
