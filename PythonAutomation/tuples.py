# Tuples are considered as read-only

tu = (23,34.2,"string value")
print(tu)
print(tu[0])
print(len(tu))
print("")

# concat tuples
tu1 = (123,234.2,"string value")
tu2 = tu + tu1
print(tu2)