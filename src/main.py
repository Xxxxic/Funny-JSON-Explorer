import argparse
import json
import sys
from json_explorer import FunnyJsonExplorer
from factories.concrete_factory import ConcreteFactory1

# def main():
#     parser = argparse.ArgumentParser(description="Process a JSON file with style and icon family options.")
#     parser.add_argument('-f', '--file', type=str, required=True, help='Path to the JSON file')
#     parser.add_argument('-s', '--style', type=str, required=True, default='tree', help='Style to be applied')
#     parser.add_argument('-i', '--icon', type=str, required=True, default='poker', help='Icon family to be used')
#     parser.add_argument('-c', '--config', type=str, required=False, default='',
#                         help='Path to the JSON file including other icon families')
#
#     args = parser.parse_args()
#
#     try:
#         fje = FunnyJsonExplorer(args.style, args.icon, args.config)
#         fje._load(args.file)
#         fje.build()
#         fje.show()
#
#     except FileNotFoundError:
#         print(f"Error: The file {args.file} was not found.")
#         sys.exit(1)
#     except json.JSONDecodeError:
#         print(f"Error: The file {args.file} is not a valid JSON file.")
#         sys.exit(1)
#
#
# if __name__ == "__main__":
#     main()

if __name__ == "__main__":
    json_str = '''
    {
        "oranges": {
            "mandarin": {
                "clementine": null,
                "tangerine": "cheap & juicy!"
            }
        },
        "apples": {
            "gala": null,
            "pink lady": null
        }
    }
    '''

    explorer = FunnyJsonExplorer(ConcreteFactory1())
    json_data = explorer._load(json_str)
    explorer.show(json_data)
