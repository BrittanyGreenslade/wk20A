import dbcreds
import mariadb
import traceback
conn = mariadb.connect(database=dbcreds.database, host=dbcreds.host,
                       port=dbcreds.port, user=dbcreds.user, password=dbcreds.password)

cursor = conn.cursor()
cursor.execute("SELECT * FROM blog_post")


def getUsername():
    return input("Please enter your username: ")


def getPosts():
    cursor.execute("SELECT username, content FROM blog_post")
    all_posts = cursor.fetchall()
    print(all_posts)


username = getUsername()
selection = int(input(
    f"Hello {username}. Please select from the following options: \n 1. Make a post \n 2. See all posts \n Your selection: "))


def createPost():
    cursor.execute(
        f"INSERT INTO blog_post(username, content) VALUES('{username}','{postContent}')")
    conn.commit()


try:
    if selection == 1:
        postContent = input("Please write your blog post below:\n")
        if postContent:
            createPost()
    elif selection == 2:
        getPosts()
except:
    print("Sorry something went wrong")
    traceback.print_exc()


# if try cursor.close is here (outside of above try block),
# we ALWAYS try to close it. so the actually connection closes, even if above errors
try:
    cursor.close()
except:
    print("Error in closing cursor")
    traceback.print_exc()
try:
    conn.close()
except:
    print("Error in closing connection")
    traceback.print_exc()
