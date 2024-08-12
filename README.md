# Fake Profile

A Python package to generate fake social media user data and interactions for testing and development.

<em> currently supports twitter(X), more comming soon </em>

## Installation

Install the package using pip:

```bash
pip install fake-profile

```


# Example usage
```
    # Twitter
    xprofile = Xprofile()
    twitter_users, tweets, comments, likes, retweets = xprofile.generate_fake_twitter_data()
    with open("twitter_data.json", "w") as f:
        json.dump({
            "users": twitter_users,
            "tweets": tweets,
            "comments": comments,
            "likes": likes,
            "retweets": retweets,
        }, f, indent=4)

    # Instagram
    insta = InstaProfile()
    insta_users, posts, insta_comments, insta_likes, insta_reposts = insta.generate_fake_instagram_data()
    with open("insta_data.json", "w") as f:
        json.dump({
            "users": insta_users,
            "posts": posts,
            "comments": insta_comments,
            "likes": insta_likes,
            "reposts": insta_reposts,
        }, f, indent=4)

    # LinkedIn
    linkedin = LinkedInProfile()
    linkedin_users, linkedin_posts, linkedin_comments, linkedin_likes, linkedin_shares = linkedin.generate_fake_linkedin_data()
    with open("linkedin_data.json", "w") as f:
        json.dump({
            "users": linkedin_users,
            "posts": linkedin_posts,
            "comments": linkedin_comments,
            "likes": linkedin_likes,
            "shares": linkedin_shares,
        }, f, indent=4)
