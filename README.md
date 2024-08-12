# Fake Profile

A Python package to generate fake social media user data and interactions for testing and development.

<em> currently supports twitter(X), Instagram, LinkedIn, more comming soon </em>

## Installation

Install the package using pip:

```bash
pip install fake-profile

```


# Example usage
### For LinkedIn
```python
from fake_profile import LinkedInProfile

linkedInProfile = LinkedInProfile()
print(linkedInProfile.generate_fake_linkedin_data())
```
### For X/Twitter
```python
from fake_profile import Xprofile

xProfile = Xprofile()
print(xProfile.generate_fake_twitter_data())
```
### For Instagram
```python
from fake_profile import InstaProfile

instaProfile = InstaProfile()
print(instaProfile.generate_fake_instagram_data())
```

### For more specific usage
```python
from fake_profile import Xprofile, InstaProfile, LinkedInProfile
```
## Create an instance of Xprofile
```python
generator = Xprofile()

# Generate Twitter data
users, tweets, comments, likes, retweets = generator.generate_fake_twitter_data(user_count=5, tweets_per_user=3)

print(users)
print(tweets)
print(comments)
print(likes)
print(retweets)
```
## Create an instance of InstaProfile
```python
generator = InstaProfile()

# Generate Instagram data
users, posts, comments, likes, reposts = generator.generate_fake_instagram_data(user_count=5, posts_per_user=3)

print(users)
print(posts)
print(comments)
print(likes)
print(reposts)
```
## Create an instance of LinkedInProfile
```python
generator = LinkedInProfile()

# Generate LinkedIn data
users, posts, comments, likes, shares = generator.generate_fake_linkedin_data(user_count=5, posts_per_user=3)

print(users)
print(posts)
print(comments)
print(likes)
print(shares)
```
