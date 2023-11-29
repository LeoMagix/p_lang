#Having fun with Python's alias
first = input("What's your first name?\n")
#print()
last = input("And your last name?\n")

from menthor import name_user as nm
name = nm(first, last)
print(name)

from menthor import call_user as cu
cu(first, last)
