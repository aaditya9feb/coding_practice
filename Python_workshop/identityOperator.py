a='hello'
b="hello"
print(a is b)
if(id(a) == id(b)):
    print("True")
    print(f"id of a {id(a)} id of b {id(b)}")

