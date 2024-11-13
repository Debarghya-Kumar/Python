#Program using keyword length argument
def myPrg(**kwargs):
    for key, value in kwargs.items():
        print(key,"==",value)
myPrg(first='Hello', mid='Welcome', last='Hello')
