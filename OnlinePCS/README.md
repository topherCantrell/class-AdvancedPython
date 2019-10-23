# Online Class Resources

Note that the course needs to be updated to include the new `bytes` type in python3.

In python3, the socket functions take a `bytes` object instead of a `str`.

Bytes and strings are pretty much the same. You can work with them the same way, and it is easy to convert between the two.

```python

my_string = 'This is a string'

my_bytes = b'This is bytes' # Notice the 'b' out front

x = 'Hello World'
y = x.encode() # This converts a string to bytes

x = b'Some bytes'
y = x.decode() * This converts bytes to a string
```
