import praw
import datetime
import random 

def main():
    reddit = praw.Reddit(client_id = '',
                         client_secret = '',
                         username = '',
                         password = '',
                         user_agent = 'praw tutorial',)

    subreddit = reddit.subreddit('analog')
    hot_python = subreddit.hot(limit = 5)

    print(subreddit.title)
    for submission in hot_python:
        if not submission.stickied:
            print(str(submission.ups) + " " + submission.title)
            print()

if __name__ == '__main__':
    main()