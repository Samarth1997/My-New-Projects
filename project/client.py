import requests

class DeepSeekAIClient:
    def __init__(self, api_key, base_url="https://api.deepseek.com/v1"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def send_request(self, endpoint, payload):
        """
        Sends a POST request to the DeepSeek AI API.
        
        :param endpoint: The API endpoint (e.g., "/chat/completions").
        :param payload: The data to send in the request body.
        :return: JSON response from the API.
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, headers=self.headers, json=payload)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

# Example usage
if __name__ == "__main__":
    # Replace with your actual API key
    API_KEY = "sk-82fcf7aadf0e4764be99225ea03f0535"
    
    # Initialize the client
    client = DeepSeekAIClient(api_key=API_KEY)
    
    # Define the API endpoint and payload
    endpoint = "/chat/completions"  # Example endpoint
    payload = {
        "model": "deepseek-chat",  # Specify the model
        "messages": [
            {"role": "system", "content": "You are virtual AI assistance named jarvis skilled in general task like alexa"},
            {"role": "user", "content": "what is cricket"}
        ]
    }
    
    # Send the request
    response = client.send_request(endpoint, payload)
    
    # Print the response
    if response:
        print("API Response:", response)