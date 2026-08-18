#!/usr/bin/env python3
"""Build the Karla Marie / Free Publishing Academy swipe site.

Run: python3 build_site.py
"""
import sys, os
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import build

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/Swipes/KARLA_MARIE_Swipe")

CONFIG = {
    "SITE": "Karla Marie — Free Publishing Academy",
    "CREATOR": "Karla Marie",
    "ADS_KEY": "karla_marie",
    "FUNNEL_IDS": ["F116"],
    "CAPTURED": "31 July 2026",
    "REPO": REPO,
    "PACKAGE": "~/Downloads/Swipes/KARLA_MARIE_Swipe",
    "BLURB": "A $1,995 Amazon-Kindle publishing offer sold to women off a daily "
             "&ldquo;live&rdquo; workshop that is actually a recording. The standout mechanic is "
             "a $500 cash rebate paid to anyone who publishes one ebook.",

    "PAGES": [
        ("index.html", "Overview"),
        ("analysis.html", "Analysis"),
        ("webinar.html", "Webinar slides"),
        ("transcripts.html", "Transcript"),
        ("videos.html", "Video library"),
    ],

    "STATS": [
        ("Price", "$1,995"),
        ("Anchor", "$3,000"),
        ("Webinar", "2h 00m"),
        ("Words", "20,890"),
        ("Frames", "346"),
        ("Bonuses", "7"),
        ("Rebate", "$500"),
        ("Spots claimed", "50"),
    ],

    "OFFER": [
        ("Product", "Free Publishing Academy — AI-assisted Kindle publishing"),
        ("Price", "<b>$1,995</b> one-time, verified on the slide at 01:07:48"),
        ("Anchor", "$3,000 normal price"),
        ("Discount framing", "&ldquo;Save over $1,000&rdquo;, webinar only"),
        ("Core deliverable", "6 modules, live group coaching 6&times;/week, 4 one-to-one calls, "
                             "private community, Bookmaker Vault"),
        ("Software", "FictionPub AI. 2 free book credits, then $50 per 10,000 words"),
        ("Scarcity", "&ldquo;50 founding user spots&rdquo;"),
        ("Bonus 1", "<b>$500 action-taker rebate</b> — cash back for publishing one ebook"),
        ("Bonus 2", "Free resort stay through a hotel network (taxes/surcharges excluded)"),
        ("Bonus 3", "First ebook topic chosen for you"),
        ("Bonus 4", "Direct access to a vetted team of low-cost experts"),
        ("Bonus 6", "Partner program membership"),
    ],

    "FINDINGS": [
        ("The $500 action-taker rebate",
         "She pays new members $500 for publishing a single ebook by her system, and shows "
         "screenshots of people receiving it. It buys activation, manufactures fresh proof, and "
         "defuses the refund conversation in one move. The strongest single mechanic in this "
         "swipe file."),
        ("The live workshop is a recording",
         "The room advertised as a daily live event at 9:00 AM ET serves a pre-recorded Vimeo "
         "file. Same play as Richard Yu, different platform."),
        ("Price is $1,995, not $19.95",
         "Whisper transcribed it as &ldquo;$19.95&rdquo;. The slide says <b>$1,995</b>. Worth "
         "flagging because the transcript alone would have propagated a 100&times; error."),
        ("Travel incentive instead of a discount",
         "Rather than cutting price further she bolts on a free resort stay sourced from a hotel "
         "network that wants empty rooms filled. She pre-empts the timeshare objection out loud."),
        ("The investment donut",
         "Before the price she shows a chart of &ldquo;our investment&rdquo; versus &ldquo;your "
         "investment&rdquo; as a giant ring with a hairline slice. The number lands after the "
         "visual has already framed it as trivial."),
        ("Software as recurring back end",
         "FictionPub AI gives two free credits then charges $50 per 10,000 words. The mentorship "
         "is the front end; consumption is the annuity."),
    ],

    "FUNNEL": [
        ("Workshop opt-in (fb-v2)", "fpaworkshop.com/workshop-fb-v2",
         "Requires first name, last name, email and <b>phone</b>. Countdown to a 9:00 AM ET slot."),
        ("Waiting room", "fpaworkshop.com/waiting-room-fb-v2-1",
         "Hands over the unique join link and a calendar add."),
        ("LIVE room", "event.webinarjam.com/4762v/go/live/…",
         '<span class="tag bad">pre-recorded</span> 2h00m Vimeo file'),
        ("Checkout", "shown on screen during the pitch",
         "Installments offered. Never submitted."),
    ],

    "TRANSCRIPT_GROUPS": [
        ("Webinar — 2h 00m", [os.path.join(PKG, "Transcript/webinar_transcript.md")]),
    ],

    "SLIDE_PAGES": [
        ("Webinar slides", "webinar.html", "Screenshots", "web_",
         "The full two-hour pitch. Price reveal at 01:07:48, bonus stack from 01:19."),
    ],

    "DECKS": [
        ("Webinar — the full 2h pitch", 299,
         "https://docs.google.com/presentation/d/1A2Q7sYqcva0sBLE_BI_JJNTOxqzGKp-A2sB8N5cv2bg/edit"),
    ],

    "VIDEOS": [
        ("karla_marie_webinar.mp4", 7218, "442 MB",
         "The evergreen &ldquo;live&rdquo; workshop. The entire pitch."),
    ],

    "ANALYSIS": """
<div class="note warn"><b>Read this first.</b> The workshop presented as live is a recording,
so the &ldquo;50 founding spots&rdquo; and the urgency around them are production choices.</div>

<h2 class="sec">The structure</h2>
<div class="tablewrap"><table>
<tr><th>Time</th><th>Beat</th><th>What she is doing</th></tr>
<tr><td>00:52</td><td>Mechanism</td><td>The &ldquo;one hour, one book&rdquo; framework and a live FictionPub build</td></tr>
<tr><td>00:56</td><td>Transition</td><td>&ldquo;You saw the framework — now here's the shortcut, with me&rdquo;</td></tr>
<tr><td>01:05</td><td>Stack</td><td>6 modules, coaching 6&times;/week, 4 one-to-ones, community, vault</td></tr>
<tr><td>01:07</td><td>Investment framing</td><td>Payroll costs, then the donut chart, then <b>$1,995</b></td></tr>
<tr><td>01:08</td><td>Sweetener</td><td>Doubles the free book credits from one to two, live</td></tr>
<tr><td>01:10</td><td>Travel bonus</td><td>Free resort stay, with the timeshare objection pre-empted</td></tr>
<tr><td>01:19</td><td>Rebate</td><td><b>$500</b> action-taker rebate plus receipts from past claimants</td></tr>
<tr><td>01:34</td><td>Q&amp;A</td><td>Editing quality, AI-isms, VAs, copyright, software cost</td></tr>
</table></div>

<h2 class="sec">Worth taking</h2>
<div class="grid g2">
<div class="card"><h3>Pay for the first action</h3><p>$500 to publish one ebook. For us the
equivalent is paying a new creator for landing their first brand deal or shipping their first
portfolio piece. It converts a refund-risk window into a proof-generation window, and it makes
the guarantee conversation moot because the member has already been paid.</p></div>
<div class="card"><h3>Sweeten live rather than discount</h3><p>She doubles the credits mid-pitch
instead of cutting price. The perceived value moves without touching the number.</p></div>
<div class="card"><h3>Visual before numeric</h3><p>The investment donut lands the emotional
comparison before the price is spoken. Cheap to reproduce in any deck.</p></div>
<div class="card"><h3>Objection pre-empted by name</h3><p>&ldquo;This definitely is not a
timeshare thing.&rdquo; She names the exact suspicion the bonus creates and kills it in one line.</p></div>
</div>

<h2 class="sec">Not worth taking</h2>
<p>The fake-live framing, and the resort bonus itself — it is a third-party lead-gen arrangement
dressed as generosity, and it invites precisely the scepticism she has to spend a minute of
pitch time defusing.</p>
""",
}

if __name__ == "__main__":
    build(CONFIG)
