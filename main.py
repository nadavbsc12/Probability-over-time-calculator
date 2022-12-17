def probability_calculator(probability, iterations):
  # Convert iterations to an integer
  iterations = int(iterations)

  # Convert the probability to a decimal value
  probability = probability / 100
  for i in range(iterations):
    result = probability**(i+1)
    print("Iteration {}: {:.100f}".format(i+1, result * 100))
    result = result * 100
  return result

# Get input from the user
probability = float(input("Enter probability numerator(Out Of 100): "))
iterations = float(input("Enter the number of iterations: "))

# Test the probability calculator
print("Final Result: {:.100f}".format(probability_calculator(probability, iterations)))
