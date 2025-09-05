def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def num_of_words(s):
    words = s.split()
    return len(words)

def count_characters(s):
    lower = s.lower()
    output = {}
    for char in lower:
        if char.isalpha():
            output[char] = output.get(char, 0) + 1
    return output

def sort_on(item):
    return item["num"]

def chars_dict_to_sorted_list(char_dict):
    # Convert dictionary to list of dicts
    sorted_list = [{"char": char, "num": num} for char, num in char_dict.items()]
    # Sort from greatest to least
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
