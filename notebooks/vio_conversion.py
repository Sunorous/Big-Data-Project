import csv

# Open the input and output CSV files
with open('violation.csv', 'r') as input_file, open('sql_vio.csv', 'w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    
    # Write the header row to the output file
    header_row = next(reader)
    output_header = [header_row[0]] + [col.replace(" ", "").replace("-", "_") for col in header_row[1:]]
    writer.writerow(output_header)
    
    # Iterate over the rows in the input file and write the converted values to the output file
    for row in reader:
        output_row = [row[0]]
        for col in row[1:]:
            output_col = "case when Violation = '{}' then 1 else 0 end as {},".format(col, col.replace(" ", "").replace("-", "_"))
            output_row.append(output_col)
        writer.writerow(output_row)