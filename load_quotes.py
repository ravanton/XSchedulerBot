from utils.db import add_quote

sample_quotes = [
    ("The best way to predict the future is to invent it.", "Alan Kay"),
    ("Life is what happens when you're busy making other plans.", "John Lennon"),
    ("Do not go where the path may lead, go instead where there is no path and leave a trail.", "Ralph Waldo Emerson"),
    ("It always seems impossible until it's done.", "Nelson Mandela"),
    ("Success is not final, failure is not fatal: It is the courage to continue that counts.", "Winston Churchill")
]

for text, author in sample_quotes:
    add_quote(text, author)

print("Sample quotes added.")
