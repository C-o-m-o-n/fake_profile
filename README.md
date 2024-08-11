# Fake Profile

A Python package to generate fake social media user data and interactions for testing and development.

<em> currently supports twitter(X), more comming soon </em>

## Installation

Install the package using pip:

```bash
pip install fake-profile

```

## Usage
```python
from fake_profile import Xprofile

generator = Xprofile()

# Generate data
users, tweets, comments, likes, retweets = generator.generate_fake_twitter_data(user_count=5, tweets_per_user=3)

print(users)
print(tweets)
print(comments)
print(likes)
print(retweets)

```
