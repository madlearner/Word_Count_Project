import csv


class PreProcessing:
    def __init__(self, raw_data_path, clean_data_path):
        self.raw_data = raw_data_path
        self.clean_data = clean_data_path

    def pre_process(self):
        raw_data = []

        # Read data from input CSV file
        with open(self.raw_data, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) > 0:  # Ensuring that there is data in the row
                    line = ','.join(row)    # Join the row into a single string
                    raw_data.append(line)
        
        # Write data to CSV file
        with open(self.clean_data, 'w',
                  newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
            
            # Process and write rows
            for line in raw_data:
                # Split the line, replace the curly quotes, 
                # then strip extra spaces and remove quotes
                parts = [part.strip().replace('”', '').replace('“', '') for part in line.split(',')]

                # join the string from the 3rd element (original_text)
                joined_text = ' '.join(parts[2:])
                parts = [parts[0], parts[1], joined_text]
                
                # Check if we have three parts(id, source, original_text)
                if len(parts) == 3:
                    writer.writerow(parts)
                else:
                    print(f"Skipping invalid data: {line}")
