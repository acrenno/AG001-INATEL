import sympy

# CALCULANDO A VARIAVEL C
MATRICULA = 250

C = MATRICULA % 10

def function(x, C):

    #EQUACAO PADRAO DOS CALCULOS
    return (((C+1)-sympy.sqrt(x))/(((C+1)**2)-x))


def calculate_limit(function, variable, tendencies):

    #CALCULANDO E RETORNANDO O LIMITE DA FUNCAO COM TENDENCIA ESPECIFICA

    #DEFININDO OS RESULTADOS
    results = []


    for tendency in tendencies:

       #FUNCAO PARA LIMITE
        limit = sympy.Limit(function, variable, tendency)

        # CALCULANDO VALOR DO LIMITE
        result = limit.doit()

        #ADICIONADNO O RESULTADO
        results.append(result)

    # RETORNANDO O RESULTADO
    return results


# DEFININDO VARIAVEL
VARIAVEL = sympy.Symbol('x')

# CHAMANDO FUNCAO
FUNCTION = function(VARIAVEL, C)



# DEFININDO AS CONSTANTES INFINITAS
INFINITY = sympy.oo

NEGATIVE_INFINITY = -sympy.oo


# DEFININDO AS TENDENCIAS
TENDENCIES = [(C+1)**2, INFINITY, NEGATIVE_INFINITY]



# CHAMANDO A FUNCAO
results = calculate_limit(FUNCTION, VARIAVEL, TENDENCIES)


# SAINDO COM OS RESULTADOS
for i in range(len(results)):
    print(f'Exercicio {i+1}: Calculando limite quando {VARIAVEL} tende a {TENDENCIES[i]}:  {results[i]}\n')