import sqlite3
import os
import shutil
import pandas as pd
from helpers import Helpers


class Processing:
    def __init__(self, input_file, db_file, processed_folder, common_words):
        self.input_file = input_file
        self.db_file = db_file
        self.processed_folder = processed_folder
        self.common_words = common_words

    def process_csv(self):
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()

            # Create table if it doesn't exist
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS word_frequency (
                    id INTEGER,
                    source TEXT,
                    word TEXT,
                    count INTEGER
                )
            ''')

            df = pd.read_csv(self.input_file)
            for index, row in df.iterrows():
                text = row['original_text']
                if not isinstance(text, str):
                    print(f"Warning: Skipping row {index} due to invalid text data.")
                    continue

                freq = Helpers.word_count(self, text, self.common_words)
                for word, count in freq.items():
                    cursor.execute('''
                        INSERT INTO word_frequency (id, source, word, count)
                        VALUES (?, ?, ?, ?)
                    ''', (row['id'], row['source'], word, count))

            conn.commit()

            # Move the processed file to processed_data folder
            if not os.path.exists(self.processed_folder):
                os.makedirs(self.processed_folder)
            shutil.move(self.input_file, os.path.join(self.processed_folder,
                        os.path.basename(self.input_file)))
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
        finally:
            conn.close()
