def calculate_pi(accuracy = 100):
    print(f"Using the Gregory Leibniz Theory ({ accuracy } iterations)")
    result = 0
    for index in range(accuracy):
        sign = -1 if index % 2 == 1 else 1
        denominator = index * 2 + 1
        result += sign * (4 / denominator)
        # print(f"#{ index }: { result }")
    return result


if __name__ == "__main__":
    estimate = calculate_pi(accuracy=1000000)
    print(f"Estimate: { estimate }")
