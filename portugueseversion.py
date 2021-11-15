



cpf = input("Digite o cpf no formato xxx.xxx.xxx-xx:")
#verificando se segue o padrão solicitado

import re

formato_cpf = re.compile("[0-9][0-9][0-9][.][0-9][0-9][0-9][.][0-9][0-9][0-9][-][0-9][0-9]")

verificando_padrao = formato_cpf.search(cpf)

if verificando_padrao and len(cpf) == 14:

    cpf_sem_ponto = cpf.replace('.','')
    cpf_limpo = cpf_sem_ponto.replace('-','')
    resultado = 0
    # Verificando se todos os digitos são iguais
    if cpf_limpo[0] == cpf_limpo[1] == cpf_limpo[2] == cpf_limpo[3] == cpf_limpo[4] == cpf_limpo[5] == cpf_limpo[6] == cpf_limpo[7] == cpf_limpo[8] == cpf_limpo[9] == cpf_limpo[10]:
        print('O cpf é inválido!')
    else:
        # verificação do 1 dígito
        contador = 10
        for letra in cpf_sem_ponto:
            if letra == '-':
                break
            letra = int(letra)
            multiplica = letra * contador
            contador -= 1
            resultado += multiplica  
        validacao2 = resultado *10%11
        # verificação do 2 dígito 
        contador2 = 11
        multiplica2 =0
        resultado2 = 0
        cpf_limpo_sem_o_ultimodigito = cpf_limpo[:10]
        for numero in cpf_limpo_sem_o_ultimodigito:
            numero_float = float(numero)
            multiplica2 = numero_float * contador2
            contador2 -= 1
            resultado2 += multiplica2
        validacao3 = resultado2 * 10%11

        # retorno ao usuário se o cpf é falso ou verdadeiro
        if validacao2 and validacao3:
            print('Este cpf é válido!')
        else:
            print('Este cpf é inválido!')    
else:
    print("Use o padrão solicitado!")
