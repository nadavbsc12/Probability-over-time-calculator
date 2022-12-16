def probability_calculator(probability, total, iterations):
  # Convert iterations to an integer
  iterations = int(iterations)

  # Convert the probability to a decimal value
  probability = probability / total

  print("Iteration 0: {}".format(probability))
  for i in range(iterations):
    probability = probability * (1 - probability)
    print("Iteration {}: {}".format(i+1, probability))
  return probability

# Get input from the user
probability = float(input("Enter probability numerator(Out Of 100): "))
total = 100 # float(input("Enter probability denominator: "))
iterations = float(input("Enter the number of iterations: "))

# Test the probability calculator
print("Final Result:", probability_calculator(probability, total, iterations))