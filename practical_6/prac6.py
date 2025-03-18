class RecursiveDescentParser:
    def __init__(self, input_str):
        self.input = input_str
        self.i = 0  # Index for parsing the input string

    def S(self):
        if self.i < len(self.input) and self.input[self.i] == 'a':
            self.i += 1  # Consume 'a'
            return True
        elif self.i < len(self.input) and self.input[self.i] == '(':
            self.i += 1  # Consume '('
            if self.L():
                if self.i < len(self.input) and self.input[self.i] == ')':
                    self.i += 1  # Consume ')'
                    return True
        return False

    def L(self):
        if self.S():
            return self.LPrime()
        return False

    def LPrime(self):
        if self.i < len(self.input) and self.input[self.i] == ',':
            self.i += 1  # Consume ','
            if self.S():
                return self.LPrime()
            else:
                return False
        return True  # Epsilon (ε) transition

    def validate(self):
        self.i = 0  # Reset index
        if self.S() and self.i == len(self.input):
            print("Valid string")
        else:
            print("Invalid string")


if __name__ == "__main__":
    test_cases = [
        "a", "(a)", "(a,a)", "(a,(a,a),a)", "(a,a),(a,a)", "a)", "(a", "a,a", "a,", "(a,a),a"
    ]

    for test in test_cases:
        print(f"ip: {test} -> ", end="")
        parser = RecursiveDescentParser(test)
        parser.validate()
