import stripe
from fastapi import HTTPException

stripe.api_key = "your_stripe_secret_key"

def create_stripe_session(user_email: str):
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            customer_email=user_email,
            line_items=[{'price': 'price_ID_here', 'quantity': 1}],
            mode='subscription',
            success_url="http://localhost:8501/success",
            cancel_url="http://localhost:8501/cancel"
        )
        return checkout_session.url
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
