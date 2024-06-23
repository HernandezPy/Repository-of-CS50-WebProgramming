def interpreter_expression(expression):
     try:

        x, y, z = expression.split()

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

    except ValueError:
        return "Error: Invalid input. Ensure the input is  formatted as 'x y z' where x and z are integers and y an operator (+,-,*,/)."
    except ZeroDivisionError:
        return 'Error: Division with zero is not allowed.'



def main():
        expression = input('Expression: ').strip()
        result = interpreter_expression(expression)
        print(result)


if __name__ == '__main__':
 main()
