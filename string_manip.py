import time

# Python string to bytes
mystring = "Solar Power"
# start = time.time()
b1 = bytes(mystring, 'utf-8')
# print(f"bytes function took {time.time()-start} seconds")
# start = time.time()
b2 = mystring.encode('utf-8')
# print(f"encode function took {time.time()-start} seconds")

# Python bytes to string
s1 = b1.decode("utf-8")
s2 = b2.decode("utf-8")
# print(s1)
# print(s2)

# Python ljust example
# print(repr(s1.ljust(25)))
# print(s1.ljust(25, "!"))
# print(s2.ljust(25, "#"))

# Python ljust + negative indices
s3 = s1.ljust(25, "$")
# print(s3[0])
# print(s3[10])
# print(s3[24])

# print(s3[-25])
# print(s3[-15])
# print(s3[-1])

# python string copy example + memory alloc
import copy
s4 = s3
s5 = copy.copy(s3)
s6 = copy.deepcopy(s3)
# locations = map(id, [s3, s4, s5, s6])
# for loc in locations:
#     print(f"Memory located at: {loc}")
s3 += "a"
s4 += "x"
s5 += "y"
s6 += "z"
# print(f"String 3: {s3}")
# print(f"String 4: {s4}")
# print(f"String 5: {s5}")
# print(f"String 6: {s6}")
# locations = map(id, [s3, s4, s5, s6])
# for loc in locations:
#     print(f"Memory located at: {loc}")

# Python isupper function
# print(f"{s3} is upper case? {s3.isupper()}")
# print(f"{s3[:4]} is upper case? {s3[:4].isupper()}")
# print(f"{s3[:1]} is upper case? {s3[:1].isupper()}")
# print(f"{s3[:-2]} is upper case? {s3[:-2].isupper()}")
# print(f"{s3[6]} is upper case? {s3[6].isupper()}")

# Python islower function
# print(f"{s3} is lower case? {s3.islower()}")
# print(f"{s3[:4]} is lower case? {s3[:4].islower()}")
# print(f"{s3[1:4]} is lower case? {s3[1:4].islower()}")
# print(f"{s3[:-16]} is lower case? {s3[:-16].islower()}")
# print(f"{s3[8]} is lower case? {s3[8].islower()}")

# Python casefold vs lower
s3 += "ẞ"
# print(s3.casefold())
# print(s3.lower())

# check for alphanumeric with isalnum
print(f"Is {s3} alphanumeric? {s3.isalnum()}")
print(f"Is {s1} alphanumeric? {s1.isalnum()}")
print(f"Is {s5} alphanumeric? {s5.isalnum()}")
print(f"Is {s3[:3]} alphanumeric? {s3[:3].isalnum()}")
