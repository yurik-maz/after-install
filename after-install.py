#!/usr/bin/env python3
# -*-coding: utf-8 -*-
__author__ = 'yurik'
import os


def install():
    file_data = open('commands.txt')
    line = file_data.readline()
    while line:
        if line.strip() != '' and line[0] != '#':
            os.system(line)
        line = file_data.readline()
    file_data.close()


if __name__ == "__main__":
    install()
