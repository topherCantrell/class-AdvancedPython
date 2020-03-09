

def gen_things():    
    print('Start of gen_things')    
    yield 'ONE'    
    print('Here 1')    
    yield 'TWO'    
    print('Here 2')    
    yield 'THREE'    
    print('End of gen_things')
    
print('Entering loop')
for s in gen_things():
    print(s)
print('Done with loop')