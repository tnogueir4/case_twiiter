import mysql.connector
import logging
from flask import Flask, make_response, jsonify, request


mydb = mysql.connector.connect(
    host='my_db',
    user='root',
    password='pw',
    database='social_media'
)

logging.basicConfig(filename='record.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

#######################################
# Definitions for the API /USERS/FOLLOWERS/TOP5
@app.route('/USERS/FOLLOWERS/TOP5', methods=['GET'])
def get_followers():
    
    my_cursor = mydb.cursor()
    my_cursor.execute('SELECT user_name, user_followers_count FROM top_user_followers ORDER BY user_followers_count DESC LIMIT 5')
    top_followers = my_cursor.fetchall()
    
    follow = list()
    for followers in top_followers:
        follow.append(
            {
                'username': followers[0],
                'followers': followers[1]
            }
        )
    
    return make_response(
        jsonify(
            mensagem='Top 5 users by followers',
            dados=follow
        )
    )

@app.route('/')
def main():
  # showing different logging levels
  app.logger.debug("debug log info")
  app.logger.info("Info log information")
  app.logger.warning("Warning log info")
  app.logger.error("Error log info")
  app.logger.critical("Critical log info")
  return "testing logging levels."

#######################################
# Definitions for the API /USERS/FOLLOWERS/TOP5/ADD
@app.route('/USERS/FOLLOWERS/TOP5/ADD', methods=['POST'])
def create_followers():
    followers = request.json
    
    my_cursor = mydb.cursor()
    sql = f"INSERT INTO top_user_followers (user_name, user_followers_count) VALUES ('{followers['username']}',{followers['followers']})"
    my_cursor.execute(sql)
    mydb.commit()
    
    return make_response(
        jsonify(
            mensagem='Inserted record',
            followers=followers
        )
    )

#######################################
# Definitions for the API /USERS/FOLLOWERS/TOP5/DEL
@app.route('/USERS/FOLLOWERS/TOP5/DEL', methods=['DELETE'])
def delete_followers():
    followers = request.json
    
    my_cursor = mydb.cursor()
    sql = f"DELETE FROM top_user_followers WHERE user_name = '{followers['username']}' AND {followers['followers']}"
    my_cursor.execute(sql)
    mydb.commit()
    
    return make_response(
        jsonify(
            mensagem='Record deleted',
            followers=followers
        )
    )
    
#######################################
# Definitions for the API /USERS/POSTS/COUNT
@app.route('/USERS/POSTS/COUNT', methods=['GET'])
def get_countposts():
    
    my_cursor = mydb.cursor()
    my_cursor.execute('SELECT DISTINCT created_at, num_posts FROM all_posts_by_datetime')
    count_posts = my_cursor.fetchall()
    
    ctposts = list()
    for cposts in count_posts:
        ctposts.append(
            {
                'created_at': cposts[0],
                'count_posts': cposts[1]
            }
        )
    
    return make_response(
        jsonify(
            mensagem='Count posts by datetime',
            dados=ctposts
        )
    )

#######################################
# Definitions for the API /USERS/POSTS/COUNT/CLEAN
@app.route('/USERS/POSTS/COUNT/CLEAN', methods=['DELETE'])
def reset_countposts():
    
    my_cursor = mydb.cursor()
    sql = f"DELETE FROM all_posts_by_datetime"
    my_cursor.execute(sql)
    mydb.commit()
    
    return make_response(
        jsonify(
            mensagem='All route data /countposts has been deleted.'
        )
    )
    
#######################################
# Definitions for the API /USERS/POSTS/TAGS/LOCALE
@app.route('/USERS/POSTS/TAGS/LOCALE', methods=['GET'])
def get_posttaglocale():
    
    my_cursor = mydb.cursor()
    my_cursor.execute('SELECT num_posts, text_hashtags, user_location FROM post_tag_per_location WHERE user_location <> "" ORDER BY text_hashtags')
    ptlocale = my_cursor.fetchall()
    
    pt_locale = list()
    for rs_locale in ptlocale:
        pt_locale.append(
            {
                'count_posts': rs_locale[0],
                '#tags': rs_locale[1],
                'user_location': rs_locale[2]
            }
        )
    
    return make_response(
        jsonify(
            mensagem='Total posts per #tags by user location',
            dados=pt_locale
        )
    )

#######################################
# Definitions for the API /USERS/POSTS/TAGS/LOCALE/CLEAN
@app.route('/USERS/POSTS/TAGS/LOCALE/CLEAN', methods=['DELETE'])
def reset_posttaglocale():
    
    my_cursor = mydb.cursor()
    sql = f"DELETE FROM post_tag_per_location"
    my_cursor.execute(sql)
    mydb.commit()
    
    return make_response(
        jsonify(
            mensagem='All route data /posttaglocation has been deleted.'
        )
    )
if __name__ == '__main__':
  app.run(debug=True)