"""Inventory management system with add/remove and save/load operations."""

import json
from datetime import datetime

stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add quantity to the stock for a given item."""
    if not item or not isinstance(item, str):
        return

    if not isinstance(qty, int):
        print(f"[ERROR] Invalid quantity: {qty}")
        return

    stock_data[item] = stock_data.get(item, 0) + qty

    if logs is None:
        logs = []
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove quantity from stock safely."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"[WARNING] Tried to remove non-existent item: {item}")
    except TypeError:
        print(f"[ERROR] Invalid quantity for removal: {qty}")


def get_qty(item):
    """Return quantity of a specific item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load stock data from JSON file."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            global stock_data
            stock_data = json.load(f)
    except FileNotFoundError:
        print(f"[INFO] File '{file}' not found, starting fresh.")


def save_data(file="inventory.json"):
    """Save current stock data to JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)


def print_data():
    """Print current inventory."""
    print("\nItems Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return list of items below threshold."""
    return [i for i, q in stock_data.items() if q < threshold]


def main():
    """Main function to demonstrate inventory operations."""
    add_item("apple", 10)
    add_item("banana", 2)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
