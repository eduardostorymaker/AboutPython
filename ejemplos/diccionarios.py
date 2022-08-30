def main():
    print('funciona')
    mydict = {
        'uno': 1,
        'dos': 2,
        'tres': 3,
    }

    for llave in mydict.keys():
        print(mydict[llave])

if __name__ == '__main__':
    main()