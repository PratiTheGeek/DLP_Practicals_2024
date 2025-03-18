from collections import defaultdict

grammar = {
    "S": ["A B C", "D"],
    "A": ["a", "ε"],
    "B": ["b", "ε"],
    "C": ["( S )", "c"],
    "D": ["A C"]
}

first_sets = {}
follow_sets = {}

def compute_first(symbol):
    if symbol in first_sets:
        return first_sets[symbol]
    
    first = set()
    if symbol not in grammar:
        first.add(symbol)
        return first
    
    for production in grammar[symbol]:
        tokens = production.split()
        for token in tokens:
            token_first = compute_first(token)
            first.update(token_first - {"ε"})
            if "ε" not in token_first:
                break
        else:
            first.add("ε")
    
    first_sets[symbol] = first
    return first

def compute_follow(symbol):
    if symbol in follow_sets:
        return follow_sets[symbol]
    
    follow = set()
    if symbol == "S":
        follow.add("$")
    
    for lhs, productions in grammar.items():
        for production in productions:
            tokens = production.split()
            for i, token in enumerate(tokens):
                if token == symbol:
                    next_index = i + 1
                    while next_index < len(tokens):
                        next_first = compute_first(tokens[next_index])
                        follow.update(next_first - {"ε"})
                        if "ε" not in next_first:
                            break
                        next_index += 1
                    if next_index == len(tokens) and lhs != symbol:
                        follow.update(compute_follow(lhs))
    
    follow_sets[symbol] = follow
    return follow

def main():
    for non_terminal in grammar:
        compute_first(non_terminal)
    for non_terminal in grammar:
        compute_follow(non_terminal)
    
    print("First Sets:")
    for nt, first in first_sets.items():
        print(f"First({nt}) = {first}")
    
    print("\nFollow Sets:")
    for nt, follow in follow_sets.items():
        print(f"Follow({nt}) = {follow}")

if __name__ == "__main__":
    main()