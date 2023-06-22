import numpy
import matplotlib

# CALCULANDO A VARIAVEL C
MATRICULA = 250

C = MATRICULA % 10

def calculate_voltage(function_constant, C):

    # DEFININDO A FUNCAO
    return function_constant + 2 * C


def generate_matrix(dict_matrix):


    matrix = numpy.matrix([
        dict_matrix['line_1'],
        dict_matrix['line_2'],
        dict_matrix['line_3']
    ])

    return matrix


def calculate_system(dict_A, dict_B):

    # GERANDO MATRIX
    A = generate_matrix(dict_A)

    B = generate_matrix(dict_B)

    # INVERTENDO A
    A_inv = numpy.linalg.inv(A)

    # MULTIPLICANDO A E B
    X = A_inv * B

    # RETORNANDO RESULTADO
    return X


matrix_A = {}

matrix_A['line_1'] = [1, 1, 1]
matrix_A['line_2'] = [25, -10, 0]
matrix_A['line_3'] = [0, -10, 20]

# DEFININDO MATRIX
matrix_B = {}

matrix_B['line_1'] = [0]
matrix_B['line_2'] = [calculate_voltage(7, C)]
matrix_B['line_3'] = [calculate_voltage(12, C)]


matrix_X = calculate_system(matrix_A, matrix_B)

# PRINTANDO RESULTADO
eng_format = matplotlib.ticker.EngFormatter()

for i in range(len(matrix_X)):
    current_value = eng_format(float(matrix_X[i]))

    current_value = current_value.replace('m', '[mA]')

    print(f'I{i + 1}: {current_value}\n')
