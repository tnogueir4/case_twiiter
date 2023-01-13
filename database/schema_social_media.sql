DROP DATABASE IF EXISTS social_media;

CREATE database social_media;
use social_media;

DROP TABLE IF EXISTS tweet;

CREATE TABLE tweet
(
    id INTEGER AUTO_INCREMENT,
    search_val VARCHAR(25),
    created_at DATETIME,
    tweet_id VARCHAR(30),
    text TEXT(280),
    text_hashtags VARCHAR(25),
    source TEXT(100),
    in_reply_to_status_id VARCHAR(50),
    in_reply_to_user_id VARCHAR(50),
    in_reply_to_screen_name VARCHAR(20),
    user_name VARCHAR(50),
    user_screen_name VARCHAR(25),
    user_location VARCHAR(50),
    user_url VARCHAR(50),
    user_description TEXT(180),
    user_verified VARCHAR(5),
    user_followers_count INT(5),
    user_friends_count INT(5),
    user_listed_count INT(5),
    user_favourites_count INT(3),
    user_created_at DATETIME,
    user_id VARCHAR(50),
    user_profile_image_url_https TEXT(150),
    coordinates_lat VARCHAR(25),
    coordinates_lon VARCHAR(25),
    place_country VARCHAR(15),
    place_country_code VARCHAR(15),
    place_full_name VARCHAR(25),
    place_id INT(10),
    place_type INT(10),
    quoted_status_id VARCHAR(50),
    retweeted_status VARCHAR(10),
    quote_count INT(10),
    reply_count INT(10),
    retweet_count INT(10),
    favorite_count INT(10),
    retweeted VARCHAR(20),
    entities TEXT,
    lang VARCHAR(20),
    feeds_link TEXT(120),
    feeds_video TEXT(120),
    feeds_image TEXT(120),
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS top_user_followers;

CREATE TABLE top_user_followers
(
    id INTEGER AUTO_INCREMENT,
    user_name VARCHAR(50),
    user_followers_count INT(5),
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS all_posts_by_datetime;

CREATE TABLE all_posts_by_datetime
(
    id INTEGER AUTO_INCREMENT,
    num_posts INT(5),
    created_at DATETIME,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS post_tag_per_location;

CREATE TABLE post_tag_per_location
(
    id INTEGER AUTO_INCREMENT,
    num_posts INT(5),
    text_hashtags VARCHAR(25),
    user_location VARCHAR(50),
    PRIMARY KEY (id)
);