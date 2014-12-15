# coding=utf8
"""
launchpad.py - Willie Github Module
"""
from __future__ import unicode_literals

from datetime import datetime
import sys
if sys.version_info.major < 3:
    from urllib2 import HTTPError
else:
    from urllib.error import HTTPError
import json
from willie import web, tools
from willie.module import commands, rule, NOLIMIT
import os
import re

from launchpadlib.launchpad import Launchpad
cachedir = "/Users/NobodyCam/.willie/lpcache"

@rule(u'$nickname[,:]\s+("is there a bug about")+\s')
def findIssue(bot, trigger):
    """Search for a launchpad bug by keyword or ID. usage: .findissue search keywords/ID (optional) You can specify the first keyword as "CLOSED" to search closed issues."""
    if not trigger.group(2):
        return bot.reply('What are you searching for?')

    launchpad = Launchpad.login_anonymously('just testing', 'production', cachedir)
    bug_one = launchpad.bugs[1]
    
    try:
        if firstParam.isdigit():
            data = bug_one.title
        else:
            data = bug_one.title
    except (KeyError, IndexError):
        return bot.say('No search results.')
    try:
        if len(data['body'].split('\n')) > 1:
            body = data['body'].split('\n')[0] + '...'
        else:
            body = data['body'].split('\n')[0]
    except (KeyError):
        bot.debug(
            'GitHub KeyErr',
            ('API returned an invalid result on query request ' +
             trigger.group(2)),
            'always')
        bot.say('Invalid result, please try again later.')
        return NOLIMIT
    bot.reply('[#%s]\x02title:\x02 %s \x02|\x02 %s' % (data['number'], data['title'], body))
    bot.say(data['html_url'])


@rule('.*(\\s+)*')
def issue_info(bot, trigger, match=None):
    match = match or trigger
    search_for_raw = match.group(0)
    search_for_list = search_for_raw.split()
    search_for = search_for_list[6]
    bot.say("Okay let me Search for bugs with %s" % search_for)
    launchpad = Launchpad.login_anonymously('just testing', 'production', cachedir)
    lp = launchpad.projects['ironic']

    bugs = lp.searchTasks(status = ['New', 'Incomplete', 'Triaged', 'Opinion', 'Invalid', 'Won\'t Fix', 'Confirmed', 'In Progress', 'Fix Committed', 'Fix Released'])

    for bug in bugs:
        if search_for in bug.title:
            bot.say('found: %s' % bug.title)
    bot.say("That's all I found.")
