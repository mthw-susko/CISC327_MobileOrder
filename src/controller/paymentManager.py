class PaymentManager:
    def processPayment(self, creditCardInfo):
        # Add in the logic for processing.
        if self.validateCreditCard(creditCardInfo):
            # Payment was successfully processed
            print("Payment processed successfully.")
            return True
        else:
            # Payment processing failed
            print("Payment processing failed.")
            return False

    def validateCreditCard(self, creditCardInfo):
        # Add in the logic for validation. Regex maybe? Can push to backend prototyping?
        return bool(creditCardInfo)