# objects with __iter__() return an iterator object that you call __next__() on.

# try this in the interactive

nums = [2,3,5,7]

dir(nums)
# Notice the "__iter__"

i = nums.__iter__()
# Notice the "__next__"

i.__next__()
i.__next__()
i.__next__()
i.__next__()
# You get the "StopIteration" exception when done. I'm not happy about this plan, by the way.

tt = nums.__iter__()
while True:
    try:
        i = tt.__next__()
        # Using i in this code
        print(i)
        # End of using i
    except StopIteration:
        break

print("or")

for i in nums:
    print(i)
        
