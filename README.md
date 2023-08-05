# X_Twitter_Feed_Libre

Want to add Tweets to this list for your BRC20?

Fork this repo and submit a PR with a an array of Tweet(X) IDs added to append to the index.json here in this repo.

Example:

Here is a tweet - let's say I want to make this show for the token "BENN":
https://twitter.com/bensig/status/1687146117396406284


This can be done by typing:

`python add_tweet BENN https://twitter.com/bensig/status/1687146117396406284`

or 

`python add_tweet BENN 1687146117396406284`

Here is the data that will be added to the bottom of index.json:

```
  "BENN": [
    "1687146117396406284"
  ]
```

We will review and merge these PRs. Thanks!