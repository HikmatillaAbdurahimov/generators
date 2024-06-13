from typing import Optional

""" RANGE IFODANI FLOAT SOLAR UCHUN HAM ISHLASHI """
def range(start:Optional[float]=None, stop:Optional[float]=None, step:Optional[float]=None):
    number = 0
    if start:
        print(start)
        while number < stop:
            number = start + step
            start = number
            yield number
    else:
        start = 0
        print(start)
        while number < stop:
            number = start + step
            start = number
            yield number

""" FIBONACHI SONLAR """
def fibo(stop):
    start=0
    _and=1
    if isinstance(stop,int):
        print(start)
        while _and<=stop:
            fibo_numbers=start+_and
            start=_and
            _and=fibo_numbers
            yield fibo_numbers

def run():
    runserver=input("""
        generators:
             1.range_func
             2.fiobo_numbers
                  ==> :""")
    if runserver=="1":
        num = range(stop=10, step=2.5)
        for i in num:
            print(i)
        _run=input("""
             back to minu
                 1.yes
                 ==>""")
        if _run=="1":
            return run()
    elif runserver=="2":
        fibo_num = fibo(100)
        for i in fibo_num:
            print(i)
        _run = input("""
                   back to minu
                       1.yes
                       ==>""")
        if _run == "1":
            return run()
if __name__=="__main__":
    run()













