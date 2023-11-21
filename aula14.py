a = 'A'
b = 'B'
c = 1.1

string = 'a={0} b={1} c={2:.2f}'  # utilizando índices
formato = string.format(a, b, c)

string = 'a={0} b={1} c={2:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)  # utilizando parametros

print(formato)

# erro out of range -> quer dizer que ta buscando algo que já terminou
