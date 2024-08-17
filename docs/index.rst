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

  generate_fake_user()

  #returns a fake user object 
  {
  "user_id": "263705fa-3689-4f7a-a2bc-2e38754d5a75",
  "username": "yhayes",
  "name": "Ronald Lewis",
  "bio": "Pay month center simple sort ten make. Number bar arrive simply along look economic. Policy tonight training.",
  ......
  }


  - *generate_fake_tweet*

.. code-block:: python

  generate_fake_tweet(user_id: str)

  #returns a fake tweet object
  {
  'tweet_id': 'cab09fc9-ad86-472e-ab84-c11decc1b3d4',
  'user_id': '263705fa-3689-4f7a-a2bc-2e38754d5a75',
  'text': 'Plan name for without receive machine even serious management view town line term past safe deep book difference here next cover sell reflect.',
  .......
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
