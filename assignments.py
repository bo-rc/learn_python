#!/Users/boliu/anaconda/bin/python

import abc
import datetime


class MaxSizeList(object):
    def __init__(self, max_len):
        self.max_len = max_len
        self.list = []
        self.len = 0

    def push(self, str):
        if self.len < self.max_len:
            self.len += 1
            self.list.append(str)
        else:
            self.list.pop(0)
            self.list.append(str)

    def get_list(self):
        return self.list


class WriteFile(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, filename):
        self.filename = filename

    @abc.abstractclassmethod
    def write(self, string):
        return

    def write_line(self, line):
        fd = open(self.filename, 'a')
        fd.write(line + '\n')


class LogFile(WriteFile):
    @classmethod
    def dt(cls):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

    def write(self, string):
        self.write_line('{time}    {text}'.format(time=LogFile.dt(), text=string))


class DelimFile(WriteFile):
    def __init__(self, filename, delim):
        super(DelimFile, self).__init__(filename)
        self.delim = delim

    def write(self, string):
        text = self.delim.join(string)
        self.write_line(text)




