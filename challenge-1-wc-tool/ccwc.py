import argparse
import sys
import locale

def count_bytes_in_text(text):
    byte_count = len(text.encode('utf-8'))
    return byte_count

def count_words_in_text(text):
    word_count = len(text.split())
    return word_count

def count_lines_in_text(text):
    line_count = len(text.splitlines())
    return line_count

def count_characters_in_text(text):
    # Counting characters in a multibyte-aware way
    try:
        char_count = len(text.encode(locale.getpreferredencoding()))
    except UnicodeEncodeError:
        # Handle the case where encoding fails
        char_count = len(text)
    return char_count

def parse_arguments():
    parser = argparse.ArgumentParser(description='Count bytes, words, lines, and characters in a text file or from standard input.')
    parser.add_argument('-w', action='store_true', help='Count words instead of bytes.')
    parser.add_argument('-l', action='store_true', help='Count lines instead of bytes.')
    parser.add_argument('-m', action='store_true', help='Count characters instead of bytes (multibyte-aware).')
    parser.add_argument('file', metavar='FILE', type=str, nargs='?', help='Specify the path to the text file. If not provided, read from standard input.')
    return parser.parse_args()

def execute_counting(args):
    file_path = args.file

    # Define a dictionary to map options to functions
    option_functions = {
        'w': count_words_in_text,
        'l': count_lines_in_text,
        'm': count_characters_in_text,
        'c': count_bytes_in_text
    }

    # Check if the user provided any specific options
    selected_options = [option for option in option_functions if hasattr(args, option) and getattr(args, option)]

    if not selected_options:
        # If no specific options provided, count all options
        selected_options = list(option_functions.keys())

    if file_path:
        # If a file is provided, read from the file
        with open(file_path, 'r') as file:
            text = file.read()
    else:
        # If no file is provided, read from standard input
        text = sys.stdin.read()

    # Iterate through selected options and call the corresponding function
    for option in selected_options:
        count_function = option_functions.get(option)
        count = count_function(text)
        option_name = {
            'w': 'words',
            'l': 'lines',
            'm': 'characters',
            'c': 'bytes'
        }[option]
        print(f"Number of {option_name} in input: {count}")

def main():
    args = parse_arguments()
    execute_counting(args)

if __name__ == '__main__':
    main()
