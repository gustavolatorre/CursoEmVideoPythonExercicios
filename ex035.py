print('=-'*15)
print('Analisador de Triângulos')
print('=-'*15)

segmento1 = float(input('Primeiro segmento: '))
segmento2 = float(input('Segundo segmento: '))
segmento3 = float(input('Terceiro segmento: '))

if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento1 + segmento2:
    print('Os segmentos digitados PODEM FORMAR um triângulo!')
else:
    print('Os segmentos digitados NÃO PODEM FORMAR um triângulo!')
