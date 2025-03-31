import hashlib
import tkinter as tk
from tkinter import messagebox
words = [
    "apple", "banana", "car", "drive", "eat", "happy", "sad", "orange", "cat", "house", "book",
    "drink", "table", "walk", "quickly", "jump", "laugh", "run", "play", "sun", "beautiful",
    "flower", "morning", "sky", "coffee", "window", "garden", "quiet", "evening", "listen", "sleep",
    "chair", "talk", "street", "music", "phone", "rain", "tree", "smile", "food", "park",
    "bird", "bicycle", "clean", "friend", "picture", "write", "sandwich", "door", "travel", "world",
    "I", "me", "you", "they", "she", "it", "we", "he", "are", "is", "were", "was", "do", "did", "have", "has",
    "on", "in", "am","my","name","fruit", "an"
]
def hash_sha256(input_string):
    sha_hash256 = hashlib.sha256()
    sha_hash256.update(input_string.encode('utf-8'))
    return sha_hash256.hexdigest()
hash_keys = {hash_sha256(word.lower()): word for word in words}

def wagner_fischer(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)
    if len_s1 > len_s2:
        s1, s2 = s2, s1
        len_s1, len_s2 = len_s2, len_s1

    current_row = range(len_s1 + 1)
    for i in range(1, len_s2 + 1):
        previous_row, current_row = current_row, [i] + [0] * len_s1
        for j in range(1, len_s1 + 1):
            add, delete, change = previous_row[j] + 1, current_row[j-1] + 1, previous_row[j-1]
            if s1[j-1] != s2[i-1]:
                change += 1
            current_row[j] = min(add, delete, change)
    return current_row[len_s1]

def get_suggestions(misspelled_word):
    suggestions = []
    for correct_word in words:
        distance = wagner_fischer(misspelled_word.lower(), correct_word)
        suggestions.append((correct_word, distance))
    suggestions.sort(key=lambda x: x[1])
    return [word for word, distance in suggestions[:3]]

def spell_check_revised(sentence):
    words_in_sentence = sentence.split()
    output_text.delete(1.0, tk.END)  # Clear previous text
    for word in words_in_sentence:
        hashed_word = hash_sha256(word.lower())
        if hashed_word not in hash_keys:
            output_text.insert(tk.END, f"'{word}' is misspelled.\n")
            suggestions = get_suggestions(word)
            output_text.insert(tk.END, f"Suggestions: {', '.join(suggestions)}\n\n")

def check_spelling():
    sentence = input_text.get("1.0", "end-1c")  # Get input text
    spell_check_revised(sentence)

root = tk.Tk()
root.title("Spell Checker")

input_label = tk.Label(root, text="Enter a sentence:")
input_label.pack(pady=10)

input_text = tk.Text(root, height=5, width=50)
input_text.pack()

check_button = tk.Button(root, text="Check Spelling", command=check_spelling)
check_button.pack(pady=10)

output_text = tk.Text(root, height=10, width=50)
output_text.pack()
root.mainloop()
