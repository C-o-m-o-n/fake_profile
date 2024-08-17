.. fake_profile documentation master file, created by
   sphinx-quickstart on Fri Aug 16 08:52:37 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

fake_profile documentation
==========================

fake_profile is a Python package for generating fake social media profiles, posts, interactions, and more for Twitter, LinkedIn, Instagram, and Facebook. This tool is ideal for developers who need to create dummy data for testing or demo purposes.

Features
--------

- Generate complete user profiles for Twitter, LinkedIn, Instagram, and Facebook.
- Create posts, tweets, comments, likes, and retweets associated with each profile.
- Customize the data generated with specific parameters.
- Use the generated data in testing environments or for populating mock databases.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Installation
------------

To install fake_profile, use pip:

.. code-block:: bash

    pip install fake-profile
  
Classes and Methods
-------------------

- **Class Xprofile**

  - *generate_fake_user*

.. code-block:: python

  generate_fake_user() -> {
  user_id,
  username,
  name,
  bio,
  location,
  url,
  profile_image_url,
  banner_image_url,
  join_date,
  verified_status,
  follower_count,
  following_count,
  tweet_count,
  likes_count,
  list_memberships,
  timezone,
  language,
  protected_status,
  suspended_status,
  default_profile,
  default_profile_image
          }

Usage
-----

Here's a quick example of how to use fake_profile to generate a Twitter user profile and some tweets:

.. code-block:: python

  from fake_profile import Xprofile
  generator = Xprofile()

  # Generate Twitter data
  users, tweets, comments, likes, retweets = generator.generate_fake_twitter_data(user_count=5, tweets_per_user=3)
  
  print(users)
  print(tweets)
  print(comments)
  print(likes)
  print(retweets)

Refer to the Usage section for more detailed examples and use cases.

Further Reading
---------------

- For more detailed examples, see the Usage section.
- Learn about the underlying concepts in the Concepts section.
- See the Installation section for help with installation.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`