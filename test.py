import timeit

if __name__ == '__main__':
    c = 4
    while c < 17 and c != 0 and c != -5:
        c += 1

    c = 4
    cont = True
    while cont:
        if c >= 17 or c == 0 or c == -5:
            cont = False
        c += 1

    # code snippet whose execution time is to be measured
    minus1 = '''def example():
                c = 4
                while c < 17 and c != 0 and c != -5:
                    c += 1'''

    minus2 = '''def example():
                c = 4
                cont = True
                while cont:
                    if c >= 17 or c == 0 or c == -5:
                        cont = False
                    c += 1'''



    num = 100000000
    # timeit statement
    print("minus1", timeit.timeit(stmt=minus1, number=num))
    print("minus2", timeit.timeit(stmt=minus2, number=num))


"""

# code snippet to be executed only once
mysetup = "from math import sqrt"

# code snippet whose execution time is to be measured
mycode = ''' 
def example(): 
    mylist = [] 
    for x in range(100): 
        mylist.append(sqrt(x)) 
'''

# timeit statement
print
timeit.timeit(setup=mysetup,
              stmt=mycode,
              number=10000)

"""