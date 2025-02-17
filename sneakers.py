from pprint import pprint
filters = ['title', 'color', 'full_price', 'current_price', 'pulbish_date']


def beolvas():
    sneakers = []
    with open('sneakers.csv', 'r') as forras:
        forras.readline()
        for sor in forras:
            adatok = sor.strip().split(',')
            szotar = {}
            szam = 0
            for _ in range(5):
                szotar[filters[szam]] = adatok[szam]
                szam = szam + 1
            sneakers.append(szotar)
    return sneakers


def szempontvalasztas():
    print('Válassz melyik szempont alapján rendezzem a cipőket?')
    for index in range(len(filters)):
        print(f'{index+1} - {filters[index]}')
    lehetoseg = int(input('Add meg a lehetőség számát!  '))
    return lehetoseg


def kiir(szempont, kiiras):
    pprint(sorted(kiiras, key=lambda sneaker: sneaker[filters[szempont-1]]))


def main():
    szotarak = beolvas()
    valasztas = szempontvalasztas()
    kiir(valasztas, szotarak)


main()
