import argparse
from src.Event import EventHandler

if __name__ == '__main__':
    start_script = argparse.ArgumentParser(
        description='Sort json file with events')
    start_script.add_argument('input_file', type=str, help='Input file')
    start_script.add_argument('output_file', type=str, help='Output file')
    args = start_script.parse_args()

    forming_data = EventHandler()
    forming_data.load_data_from_file(args.input_file)
    ready_data = forming_data.sort_and_form()
    forming_data.create_json_file(args.output_file, ready_data)
