from _tracemalloc import start

# Keeping state -- all the local variables

# ai+1 = (ai+x)*start

def seq(start,x,num):
    ai = start
    for i in range(num): # What is range? we'll see shortly
        print(ai,end=' ')
        ai = (ai+x)*start
    # Function eventually returns here
        
seq(2,3,4)

# What if you wanted to do something with each value instead of just print it.
# You could generate a list and return that. But that might take a long time.
# Maybe the using-code is going to break out early? You don't want to pre-generate
# All those numbers.

def seq2(start,x,num):
    ai = start
    for i in range(num):
        yield ai
        ai = (ai+x)*start
    # Function eventually returns here
        
# yield is like return except that it preserves the stack (locals, code position, etc)

# SEQ2 DOES NOT RETURN VALUES. IT RETURNS A GENERATOR OBJECT.

g = seq2(2,3,4)
print(g)

# This object is iterable. You can ask for its iterator:

it = g.__iter__()

print(it.__next__())

# Usually done like this:

for v in seq2(2,3,4):
    print(v)
        
# Talk about range ... simple range(n)