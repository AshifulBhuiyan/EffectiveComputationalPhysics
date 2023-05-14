# import the class
from quark import Quark
# create a Quark object
t = Quark()
# set the flavor
t.flavor = "top"
# flip the flavor
t.flip()
# print the flavor
print(t.flavor)