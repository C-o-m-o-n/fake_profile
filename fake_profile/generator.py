from faker import Faker
import random, json

class Xprofile:
    def __init__(self):
        self.fake = Faker()

    def generate_fake_user(self):
        return {
            "user_id": self.fake.uuid4(),
            "username": self.fake.user_name(),
            "name": self.fake.name(),
            "bio": self.fake.text(max_nb_chars=160),
            "location": self.fake.city(),
            "url": self.fake.url(),
            "profile_image_url": "https://randomfox.ca/",
            "banner_image_url": "https://randomfox.ca/",
            "join_date": str(self.fake.date_time_this_decade()),
            "verified_status": self.fake.boolean(chance_of_getting_true=10),
            "follower_count": random.randint(0, 1000000),
            "following_count": random.randint(0, 1000),
            "tweet_count": random.randint(0, 10000),
            "likes_count": random.randint(0, 50000),
            "list_memberships": random.randint(0, 100),
            "timezone": self.fake.timezone(),
            "language": self.fake.language_code(),
            "protected_status": self.fake.boolean(chance_of_getting_true=5),
            "suspended_status": self.fake.boolean(chance_of_getting_true=1),
            "default_profile": self.fake.boolean(chance_of_getting_true=30),
            "default_profile_image": self.fake.boolean(chance_of_getting_true=20)
        }

    def generate_fake_tweet(self, user_id):
        created_at = str(self.fake.date_time_between(start_date='-2y', end_date='now'))
        return {
            "tweet_id": self.fake.uuid4(),
            "user_id": user_id,
            "text": self.fake.sentence(nb_words=20),
            "created_at": created_at,
            "retweet_count": random.randint(0, 10000),
            "like_count": random.randint(0, 50000),
            "reply_count": random.randint(0, 2000),
            "quote_count": random.randint(0, 1000),
            "is_retweet": self.fake.boolean(chance_of_getting_true=20),
            "is_reply": self.fake.boolean(chance_of_getting_true=15),
            "is_quoted": self.fake.boolean(chance_of_getting_true=10),
            "language": self.fake.language_code(),
            "tweet_image_url": "https://randomfox.ca/",
        }

    def generate_fake_comment(self, tweet_id, user_id):
        return {
            "comment_id": self.fake.uuid4(),
            "tweet_id": tweet_id,
            "user_id": user_id,
            "text": self.fake.sentence(nb_words=15),
            "created_at": str(self.fake.date_time_between(start_date='-2y', end_date='now')),
        }

    def generate_fake_like(self, tweet_id, user_id):
        return {
            "like_id": self.fake.uuid4(),
            "tweet_id": tweet_id,
            "user_id": user_id,
            "created_at": str(self.fake.date_time_between(start_date='-2y', end_date='now')),
        }

    def generate_fake_retweet(self, tweet_id, user_id):
        return {
            "retweet_id": self.fake.uuid4(),
            "tweet_id": tweet_id,
            "user_id": user_id,
            "created_at": str(self.fake.date_time_between(start_date='-2y', end_date='now')),
        }

    def generate_fake_tweets_and_interactions(self, user_id, tweet_count=10):
        tweets = []
        comments = []
        likes = []
        retweets = []

        for _ in range(tweet_count):
            tweet = self.generate_fake_tweet(user_id)
            tweets.append(tweet)

            num_comments = random.randint(0, 10)
            num_likes = random.randint(0, 100)
            num_retweets = random.randint(0, 50)

            comments.extend([self.generate_fake_comment(tweet['tweet_id'], user_id) for _ in range(num_comments)])
            likes.extend([self.generate_fake_like(tweet['tweet_id'], user_id) for _ in range(num_likes)])
            retweets.extend([self.generate_fake_retweet(tweet['tweet_id'], user_id) for _ in range(num_retweets)])

        return tweets, comments, likes, retweets

    def generate_fake_twitter_data(self, user_count=4, tweets_per_user=2):
        users = []
        all_tweets = []
        all_comments = []
        all_likes = []
        all_retweets = []

        for _ in range(user_count):
            user = self.generate_fake_user()
            users.append(user)

            user_tweets, user_comments, user_likes, user_retweets = self.generate_fake_tweets_and_interactions(
                user['user_id'], tweet_count=tweets_per_user)

            all_tweets.extend(user_tweets)
            all_comments.extend(user_comments)
            all_likes.extend(user_likes)
            all_retweets.extend(user_retweets)

        return users, all_tweets, all_comments, all_likes, all_retweets


