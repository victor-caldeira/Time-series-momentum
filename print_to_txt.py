import sys

def print_to_txt(message, file):
    print(message)

    original_stdout = sys.stdout # Save a reference to the original standard output

    with open(file, 'a') as f:
        sys.stdout = f # Change the standard output to the file we created.
        print(message)
        sys.stdout = original_stdout # Reset the standard output to its original value
    
    f.close()