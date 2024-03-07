def is_palindrome(word):
    cleaned_word = word.lower()
    return cleaned_word == cleaned_word[::-1]

# Example usage:
word_to_check = input("enter a word and lemme check if it is a palindrome ")
result = is_palindrome(word_to_check)

print(f"{word_to_check} is {'a palindrome' if result else 'not a palindrome'}.")
