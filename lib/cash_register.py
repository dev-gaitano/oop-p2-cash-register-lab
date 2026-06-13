#!/usr/bin/env python3


class CashRegister:
    def __init__(
        self, discount=0, total=0, items=None, previous_transactions=None
    ) -> None:
        self.discount = discount
        self.total = total
        self.items = items if items is not None else []
        self.previous_transactions = (
            previous_transactions if previous_transactions is not None else []
        )

    @property
    def discount(self):
        """The discount property."""
        return self._discount

    @discount.setter
    def discount(self, value):
        if not isinstance(value, int) or not (0 <= value <= 100):
            print("Not valid discount")
        self._discount = value

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append(
            {"item": item, "price": price, "quantity": quantity}
        )

    def apply_discount(self):
        if self.discount > 0:
            self.total -= self.total * (self.discount / 100)
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.previous_transactions:
            last = self.previous_transactions.pop()
            self.total -= last["price"] * last["quantity"]
            for _ in range(last["quantity"]):
                if last["item"] in self.items:
                    self.items.remove(last["item"])

    def reset_register_totals(self):
        self.total = 0
        self.items = []
        self.previous_transactions = []
