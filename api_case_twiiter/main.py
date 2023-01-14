import mysql.connector
from flask import Flask, make_response, jsonify, request


mydb = mysql.connector.connect(
    host='my_db',
    user='root',
    password='pw',
    database='social_media'
)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

#######################################
# Definitions for the API /topfollowers
@app.route('/topfollowers', methods=['GET'])
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
    
@app.route('/topfollowers', methods=['POST'])
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
    
@app.route('/topfollowers', methods=['DELETE'])
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
# Definitions for the API /countposts
@app.route('/countposts', methods=['GET'])
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
    
@app.route('/countposts', methods=['DELETE'])
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
# Definitions for the API /posttaglocation
@app.route('/posttaglocation', methods=['GET'])
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
    
@app.route('/posttaglocation', methods=['DELETE'])
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
app.run()