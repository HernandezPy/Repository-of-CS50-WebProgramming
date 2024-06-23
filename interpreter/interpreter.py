def interpreter_expression(expression):

        x, y, z, = expression.split()

        x = int(x)
        y = int(y)

        if y == '+':
            return x + z
        elif y == '-':
            return x - z
        elif y == '*':
            return x * z
        elif y == '/':
            return x / z
        else:
            return 'Error: Invalid operator.'
        return f'{result:.1f}'





def main():
        expression = input('Expression: ').strip()
        result = interpreter_expression(expression)
        print(result)


if __name__ == '__main__':
 main()
