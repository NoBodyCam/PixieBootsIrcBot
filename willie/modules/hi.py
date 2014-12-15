# coding=utf8
"""
seen.py - Willie Seen Module
Copyright 2008, Sean B. Palmer, inamidst.com
Copyright © 2012, Elad Alfassa <elad@fedoraproject.org>
Licensed under the Eiffel Forum License 2.

http://willie.dftba.net
"""
from __future__ import unicode_literals

import time
import datetime
from willie.tools import Ddict, Nick, get_timezone, format_time
from willie.module import commands, rule, priority

seen_dict = Ddict(dict)


@rule(u'$nickname[,:]\s+(H|h)(I|i)')
@priority('low')
def hi(bot, trigger):
    """Responds to hi."""
    bot.reply("Hi there ")
    return
