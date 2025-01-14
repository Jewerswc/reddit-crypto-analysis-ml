import praw

# Initialize Reddit API
reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                     client_secret='YOUR_CLIENT_SECRET',
                     user_agent='YOUR_USER_AGENT')

# Access the 'CryptoCurrency' subreddit
subreddit = reddit.subreddit('CryptoCurrency')

# Example: Print titles of hot posts
for post in subreddit.hot(limit=5):
    print(post.title)