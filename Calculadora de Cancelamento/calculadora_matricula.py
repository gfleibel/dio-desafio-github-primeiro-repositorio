valorCurso = float(input("Insira o valor do curso:"))
aulasFeitas = int(input("Insira a quantidade de aulas realizadas:"))
aulasTotais = int(input("Insira a quantidade total de aulas do curso:"))
metodoPagamento = input("Insira o método de pagamento:\n1.Cartão de Crédito\n2.Boleto")
listaBoleto = ["boleto", "Boleto", "boleto bancário", "Boleto Bancário", "Boleto bancário", "2"]
parcelas = int(input("Insira o número de parcelas:"))
parcelasPagas = int(input("Insira o número de parcelas pagas:"))
valorParcelas = valorCurso/parcelas
valorPago = valorParcelas*parcelasPagas
valorRestante = valorCurso - valorPago
valorAulasFeitas = (valorCurso/aulasTotais)*aulasFeitas

if(metodoPagamento in listaBoleto):
    multa = (parcelas - parcelasPagas) * 10
else:
    multa = valorRestante * 0.20

debitos = valorAulasFeitas + multa
rescisao = float(debitos - valorPago)

if(rescisao>=0):
    print(f"O valor a ser pago no cancelamento é de R4{rescisao}.")
else:
    print(f"O valor a ser devolvido é de R${-1*rescisao}.")