#!/usr/bin/env python3
# -*- coding: utf-8 -*-

imap_password = input("Enter your crypted imap password:")

passwordCryptedLogin = input("Enter your password to encrypt your password:")

bashCommand = 'linuxconsolestringcryptor d ' + passwordCryptedLogin + ' ' + imap_password
import subprocess
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

print(output.decode('UTF-8'))
