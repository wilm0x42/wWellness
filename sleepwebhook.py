#!/usr/bin/env python3

import sys
import random
import requests

if __name__ == "__main__":
	
	if len(sys.argv) < 3:
		print("Usage: sleepwebhook.py <@someone's discord ID> https://discord.com/your/webhook/url")
	else:
		ping = sys.argv[1] # Use format "<@336685325231325184>" to have it actually ping
		discordUrl = sys.argv[2]

		sleepLines = [
			"Hey %s, go to bed." % ping,
			"%s, it is advisable that you attempt to sleep soon." % ping,
			"Yo %s, the land of  s l e e p  awaits" % ping,
			"%s bed time" % ping,
			"You know they'll be looking for dudes up past their bed time %s" % ping,
			"%s Hey, if you stay up much later, you may risk heckin' up your sleep schedule." % ping,
			"%s Just want to remind you of how bad it feels to not get a good night's sleep, and that you can try to prevent that by going to bed now instead of later." % ping,
			"%s It is time to let the  m e l a t o n i n  start getting your mind and body  mela_toned_ down." % ping,
			"Hey everyone, please get mad at %s if they don't go to bed soon." % ping,
			"BED TIME **ALERT**\n%s IS NEARING THEIR APPOINTED TIME TO REST." % ping,
			"%s Yeah, being awake is cool and all, but sleeping makes being awake _even better_ tomorrow." % ping,
			"%s Imagine being up past your bedtime" % ping,
			"%s, my friend, you and I both know that you need sleep. Take care of yourself, please." % ping,
			"%s :clock: :bed: :zzz:" % ping,
			"%s Aaight, time to hug everyone and go to bed." % ping,
			"%s It's okay to stretch your sleep cycle a little bit sometimes, but *please* don't make it a habit. Get the rest you need." % ping,
			"Get a load of this %s character, being up this late." % ping,
			"%s sleeeeeeeeeeeeep" % ping,
			"%s sheep lime" % ping,
			"%s Unless you're desperately racing a deadline, what you're doing will still be there tomorrow, so chill and get some sleep. <3" % ping,
			"All in favor of %s going to bed now so they get enough sleep say aye" % ping,
			"%s May I recommend https://www.youtube.com/watch?v=UfcAVejslrU to help you wind down so you can get to bed" % ping,
			"%s If things have been going as expected, then you've been awake for approximately 14-16 hours at this point. You've earned yourself some rest." % ping,
			"%s You're late for your 8-hour sleep appointment." % ping,
			"%s You may not _think_ you need to go to bed now, but you probably do." % ping,
			"%s Being nice to your current self is good, but being nice to your future self is important too, and I bet your future self will appreciate having gotten a full night's sleep." % ping,
			"%s i will be VEWWY sad if you don't go to bed soon uwu" % ping,
		]

		data = {
			"content" : random.choice(sleepLines),
			"username" : "Wellness Board"
		}
		
		# this is the part where you get the chance to see a *rare* message :)
		if random.randint() % 500 == 0:
			data["content"] = "https://cdn.discordapp.com/attachments/430078268037660686/899758205901635604/unknown.png"
		
		result = requests.post(discordUrl, json=data)
		
		print("Yeet")
