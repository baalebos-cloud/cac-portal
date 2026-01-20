import requests
import os
import json

WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
WHATSAPP_PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID")


def send_whatsapp_alert(phone_number, user_name, payment_id, amount, status):
    if not WHATSAPP_TOKEN or not WHATSAPP_PHONE_NUMBER_ID:
        raise ValueError("WhatsApp credentials not set in environment variables")

    url = f"https://graph.facebook.com/v24.0/{WHATSAPP_PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": phone_number,
        "type": "template",
        "template": {
            "name": "payment_status_update",  # MUST be an approved template
            "language": {"code": "en_US"},
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {"type": "text", "text": user_name},
                        {"type": "text", "text": str(payment_id)},
                        {"type": "text", "text": f"₦{amount:,}"},
                        {"type": "text", "text": status}
                    ]
                }
            ]
        }
    }

    response = requests.post(
        url,
        headers=headers,
        data=json.dumps(payload),
        timeout=10
    )

    return response.json()
