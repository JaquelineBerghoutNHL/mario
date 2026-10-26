def generate_pyramid(n):
    return "\n".join(" " * (n - i) + "#" * i for i in range (1, n + 1))

def main():
    ask = int(input("height? "))
    print(generate_pyramid(ask))

if __name__ == "__main__":
    print("Better mario! it's better because I say so.")
    main()    
