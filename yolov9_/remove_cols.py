import csv

def remove_columns(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            # Remove the first two columns
            modified_row = row[2:]
            writer.writerow(modified_row)

if __name__ == "__main__":
    # Replace 'input.csv' and 'output.csv' with your file names
    input_csv = '/home/aswin/PycharmProjects/yolov9/input.csv'
    output_csv = 'output.csv'

    remove_columns(input_csv, output_csv)
    print(f"Columns removed and saved to {output_csv}")
