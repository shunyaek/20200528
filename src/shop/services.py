import stripe
import json

# Set your secret key. Remember to switch to your live secret key in production!
# See your keys here: https://dashboard.stripe.com/account/apikeys
stripe.api_key = 'sk_test_51GwRA6DI55EkTlecJCcPA0bNblwPuX4IuYkjNgjfhAs9BdrWFqfsXQKd1vUiLFuPEGKCjQydmlm6HbfxRnTtfxJQ00dapjP6T6'

intent = stripe.PaymentIntent.create(
  amount=1099,
  currency='inr',
  # Verify your integration in this guide by including this parameter
  metadata={'integration_check': 'accept_a_payment'},
)
