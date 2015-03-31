#!/usr/bin/env python3
# -*-coding: utf-8 -*-
__author__ = 'yurik'
import os


def install(file):
    file_data = open(file)
    line = file_data.readline()
    while line:
        if line.strip() != '' and line[0] != '#':
            os.system(line)
        line = file_data.readline()
    file_data.close()

    ssh_generator()
    install_soft()


def ssh_generator():
    email = input('Enter e-mail for ssh-key:')
    if email == '':
        ssh_generator()

    os.system('ssh-keygen -t rsa -C "' + email + '"')
    os.system('xclip -sel clip < ~/.ssh/id_rsa.pub')
    print('Key copy to clipboard...')


def install_soft():
    ch = input('Install other soft (y/n):')
    if ch == 'y':
        install('soft.txt')


if __name__ == "__main__":
    install('commands.txt')
