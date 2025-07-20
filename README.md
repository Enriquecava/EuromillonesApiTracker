🧪 EuroMillions Raffle API

This is a simple Python-based API that provides EuroMillions raffle results for a given date. It uses a two-step request system involving authentication and data retrieval.
🚀 Features

    🔐 Auth Request – Get a Bearer token using your email.

    🎟️ Raffle Data Retrieval – Fetch EuroMillions results (prizes, stars, and balls) by date.

📬 Authentication
POST /auth

Authenticate by sending your email. The server will respond with a Bearer token required for subsequent requests.
Request
```
POST /auth
Content-Type: application/json

{
  "email": "you@example.com"
}

Response

{
  "token": "your-bearer-token"
}
```
🎯 Get EuroMillions Raffle
```
GET /euromillones?date={date}

Retrieve the EuroMillions results for a specific date. Requires the Bearer token in the Authorization header.
Headers

Authorization: Bearer your-bearer-token
```

🧪 Running Locally
```
git clone https://github.com/yourusername/euromillones-api.git
cd euromillones-api
pip install -r requirements.txt
python app/app.py
```

