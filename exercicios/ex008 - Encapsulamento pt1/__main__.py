from ex008 import *

def main():
    c1 = ContaBancaria(111, 'Claudio Sperb', 5000)
    c1.depositar(1000)
    c1._nome = 'Claudio'

    print(c1)

if __name__ == '__main__':
    main()