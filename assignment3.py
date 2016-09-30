#!/usr/bin/python


class ConfigDict(dict):

    def __setitem__(self, key, val):
        dict.__setitem__(self, key, val)



