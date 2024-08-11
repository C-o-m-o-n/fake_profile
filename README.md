# Fake Profile Generaator



A Python package to generate fake social media user data and interactions for testing and development.

## Installation

Install the package using pip:

```bash
pip install fake_profile


## Usage

from fake_profile import Xprofile

generator = Xprofile()

# Generate data
users, tweets, comments, likes, retweets = generator.generate_fake_twitter_data(user_count=5, tweets_per_user=3)

print(users)
print(tweets)
print(comments)
print(likes)
print(retweets)

