def do_fizzbuzz(num:int):
    """
    3: fizz
    5: buzz
    15: fizzbuzz
    etc: num
    """
    for i in range(1,num+1):
        if i%3==0:
            print('fizz')
        else:
            print(f'{i}')

    print('hello')


if __name__=='__main__':
    do_fizzbuzz(16)
