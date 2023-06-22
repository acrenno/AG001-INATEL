import sympy

# CALCULANDO A VARIAVEL C
MATRICULA = 250

C = MATRICULA % 10




def get_function_1(variable, C):

    return sympy.exp((-1*VARIABLE) - 1) + sympy.exp((-1*VARIABLE) - 3) + sympy.exp(VARIABLE) - (5*C) - 5


def get_function_2(variable, C):


    return ((C+2)*(variable**3))-((C+1)*(variable**2))-(5*variable)+(4*C)


def get_function_3(variable, C):

    return 2 * sympy.sin(4*(C-3)*variable) -10


def calculate_function(function):

    result = sympy.solve(function)

    return result


# DEFININDO AS VARIAVEIS DAS FUNCOES
VARIABLE = sympy.Symbol('x')

# DEFININDO AS FUNCOES
function_1 = get_function_1(VARIABLE, C)

function_2 = get_function_2(VARIABLE, C)

function_3 = get_function_3(VARIABLE, C)

functions = [function_1, function_2, function_3]

# CALCULANDO AS FUNCOES
results = []

for function in functions:
    result = calculate_function(function)

    results.append(result)

# SAINDO COM OS RESULTADOS
for i in range(len(results)):
    try:
        result = float(results[i][0])
    except:
        result = complex(results[i][0])

    print(f'Exercicio {i + 1}: Calculando a funcao: {result}\n')
