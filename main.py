from stats import num_of_words, get_book_text, count_characters, chars_dict_to_sorted_list

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    text = get_book_text("books/frankenstein.txt")

    print("----------- Word Count ----------")
    total_words = num_of_words(text)
    print(f"Found {total_words} total words")

    print("--------- Character Count -------")
    char_dict = count_characters(text)
    sorted_chars = chars_dict_to_sorted_list(char_dict)

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
