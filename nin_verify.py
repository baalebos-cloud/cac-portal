import requests
import os

def verify_nin(nin, dob):
    url = os.getenv("NIN_API_URL")
    headers = {"Authorization": f"Bearer {os.getenv('lv_Aijalon_19uxfaes4knzv3gbm28t8706911oh7d4')}"}
    payload = {"nin": nin, "dob": dob}
    response = requests.post(url, json=payload, headers=headers)
    return response.status_code == 200
