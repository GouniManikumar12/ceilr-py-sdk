import requests

class CeilR:
    BASE_URL = "https://api.ceilr.com"

    def __init__(self, api_key: str, customer_id: str):
        self.api_key = api_key
        self.customer_id = customer_id

    def check_feature(self, feature_name: str) -> bool:
        """Check if a feature is enabled for the user"""
        try:
            response = requests.post(f"{self.BASE_URL}/check-feature", json={
                "apiKey": self.api_key,
                "customerId": self.customer_id,
                "featureName": feature_name
            })
            return response.json().get("allowed", False)
        except requests.RequestException as e:
            print(f"CeilR Error: {e}")
            return False

    def track_usage(self, feature_name: str, count: int = 1):
        """Track feature usage"""
        try:
            requests.post(f"{self.BASE_URL}/track-usage", json={
                "apiKey": self.api_key,
                "customerId": self.customer_id,
                "featureName": feature_name,
                "count": count
            })
        except requests.RequestException as e:
            print(f"CeilR Error: {e}")

    def get_user_entitlements(self):
        """Fetch user entitlements"""
        try:
            response = requests.get(f"{self.BASE_URL}/user-entitlements", headers={
                "Authorization": f"Bearer {self.api_key}"
            })
            return response.json().get("entitlements", [])
        except requests.RequestException as e:
            print(f"CeilR Error: {e}")
            return []
