def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_line = []
    second_line = []
    dashes_line = []
    answers_line = []

    for problem in problems:
        parts = problem.split()
        
        if parts[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        if not parts[0].isdigit() or not parts[2].isdigit():
            return "Error: Numbers must only contain digits."
        
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        operand1 = parts[0]
        operand2 = parts[2]
        operator = parts[1]
        
        if operator == '+':
            answer = str(int(operand1) + int(operand2))
        elif operator == '-':
            answer = str(int(operand1) - int(operand2))

        width = max(len(operand1), len(operand2)) + 2
        
        first_line.append(operand1.rjust(width))
        second_line.append(operator + operand2.rjust(width - 1))
        dashes_line.append('-' * width)
        answers_line.append(answer.rjust(width))

    arranged_problems = '    '.join(first_line) + '\n' + '    '.join(second_line) + '\n' + '    '.join(dashes_line)
    if display_answers:
        arranged_problems += '\n' + '    '.join(answers_line)
    
    return arranged_problems

    arithmetic_arranger(["3801 - 2", "123 + 49"])
    arithmetic_arranger(["1 + 2", "1 - 9380"])
    arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
    arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])
    arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])
    arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])
    arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])
    arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])
    arithmetic_arranger(["3 + 855", "988 + 40"], True)
    arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)