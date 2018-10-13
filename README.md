# TwitterBot
## Overview
The objective of this is to gather a large number of Tweets via Twitter API and then perform statistical analysis on them. I am using the [Tweepy](https://github.com/tweepy/tweepy) library and Python to gather them. Originally, I was going to perform this all on the same machine, but after more thinking, I decided to make a second computer for this and do it with a GPU-Accelerated Database, more specifically [OmniSci](https://www.omnisci.com/), previously known as MapD.
## Goals
My initial goal was to get more API work and improve my SQL knowledge. I wanted to attempt to work on a big data project due to the popularity of it, and it also seems interesting to create associations with data that might not seem obvious
## Progress Currently
Currently the collection process is working, and bulk inserting them via SQL into a local database is working. However, this was before I decided to use OmniSci, so I will need to rewrite the SQL connections and figure out new drivers as it is based in Linux as opposed to Windows 10
## Next Steps
Next step is to fully set-up a Linux distro (currently thinking about CentOS) and get OmniSci working. I did at one point have this done, but I replaced my hard drive and decided to start over to get practice with Linux.<br/><br/>
After that, I then need to figure out how OmniSci works and import the tweets into a table. Then I will need to work on the SQL. Due to the size of this, I will also need to optimize my queries as I was gathering between .5-2 million tweets per day.
## Extended Goals
When planning this project, I wanted to attempt to discover something interesting. I was looking up the estimated [word frequencies](https://www.wordfrequency.info/free.asp?s=y) of the English language, and was interested how Tweets would reflect this. This is a lot of statistical work and going to be a lot of calculations needed to be made (assumingly via SQL), so it is a goal that may take a lot of time, but I will be learning a lot along the way<br/><br/>
Another goal would be to have this display on a website in real (or cached but updated frequently) time. This way I can use something like R or a JavaScript library since I don't have any current experience with either of them.
