
def main():
  for b in range(1001):
    for a in range(1000):
      for n in range(1000):
        quadratic_expression = n**2 + a*n + b

        print(quadratic_expression)

if __name__ == "__main__":
  main()