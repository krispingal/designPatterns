""""Bridge design pattern implementation on a payment processor."""
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass

class StripeGateway(PaymentGateway):
    def process_payment(self, amount: float) -> None:
        print(f'Processing ${amount} payment through Stripe.')

class SquareGateway(PaymentGateway):
    def process_payment(self, amount: float) -> None:
        print(f'Processing ${amount} payment through Square.')

class PaymentMethod(ABC):
    def __init__(self, gateway: PaymentGateway):
        self.gateway = gateway

    @abstractmethod
    def make_payment(self, amount: float) -> None:
        pass

class CreditCard(PaymentMethod):
    def make_payment(self, amount: float) -> None:
        print("Initiating credit card payment.")
        self.gateway.process_payment(amount)

class Paypal(PaymentMethod):
    def make_payment(self, amount: float) -> None:
        print("Initiating paypal payment.")
        self.gateway.process_payment(amount)

if __name__ == '__main__':
    stripe_gateway = StripeGateway()
    square_gateway = SquareGateway()

    credit_card_payment = CreditCard(stripe_gateway)
    credit_card_payment.make_payment(120.00)

    paypal_payment = Paypal(square_gateway)
    paypal_payment.make_payment(250.00)



