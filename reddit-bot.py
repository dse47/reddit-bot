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

    for submission in hot_python:
        if not submission.stickied:
            print(submission.title)
            print()

if __name__ == '__main__':
    main()