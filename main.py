import re

class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


PRECEDENCE = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "u+": 3,
    "u-": 3
}

RIGHT_ASSOCIATIVE = {"u+", "u-"}


def tokenize(expression):

    pattern = r"\d+(?:\.\d*)?|\.\d+|[()+\-*/]"

    tokens = re.findall(pattern, expression)

    remaining = re.sub(pattern, "", expression)

    if remaining.strip():
        raise ValueError(
            f"Invalid character(s): {remaining.strip()}"
        )

    if not tokens:
        raise ValueError("Expression is empty")

    return tokens



def infix_to_postfix(expression):

    tokens = tokenize(expression)

    output = []
    operators = Stack()
    previous = None

    for token in tokens:

        if re.fullmatch(r"\d+(?:\.\d*)?|\.\d+", token):

            if previous in ("number", ")"):
                raise ValueError("Missing operator")

            output.append(token)
            previous = "number"

        elif token == "(":

            if previous in ("number", ")"):
                raise ValueError(
                    "Missing operator before '('"
                )

            operators.push(token)
            previous = "("

        elif token == ")":

            if previous in (None, "operator", "("):
                raise ValueError(
                    "Invalid or empty parentheses"
                )

            while (
                not operators.is_empty()
                and operators.peek() != "("
            ):
                output.append(operators.pop())

            if operators.is_empty():
                raise ValueError("Mismatched parentheses")

            operators.pop()

            previous = ")"

        else:

      
            if token in ("+", "-") and previous in (
                None, "operator", "("
            ):

                operator = "u+" if token == "+" else "u-"

            else:

                operator = token

                if previous in (
                    None, "operator", "("
                ):
                    raise ValueError(
                        f"Operator '{token}' is missing "
                        "an operand"
                    )

            while not operators.is_empty():

                top = operators.peek()

                if top == "(":
                    break

                should_pop = (
                    PRECEDENCE[top] > PRECEDENCE[operator]
                    or (
                        PRECEDENCE[top] == PRECEDENCE[operator]
                        and operator not in RIGHT_ASSOCIATIVE
                    )
                )

                if should_pop:
                    output.append(operators.pop())
                else:
                    break

            operators.push(operator)

            previous = "operator"

   
    if previous in (None, "operator", "("):
        raise ValueError("Incomplete expression")

    while not operators.is_empty():

        operator = operators.pop()

        if operator == "(":
            raise ValueError("Mismatched parentheses")

        output.append(operator)

    return output



def evaluate_postfix(postfix):

    values = Stack()

    for token in postfix:

    
        if re.fullmatch(r"\d+(?:\.\d*)?|\.\d+", token):

            if "." in token:
                values.push(float(token))
            else:
                values.push(int(token))

    
        elif token in ("u+", "u-"):

            if values.size() < 1:
                raise ValueError("Missing operand")

            number = values.pop()

            if token == "u-":
                values.push(-number)
            else:
                values.push(number)

        
        else:

            if values.size() < 2:
                raise ValueError("Missing operand")

            right = values.pop()
            left = values.pop()

            if token == "+":
                result = left + right

            elif token == "-":
                result = left - right

            elif token == "*":
                result = left * right

            elif token == "/":

                if right == 0:
                    raise ValueError("Division by zero")

                result = left / right

            else:
                raise ValueError(
                    f"Unsupported operator: {token}"
                )

            values.push(result)

    if values.size() != 1:
        raise ValueError("Invalid mathematical expression")

    return values.pop()


def evaluate_expression(expression):

    postfix = infix_to_postfix(expression)

    return evaluate_postfix(postfix)



def format_result(result):

    if isinstance(result, float) and result.is_integer():
        return str(int(result))

    return str(result)


def process_files():

    try:

        with open(
            "input.txt", "r", encoding="utf-8"
        ) as input_file:

            lines = input_file.readlines()

        results = []

       
        for line_number, line in enumerate(
            lines, start=1
        ):

            expression = line.strip()

          
            if not expression:
                results.append("")
                continue

        
            if re.fullmatch(r"-+", expression):
                results.append(expression)
                continue

           
            try:

                result = evaluate_expression(expression)

                results.append(format_result(result))

            except (ValueError, ZeroDivisionError) as error:

                results.append(
                    f"ERROR on line {line_number}: {error}"
                )

       
        with open(
            "output.txt", "w", encoding="utf-8"
        ) as output_file:

            output_file.write(
                "\n".join(results) + "\n"
            )

        print("Program executed successfully!")
        print("Results have been saved to output.txt.")

    except FileNotFoundError:

        print(
            "Error: input.txt was not found. "
            "Place it in the same folder as main.py."
        )



if __name__ == "__main__":
    process_files()