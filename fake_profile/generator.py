from faker import Faker
import random, json


class Xprofile:
    def __init__(self):
        self.fake = Faker()

    # Generate fake Twitter user data
    def generate_fake_user(self):
        return {
            "user_id": self.fake.uuid4(),
            "username": self.fake.user_name(),
            "name": self.fake.name(),
            "bio": self.fake.text(max_nb_chars=160),
            "location": self.fake.city(),
            "url": self.fake.url(),
            "profile_image_url": "https://randomfox.ca/", #fake.image_url(width=400, height=400),
            "banner_image_url": "https://randomfox.ca/", #fake.image_url(width=1500, height=500),
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
    # Generate fake tweet data associated with a user
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
            "tweet_image_url": "https://randomfox.ca/", #fake.image_url(width=400, height=400),
        }
    # Generate fake comments for a tweet
    def generate_fake_comment(self, tweet_id, user_id):
        return {
            "comment_id": self.fake.uuid4(),
            "tweet_id": tweet_id,
            "user_id": user_id,
            "text": self.fake.sentence(nb_words=15),
            "created_at": str(self.fake.date_time_between(start_date='-2y', end_date='now')),
        }
    # Generate fake likes for a tweet
    def generate_fake_like(self, tweet_id, user_id):
        return {
            "like_id": self.fake.uuid4(),
            "tweet_id": tweet_id,
            "user_id": user_id,
            "created_at": str(self.fake.date_time_between(start_date='-2y', end_date='now')),
        }
    # Generate fake retweets for a tweet
    def generate_fake_retweet(self, tweet_id, user_id):
        return {
            "retweet_id": self.fake.uuid4(),
            "tweet_id": tweet_id,
            "user_id": user_id,
            "created_at": str(self.fake.date_time_between(start_date='-2y', end_date='now')),
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
 
class InstaGram:
  def __init__(self):
    self.fake = Faker()
    # Generate fake Twitter user data
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
      "comment_id":self.fake.uuid4(),
      "user": user_id,
      "post": post_id,
      "comment": self.fake.text(max_nb_chars=200),
      "likes": random.randint(0, 50000),
      "created_at": str(self.fake.date_time_between(start_date='-2y', end_date='now')),
    }
  # Generate fake likes for a post
  def generate_like(self, post_id, user_id):
    return {
      "like_id": self.fake.uuid4(),
      "post_id": post_id,
      "user_id": user_id,
      "created_at": str(self.fake.date_time_between(start_date='-2y', end_date='now')),
        }
  # Generate fake retweets for a post
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
  # Generate a list of posts and their interactions for a user
  def generate_post_and_interactions(self, user_id, post_count=10):
    posts = []
    comments = []
    likes = []
    reposts = []
    
    for _ in range(post_count):
      post = self.generate_post(user_id)
      posts.append(post)
      # Generate interactions for each post
      num_comments = random.randint(0, 10)
      num_likes = random.randint(0, 100)
      num_reposts = random.randint(0, 50)
      comments.extend([
        self.generate_comment(post['post_id'], user_id) for _ in range(num_comments)
        ])
      likes.extend([self.generate_like(post['post_id'], user_id) for _ in range(num_likes)])
      reposts.extend([self.generate_repost(post['post_id'], user_id) for _ in range(num_reposts)])
      return posts, comments, likes, reposts
    
  # Generate a list of fake InstaGram users and their associated posts and interactions
  def generate_fake_user_data(self, user_count=10, posts_per_user=5):
      users = []
      all_posts = []
      all_comments = []
      all_likes = []
      all_reposts = []

      for _ in range(user_count):
          user = self.generate_user()
          users.append(user)

          user_posts, user_comments, user_likes, user_reposts = self.generate_post_and_interactions(user['user_id'], post_count=posts_per_user)

          all_posts.extend(user_posts)
          all_comments.extend(user_comments)
          all_likes.extend(user_likes)
          all_reposts.extend(user_reposts)

      return users, all_posts, all_comments, all_likes, all_reposts

#save the fake user profile to a file
def save_user_data(fake_user,filename="fake_data.json"):
  with open(filename, "w") as file:
    json.dump(fake_user, file)
