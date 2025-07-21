import re
from collections import defaultdict

def parse_polynomial(poly):
    # Find all terms using regex, e.g., ['2x^2', '+4']
    terms = re.findall(r'[+-]?\d*x(?:\^\d+)?|[+-]?\d+', poly)
    parsed = []
    for term in terms:
        if 'x' in term:
            if '^' in term:
                coeff, power = term.split('x^')
                power = int(power)
            else:
                coeff = term[:-1]
                power = 1
            if coeff in ('', '+'):
                coeff = 1
            elif coeff == '-':
                coeff = -1
            else:
                coeff = int(coeff)
        else:
            coeff = int(term)
            power = 0
        parsed.append((power, coeff))
    return parsed

def simplify_polynomial_expression(expression):
    # Remove outer parentheses and split into two polynomials
    match = re.fullmatch(r'\(([^()]+)\)\(([^()]+)\)', expression)
    if not match:
        raise ValueError("Invalid format. Must be like '(poly1)(poly2)'")
    poly1, poly2 = match.groups()

    terms1 = parse_polynomial(poly1)
    terms2 = parse_polynomial(poly2)

    result_terms = defaultdict(int)

    # Multiply each term from poly1 by each from poly2
    for p1, c1 in terms1:
        for p2, c2 in terms2:
            result_terms[p1 + p2] += c1 * c2

    # Sort terms by descending degree and format output
    result = ''
    for power in sorted(result_terms.keys(), reverse=True):
        coeff = result_terms[power]
        if coeff == 0:
            continue
        sign = '+' if coeff > 0 and result else ''
        abs_coeff = abs(coeff)

        if power == 0:
            term = f'{coeff}'
        elif power == 1:
            term = f'{coeff}x' if abs_coeff != 1 else f'{sign}x' if coeff > 0 else f'-x'
        else:
            term = f'{coeff}x^{power}' if abs_coeff != 1 else f'{sign}x^{power}' if coeff > 0 else f'-x^{power}'
        if abs_coeff == 1 and power != 0:
            if coeff > 0:
                term = f'{sign}x' if power == 1 else f'{sign}x^{power}'
            else:
                term = f'-x' if power == 1 else f'-x^{power}'
        else:
            term = f'{sign}{abs_coeff}x^{power}' if power > 1 else (
                f'{sign}{abs_coeff}x' if power == 1 else f'{sign}{abs_coeff}'
            ) if coeff != 0 else ''
        result += term

    return result

# Example usage
print(simplify_polynomial_expression("(2x^2+4)(6x^3+3)"))
# Output: 12x^5+24x^3+6x^2+12
