import sympy

# CALCULANDO A VARIAVEL C
MATRICULA = 250

C = MATRICULA % 10


def function(t, C):

    #EQUACAO PADRAO DOS CALCULOS'
    return (((((t**(1/3))/5)+((C+1)/(t**3)))-((C+2)*(t**2))) - 15)


def calculate_derivative(function, variable, order=1, point=None):

    #CALCULANDO E RETORNANDO DERIVADA COM DETERMINADA ORDEM

    # DEFININDO RESULTADOS
    results = []

    # USANDO FUNCAO DE DERIVAR
    derivative = sympy.Derivative(function, variable, order)

    # CALCULANDO A DERIVADA
    result = derivative.doit()

    # SE O PONTO FOI PASSADO, CALCULAR NO PONTO
    if point:
        result = result.subs({variable: point})

    # RETORNANDO RESULTADO
    return result


# DEFININDO A VARIAVEL DA FUNCAO
VARIAVEL = sympy.Symbol('t')

# CHAMANDO FUNCAO
FUNCTION = function(VARIAVEL, C)

# COLOCANDO AS ORDENS
calc_1 = {'order': 1, 'point': None}
calc_2 = {'order': 1, 'point': 7}
calc_3 = {'order': 2, 'point': None}
calc_4 = {'order': 2, 'point': 2}

arguments = [calc_1, calc_2, calc_3, calc_4]

# CHAMANDO FUNCOES
results = []

for argument in arguments:
    result = calculate_derivative(FUNCTION, VARIAVEL, argument['order'], argument['point'])
    results.append(result)

#SAINDO COM O RESULTADO
for i in range(len(results)):
    print(f'ExercICIO {i + 1}: Calculando derivada da funcao: {results[i]}\n')





