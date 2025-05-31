def count_text_elements(text_input):
  char_count = len(text_input)
  word_count = len(text_input.split())
  line_count = len(text_input.splitlines())

  print(f"Characters: {char_count}")
  print(f"Words: {word_count}")
  print(f"Lines: {line_count}")

user_text = input("Enter your text:\n")

print("\n--- Analysis ---")
count_text_elements(user_text)
