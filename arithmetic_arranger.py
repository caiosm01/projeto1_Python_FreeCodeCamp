def arithmetic_arranger(problems, solution=False):
  equations = []
  list_1 = []
  list_2 = []
  list_3 = []
  list_4 = []
  index = 0

  if len(problems) > 5:
    return "Error: Too many problems."
  
  for operation in problems:
    if '+' in operation:
      first = operation[:operation.find('+')].strip()
      second = operation[operation.find('+')+1:].strip()
      if first.isdigit() == False or second.isdigit() == False:
        return "Error: Numbers must only contain digits."
      sum = int(first) + int(second)
      equation = [first, '+', second, str(sum)]
      equations.append(equation)

    elif '-' in operation:
      first = operation[:operation.find('-')].strip()
      second = operation[operation.find('-') + 1:].strip()
      if first.isdigit() == False or second.isdigit() == False:
        return "Error: Numbers must only contain digits."
      sub = int(first) - int(second)
      equation = [first, '-', second, str(sub)]
      equations.append(equation)

    else:
      return "Error: Operator must be '+' or '-'."

  for eq in equations:
    if len(eq[0]) > 4 or len(eq[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

  for eq in equations:
    dif = (len(eq[2]) - len(eq[0]))

    #for list one
    if dif > 0:
      for num in range(dif + 2):
        list_1.append(" ")
      list_1.append(eq[0])

    else:
      list_1.append("  ")
      list_1.append(eq[0])

    if index != len(equations)-1:
      list_1.append("    ")

    #for list two
    list_2.append(eq[1])
    if dif < 0:
      for num in range(abs(dif-1)):
        list_2.append(" ")
      list_2.append(eq[2])

    else:
      list_2.append(" ")
      list_2.append(eq[2])

    if index != len(equations)-1:
      list_2.append("    ")

    #for list three
    if dif > 0:
      for line in range(len(eq[2]) + 2):
        list_3.append('-')

    else:
      for line in range(len(eq[0]) + 2):
        list_3.append('-')

    if index != len(equations)-1:
      list_3.append("    ")

    #for list four
    if dif < 0:
      dif_2 = len(eq[0]) - len(eq[3])
      if dif_2 > 0:
        for n in range(dif_2 + 2):
          list_4.append(" ")
        list_4.append(eq[3])
      else:
        if abs(dif_2) == 0:
          list_4.append("  ")
          list_4.append(eq[3])
        else:
          list_4.append(" ")
          list_4.append(eq[3])
    else:
      dif_2 = len(eq[2]) - len(eq[3])
      if dif_2 > 0:
        for n in range(dif_2 + 2):
          list_4.append(" ")
        list_4.append(eq[3])
      else:
        if abs(dif_2) == 0:
          list_4.append("  ")
          list_4.append(eq[3])
        else:
          list_4.append(" ")
          list_4.append(eq[3])

    if index != len(equations)-1:
      list_4.append("    ")

    index += 1

  if solution == True:
    arranged_problems = ''.join(list_1) + '\n' + ''.join(list_2) + '\n' + ''.join(list_3) + '\n' + ''.join(list_4)
  else:
    arranged_problems = ''.join(list_1) + '\n' + ''.join(list_2) + '\n' + ''.join(list_3)

  return arranged_problems
  