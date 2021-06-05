import dbcreds
import mariadb
import traceback
conn = mariadb.connect(database=dbcreds.database, host=dbcreds.host,
                       port=dbcreds.port, user=dbcreds.user, password=dbcreds.password)

cursor = conn.cursor()
cursor.execute("SELECT * FROM blog_post")


def get_username():
    return input("Please enter your username: ")


def get_posts():
    cursor.execute("SELECT username, content FROM blog_post")
    all_posts = cursor.fetchall()
    print(all_posts)


username = get_username()


def create_post():
    cursor.execute(
        f"INSERT INTO blog_post(username, content) VALUES('{username}','{post_content}')")
    conn.commit()


while True:
    try:
        selection = int(input(
            f"Hello {username}. Please select from the following options: \n 1. Make a post \n 2. See all posts \n Your selection: "))
        if selection == 1:
            post_content = input("Please write your blog post below:\n")
            # if post_content is input by the user, run the fn create_post
            if post_content:
                create_post()
        elif selection == 2:
            get_posts()

        else:
            print("I specifically said 1 or 2.... :)")
            continue
        break
    except ValueError:
        # this else makes ctrl c stop working in the terminal after I input a letter...
        # but.... it doesn't matter since we won't be using the terminal for this IRL right?
        print("Plz... just enter 1 or 2.....")
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
