def main():
    book_path = "book/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_frequencies = count_character(text)
    print_report(book_path, num_words, char_frequencies)


def get_book_text(book_path):
    """
    Reads and returns the contents of the file at the given path.
    """
    with open(book_path) as f:
        return f.read()


def count_words(text):
    """
    Counts and returns the number of words in the given text.
    """
    words = text.split()
    return len(words)


def count_character(text):
    """
    Takes a string and returns a dictionary with the number of times 
    each character appears in the string.
    """
    frequencies = {}
    for char in text:
        if (char.isalnum() or char.isspace()) and char.isalpha():  # Count only alphanumeric and spaces
            char = char.lower()  # Normalize to lowercase
            frequencies[char] = frequencies.get(char, 0) + 1
    return frequencies


def print_report(file_path, words_count, dict_frequency):
    """
    Prints a formatted report to the console.
    """
    print(f"\n--- Begin report of {file_path} ---\n")
    
    # Word Analysis
    print(f"{words_count} words found in the document\n")
    
    # Character Analysis
    sorted_char_list = [{'character': char, 'count': count} for char, count in sorted(dict_frequency.items(), key=lambda x: x[1], reverse=True)]
    for entry in sorted_char_list:
        print(f"The '{entry['character']}' character was found {entry['count']} times")
    
    print("\n--- End report ---")

        






main()