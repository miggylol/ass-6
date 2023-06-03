def calculate_pi(iterations):
    pi = 0
    sign = 1

    for i in range(1, iterations * 2, 2):
        term = 4 / i * sign
        pi += term
        sign *= -1

    return pi


def main():
    iterations = 1

    while True:
        print(f"Current value of PI: {calculate_pi(iterations):.3f}")
        choice = input("Enter the number of iterations (q to quit): ")

        if choice.lower() == 'q':
            break

        try:
            iterations = int(choice)
            if iterations <= 0:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    print("Program terminated.")


if __name__ == '__main__':
    main()

