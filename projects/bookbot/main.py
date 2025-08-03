from stats import *
import sys

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def main():

  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  file_path = sys.argv[1]
  
  text = get_book_text(file_path)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {file_path}...")

  # Word count section
  word_count = get_num_words(text)
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")

  # Character count section
  print("--------- Character Count -------")
  char_counts = get_char_count(text)
  sorted_chars = sort_char_count(char_counts)

  for char, count in sorted_chars:
    print(f"{char}: {count}")

  print("============= END ===============")

main()