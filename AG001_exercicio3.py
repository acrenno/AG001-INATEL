import sympy

# CALCULANDO A VARIAVEL C
MATRICULA = 250

C = MATRICULA % 10


def function(x, C):

    return ((1/5)*(x**2))+(x**(4/5))+((C+3)*x)-10


def calculate_integral(function, variable, limits=None):


    # calculando resultados
    results = []

    # limites passados
    if limits:
        integral = sympy.Integral(function, (variable, limits['min'], limits['max']))

    else:
        integral = sympy.Integral(function, variable)

    # CALCULANDO INTEGRAL
    result = integral.doit()

    # RETORNANDO O RESULTADO
    return result


# DEFININDO A FUNCAO VARIAVEL
VARIABLE = sympy.Symbol('x')

# CHAMANDO A FUNCAO
FUNCTION = function(VARIABLE, C)

# SETANDO OS LIMITES
limits = {'min': 1, 'max': 12}

# CHAMANDO A FUNCAO
result = calculate_integral(FUNCTION, VARIABLE, limits)

# SAINDO COM OS RESULTADOS
print(f'Exercicio {1}: Calculando a integral da funcao: {result}\n')

# In[ ]:



