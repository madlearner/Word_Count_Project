import json
from processing import Processing
from pre_processing import PreProcessing


with open('config.json', 'r') as f:
    config = json.load(f)


def main():
    raw_data = config['file_paths']['raw_data_path']
    input_file = config['file_paths']['clean_data_path']
    db_file = config['file_paths']['db_file_path']
    processed_folder = config['processed_folder_path']
    common_words = config['common_words']

    # Preprocess
    pre_process_raw_file = PreProcessing(raw_data, input_file)
    pre_process_raw_file.pre_process()

    # Process word_frequency 
    processor = Processing(input_file, db_file, processed_folder, common_words)
    processor.process_csv()

    print("Processing complete. The results are stored in the database and the file has been moved.")


if __name__ == "__main__":
    main()
