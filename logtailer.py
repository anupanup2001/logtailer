#!/usr/bin/python

class logtailer(object):
    def __init__(self, filename, callback):
        self.filename = filename
        self.onNewMatch = callback

    def start(self):
        print 'Starting to tail ', self.filename

    def stop(self):
        print 'Stopping tail ', self.filename

