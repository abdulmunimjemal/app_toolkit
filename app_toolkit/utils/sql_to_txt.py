import sqlite3
import argparse


def extract_data(input_db: str, table: str,  output_json: str):
    try:
        conn = sqlite3.connect(input_db)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table}")
        data = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

        with open(output_json, 'w', encoding="utf-8") as f:
            for row in data:
                value = row[-1]  # the amharic part
                if isinstance(value, str):
                    value = value.encode('utf-8').decode('utf-8')
                    f.write(value)
                    f.write('\n')
        print(f"Data from {table} table extracted successfully!")
    except Exception as e:
        print(f"Error extracting data from {table} table: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract data from SQLLite to JSON")
    parser.add_argument('input_db', type=str, help="Input database path")
    parser.add_argument('table', type=str,
                        help="Table name", default="dictionary")
    parser.add_argument('output_json', type=str, help="Output JSON path")

    args = parser.parse_args()
    extract_data(args.input_db, args.table, args.output_json)
