import math
import argparse 

def main(number):
    print("Hello World!")
    print(f"The square root of {number} is:", math.sqrt(number))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number", type=int, help="Number to calculate the square root of.")
    args = parser.parse_args()
    main(number=args.number)
