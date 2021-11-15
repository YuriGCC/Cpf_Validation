

cpf = input("type the cpf in format ###.###.###-##:")
#checking the requested pattern
import re

cpf_format = re.compile("[0-9][0-9][0-9][.][0-9][0-9][0-9][.][0-9][0-9][0-9][-][0-9][0-9]")

check_pattern = cpf_format.search(cpf)

if check_pattern and len(cpf) == 14:

    cpf_without_point = cpf.replace('.','')
    cpf_cleaned = cpf_without_point.replace('-','')
    result = 0
    # checking that all digits are equal
    if cpf_cleaned[0] == cpf_cleaned[1] == cpf_cleaned[2] == cpf_cleaned[3] == cpf_cleaned[4] == cpf_cleaned[5] == cpf_cleaned[6] == cpf_cleaned[7] == cpf_cleaned[8] == cpf_cleaned[9] == cpf_cleaned[10]:
        print('This cpf is invalid!')
    else:
        # checking the first digit
        counter = 10
        for lyric in cpf_without_point:
            if lyric == '-':
                break
            lyric = int(lyric)
            multiplies = lyric * counter
            counter -= 1
            result += multiplies  
        validation2 = result *10%11
        # checking the second digit 
        counter2 = 11
        multiplies2 =0
        result2 = 0
        only_numbers = cpf_cleaned[:10]
        for numero in only_numbers:
            float_number = float(numero)
            multiplies2 = float_number * counter2
            counter2 -= 1
            result2 += multiplies2
        validation3 = result2 * 10%11

        # feedback to the user
        if validation2 and validation3:
            print('This cpf is valid!')
        else:
            print('This cpf is invalid!')    
else:
    print("Use o padrão solicitado!")
