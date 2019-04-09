# coding=utf-8
"""
gender.py - Random Gender Module

http://sopel.chat/
"""
from __future__ import unicode_literals, absolute_import, print_function, division
import random

import sopel.module

@sopel.module.commands("gender")
def gender(bot, trigger):
    """.gender, rolls dice and assigns a random gender.
    
    http://www.robot-hugs.com/gender-rolls/
    """
    parts = (
        [
            "Agender",
            "Genderqueer",
            "Trans",
            "Genderfluid",
            "Cis",
            "Non-binary",
            "Questioning",
            "Bigender"
        ],
        [
            "Dapper",
            "Femmetype",
            "Twinky",
            "Sophisticate",
            "Androgenous",
            "Leather",
            "Flexible",
            "Soft",
            "Queerdo",
            "Nonconforming"
        ],
        [
            "Princex",
            "Dragon",
            "Beefcake",
            "Shortcake",
            "Dudebro",
            "Gentleperson",
            "Cumberbatch",
            "Butch",
            "Bear",
            "Dandy",
            "Otter",
            "Queen"
        ]
    )

    gender_result = " ".join([random.choice(p) for p in parts])
    bot.reply("You rolled {}".format(gender_result))

if __name__ == "__main__":
    from sopel.test_tools import run_example_tests
    run_example_tests(__file__)
