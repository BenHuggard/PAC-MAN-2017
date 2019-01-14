import discord
#discord API

from bs4 import BeautifulSoup as soup
#HTML parsing

from discord.ext.commands import Bot
#discord bot command

import requests as rq
#grabbing HTMl

import wolframalpha as wa
#wa API

import wikipedia

discord_client = discord.Client()
#initializing discord client

wolfram_client = wa.Client('98662U-WP7PERLYUP')
#initializing wa client

def specific_counters_find(url, champ):
    #finds specific matchups between two champions
    global counter_table
    try:
        request = rq.get(url)
        html_info = soup(request.content, 'html.parser')
        counter_table = html_info.find('div', {"class": "block3 _all"})
        #gets table of all matchups
        try:
            champ_in_table = counter_table.find('a', {"href": "/champions/" + champ})
            return champ_in_table.parent.parent.parent['class']
        except:
            #if champ not in list
            return 'None'
    except:
        #if website not found
        return False

def wolfram_alpha(query):
    response = ''
    try:
        res = wolfram_client.query(query).results
        for item in res:
            for result in item.subpods:
                response += result['plaintext'] + '\n'
        return response
    except:
        return "(data not available)\n"

def wiki_summary(query):
    response = ''
    try:
        response = wikipedia.summary(query)
        #return 2000 char chunks to overcome discords 2000 char message limit
        return (response[0+i:2000+i] for i in range(0, len(response), 2000))
    except:
        return 0

def mastery_grab(champ, position):
    #gets three images with mastery info on them
    guides_url = "http://www.lolking.net/guides/champion/" + champ
    guide_request = rq.get(guides_url)
    for i in range(0, 15, 1):
        guide_title = soup(guide_request.content, 'html.parser').find("h2", {
            "style": "font: bold 20px 'Trebuchet Ms'; text-shadow: 0 0 1px #000; max-height: 52px; overflow: hidden;"})

        position_banner = guide_title.parent.parent.parent.find("div", {
            "style": "display: table-cell; padding: 0 1px 0 1px; vertical-align: top;"})
        if position_banner.div["class"] == "meta_flag meta_flag_" + position:
            url = "http://www.lolking.net" + guide_title.a["href"]
            break
        else:
            guide_title = guide_title.next_sibling()
    request = rq.get(url)

def scc_assemble(url, champ1, champ2):
    #creates response
    response = ''
    if specific_counters_find(url, champ2) == ['weak']:
        response = champ1 + ' is weak against ' + champ2 + '.\nhttp://lolcounter.com/champions/' + champ1
    elif specific_counters_find(url, champ2) == ['strong']:
        response = champ1 + ' is strong against ' + champ2 + '.\nhttp://lolcounter.com/champions/' + champ1


@discord_client.event
async def on_message(message):
    #lists functions
    if message.content.startswith('!dbhelp'):
        print('found')
        await discord_client.send_message(message.channel, "Commands:\n!lgc (champion): links to lolcounter site for champion\n")

    #links to lolcounter
    if message.content.startswith('!lgc'):
        print('detected')
        message_words = message.content.split()
        await discord_client.send_message(message.channel, 'http://lolcounter.com/champions/' + message_words[1])

    #finds specific matchups
    if message.content.startswith('!scc'):
        message_words = message.content.split()
        url = 'http://lolcounter.com/champions/' + message_words[1]
        print(specific_counters_find(url, message_words[2]))
        if specific_counters_find(url, message_words[2]) == ['weak']:
            await discord_client.send_message(message.channel, message_words[1] + ' is weak against ' + message_words[2] + '.\nhttp://lolcounter.com/champions/' + message_words[1])
        elif specific_counters_find(url, message_words[2]) == ['strong']:
            await discord_client.send_message(message.channel, message_words[1] + ' is strong against ' + message_words[2] + '.\nhttp://lolcounter.com/champions/' + message_words[1])
        elif specific_counters_find(url, message_words[2]) == ['even']:
            await discord_client.send_message(message.channel, message_words[1] + ' goes even with ' + message_words[2] + '.\nhttp://lolcounter.com/champions/' + message_words[1])
        elif specific_counters_find(url, message_words[2]) == ['well']:
            await discord_client.send_message(message.channel, message_words[1] + ' goes well with ' + message_words[2] + '.\nhttp://lolcounter.com/champions/' + message_words[1])
        elif specific_counters_find(url, message_words[2]) == 'None':
            await discord_client.send_message(message.channel, message_words[1] + ' is not weak or strong against ' + message_words[2] + '.\nhttp://lolcounter.com/champions/' + message_words[1])
        else:
            await discord_client.send_message(message.channel, "Not a champion!")
    #wolfram alpha simple responses
    if message.content.startswith('!wa'):
        response = wolfram_alpha(message.content[4:])
        if response == "(data not available)\n":
            response += ':('
        await discord_client.send_message(message.channel, "According to Wolfram Alpha...\n" + response)

    #wikipedia summaries
    if message.content.startswith('!wsum'):
        response = wiki_summary(message.content[6:])
        if response != '0':
            await discord_client.send_message(message.channel, "Wikipedia summarizes...\n")
            for chunk in response:
                await discord_client.send_message(message.channel, chunk)
        else:
            await discord_client.send_message(message.channel, "Not a valid page title\n")

discord_client.run("MzUwNzUxMzc5NjU4Mzc1MTk5.DIIneg.Z2rZUCvfGv9QtfsaxHxVJvxnNO8")
discord_client.close()