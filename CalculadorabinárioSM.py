def binario_para_decimal(binario):
    sinal = int(binario[0])
    magnitude = binario[1:]

    decimal = 0
    for i in range(31):
        if magnitude[i] == "1":
            decimal += 2 ** (30 - i)

    if sinal == 1:
        decimal = -decimal
    print(decimal)


def soma1(bin1, bin2):
    emprestimo = 0
    final = []
    for i in range(31, -1, -1):
        digito1 = int(bin1[i])
        digito2 = int(bin2[i])

        soma = digito1 + digito2 + emprestimo
        if soma == 2:
            emprestimo = 1
            final.insert(0, '0')
        elif soma == 3:
            emprestimo = 1
            final.insert(0, '1')
        elif soma == 1:
            emprestimo = 0
            final.insert(0, '1')
        else:
            emprestimo = 0
            final.insert(0, '0')

    return ''.join(final)


def soma2(bin1, bin2):
    emprestimo = 0
    final = []
    for i in range(31, -1, -1):
        digito1 = int(bin1[i])
        digito2 = int(bin2[i])

        soma = digito1 + digito2 + emprestimo
        if soma == 2:
            emprestimo = 1
            final.insert(0, '0')
        elif soma == 3:
            emprestimo = 1
            final.insert(0, '1')
        elif soma == 1:
            emprestimo = 0
            final.insert(0, '1')
        else:
            emprestimo = 0
            final.insert(0, '0')
    final.pop(0)
    if bin1[0] == '0':
        final.insert(0, '0')
    else:
        final.insert(0, '1')

    return ''.join(final)


def subtração1(bin1, bin2):
    emprestimo = 0
    final2 = []
    if int(bin1[1:], 2) > int(bin2[1:], 2):
        for i in range(31, -1, -1):
            bit1 = int(bin1[i])
            bit2 = int(bin2[i])
            diff = bit1 - bit2 - emprestimo
            if diff == 0:
                final2.insert(0, '0')
                emprestimo = 0
            elif diff == 1:
                final2.insert(0, '1')
                emprestimo = 0
            elif diff == -1:
                final2.insert(0, '1')
                emprestimo = 1
            else:
                final2.insert(0, '0')
                emprestimo = 1
        final2.pop(0)
        if bin1[0] == '0':
            final2.insert(0, '0')
        if bin1[0] == '1':
            final2.insert(0, '1')
        return ''.join(final2)

    else:
        for i in range(31, -1, -1):
            bit1 = int(bin2[i])
            bit2 = int(bin1[i])
            diff = bit1 - bit2 - emprestimo
            if diff == 0:
                final2.insert(0, '0')
                emprestimo = 0
            elif diff == 1:
                final2.insert(0, '1')
                emprestimo = 0
            elif diff == -1:
                final2.insert(0, '1')
                emprestimo = 1
            else:
                final2.insert(0, '0')
                emprestimo = 1
        final2.pop(0)
        if bin2[0] == '0':
            final2.insert(0, '0')
        if bin2[0] == '1':
            final2.insert(0, '1')
        return ''.join(final2)


def subtração2(bin1, bin2):
    emprestimo = 0
    final2 = []
    if int(bin1[1:], 2) > int(bin2[1:], 2):
        for i in range(31, -1, -1):
            bit1 = int(bin1[i])
            bit2 = int(bin2[i])
            diff = bit1 - bit2 - emprestimo
            if diff == 0:
                final2.insert(0, '0')
                emprestimo = 0
            elif diff == 1:
                final2.insert(0, '1')
                emprestimo = 0
            elif diff == -1:
                final2.insert(0, '1')
                emprestimo = 1
            else:
                final2.insert(0, '0')
                emprestimo = 1
        final2.pop(0)
        if bin1[0] == '0':
            final2.insert(0, '0')
        if bin1[0] == '1':
            final2.insert(0, '1')
        return ''.join(final2)

    else:
        for i in range(31, -1, -1):
            bit1 = int(bin2[i])
            bit2 = int(bin1[i])
            diff = bit1 - bit2 - emprestimo
            if diff == 0:
                final2.insert(0, '0')
                emprestimo = 0
            elif diff == 1:
                final2.insert(0, '1')
                emprestimo = 0
            elif diff == -1:
                final2.insert(0, '1')
                emprestimo = 1
            else:
                final2.insert(0, '0')
                emprestimo = 1
        final2.pop(0)
        if bin2[0] == '0':
            final2.insert(0, '1')
        if bin2[0] == '1':
            final2.insert(0, '0')
        return ''.join(final2)


x = input('Digite X: ')
y = input('Digite Y: ')


def OPERADOR_SOMA(x, y):
    if x[0] == '0' and y[0] == '0':
        return soma1(x, y)
    if x[0] == '1' and y[0] == '1':
        return soma2(x, y)
    if x[0] == '1' and y[0] == '0':
        return subtração1(x, y)
    if x[0] == '0' and y[0] == '1':
        return subtração1(x, y)


def OPERADOR_SUBTRAÇÃO(x, y):
    if x[0] == '0' and y[0] == '0' and int(y[1:]) > int(x[1:]):
        return subtração2(x, y)
    if x[0] == '0' and y[0] == '0' and int(y[1:]) < int(x[1:]):
        return subtração1(x, y)
    if x[0] == '1' and y[0] == '1' and int(y[1:]) > int(x[1:]):
        return subtração2(x, y)
    if x[0] == '1' and y[0] == '1' and int(y[1:]) < int(x[1:]):
        return subtração1(x, y)
    if x[0] == '0' and y[0] == '1':
        return soma2(x, y)
    if x[0] == '1' and y[0] == '0':
        return soma2(x, y)


xfinal = OPERADOR_SOMA(x, y)
yfinal = OPERADOR_SUBTRAÇÃO(x, y)

print('')
binario_para_decimal(x)
binario_para_decimal(y)
print('--------')
print(OPERADOR_SOMA(x, y))
print(OPERADOR_SUBTRAÇÃO(x, y))
print('--------')
binario_para_decimal(xfinal)
binario_para_decimal(yfinal)
print('')