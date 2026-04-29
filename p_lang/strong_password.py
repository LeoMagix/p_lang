"""Use Regex to check for strong password"""
import re

strong_passwrd = re.compile(r'[A-Za-z0-9]{8,}')
password = strong_passwrd.findall('Anothen96, anothen96, anoth1')
print(password)

