from app.client import Client
import argparse
from dotenv import load_dotenv


def main(args):
    PIN = args["PIN"]
    Client(PIN)


if __name__ == "__main__":
    all_args = argparse.ArgumentParser()
    all_args.add_argument("-PIN", "--PIN", required=True, help="Your Phone's PIN Code")
    args = vars(all_args.parse_args())

    load_dotenv()

    main(args)
