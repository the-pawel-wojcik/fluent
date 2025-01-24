from typing import Callable, Sequence
from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Customer:
    name: str
    fidelity: int

@dataclass
class LineItem:
    product: str
    quantity: int
    price: Decimal

    def total(self) -> Decimal:
        return self.quantity * self.price

@dataclass(frozen=True)
class Order:
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Callable[['Order'], Decimal] | None = None

    def total(self) -> Decimal:
        totals = (item.total() for item in self.cart)
        return sum(totals, start=Decimal(0))

    def due(self) -> Decimal:
        if self.promotion is None:
            discount = Decimal(0)
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        return f'<Order total: {self.total():.2f} due: {self.due():.2f}>'


Promotion = Callable[[Order], Decimal]
promos = list()

def promotion(promo: Promotion) -> Promotion:
    promos.append(promo)
    return promo

def best_promo(order: Order) -> Decimal:
    return max(promo(order) for promo in promos)

@promotion
def fidelity(order: Order) -> Decimal:
    if order.customer.fidelity >= 8:
        return order.total() * Decimal('0.05')
    return Decimal()

@promotion
def bulk_item(order: Order) -> Decimal:
    DISCOUNT_RATE = Decimal('0.1')
    discount = Decimal(0)
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * DISCOUNT_RATE
    return discount

@promotion
def large_order(order: Order) -> Decimal:
    DISCOUNT_RATE = Decimal('0.07')
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) > 9:
        return order.total() * DISCOUNT_RATE
    return Decimal(0)


joe = Customer('Joe Doe', 0)
ann = Customer('Ann Wan', 1100)
cart = [
    LineItem('banana', 4, Decimal('0.5')),
    LineItem('apple', 10, Decimal('1.0')),
    LineItem('berry', 5, Decimal(5)),
]
banana_cart = [
    LineItem('banana', 30, Decimal('.5')),
]
long_cart = [
    LineItem(str(i), 1, Decimal(i+1)) for i in range(10)
]
print(f'{Order(joe, cart, fidelity)=}')
print(f'{Order(joe, banana_cart, bulk_item)=}')
print(f'{Order(joe, banana_cart)=}')
print(f'{Order(joe, long_cart)=}')
print(f'{Order(joe, long_cart, large_order)=}')
print(f'{Order(joe, long_cart, best_promo)=}')
print(f'{Order(joe, cart, best_promo)=}')
print(f'{Order(ann, cart, best_promo)=}')