class InstaProfile:
    def __init__(self):
        self.fake = Faker()

    def generate_user(self):
        return {
            "user_id": self.fake.uuid4(),
            "username": self.fake.user_name(),
            "full_name": self.fake.name(),
            "bio": self.fake.text(max_nb_chars=160),
            "profile_image_url": "https://randomfox.ca/",
            "website": self.fake.url(),
            "followers": random.randint(0, 1000000),
            "following": random.randint(0, 1000),
        }

    def generate_comment(self, post_id, user_id):
        return {
            "comment_id": self.fake.uuid4(),
            "user": user_id,
            "post": post_id,
            "comment": self.fake.text(max_nb_chars=200),
            "likes": random.randint(0, 50000),
            "created_at": str(self.fake.date_time_between(start_date='-2y', end_date='now')),
        }

    def generate_like(self, post_id, user_id):
        return {
            "like_id": self.fake.uuid4(),
            "post_id": post_id,
            "user_id": user_id,
            "created_at": str(self.fake.date_time_between(start_date='-2y', end_date='now')),
        }

    def generate_repost(self, post_id, user_id):
        return {
            "retweet_id": self.fake.uuid4(),
            "post_id": post_id,
            "user_id": user_id,
            "created_at": str(self.fake.date_time_between(start_date='-2y', end_date='now')),
        }

    def generate_post(self, user_id):
        return {
            "post_id": self.fake.uuid4(),
            "image_url": "https://randomfox.ca/",
            "caption": self.fake.text(),
            "likes": random.randint(0, 50000),
        }

    def generate_post_and_interactions(self, user_id, post_count=10):
        posts = []
        comments = []
        likes = []
        reposts = []

        for _ in range(post_count):
            post = self.generate_post(user_id)
            posts.append(post)

            num_comments = random.randint(0, 10)
            num_likes = random.randint(0, 100)
            num_reposts = random.randint(0, 50)

            comments.extend([self.generate_comment(post['post_id'], user_id) for _ in range(num_comments)])
            likes.extend([self.generate_like(post['post_id'], user_id) for _ in range(num_likes)])
            reposts.extend([self.generate_repost(post['post_id'], user_id) for _ in range(num_reposts)])

        return posts, comments, likes, reposts

    def generate_fake_instagram_data(self, user_count=4, posts_per_user=2):
        users = []
        all_posts = []
        all_comments = []
        all_likes = []
        all_reposts = []

        for _ in range(user_count):
            user = self.generate_user()
            users.append(user)

            user_posts, user_comments, user_likes, user_reposts = self.generate_post_and_interactions(
                user['user_id'], post_count=posts_per_user)

            all_posts.extend(user_posts)
            all_comments.extend(user_comments)
            all_likes.extend(user_likes)
            all_reposts.extend(user_reposts)

        return users, all_posts, all_comments, all_likes, all_reposts


class LinkedInProfile:
    def __init__(self):
        self.fake = Faker()

    def generate_user(self):
        return {
            "user_id": self.fake.uuid4(),
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
            "headline": self.fake.job(),
            "location": f"{self.fake.city()}, {self.fake.country()}",
            "summary": self.fake.text(max_nb_chars=300),
            "profile_image_url": "https://randomfox.ca/",
            "industry": self.fake.bs(),
            "education": self.fake.catch_phrase(),
            "experience": self.fake.text(max_nb_chars=300),
            "skills": [self.fake.word() for _ in range(5)],
            "connections": random.randint(50, 5000),
        }

    def generate_post(self, user_id):
        return {
            "post_id": self.fake.uuid4(),
            "user_id": user_id,
            "content": self.fake.text(),
            "likes": random.randint(0, 50000),
            "comments": random.randint(0, 1000),
            "shares": random.randint(0, 1000),
            "created_at": str(self.fake.date_time_between(start_date='-2y', end_date='now')),
        }

    def generate_comment(self, post_id, user_id):
        return {
            "comment_id": self.fake.uuid4(),
            "post_id": post_id,
            "user_id": user_id,
            "text": self.fake.text(max_nb_chars=200),
            "created_at": str(self.fake.date_time_between(start_date='-2y', end_date='now')),
        }

    def generate_like(self, post_id, user_id):
        return {
            "like_id": self.fake.uuid4(),
            "post_id": post_id,
            "user_id": user_id,
            "created_at": str(self.fake.date_time_between(start_date='-2y', end_date='now')),
        }

    def generate_share(self, post_id, user_id):
        return {
            "share_id": self.fake.uuid4(),
            "post_id": post_id,
            "user_id": user_id,
            "created_at": str(self.fake.date_time_between(start_date='-2y', end_date='now')),
        }

    def generate_post_and_interactions(self, user_id, post_count=10):
        posts = []
        comments = []
        likes = []
        shares = []

        for _ in range(post_count):
            post = self.generate_post(user_id)
            posts.append(post)

            num_comments = random.randint(0, 10)
            num_likes = random.randint(0, 100)
            num_shares = random.randint(0, 50)

            comments.extend([self.generate_comment(post['post_id'], user_id) for _ in range(num_comments)])
            likes.extend([self.generate_like(post['post_id'], user_id) for _ in range(num_likes)])
            shares.extend([self.generate_share(post['post_id'], user_id) for _ in range(num_shares)])

        return posts, comments, likes, shares

    def generate_fake_linkedin_data(self, user_count=4, posts_per_user=2):
        users = []
        all_posts = []
        all_comments = []
        all_likes = []
        all_shares = []

        for _ in range(user_count):
            user = self.generate_user()
            users.append(user)

            user_posts, user_comments, user_likes, user_shares = self.generate_post_and_interactions(
                user['user_id'], post_count=posts_per_user)

            all_posts.extend(user_posts)
            all_comments.extend(user_comments)
            all_likes.extend(user_likes)
            all_shares.extend(user_shares)

        return users, all_posts, all_comments, all_likes, all_shares
    
