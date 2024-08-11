from faker import Faker
import random, json

fake = Faker()

class Xprofile:
    def __init__(self):
        pass

    # Function to generate fake Twitter user data
    def generate_fake_user(self):
        return {
            "user_id": fake.uuid4(),
            "username": fake.user_name(),
            "name": fake.name(),
            "bio": fake.text(max_nb_chars=160),
            "location": fake.city(),
            "url": fake.url(),
            "profile_image_url": "https://randomfox.ca/", #fake.image_url(width=400, height=400),
            "banner_image_url": "https://randomfox.ca/", #fake.image_url(width=1500, height=500),
            "join_date": str(fake.date_time_this_decade()),
            "verified_status": fake.boolean(chance_of_getting_true=10),
            "follower_count": random.randint(0, 1000000),
            "following_count": random.randint(0, 1000),
            "tweet_count": random.randint(0, 10000),
            "likes_count": random.randint(0, 50000),
            "list_memberships": random.randint(0, 100),
            "timezone": fake.timezone(),
            "language": fake.language_code(),
            "protected_status": fake.boolean(chance_of_getting_true=5),
            "suspended_status": fake.boolean(chance_of_getting_true=1),
            "default_profile": fake.boolean(chance_of_getting_true=30),
            "default_profile_image": fake.boolean(chance_of_getting_true=20)
        }

    # Function to generate fake tweet data associated with a user
    def generate_fake_tweet(self, user_id):
        created_at = str(fake.date_time_between(start_date='-2y', end_date='now'))
        return {
            "tweet_id": fake.uuid4(),
            "user_id": user_id,
            "text": fake.sentence(nb_words=20),
            "created_at": created_at,
            "retweet_count": random.randint(0, 10000),
            "like_count": random.randint(0, 50000),
            "reply_count": random.randint(0, 2000),
            "quote_count": random.randint(0, 1000),
            "is_retweet": fake.boolean(chance_of_getting_true=20),
            "is_reply": fake.boolean(chance_of_getting_true=15),
            "is_quoted": fake.boolean(chance_of_getting_true=10),
            "language": fake.language_code(),
            "tweet_image_url": "https://randomfox.ca/", #fake.image_url(width=400, height=400),
        }

    # Function to generate fake comments for a tweet
    def generate_fake_comment(self, tweet_id, user_id):
        return {
            "comment_id": fake.uuid4(),
            "tweet_id": tweet_id,
            "user_id": user_id,
            "text": fake.sentence(nb_words=15),
            "created_at": str(fake.date_time_between(start_date='-2y', end_date='now')),
        }

    # Function to generate fake likes for a tweet
    def generate_fake_like(self, tweet_id, user_id):
        return {
            "like_id": fake.uuid4(),
            "tweet_id": tweet_id,
            "user_id": user_id,
            "created_at": str(fake.date_time_between(start_date='-2y', end_date='now')),
        }

    # Function to generate fake retweets for a tweet
    def generate_fake_retweet(self, tweet_id, user_id):
        return {
            "retweet_id": fake.uuid4(),
            "tweet_id": tweet_id,
            "user_id": user_id,
            "created_at": str(fake.date_time_between(start_date='-2y', end_date='now')),
        }
    
    # Generate a list of fake tweets and their interactions for a user
    def generate_fake_tweets_and_interactions(self, user_id, tweet_count=10):
        tweets = []
        comments = []
        likes = []
        retweets = []

        for _ in range(tweet_count):
            tweet = self.generate_fake_tweet(user_id)
            tweets.append(tweet)

            # Generate interactions for each tweet
            num_comments = random.randint(0, 10)
            num_likes = random.randint(0, 100)
            num_retweets = random.randint(0, 50)

            comments.extend([self.generate_fake_comment(tweet['tweet_id'], user_id) for _ in range(num_comments)])
            likes.extend([self.generate_fake_like(tweet['tweet_id'], user_id) for _ in range(num_likes)])
            retweets.extend([self.generate_fake_retweet(tweet['tweet_id'], user_id) for _ in range(num_retweets)])

        return tweets, comments, likes, retweets

    # Generate a list of fake Twitter users and their associated tweets and interactions
    def generate_fake_twitter_data(self, user_count=10, tweets_per_user=5):
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
    
    #save the user profile to a file
    def save_fake_user(self, fake_twitter_users, fake_twitter_tweets, fake_twitter_comments, fake_twitter_likes, fake_twitter_retweets, format="json", filename="fake_data.json"):
        data = [fake_twitter_users, fake_twitter_tweets, fake_twitter_comments, fake_twitter_likes, fake_twitter_retweets]
        if format == "json":
            with open(filename, "w") as file:
                json.dump(data, file)