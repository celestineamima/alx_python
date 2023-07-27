import sys

def print_arguments():
    num_arguments = len(sys.argv) - 1
    arguments_list = sys.argv[1:]

    print(f"Number of arguments: {num_arguments}")
    print("List of arguments:")
    for idx, arg in enumerate(arguments_list, 1):
        print(f"{idx}. {arg}")

if __name__ == "__main__":
    print_arguments()
