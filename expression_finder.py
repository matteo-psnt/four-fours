import argparse
import itertools
from operations import binary_operations, unary_operations, Number

def generate_combinations(numbers):
    if len(numbers) == 1:
        return [[numbers[0]]]
    
    rest_combinations = generate_combinations(numbers[1:])
    
    combinations = [[numbers[0]] + combo for combo in rest_combinations]

    for i, combo in enumerate(rest_combinations):
        if isinstance(combo[0], int):
            new_combo = [int(str(numbers[0]) + str(combo[0]))] + combo[1:]
            if new_combo not in combinations:
                combinations.append(new_combo)
    
    return combinations

def generate_all_combinations(numbers):
    unique_permutations = set(itertools.permutations(numbers))
    all_combinations = []
    
    for perm in unique_permutations:
        all_combinations.extend(generate_combinations(list(perm)))
    
    unique_combinations = set(tuple(combo) for combo in all_combinations)
    
    return [list(combo) for combo in unique_combinations]

def generate_expressions(numbers):
    if len(numbers) == 1:
        yield Number(numbers[0])
        for unary_op in unary_operations:
            yield unary_op(Number(numbers[0]))
    else:
        for i in range(1, len(numbers)):
            left_numbers, right_numbers = numbers[:i], numbers[i:]            
            for left_expr in generate_expressions(left_numbers):
                for right_expr in generate_expressions(right_numbers):
                    for binary_op in binary_operations:
                        yield binary_op(left_expr, right_expr)
                        for unary_op in unary_operations:
                            yield unary_op(binary_op(left_expr, right_expr))

def generate_expression_dict(numbers, min_value, max_value, show_all):
        expressions = set()
        for permutation in generate_all_combinations(numbers):
            expressions.update(generate_expressions(permutation))
        
        expression_dict = {result: None for result in range(min_value, max_value + 1)} if show_all else {}
        for expr in expressions:
            try:
                result = expr.evaluate()
                if min_value <= result <= max_value and result == int(result):
                    if expression_dict.get(result) is None or len(str(expr)) < len(expression_dict[result]):
                        expression_dict[result] = str(expr)
            except (ZeroDivisionError, ValueError, OverflowError):
                continue

        return expression_dict

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate expressions that evaluate to all possible results from a list of numbers.")
    parser.add_argument('numbers', metavar='N', type=int, nargs='+',
                        help='An integer for the list to generate expressions from')
    parser.add_argument('--min', dest='min_value', type=int, default=1,
                        help='Minimum value of results to show (default: 1)')
    parser.add_argument('--max', dest='max_value', type=int, default=100,
                        help='Maximum value of results to show (default: 100)')
    parser.add_argument('--show-all', action='store_true',
                        help='Show all numbers within the range, including those without a solution')

    args = parser.parse_args()
    expression_dict = generate_expression_dict(args.numbers, args.min_value, args.max_value, args.show_all)
    for result in sorted(expression_dict.keys()):
        expr = expression_dict[result]
        if expr:
            print(f'{result} = {expr}')
        elif args.show_all:
            print(f'{result}')