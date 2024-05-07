mport requests

def number_of_subscribers(subreddit_name):
    url = f"https://www.reddit.com/r/{subreddit_name}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}  # Reddit API requires a user-agent header
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad response status
        data = response.json()
        return data['data']['subscribers']
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except KeyError as key_err:
        print(f"Key error occurred: {key_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return 0

# Example usage:
subreddit = input("Enter subreddit name: ")
subscribers = number_of_subscribers(subreddit)
print(f"The number of subscribers in r/{subreddit} is: {subscribers}")
