# When bool is truthy, func1 should be called, otherwise call the func2.

def _if(bool, func1, func2):
    if bool:
        return func1()
    else:
        return func2()

# func1
def truthy(): 
    print("Yes")
# func2
def falsey(): 
    print("No")
  
_if(True, truthy, falsey)
_if(False, truthy, falsey)

