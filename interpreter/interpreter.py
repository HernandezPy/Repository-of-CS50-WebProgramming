def interpreter_expression(expression):

        x, y, z = expression.split()

        x = int(x)
        z = int(z)

        if y == '+':
            result = x + z
        elif y == '-':
            result = x - z
        elif y == '*':
            result = x * z
        elif y == '/':
            result = x / z
        else:
            return 'Error: Invalid operator.'
        return f'{result:.1f}'





def main():
        expression = input('Expression: ').strip()
        result = interpreter_expression(expression)
        print(result)


if __name__ == '__main__':
 main()
