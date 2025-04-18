# Prog1.py - Predictive Parser for arithmetic expressions with detailed stack trace

parsing_table = {
    'E': {'a': ['T', 'Q'], '(': ['T', 'Q']},
    'Q': {'+': ['+', 'T', 'Q'], '-': ['-', 'T', 'Q'], ')': ['ε'], '$': ['ε']},
    'T': {'a': ['F', 'R'], '(': ['F', 'R']},
    'R': {'+': ['ε'], '-': ['ε'], '*': ['*', 'F', 'R'], '/': ['/', 'F', 'R'], ')': ['ε'], '$': ['ε']},
    'F': {'a': ['a'], '(': ['(', 'E', ')']}
}

terminals = ['a', '+', '-', '*', '/', '(', ')', '$']

def predictive_parse(input_string):
    input_string = list(input_string)
    stack = ['$', 'E']
    index = 0
    step = 1

    print(f"{'Step':<5}{'Stack':<20}{'Input':<20}{'Action'}")
    print("-" * 60)

    while len(stack) > 0:
        top = stack[-1]
        current_input = input_string[index] if index < len(input_string) else '$'
        stack_content = ''.join(stack)
        input_remaining = ''.join(input_string[index:])
        print(f"{step:<5}{stack_content:<20}{input_remaining:<20}", end='')

        if top == current_input == '$':
            print("Accepted")
            break
        elif top == current_input:
            stack.pop()
            index += 1
            print(f"Match '{top}'")
        elif top in terminals:
            print(f"Error: Unexpected terminal '{top}'")
            break
        elif current_input in parsing_table[top]:
            production = parsing_table[top][current_input]
            stack.pop()
            if production != ['ε']:
                for symbol in reversed(production):
                    stack.append(symbol)
            print(f"{top} -> {' '.join(production)}")
        else:
            print(f"Error: No rule for {top} with lookahead '{current_input}'")
            break
        step += 1

# === Run with user input ===
if __name__ == "__main__":
    user_input = input("Enter input string (end with $): ").strip()
    if not user_input.endswith('$'):
        print("Error: Input must end with '$'")
    else:
        predictive_parse(user_input)
