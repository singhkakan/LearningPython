#!usr/bin/python

import re

phone = "602-343-8747"
print(type(phone))
print phone
match = re.findall(r'^.{0,3}', phone)
print(type(match))

print "The area code is:", match[0]
