import requests

# Exercise 1: Perform a simple GET request
def get_request(url):
    try:
        response = requests.get(url)
        return f"Status: {response.status_code}\nHeaders: {response.headers}\nContent: {response.text}"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Exercise 2: Perform a GET request with parameters
def get_request_with_params(url, params):
    try:
        response = requests.get(url, params=params)
        return f"Status: {response.status_code}\nHeaders: {response.headers}\nContent: {response.text}"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Exercise 3: Perform a POST request
def post_request(url, data):
    try:
        response = requests.post(url, data=data)
        return f"Status: {response.status_code}\nHeaders: {response.headers}\nResponse Data: {response.json() if response.headers['Content-Type'] == 'application/json' else response.text}"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Exercise 4: Perform a PUT request
def put_request(url, data):
    try:
        response = requests.put(url, data=data)
        return f"Status: {response.status_code}\nHeaders: {response.headers}\nResponse Data: {response.json() if response.headers['Content-Type'] == 'application/json' else response.text}"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Exercise 5: Perform a PATCH request
def patch_request(url, data):
    try:
        response = requests.patch(url, data=data)
        return f"Status: {response.status_code}\nHeaders: {response.headers}\nContent: {response.text}"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Exercise 6: Perform a DELETE request
def delete_request(url):
    try:
        response = requests.delete(url)
        return f"Status: {response.status_code}\nHeaders: {response.headers}\nContent: {response.text}"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Exercise 7: Inspect headers during a redirect request
def get_redirect_location(url):
    try:
        response = requests.get(url, allow_redirects=False)
        if response.status_code in [301, 302, 303, 307, 308]:  # Redirection status codes
            location = response.headers.get('Location')
            return f"Redirect Location: {location}\nHeaders: {response.headers}"
        return "No redirection"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Main function for testing manually if needed
if name == "main":
    url = 'https://example.com'

    print("1. Performing a simple GET request:")
    print(get_request(url))

    print("\n2. Performing a GET request with parameters:")
    params = {'q': 'python language'}
    print(get_request_with_params('https://www.google.com/search', params))

    print("\n3. Performing a POST request:")
    data = {'key': 'value'}
    print(post_request(url, data))

    print("\n4. Performing a PUT request:")
    print(put_request(url, data))

    print("\n5. Performing a PATCH request:")
    print(patch_request(url, data))

    print("\n6. Performing a DELETE request:")
    print(delete_request(url))

    print("\n7. Inspecting headers during a redirect request:")
    redirect_url = 'http://httpbin.org/redirect-to?url=https://example.com'
    print(get_redirect_location(redirect_url))