#Activity 3.2.2 Step 7
from Post import Post

all_posts_archive = []

username = input("What do you want your username to be?")
print("Welcome  " + username)
# your code here
post1 = Post("Marie", "This is my first post!")
post2 = Post("Brandon420", "Yo man I just bought twitter for 4.2069 Bitcoin!")
post3 = Post("elon_musk", "Word? I did the same thing!")


user_input = input(""" What would you like to do?
"add" - Add a post to the archive
"remove" - Remove a post from the archive
"change user" - Change the user name associated with any future posts
"print" - Display the current up to date list of all posts
"quit" - End the program
""")

while (user_input != "quit"):
    # what will happen if the user doesn't enter quit
    # Notice this is tabbed over. This represents the body of
    # the while loop.
    if user_input == 'add':
        message = input("what data would you like to post?")
        all_posts_archive.append(Post(username, message))

    elif user_input == "remove":
        index = input("What is the index of what you want to remove?")
        del all_posts_archive[int(index)]

    elif user_input == "change user":
        username = input("What is your new username?")

    elif user_input == "print":
        for post in all_posts_archive:
            print(post)

    else:
        user_input = input("Maybe try that again? that method doesn't exist.")

    user_input = input(""" What would you like to do?
    "add" - Add a post to the archive
    "remove" - Remove a post from the archive
    "change user" - Change the user name associated with any future posts
    "print" - Display the current up to date list of all posts
    "quit" - End the program
    """)