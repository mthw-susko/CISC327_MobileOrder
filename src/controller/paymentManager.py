class PaymentManager:
    def processPayment(self, creditCardInfo):
        # Logic for payment processing
        if self.validateCreditCard(creditCardInfo):
            # Payment was successfully processed
            print("Payment processed successfully.")
            return True
        else:
            # Payment processing failed
            print("Payment processing failed.")
            return False

    def validateCreditCard(self, creditCardInfo):
        # Validation
        return bool(creditCardInfo)