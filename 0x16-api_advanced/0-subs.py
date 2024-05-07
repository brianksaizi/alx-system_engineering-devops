import requests

def number_of_subscribers(subreddit_name):
    url = f"https://www.reddit.com/r/{subreddit_name}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}  # Reddit API requires a user-agent header
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0  # Invalid subreddit or other error
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

# Example usage:
subreddit = input("Enter subreddit name: ")
subscribers = number_of_subscribers(subreddit)
print(f"The number of subscribers in r/{subreddit} is: {subscribers}")
