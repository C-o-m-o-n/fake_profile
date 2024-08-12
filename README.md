# Fake Profile

A Python package to generate fake social media user data and interactions for testing and development.

<em> currently supports twitter(X), more comming soon </em>

## Installation

Install the package using pip:

```bash
pip install fake-profile

```


# Example usage
### For LinkedIn
```
from fake_profile import LinkedInProfile

linkedInProfile = LinkedInProfile()
print(linkedInProfile.generate_fake_linkedin_data())
```
### For X/Twitter
```
from fake_profile import Xprofile

xProfile = Xprofile()
print(xProfile.generate_fake_twitter_data())
```
### For Instagram
```
from fake_profile import InstaProfile

instaProfile = InstaProfile()
print(instaProfile.generate_fake_instagram_data())
