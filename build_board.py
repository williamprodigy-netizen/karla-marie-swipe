#!/usr/bin/env python3
"""Karla Marie / Free Publishing Academy — the whole business, wired.

Run: python3 build_board.py  ->  board.html
"""
import sys, os
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from boardbuild import build, X

REPO = os.path.dirname(os.path.abspath(__file__))
S = os.path.expanduser("~/UNDERGROUND_FUNNELS_SSOT/01_RAW_FUNNELS")
P = f"{S}/Karla_Marie - Free_Publishing_Academy_Workshop - 2026-07-31/02_Pages"

CONFIG = {
    "OUT": os.path.join(REPO, "board.html"),
    "KICK": "Competitor swipe · captured 31 July 2026",
    "TITLE": "Karla Marie — the whole business, wired",
    "BLURB": "One mechanism: a daily &ldquo;live&rdquo; workshop that is actually a recording, "
             "selling AI-assisted Kindle publishing at $1,995. The mechanic worth stealing sits "
             "in the bonus stack &mdash; she pays members $500 for publishing their first ebook.",

    "SHOTS": {
        "optin": {
            "col": 1, "y": 120, "lane": "event", "step": "Entry · paid traffic",
            "title": "Workshop opt-in (fb-v2)",
            "url": "fpaworkshop.com/workshop-fb-v2",
            "img": f"{P}/01_Workshop_opt-in_fb-v2/20260731T103121Z__screenshot_fullpage.png",
            "max_h": 1000,
            "note": "&ldquo;Why Amazon is paying regular people $600 a day.&rdquo; First name, "
                    "last name, email and a <b>required phone</b>. Countdown to a 9:00 AM ET slot, "
                    "&ldquo;Join 4,847 others already registered&rdquo;.",
        },
        "waiting": {
            "col": 2, "y": 120, "lane": "event", "step": "Confirmation",
            "title": "Waiting room",
            "url": "fpaworkshop.com/waiting-room-fb-v2-1",
            "img": f"{P}/P2_optin_P2_20260731T115714Z/20260731T115815Z__s1_before__screenshot_fullpage.png",
            "max_h": 900,
            "note": "&ldquo;#1 Check your email for [Must Open] Your Ticket Confirmation. "
                    "#2 Save to your calendar and use your unique link to join.&rdquo;",
        },
    },

    "DATA": {
        "live": {
            "col": 3, "y": 120, "lane": "event", "step": "The pitch",
            "title": "&ldquo;LIVE&rdquo; workshop — 2h 00m",
            "kv": [("Advertised", "live, 9:00 AM ET daily"),
                   ("Actually", "pre-recorded Vimeo"),
                   ("Words", "20,890"), ("Frames", "346"),
                   ("Price reveal", "01:07:48"), ("Q&amp;A from", "01:34")],
            "note": "Same fake-live play as Richard Yu, different platform. "
                    "yt-dlp 403s on the player; the signed CDN URL from the network log works.",
        },
        "mech": {
            "col": 4, "y": 120, "lane": "ever", "step": "Mechanism",
            "title": "One hour, one book",
            "kv": [("Tool", "FictionPub AI"), ("Free credits", "2 books"),
                   ("After that", "$50 / 10,000 words"),
                   ("Paperback", "Amazon prints free")],
            "note": "She builds a book live on screen, then sells the shortcut to doing it "
                    "with her. Software consumption is the annuity behind the mentorship.",
        },
        "offer": {
            "col": 5, "y": 120, "lane": "event", "step": "Close",
            "title": "The offer — $1,995",
            "kv": [("Price", "$1,995"), ("Anchor", "$3,000"),
                   ("Framing", "save over $1,000"), ("Spots", "50 founding users"),
                   ("Coaching", "6&times; per week"), ("1-to-1 calls", "4"),
                   ("Modules", "6")],
            "note": "Verified on the slide. The transcript renders it &ldquo;$19.95&rdquo; "
                    "&mdash; a 100&times; error that the still caught.",
        },
        "bonus": {
            "col": 6, "y": 120, "lane": "back", "step": "Bonus stack",
            "title": "Seven bonuses",
            "kv": [("Bonus 1", "<b>$500 cash rebate</b>"),
                   ("Bonus 2", "free resort stay"),
                   ("Bonus 3", "first topic chosen"),
                   ("Bonus 4", "low-cost expert team"),
                   ("Bonus 6", "partner program"),
                   ("Bonus 7", "&ldquo;pampering&rdquo;")],
            "note": "She claims the bonus stack is worth as much as the program itself.",
        },
    },

    "EDGES": [
        ("optin", "waiting"), ("waiting", "live"),
        ("live", "mech"), ("mech", "offer"), ("offer", "bonus"),
    ],

    "LABELS": [
        {"x": X[1], "y": 60, "t": "Single mechanism — evergreen workshop"},
        {"x": X[1], "y": 1500, "t": "Routing logic"},
    ],

    "BRANCH": [
        {"id": "b_rebate", "x": X[1] + 10, "y": 1560, "state": "yes",
         "cond": "Buys → gets paid $500 back",
         "body": "The action-taker rebate pays <b>$500</b> to anyone who puts one ebook on "
                 "Kindle by her system. She shows screenshots of people receiving it and says "
                 "&ldquo;we love sending out this money because it benefits everyone.&rdquo; "
                 "It buys activation, manufactures fresh proof, and makes the refund "
                 "conversation moot because the member has already been paid.",
         "ev": "VERIFIED · webinar 01:19:10 &amp; 01:20:00, recipient screenshots shown"},
        {"id": "b_fake", "x": X[3] + 10, "y": 1560, "state": "dq",
         "cond": "The LIVE room is a recording",
         "body": "The room requests a Vimeo progressive file (id <code>1199947645</code>). "
                 "Registration says &ldquo;Today! Friday 31 July, 9:00 AM ET&rdquo; with a "
                 "live countdown, but the asset is static and dateless.",
         "ev": "VERIFIED · network capture 31 Jul · 2h00m16s pulled"},
        {"id": "b_resort", "x": X[5] + 10, "y": 1560, "state": "unver",
         "cond": "Buys → free resort stay",
         "body": "A third-party resort network gives registrants free room nights, betting they "
                 "will spend on site. She pre-empts the obvious suspicion out loud: "
                 "&ldquo;this definitely is not a timeshare thing.&rdquo; Naming the objection "
                 "the bonus creates is the move; the bonus itself invites the scepticism.",
         "ev": "UNVERIFIED · claimed on the webinar, redemption not tested"},
        {"id": "b_software", "x": X[7] + 10, "y": 1560, "state": "yes",
         "cond": "After 2 free credits → $50 per 10,000 words",
         "body": "The mentorship is the front end. Every book after the first two is a "
                 "software charge, so usage compounds into recurring revenue without a "
                 "subscription being sold.",
         "ev": "VERIFIED · stated in the Q&amp;A at 01:44:14"},
    ],

    "LEGEND": [("event", "Workshop mechanism"), ("ever", "Software"), ("back", "Bonus stack")],
}

if __name__ == "__main__":
    build(CONFIG)
