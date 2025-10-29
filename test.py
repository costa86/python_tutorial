import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "--branch",
    help="branch you work at",
    choices=["scranton", "stanford", "buffalo"],
)
parser.add_argument(
    "--name", help="your name", type=str, required=True, metavar="STRING"
)

parser.add_argument(
    "--sales", help="total in sales", type=float, default=0.0, metavar="FLOAT"
)
args = parser.parse_args()
message = f"My name is {args.name}, I work at the {args.branch} branch. \
My total in sales is {args.sales}"
print(message)
