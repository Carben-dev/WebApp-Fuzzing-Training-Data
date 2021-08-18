def main():
    import csv
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                if row[2] == "1":
                    print(f'{row[1]}')
                line_count += 1
        print(f'Processed {line_count} lines.')


if __name__ == '__main__':
    main()