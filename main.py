def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
        char_dict = count_characters(file_contents)
        print_report(char_dict, word_count)

def count_characters(file_contents):
    count = {}
    lowered_string = file_contents.lower()
    for i in range(0, len(lowered_string), 1):
        if lowered_string[i] in count:
            count[lowered_string[i]] += 1
        else:
            count[lowered_string[i]] = 1
    return count

def print_report(char_dict, word_count):
    chars = []
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")

    for char in char_dict:
        if char.isalpha():
            temp_dict = {"char": char, "count": char_dict[char]}
            chars.append(temp_dict)
    
    chars.sort(reverse=True, key=sort_on)

    for char in chars:
        print(f"The \'{char['char']}\' character was found {char['count']} times")
    
    print("--- End report ---")

def sort_on(dict):
    return dict["count"]



main()



    