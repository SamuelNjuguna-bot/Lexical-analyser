def lexical_analyzer(source_code):
    length = len(source_code)
    i = 0
    tokens = []

    while i < length:
        current_char = source_code[i]

        # Skip whitespace
        if current_char.isspace():
            i += 1
            continue

        # Check for operators
        if current_char == '+':
            tokens.append(("PLUS_OPERATOR", '+'))
            i += 1
        elif current_char == '-':
            tokens.append(("MINUS_OPERATOR", '-'))
            i += 1
        elif current_char == '=':
            tokens.append(("ASSIGNMENT_OPERATOR", '='))
            i += 1
        elif current_char == '>':
            tokens.append(("GREATER_THAN", '>'))
            i += 1
        elif current_char == '<':
            tokens.append(("LESS_THAN", '<'))
            i += 1
        elif current_char == ';':
            tokens.append(("SEMICOLON", ';'))
            i += 1

        # Check for identifiers (keywords or variables)
        elif current_char.isalpha():
            identifier = ""
            while i < length and (source_code[i].isalnum() or source_code[i] == '_'):  # Capture alphanumeric characters and underscore
                identifier += source_code[i]
                i += 1

            # Recognize keywords
            if identifier == "if":
                tokens.append(("IF_KEYWORD", identifier))
            elif identifier == "else":
                tokens.append(("ELSE_KEYWORD", identifier))
            elif identifier == "do":
                tokens.append(("DO_KEYWORD", identifier))
            elif identifier == "while":
                tokens.append(("WHILE_KEYWORD", identifier))
            elif identifier in ["int", "float", "char", "string"]:
                tokens.append(("DATATYPE", identifier))
            else:
                tokens.append(("IDENTIFIER", identifier))

        # Check for numbers (literals)
        elif current_char.isdigit():
            number = ""
            while i < length and source_code[i].isdigit():  # Capture integer numbers
                number += source_code[i]
                i += 1

            # Check if it's a floating-point literal
            if i < length and source_code[i] == '.':
                number += '.'
                i += 1
                while i < length and source_code[i].isdigit():  # Capture fractional part
                    number += source_code[i]
                    i += 1
                tokens.append(("FLOAT_LITERAL", number))
            else:
                tokens.append(("INT_LITERAL", number))

        # Handle unrecognized characters
        else:
            tokens.append(("ERROR", f"Unrecognized character '{current_char}'"))
            i += 1

    return tokens

# Sample Zara code to test
source_code = '''
int x = 5;
float y = 3.14;
if (x > y) {
    x = x + 1;
} else {
    do {
        y = y - 1.0;
    } while (y > 0);
}
'''

# Test the lexical analyzer
tokens = lexical_analyzer(source_code)
print("Lexical analysis of the source code:")
for token in tokens:
    print(token)
