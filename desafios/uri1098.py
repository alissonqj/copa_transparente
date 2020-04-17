def desafio():
    for i in range(11):
        for j in range(1, 4):
            x = i * 0.2
            y = j + x
            x_eh_inteiro = x % 1 == 0
            y_eh_inteiro = y % 1 == 0
            if x_eh_inteiro:
                i_string = "I={}".format(int(x))
            else:
                i_string = "I={:.1f}".format(x)

            if y_eh_inteiro:
                j_string = " J={}".format(int(y))
            else:
                j_string = " J={:.1f}".format(y)

            print(i_string + j_string)
