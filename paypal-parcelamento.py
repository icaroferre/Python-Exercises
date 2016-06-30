def calculo(valor, parcelas):
	taxa_paypal = 0.05
	taxa_parcelamento = 0.024
	taxa_transferencia = 0.6
	return valor + (valor * taxa_paypal) + taxa_transferencia + (valor * (parcelas * taxa_parcelamento))

print 
print "Calculador de Parcelamento do Paypal"
print 

valor_inicial = int(raw_input("Qual o Valor do Pagamento? "))
numero_de_parcelas = int(raw_input("Qual o Numero de Parcelas? "))
valor_final = calculo(valor_inicial, numero_de_parcelas)

print 
print "-----------------------"
print "Valor Total: R$%s" % (format(round(valor_final,2),".2f")) 
print "Valor por Parcela: R$%s" % (format(round(valor_final / numero_de_parcelas, 2),".2f"))
print "Valor das Taxas: R$%s" % (format(round(valor_final - valor_inicial, 2),".2f")) 
print "-----------------------"
