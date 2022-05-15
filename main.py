from Banco.cliente import Cliente, ContaCorrente, ContaPoupanca

c1 = Cliente('Jonatas Emanuel', 23)

corrente = ContaCorrente(234,
                         2222,
                         100)

c1.add_corrente(corrente)
print(c1.nome)
c1.ver_corrente()
print(corrente.saldo)
corrente.sacar(700)
print(corrente.saldo)
print()

poupanca = ContaPoupanca(3333,
                         3243,
                         45)
c1.add_poupanca(poupanca)
c1.ver_poupanca()
poupanca.sacar(23)
poupanca.sacar(434)
print(poupanca.saldo)
