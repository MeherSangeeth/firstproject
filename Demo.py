def sq_num(num):
    for x in num:
	print(x*x)
        print(x)

def do_num(num):
    for x in num:
	print(x+x)
        print(x)

if __name__ == '__main__':
    lst=[1,2,3,4,5]
    sq_num(lst)
    do_num(lst)
    do_num(lst)
