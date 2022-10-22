from django.test import TestCase

# Create your tests here.

import random as r

x = r.randint(-100, 150)

if 10 <= x < 100:
    print(x, "2 digit")
elif 100 <= x < 1000:
    print(x, "3 digits")
else:
    print("crap number")
