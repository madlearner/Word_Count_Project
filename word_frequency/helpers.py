import re
from collections import Counter

class Helpers:

    def clean_text(self, text):
        # Remove number or emojis if there is any
        if not isinstance(text, str):
            print(f"Warning: Expected string but got {type(text)}. Skipping...")
            return ""

        # Remove numbers
        text = re.sub(r'\b\d+\b', '', text)
        # Remove emojis
        text = re.sub(r'[^\w\s,]', '', text)
        return text

    def word_count(self, text, common_words):
        text = Helpers.clean_text(self, text).lower()
        words = text.split()
        filtered_words = [word for word in words if word not in common_words]
        return Counter(filtered_words)

