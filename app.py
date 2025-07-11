def add(a, b):
    return a + b

def sub(a, b):
    return a - b

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 4:
        print("Usage: python app.py <add|sub> num1 num2")
        sys.exit(1)

    op, x, y = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    if op == 'add':
        print(add(x, y))
    elif op == 'sub':
        print(sub(x, y))
    else:
        print(f"Unknown operation '{op}'")
        sys.exit(1)

