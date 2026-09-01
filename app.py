from file_location import *


banks = [bank1]


def process_file_mapping():
 try:
    for bank in banks:

        response = bank()

        print("Response:", response)
 except Exception as e:
     print(e)


if __name__ == "__main__":
    process_file_mapping()