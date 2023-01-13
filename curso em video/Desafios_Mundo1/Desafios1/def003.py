n1=int(input('Digite um Número: '))
n2=int(input('Digite um número: '))
s=(n1+n2)
cores = {'limpa':'\033[m', 'verm':'\033[1:31m', 'verde':'\033[1:32m'}
print('A soma entre {}{}{} e {}{}{} é igual a {}{}{}'.format(cores['verm'], n1, cores['limpa'],
                            cores['verm'], n2, cores['limpa'], cores['verde'], s, cores['limpa']))
#""""n1 e n2 como int não str""""
