# First of all, switch statement in python3.10+
# yes we now have switch statement in python since Python 3.10 (if someone didn't know that)
match_string = "Hello World"
match match_string:
    # just a switch case
    case "Hello World":
        print("Wow, it worked")
    
    #...
    
    # default case
    case _:
        print("If nothing matches, runs this")


# Really old way to format
# Use f"" or .format() at least
name = "Fry"
age = 25

print("%s is %d %s old" % (
    name,
    age,
    # one liner if statement
    "years" if age > 1 else "year"
    )
)


# Make a len 10 list of same num/char
nums = [1]* 10
chars = ['c']* 10
print(nums, chars)


# Remove all unwanted chars from a string
bender = "$@Bender#!?"
# removes all unwanted chars
print(bender.strip("$@#!?"))
# removes specific unwanted chars
print(bender.strip("$@#"), "")


# Unpack specific amount to one var from a list
a, b, c, *d = [x for x in range(0, 11)]
print(d)


# Set data to params with list
def params_list(a, b, c):
    print(a, b, c)

params_list(*[10, 20, 30])


# Get local data and use it outside without returning it
def local_data_extraction():
    for i in range(0, 11):
        yield i

for i in local_data_extraction():
    print("* Extracted data -> %d from function" % (i))


# Make a sound =)
print("\a")


# Division trick
print(f"Division: float 100 / 10 = {100 / 10 }")
print(f"Division: int 100 // 10 = {100 // 10 }")


# Reversed string
print("Hello World!"[::-1])
# this more a longer way
string_to_reverse = "Hello World!"
reversed_string = reversed(string_to_reverse)
print("".join(reversed_string))


# Reversed list
reversed_list = ['a', 'b', 'c', 'd', 'e']
print(reversed_list)
reversed_list.reverse()
print(reversed_list)


# Set data type to a variable
name : str = "Leela"
age:int = 25


# Set return type to a method/function
# yeah you can do it in python3.5+
def return_type() -> int:
    return 0


# Big number managment
how_many_zeros = 1000000 # ?????? To hard to see, is it 100k or 1kk? 
milli = 1_000_000 # oh, now I see
print(how_many_zeros, milli) # exactly the same output -> 1000000


# Remove all duplicates
dupli_list = [1, 3, 3, 3, 5, 5, 5, 6, 6, 6, 6, 6, 10, 10]
print(set(dupli_list)) # add list() to convert to list again


# Print on single line with for loop
for i in range(0, 10):
    print(i, end=" ")

# don't forget to add \n 'cause end="" removes new line
print("\n")


# Print with separator
print("hubert.j.farnsworth", "planetexpress.com", sep="@")


# Multi line comments or multiline strings
"""
This is a multi line comment
"""

print("""
This is a multiline print
""")


# Immutable element
mutable_list = ['a', 'd', 'd', 'd', 'e']
# I can change for a example first element by doing this
mutable_list[0] = 'f'
print(mutable_list) # ->  ['f', 'b', 'c', 'd', 'e']
# but if I do like this:
immutable_list = frozenset(mutable_list)
# just to pass the exception
try:
    immutable_list[0] = 'f'
    print(immutable_list) # ->  TypeError: 'frozenset' object does not support item assignment
except TypeError:
    pass


# Multiple or statments
data = 'a'
if data in ('a', 'd', 'd', 'd', 'e'):
    print(True)
else:
    print(False)
