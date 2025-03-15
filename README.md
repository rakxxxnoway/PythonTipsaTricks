# [📖] Python: Tips&Tricks


_Here I want to share or explain some stuff that I didn't got to know when I started with beginners and if you somehow aproached this repo - try to enjoy_

**P.S.**

You can also use this as a cheatsheet


**P.S.S.**

Yes I do compare those examples with other languages


## <📰> Whats new?:
- Not really new but did you know that we have "switch case" in python? ohh yes. Thank you lord for that. Example:
```python
match_string = "Hello, World"
match match_string:
    # just a switch case
    case "Hello, World":
        print("Wow, it worked")
    
    #...
    
    # default case
    case _:
        print("If nothing matches, runs this")
```


## <📜> String formatting:

* The **old** way aka *C*/*C++* wanna be:
```python
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
```
```tty
Output:
Fry is 25 years old
```

- The **long** way:
```python
print("> Name: {}\n> Age: {}\n> Address: {}".format(name, age, addr))
# OR
print("> Name: {0}\n> Age: {2}\n> Address: {1}".format(name, age, addr))
# can be handy if you do not wanna follow the format() order
# kinda same in java:
# "%s %d %s".formatted(name, age, addr);
```
```tty
Output:
> Name: Fry
> Age: 25
> Address: Planet Express

> Name: Fry
> Age: Planet Express
> Address: 25
```

- The **standard** way:
```python
print(f"> Name: {name}\n> Age: {age}\n> Address: {addr}")
# aka in C# $"{name} {age} ...";
```
```tty
Output:
> Name: Fry
> Age: 25
> Address: Planet Express
```

- Removing unwanted characters from the string
```python
bender = "$@Bender#!?"
# removes all unwanted chars
print(bender.strip("$@#!?"))
# removes specific unwanted chars
print(bender.strip("$@#"), "")
```
```tty
Output:
Bender
Bender!?
```

- Reversing a string:
```python
# the short way
print("Hello, world!"[::-1])

# the long way
str_to_reverse = "Hello, world!"
reversed_str = reversed(str_to_reverse)
print(reversed_str)
```
```tty
Output:
!dlrow ,olleH
!dlrow ,olleH
```

- Using separator in string:
```python
print("hubert.j.farnsworth", "planetexpress.com", sep="@")
```
```tty
Output:
hubert.j.farnsworth@planetexpress.com
```


## <↗️> Lists:

- How to create a list with *n* elements in it:
```python
nums = [1] * 10
chars = ['c'] * 10
```
```tty
Output:
[1, 1, 1, ...]
["c", "c", "c", ...]
```
- Unpacking a list to variables:
```python
a, b, c, *d = [x for x in range(0,10)]
print(a)
print(b)
print(c)
print(d)
```
```tty
Output:
1
2
3
[3, 4, 5, 6, 7, 8, 9]
```
- Reverse list
```python
reversed_list = ['a', 'b', 'c', 'd', 'e']
print(reversed_list)
reversed_list.reverse()
print(reversed_list)
```
```tty
Output:
['e', 'd', 'c', 'b', 'a']
```
- Remove all duplicates
```python
dupli_list = [1, 3, 3, 3, 5, 5, 5, 6, 6, 6, 6, 6, 10, 10]
print(set(dupli_list)) # -> class 'set'
# use list() to convert back to list class
```
```tty
Output:
{1, 3, 5, 6, 10}
```


## <󠁦󠁦📈> Functions

- Set function/method parameters with list
```python
def params_list(a, b, c):
    print(a, b, c)

params_list(*[10, 20, 30])
```
```tty
Output:
10 20 30
```

- Example of the ***yield***:
```python
def local_data_extraction():
    for i in range(0, 10):
        yield i

for i in local_data_extraction():
    print("* Extracted data -> %d from function" % (i))
```
```tty
Output:
* Extracted data -> 0 from function
* Extracted data -> 1 from function
* Extracted data -> 2 from function
...
```

- Return type of the function *(python3.5+)*
```python
def return_type() -> int:
    return 0
```


## <♾️> Other

- Make a console sound:
```python
print("\a")
```

- Division trick:
```python
print(f"Division: (float) 100 / 10 = {100 / 10 }")
print(f"Division: (int) 100 // 10 = {100 // 10 }") # rounds
```
```tty
Output:
Division: (float) 100 / 10 = 10.0
Division: (int) 100 / 10 = 10
```

- Set a data type to a variable:
```python
name : str = "Leela" 
age:int = 25
# do not need spaces between :
```

- More readable longs (same in java8+):
```python
how_many_zeros = 1000000 # ?????? To hard to see, is it 100k or 1kk? 
milli = 1_000_000 # oh, now I see
print(how_many_zeros, milli)
```
```tty
Output:
1000000 1000000
```

- Single line tty with for loop (kinda same in C/C++)
```C
// C
for (int i=0; i < 10; i++)
    printf("%d ", i);

printf("\n");
```
```tty
Output:
0 1 2 ...
```

```python
# python
for i in range(0, 10):
    print(i, end=" ")

print("\n")
```
```tty
Output:
0 1 2 ...
```

- Multi line comments and strings
```python
"""
This is a multi line comment
"""

print("""
This is a multi line string
""")

# remember that each line is a new line (see Output)
```
```tty
Output:

This is a multi line string

```

- Immutable elements
```python
mutable_list = ['a', 'd', 'd', 'd', 'e']
# I can change for a example first element by doing this
mutable_list[0] = 'f'
print(mutable_list) # ->  ['f', 'b', 'c', 'd', 'e']
# but if I use frozenset():
immutable_list = frozenset(mutable_list)
# just to pass the exception
try:
    immutable_list[0] = 'f'
    print(immutable_list) # ->  TypeError: 'frozenset' object does not support item assignment
except TypeError:
    pass
```

- Multiple OR statements:
```python
char = 'a'

if char in ('a', 'd', 'd', 'd', 'e'):
    print(True)

else
    print(False)
```
```tty
Output:
True
```
