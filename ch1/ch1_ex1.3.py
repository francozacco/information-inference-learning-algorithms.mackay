

def compute_p_B(N, f):
    return (2**N) * ( ( f * (1 - f) )**(N/2) )


def main():
    f = 0.1
    for N in range(1, 100):
        p_B = compute_p_B(N, f)
        if p_B <= 10e-15:
            break
    print(f"Repetitions needed: {N}")


if __name__ == "__main__":
    main()

