from Banco.cliente import Cliente, ContaCorrente

c1 = Cliente('Jonatas Emanuel', 23)

corrente = ContaCorrente(234,
                         2222,
                         100)

c1.add_corrente(corrente)
print(c1.nome)
c1.ver_corrente()
print(corrente.saldo)
corrente.sacar(10)
corrente.sacar(15)
print(corrente.saldo)
