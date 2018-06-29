## Getting Anki

Download the most recent version from https://apps.ankiweb.net/

Make an account here http://ankiweb.net/
This will allow you to sync your data to their cloud for free. If you want to study on another device, you can then sync between devices. I do a lot of studying on my iphone...the iPhone app is $25 because the developer relies on that to fund the app. Totally worth it for me. The android app is free because it's an open source collaboration by people in the community.

## The information in the deck

Anki has a lot of knobs. But fundamentally, it's flashcards. Just, well, sometimes they can get fancy. I try to keep things simple, though. While I've gotten into modifying anki itself recently, I generally prefer to do the heavy lifting outside of anki when I actually generate the flashcards (some people go really overboard on their use of CSS and JS and stuff in Anki). As such, while I've included a package you can use, I included the process I used to generate it so you can change it around if wanted (or can tell me where you think it falls short and I can easily modify it).

First, the data itself. poem.txt.anki has a tab separated file that has all of the data. The columns will make more sense when we get to anki, but I will explain how I structured the studying. Going with what someone suggested, the python script splits each piece into 7 groups (though the final group is just "try and recite the while poem," though you can turn off the cumulative tests if desired). The idea is that you will study an 8 word chunk intensively for say an hour, then you will enable that group (though the first card in every group is the poem up to that point, as a review... this can be turned off if not desired!). So the idea is that you first study the first 8 lines of the poem, then there will be a bunch of cards. The cards will prompt you with 2 lines (configurable), and ask you to name the next line. It will do this for every line in the group. Then it will do the same, but ask you to name the next 2 lines (you can configure how many lines it goes up to). The idea is just to get better at chaining it all together. When you see whether you got it right or wrong, it will show another couple of lines to see it in context. This can all be changed, but I think it is reasonable. So the tab separated file just has this information in a way that we can surface and format nicely in anki. If you have any more questions about the nitty gritty, just ask.

## Using the deck

Open anki. Double-click the apkg file in this repo -- it should then focus on anki and there will be a deck.

The workflow I envision is this. As I said above, spend some time going over the first 8 lines. Once you've done that for a bit, start studying. The loaded cards will only be the first 8 lines (more on that in a sec). You'll want to go over all of these. Some notes: basically you'll only ever want to hit "Good." A lot of people don't like these options and there are plugins to remove them, but I don't think it's worth it. Hard can be used if you got it, but had to think for an extra long amount of time. Easy is if you would never ever forget it...perhaps useful if some of the studying gets repetitive later on, but I would caution you against using this until you have a better feel for the progress you are making.

Basically, whenever anki has a number under "due," you should open it up and go through the reviews. I'm happy to get into what I know about the algorithm (it's called spaced repetition), but basically at first it's just showing you the card according to a schedule I gave it. After that learning period, it will then use the space repetition algorithm to choose when to schedule it again.

![image](https://github.com/jcoveney/zenpoemanki/blob/master/images/options.png)

The numbers in Steps define a set of intervals that new cards will be shown in no matter what. If you get it wrong, it'll redo the step. Only when all the steps are done will it go to the SRS algorithm. The steps I've set for this is quite aggressive, in that it will generate quite a few reviews... 3 in the first day, then 1 for the next 4 days. This is because I imagine memorizing a poem like this is quite difficult, and since the overall number of cards isn't huge (93), I think a lot of repetition is going to be key. Then long-term, srs will handle making the number of reviews you need smaller and smaller. But early on, you're going to need to do lot's of reviews (though all told it's not THAT many... you can get through this few cards quite quickly).

![image](https://github.com/jcoveney/zenpoemanki/blob/master/images/options2.png)

For your knowledge, the lapses area is what happens when you fail a card that has already made it out of the initial steps. In this case, I again schedule it fairly aggressively. If you think it's too hard or too easy, let me know, and we can tweak accordingly. But all told it's not that many cards.

So, you will memorizing the passage of the current group (to start, the first 8 lines), then work through every card in that group. You'll use anki every day for at least 5 days while it schedules everything, and then you'll see how you feel. My thought was that every week you could do a new group. What does that mean? well, all of the pre-existing cards will still be in there. But you'll activate the cards related to the next 8 lines.

![image](https://github.com/jcoveney/zenpoemanki/blob/master/images/searching_for_group.png)

In the normal deck screen, click Browse. Then search for "deck:Sandokai tag:group2" (don't need quotes) and you'll see a bunch of yellow-colored lines. The yellow means these notes are suspended, which means they won't be scheduled. As before, once you've studied the corresponding 8 lines, you will go here, click ctrl+a to select all, then click "suspend" which will unsuspend them all. Then you work through all the new reviews. Continue this each week... see the next week, youd do group3, then group4, then group5, then group6, then group7. Note that group7 just has a card that has the entire poem. I was unsure whether this would be a good thing to do... you can generate the deck without it in python, or you can just delete the note! If you go to this screen (or in the review screen) you can delete notes. See how you feel about it :)

Oh and just for good measure, here is what you'll see when you are prompted:
![image](https://github.com/jcoveney/zenpoemanki/blob/master/images/what_youll_see.png)

And here is what happens when you hit space or enter and you see if you got it right:
![image](https://github.com/jcoveney/zenpoemanki/blob/master/images/when_you_hit_space.png)

The styling can all be changed... I prefer very simple cards, as I said before. But if you don't like the color blue for example, that can all be changed. I won't get into that here, just let me know if there's something you think should be different about, well, any of this.

Anki itself is super powerful. Notes, cards, plugins, etc can all be leveraged to do fancy things. But since we are both programmers, I often find it is easiest to just generate the data like this when possible!

Good luck!
