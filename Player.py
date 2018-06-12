import sys
import os


class Player:
    def __init__(self):
        self.userName = None
        self.pw = None
        self.first = None
        self.last = None
        self.days = 1

    def setUserName(self, userName):
        self.userName = userName

    def setpw(self, pw):
        self.pw = pw

    def setFirst(self, first):
        self.first = first

    def setLast(self, last):
        self.last = last


