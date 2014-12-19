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

@rule(u'$nickname[,:]\s+is there a bug about\s+(.*)')
def findIssue(bot, trigger):
    """Search for a launchpad bug by keyword or ID. usage: .findissue search keywords/ID (optional) You can specify the first keyword as "CLOSED" to search closed issues."""
    if not trigger.group(1):
        return bot.reply('What bug are you searching for?')


@rule('$nickname[,:]\s+is there a bug about\s+(.*)')
def issue_info(bot, trigger, match=None):
    match = match or trigger
    
    search_for_raw = match.group(1)
    bot.say("Okay let me Search for bugs with %s" % search_for_raw)
    launchpad = Launchpad.login_anonymously('just testing', 'production', cachedir)
    lp = launchpad.projects['ironic']

    bugs = lp.searchTasks(status = ['New', 'Incomplete', 'Triaged', 'Opinion', 'Invalid', 'Won\'t Fix', 'Confirmed', 'In Progress', 'Fix Committed', 'Fix Released'])

    for bug in bugs:
        if search_for_raw in bug.title:
            bot.say('found: %s' % bug.title)
    bot.say("That's all I found.")


@rule('https://bugs.launchpad.net/ironic/+bug/(.*)')
def bug_link_info(bot, trigger, match=None):
    match = match or trigger
    
    search_for_raw = match.group(1)
    launchpad = Launchpad.login_anonymously('just testing', 'production', cachedir)
    
    bug = launchpad.bugs[search_for_raw]
    bot.say(bug.title)