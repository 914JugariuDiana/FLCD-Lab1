from service.Scanner import Scanner

if __name__ == '__main__':
    filename = './lexicalError.txt'

    scanner = Scanner()
    print(scanner.scan(filename))

