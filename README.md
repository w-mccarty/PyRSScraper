# PyRSScraper
RSS scraper with pre-tagged html output designed to be easily formatted and embedded.


**Requires:**

- Feedparser - https://pypi.org/project/feedparser/
- Unidecode - https://pypi.org/project/Unidecode/
- Eventlet - https://pypi.org/project/eventlet/
- pytz - https://pypi.org/project/pytz/
- dateutil - https://pypi.org/project/python-dateutil/
- ```mkdir /var/www/html/rss/```

**spits out html in the following format:**

from https://www.reddit.com/r/technology/hot.rss
```
<div id="rssheadlink">Reddit Technology</div><div id="rssheadupdate">Last updated: 17:02,07-18-2024</div><div id="fdiv_26_20240718182105000013" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_13">07-18</div><div class="tfeed_day rsslink" id="rsslink_26_13"><a href="https://www.reddit.com/r/technology/comments/1e6i5mu/exclusive_usps_shared_customer_postal_addresses/" target="_blank">Exclusive: USPS shared customer postal addresses with Meta, LinkedIn and Snap</a></div><br></div>
<div id="fdiv_26_2024071818152200005" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_5">07-18</div><div class="tfeed_day rsslink" id="rsslink_26_5"><a href="https://www.reddit.com/r/technology/comments/1e6i03b/teslas_california_registrations_fell_24_in_second/" target="_blank">Tesla's California registrations fell 24% in second quarter, dealer data shows</a></div><br></div>
<div id="fdiv_26_20240718180120000012" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_12">07-18</div><div class="tfeed_day rsslink" id="rsslink_26_12"><a href="https://www.reddit.com/r/technology/comments/1e6hqva/apple_breaks_silence_on_claims_it_used_swiped/" target="_blank">Apple breaks silence on claims it used 'swiped YouTube videos' to train AI</a></div><br></div>
<div id="fdiv_26_20240718171649000017" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_17">07-18</div><div class="tfeed_day rsslink" id="rsslink_26_17"><a href="https://www.reddit.com/r/technology/comments/1e6grea/with_the_selection_of_jd_vance_for_trumps_vp_we/" target="_blank">With the selection of JD Vance for Trump's VP, we should be even more worried about KOSA and other censorship bills</a></div><br></div>
<div id="fdiv_26_20240718155102000022" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_22">07-18</div><div class="tfeed_day rsslink" id="rsslink_26_22"><a href="https://www.reddit.com/r/technology/comments/1e6et48/labgrown_meat_for_pets_was_just_approved_in_the_uk/" target="_blank">Lab-Grown Meat for Pets Was Just Approved in the UK</a></div><br></div>
<div id="fdiv_26_20240718145406000025" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_25">07-18</div><div class="tfeed_day rsslink" id="rsslink_26_25"><a href="https://www.reddit.com/r/technology/comments/1e6df16/nasa_cancels_450m_viper_moon_mission_dashing_ice/" target="_blank">NASA cancels $450M Viper moon mission, dashing ice prospecting dreams</a></div><br></div>
<div id="fdiv_26_2024071814423800009" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_9">07-18</div><div class="tfeed_day rsslink" id="rsslink_26_9"><a href="https://www.reddit.com/r/technology/comments/1e6d57k/accused_of_using_algorithms_to_fix_rental_prices/" target="_blank">Accused of using algorithms to fix rental prices, RealPage goes on offensive</a></div><br></div>
```

Jquery code to add html to webpage and format css by the last hour/day/older:
```
        //ARTICLES PUBLISHED TODAY
        $("<style type='text/css'> .tfeed_day {color:"+ cssligB2 +"; } </style>").appendTo("head");
        $("<style type='text/css'> .tfeed_day a:link {color:"+ cssligB2 +";} </style>").appendTo("head");
        $("<style type='text/css'> .tfeed_day a:visited {color:"+ cssligB2 +";} </style>").appendTo("head");
        $("<style type='text/css'> .tfeed_day a:hover {color:"+ cssligB2 +"; text-decoration: underline;}</style>").appendTo("head");
        //ARTICLES PUBLISHED YESTERDAY & OLDER
        $("<style type='text/css'> .tfeed_old {color:"+ cssligA2 +"; } </style>").appendTo("head");
        $("<style type='text/css'> .tfeed_old a:link {color:"+ cssligA2 +";} </style>").appendTo("head");
        $("<style type='text/css'> .tfeed_old a:visited {color:"+ cssligA2 +";} </style>").appendTo("head");
        $("<style type='text/css'> .tfeed_old a:hover {color:"+ cssligA2 +"; text-decoration: underline;}</style>").appendTo("head");
        //ARTICLES PUBLISHED IN THE PAST HOUR
        $("<style type='text/css'> .tfeed_now {color:"+ cssligB1 +";} </style>").appendTo("head");
        $("<style type='text/css'> .tfeed_now a:link {color:"+ cssligB1 +";} </style>").appendTo("head");
        $("<style type='text/css'> .tfeed_now a:visited {color:"+ cssligB1 +";} </style>").appendTo("head");
        $("<style type='text/css'> .tfeed_now a:hover {color:"+ cssligB1 +"; text-decoration: underline;}</style>").appendTo("head");
        //ARTICLES PUBLISHED IN THE FUTURE
        $("<style type='text/css'> .tfeed_fut {color:"+ cssligB1 +";} </style>").appendTo("head");
        $("<style type='text/css'> .tfeed_fut a:link {color:"+ cssligB1 +";} </style>").appendTo("head");
        $("<style type='text/css'> .tfeed_fut a:visited {color:"+ cssligB1 +";} </style>").appendTo("head");
        $("<style type='text/css'> .tfeed_fut a:hover {color:"+ cssligB1 +"; text-decoration: underline;}</style>").appendTo("head");

        ("#contentb12").load("rss/RedditTechnology.html");

```
