# WelcomeBot

A bot written for the Techers Discord Server to let people with the "Welcomer" role know when someone joins the server. 

Please note: A valid Discord API token is needed. Put it in on the last line in place of `token_here`

The contents of `joinMessages.json` are taken from Discord as a list of possible join messages.

Files in the `HallowsEve` folder allow integration with the Trick\`cordTreat bot such that WelcomeBot will detect when the bot posts a new visitor, allowing the host client to run a AutoHotKey script. The AHK scripts in this file need to be compiled to `.exe` files before the bot is run. This bot is a standalone application that interfaces with the same API token in production, but can be run completely standalone.