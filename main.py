def calculate_pi(accuracy = 100):
    estimate = 0
    for index in range(accuracy):
        sign = -1 if index % 2 == 1 else 1
        denominator = index * 2 + 1
        estimate += sign * (4 / denominator)
    return estimate


if __name__ == "__main__":
    print(f"Calculating Pi using Gregory Leibniz's Series.")
    precisions = [1,2,3,4,5,10,100,1000,10000,100000,1000000,5000000]
    for precision in precisions:
        estimate = calculate_pi(accuracy=precision)
        print(f"{ round(estimate, 10) } ({ precision } iterations)")
