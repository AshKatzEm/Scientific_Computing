def arithmetic_arranger(problems, solve=False): #The function takes an optional second argument. When set to True, the answers are displayed in the final arrangment.

    # Check the number of problems in the list
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialize a string for each component of the problems
    numerators = ""
    denominators = ""
    equalsLines = ""
    results = ""


    # Iterate through the problems
    for problem in problems:
        # Check that the problem only contains digits or the + or - operators
        if problem.replace(" ", "").isdigit():
            if '/' in problem or '*' in problem:
                return "Error: Operator must be '+' or '-'."
            else:
                return "Error: Numbers must only contain digits."

        # Split the problem up and save the two numbers and the operator
        first_number = problem.split()[0]
        operator = problem.split()[1]
        second_number = problem.split()[2]

        # Check that each number does not have more than four digits
        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Define problem_width as the widest of the numbers plus the operator plus a space
        problem_width = max(len(first_number), len(second_number)) + 2
        solution = ""
        equalsLine = ""
        # Justify the numbers to the right according to the problem_width
        numerator= str(first_number).rjust(problem_width)
        denominator = operator + str(second_number).rjust(problem_width - 1)
        # Calculate the solution of each problem
        if operator == "+":
            solution = int(first_number) + int(second_number)
        elif operator == "-":
            solution = int(first_number) - int(second_number)
        result = str(solution).rjust(problem_width)
      # equalsLine is proportional to problem_width
        for i in range(problem_width):
            equalsLine += "-"

        # If the problem is not the last one in the list, append the formatted parts of the problem and 4 spaces for the next problem
        if problem != problems[-1]:
            numerators += numerator+ "    "
            denominators += denominator + "    "
            equalsLines += equalsLine + "    "
            results += result + "    "
        # If it is, don't add the 4 spaces
        else:
            numerators += numerator
            denominators += denominator
            equalsLines += equalsLine
            results += result

    # Arrange the lines with newlines to separate each string.
    if solve is True:
        arranged = numerators + "\n" + denominators + "\n" + equalsLines + "\n" + results
    else:
        arranged = numerators + "\n" + denominators + "\n" + equalsLines
    return arranged
