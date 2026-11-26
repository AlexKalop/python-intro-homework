import csv
try: 
    with open('../data/messy_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        clean_rows = []
        skipped_rows= []
        for row_num, row in enumerate(reader, start=1):
            if None in row:
                skipped_rows.append(f"Row {row_num}: extra column detected — skipped")
                continue
            try:
                amount = float(row['amount'])
                clean_rows.append({
                    'name': row['name'], 
                    'category': row ['category'], 
                    'amount': amount
                })
            except (ValueError,TypeError):  
                skipped_rows.append(f"Row {row_num}: ValueError — could not convert '{row['amount']}' to float.")
            except KeyError as e:
                skipped_rows.append(f"Row {row_num}: KeyError — {e}")
        print("=== CSV Report ===")
        print(f"Rows attempted: {len(skipped_rows)+len(clean_rows)}")
        print(f"Rows parsed: {len(clean_rows)}")
        print(f"Rows skipped: {len(skipped_rows)}")
        print("")
        print("Skipped rows:")
        for row in skipped_rows:
            print(f"  {row}")
        print("")
        print("Clean data:")
        for row in clean_rows:
            print(f"  {row['name']} | {row['category']} | ${row['amount']:.2f}")
except FileNotFoundError:
    print("Error: \"../data/messy_data.csv\" was not found. Please check the file path and try again.")