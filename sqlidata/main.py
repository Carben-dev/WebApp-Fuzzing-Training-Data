def main():
    import csv
    with open('new2.csv', encoding='UTF-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                data = row[0]
                label = row[1]
                if label == "1":
                    try:
                        print(f'{data}')
                    except:
                        continue
                line_count += 1
        print(f'Processed {line_count} lines.')


if __name__ == '__main__':
    main()