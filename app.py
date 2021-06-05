import dbcreds
import mariadb
import traceback
# I might currently be thinking: but Alex, if we change a thing in the dbeaver file for
# bonus 2 to have a user_id as an FK to users instead of a username, how will you be able
# to use this code with the dbeaver downloadable file you provided us?
# And Alex would say: You're right! But.......
# ..........I'm thinking something along the lines of innerjoin so I'll try that
conn = mariadb.connect(database=dbcreds.database, host=dbcreds.host,
                       port=dbcreds.port, user=dbcreds.user, password=dbcreds.password)
# creating cursor to execute queries on the DB
cursor = conn.cursor()
cursor.execute("SELECT * FROM blog_post")


# would creating a user and their posts be a good time to make a class
# I'm confused about when it's overkill/not
def get_username():
    return input("Please enter your username: ")


def get_posts():
    # execute runs the sql
    cursor.execute("SELECT username, content FROM blog_post")
    # fetchall to get all posts
    all_posts = cursor.fetchall()
    print(f"All users' posts: {all_posts}")


def create_post():
    cursor.execute(
        f"INSERT INTO blog_post(username, content) VALUES('{username}','{post_content}')")
    print("Your post was created!")
    # need to commit when changing data
    conn.commit()

# working on 2 plz ignore
# def login_user(username, pw):


while True:
    try:
        # working on 2 plz ignore print("Welcome to Ze Blog. Please login:")
        # working on 2 plz ignore        username = input("Username: ")
        # working on 2 plz ignore        input("Password:")
        username = get_username()
# working on 2 plz ignore        password = input("Password:")
        selection = int(input(
            f"Hello {username}. Please select from the following options: \n 1. Make a post \n 2. See all posts \n 3. Exit \n Your selection: "))
        if selection == 1:
            post_content = input("Please write your blog post below:\n")
            # if post_content is input by the user, run the fn create_post
            if post_content:
                create_post()
                # lol I don't think this is what you meant by bonus 1 but.... it worked?
                continue
        elif selection == 2:
            get_posts()
            continue
        elif selection == 3:
            break
        # I think this else makes ctrl c stop working in the terminal after I input a letter...
        # but.... it doesn't matter since we won't be using the terminal for this IRL right?
        # or would I use an exception here somehow...the traceback says beyboard interrupt
        else:
            print("I specifically said 1, 2 or 3.... :)")
            continue
        break
    except ValueError:
        print("Plz... just enter 1, 2 or 3.....")
    except:
        print("Sorry something went wrong")
        traceback.print_exc()


# if try cursor.close is here (outside of above try block),
# we ALWAYS try to close it. so the cursor actually closes, even if above errors
try:
    cursor.close()
except:
    print("Error in closing cursor")
    traceback.print_exc()
# same not as above
try:
    conn.close()
except:
    print("Error in closing connection")
    traceback.print_exc()
