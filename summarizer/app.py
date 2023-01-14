import mysql.connector
import json
import time

mydb = mysql.connector.connect(
  host="my_db",
  user="root",
  passwd="pw",
  database="social_media"
)

loop_app = 0
while loop_app < 1:

    mycursor = mydb.cursor()
    # - Summarize top 5 users with most followers
    
    mycursor.execute("SELECT DISTINCT user_name, user_followers_count FROM tweet ORDER BY user_followers_count DESC LIMIT 5")
    
    myresult = mycursor.fetchall()
    
    for rs in myresult:
        sql = "INSERT INTO top_user_followers (user_name, user_followers_count) VALUES (%s,%s)"
        val = (rs[0], rs[1])
        mycursor.execute(sql,val, multi=True)
    
    # - Summarize all posts per hour
    mycursor.execute("SELECT COUNT(text), created_at FROM tweet GROUP BY created_at")
    
    myresult = mycursor.fetchall()
    
    for rs in myresult:
        sql = "INSERT INTO all_posts_by_datetime (num_posts, created_at) VALUES (%s,%s)"
        val = (rs[0], rs[1])
        mycursor.execute(sql,val, multi=True)
    
    # - Summarize total posts for each #tags by user's language/country
    mycursor.execute("SELECT user_location, text_hashtags, count(text) FROM tweet GROUP BY user_location, text_hashtags ORDER BY user_location ASC;")
    
    myresult = mycursor.fetchall()
    
    for rs in myresult:
        sql = "INSERT INTO post_tag_per_location (user_location, text_hashtags, num_posts) VALUES (%s,%s,%s)"
        val = (rs[0], rs[1], rs[2])
        mycursor.execute(sql,val, multi=True)
    
    mydb.commit()
    mycursor.close()
    time.sleep(300) # - waits 5 minutes to perform a new summary
    print("Start new summarizer")
