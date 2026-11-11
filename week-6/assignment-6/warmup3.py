def test_function ():
    secret = 24

test_function()
#print(secret)  #NameError: name 'secret' is not defined


def test_functionV2 ():
    secret = 24
    return secret

result = test_functionV2()
print (result)
