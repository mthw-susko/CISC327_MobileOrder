import time


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
        valid = True
        # creditCardInfo = [paymentMethod:String, cardNumber:Int, expiryDate:String, securityCode:Int]
        cardNumber = creditCardInfo[1]
        expiryDate = creditCardInfo[2]
        securityCode = creditCardInfo[3]

        # no card number
        if len(str(cardNumber)) == 0:
            print("Card Number has not been entered")
            valid = False

        # card number validation
        if len(str(cardNumber)) < 16 or len(str(cardNumber)) > 16:
            print("Your card number is invalid")
            valid = False

        # no expiry date
        if int(expiryDate.split("/")[0]) < 1:
            print("Your card's expiration date is invalid")
            valid = False

        # expiry date not valid
        if int(expiryDate.split("/")[0]) > 12:
            print("Your card's expiration date is invalid")
            valid = False

        # expiry date not valid
        if expiryDate == "12/23":
            print("Your card's expiration date is invalid")
            valid = False

        # expiry date not valid
        if len(expiryDate) != 5 and not "/" in expiryDate:
            print("Your card's expiration date is invalid")
            valid = False

        # no security code
        if len(str(securityCode)) == 0:
            print("Security code has not been entered")
            valid = False

        # security code invalid
        if len(str(securityCode)) > 4 or len(str(securityCode)) < 3:
            print("Security code is invalid")
            valid = False
        
        if valid:
            print("Payment Processed!")

        # security code not valid
        time.sleep(1)
        return valid
