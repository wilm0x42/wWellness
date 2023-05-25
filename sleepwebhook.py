#!/usr/bin/env python3

import sys
import random
import requests

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print(
            "Usage: sleepwebhook.py <@someone's discord ID> https://discord.com/your/webhook/url"
        )
        exit(1)
    ping = sys.argv[
        1]  # Use format "<@336685325231325184>" to have it actually ping
    discord_url = sys.argv[2]
    sleep_lines = []
    with open("sleep_lines.txt") as f:
        sleep_lines = f.readlines()
    for line in sleep_lines:
        line.replace("{ping}", ping)

    data = {
        "content": random.choice(sleep_lines),
        "username": "Wellness Board"
    }

    # this is the part where you get the chance to see a *rare* message :)
    if random.random() <= 0.002:
        # override message to be just the ping followed by the image
        data = {
            "content": ping,
        }
        result = requests.post(discord_url, json=data)
        data[
            "content"] = "https://cdn.discordapp.com/attachments/430078268037660686/899758205901635604/unknown.png"

    result = requests.post(discord_url, json=data)

    print("Yeet")
