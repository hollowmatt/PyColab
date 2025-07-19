import sys
import num2text
    
def main():
    print("Number to word converter, 1 to 100")
    if len(sys.argv) != 2:
        print("Usage: python script.py <number>")
        sys.exit(1)
    
    try:
        number = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer.")
        sys.exit(1)
    
    word = num2text.num2word(number)
    print(f"The number {number} in words is: {word}")

if __name__ == "__main__":
    print(__name__)
    main()