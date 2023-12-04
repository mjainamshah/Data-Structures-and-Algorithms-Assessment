def is_balanced(expression):
    # Stack to keep track of the opening brackets
    stack = []
    # Mapping of the closing to opening brackets
    brackets_map = {')': '(', '}': '{', ']': '['}

    # To iterate through each character in the expression
    for char in expression:
        if char in '({[':
            # Push opening brackets onto the stack
            stack.append(char)
        elif char in ')}]':
            # Check for closing brackets & their corresponding opening brackets
            if not stack or stack[-1] != brackets_map[char]:
                return False
            stack.pop()  # Removes the corresponding opening bracket
    
    # The expression is balanced if the stack is empty
    return len(stack) == 0

# SAMPLE INPUT
expression1 = "([]{})"
expression2 = "([)]"

# SAMPLE TEST CASE:
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False
