import requests, os

def init_payment(email, amount):
    headers = {"Authorization": f"Bearer {os.getenv('PAYSTACK_SECRET')}"}
    data = {
        "email": email,
        "amount": amount * 100
    }
    return requests.post(
        "https://api.paystack.co/transaction/initialize",
        headers=headers,
        json=data
    ).json()
