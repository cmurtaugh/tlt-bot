#!/usr/bin/env python

from slackbot.bot import Bot
import logging

def main():
    logging.basicConfig(level=logging.DEBUG)
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()

    