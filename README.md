# PyRSScraper
RSS scraper with pre-tagged html output designed to be easily formatted and embedded.


**Requires:**

- Feedparser - https://pypi.org/project/feedparser/
- Unidecode - https://pypi.org/project/Unidecode/
- Eventlet - https://pypi.org/project/eventlet/
- pytz - https://pypi.org/project/pytz/
- ```mkdir /var/www/html/feeds/```

**spits out html in the following format:**

from https://old.reddit.com/r/news/hot/ = /var/www/html/feeds/redditrnewshot.html
```
<div id="rssheadlink">https://www.reddit.com/r/news/hot.rss</div><div id="rssheadupdate">Last updated: 12:03,11-22-2021</div><div id="11-22-16-51-22" class="rssdiv"><div class="rssdate" id="rn11-22">11-22 16:51</div><div class="rsslink" id="rn11-22"><a href="https://www.reddit.com/r/news/comments/qzpto6/those_who_died_were_extremely_passionate_grannies/" target="_blank">Those who died were extremely passionate grannies': Milwaukee Dancing Grannies 'devastated' by loss of life in Christmas parade</a></div><br></div>
<div id="11-22-16-48-50" class="rssdiv"><div class="rssdate" id="rn11-22">11-22 16:48</div><div class="rsslink" id="rn11-22"><a href="https://www.reddit.com/r/news/comments/qzprkv/mobs_of_looters_target_bay_area_retailers_for/" target="_blank">Mobs of looters target Bay Area retailers for third straight day</a></div><br></div>
<div id="11-22-16-35-11" class="rssdiv"><div class="rssdate" id="rn11-22">11-22 16:35</div><div class="rsslink" id="rn11-22"><a href="https://www.reddit.com/r/news/comments/qzpgfx/former_nfl_player_zac_stacy_charged_with/" target="_blank">Former NFL player Zac Stacy charged with attacking ex</a></div><br></div>
<div id="11-22-16-30-08" class="rssdiv"><div class="rssdate" id="rn11-22">11-22 16:30</div><div class="rsslink" id="rn11-22"><a href="https://www.reddit.com/r/news/comments/qzpcay/mississippi_loses_supreme_court_water_fight_with/" target="_blank">Mississippi loses Supreme Court water fight with Tennessee</a></div><br></div>
<div id="11-22-16-26-23" class="rssdiv"><div class="rssdate" id="rn11-22">11-22 16:26</div><div class="rsslink" id="rn11-22"><a href="https://www.reddit.com/r/news/comments/qzp9ez/man_arrested_in_murder_of_25yearold_pregnant/" target="_blank">Man arrested in murder of 25-year-old pregnant Houston woman</a></div><br></div>
<div id="11-22-14-45-24" class="rssdiv"><div class="rssdate" id="rn11-22">11-22 14:45</div><div class="rsslink" id="rn11-22"><a href="https://www.reddit.com/r/news/comments/qzmzlq/target_to_keep_stores_closed_on_thanksgiving_for/" target="_blank">Target to keep stores closed on Thanksgiving for good | AP News</a></div><br></div>
<div id="11-22-14-32-36" class="rssdiv"><div class="rssdate" id="rn11-22">11-22 14:32</div><div class="rsslink" id="rn11-22"><a href="https://www.reddit.com/r/news/comments/qzmpsb/toddler_with_rifle_fatally_shoots_father_police/" target="_blank">Toddler with rifle fatally shoots father, police say</a></div><br></div>
<div id="11-22-14-05-17" class="rssdiv"><div class="rssdate" id="rn11-22">11-22 14:05</div><div class="rsslink" id="rn11-22"><a href="https://www.reddit.com/r/news/comments/qzm54q/official_more_than_90_of_fed_workers_got_shots_by/" target="_blank">Official: More than 90% of fed workers got shots by deadline</a></div><br></div>
<div id="11-22-13-48-46" class="rssdiv"><div class="rssdate" id="rn11-22">11-22 13:48</div><div class="rsslink" id="rn11-22"><a href="https://www.reddit.com/r/news/comments/qzlsxn/a_nursing_home_where_83_residents_died_of_covid/" target="_blank">A nursing home where 83 residents died of Covid is still in business under a new name</a></div><br></div>
<div id="11-22-13-31-15" class="rssdiv"><div class="rssdate" id="rn11-22">11-22 13:31</div><div class="rsslink" id="rn11-22"><a href="https://www.reddit.com/r/news/comments/qzlgqj/uk_bulb_energy_which_supplies_17m_customers/" target="_blank">[UK] Bulb Energy, which supplies 1.7m customers, collapses into administration | Energy industry</a></div><br></div>
<div id="11-22-13-27-51" class="rssdiv"><div class="rssdate" id="rn11-22">11-22 13:27</div><div class="rsslink" id="rn11-22"><a href="https://www.reddit.com/r/news/comments/qzlees/uber_enters_booming_cannabis_market_with_orders/" target="_blank">Uber enters booming cannabis market with orders in Ontario</a></div><br></div>
<div id="11-22-12-00-27" class="rssdiv"><div class="rssdate" id="rn11-22">11-22 12:00</div><div class="rsslink" id="rn11-22"><a href="https://www.reddit.com/r/news/comments/qzjvn8/in_first_us_added_to_annual_list_of_backsliding/" target="_blank">In first, US added to annual list of 'backsliding' democracies</a></div><br></div>
<div id="11-22-05-07-05" class="rssdiv"><div class="rssdate" id="rl11-22">11-22 05:07</div><div class="rsslink" id="rl11-22"><a href="https://www.reddit.com/r/news/comments/qzdnas/3_arrested_after_dozens_ransack_a_nordstrom_store/" target="_blank">3 arrested after dozens ransack a Nordstrom store near San Francisco, police say</a></div><br></div>
<div id="11-22-04-45-51" class="rssdiv"><div class="rssdate" id="rl11-22">11-22 04:45</div><div class="rsslink" id="rl11-22"><a href="https://www.reddit.com/r/news/comments/qzd9vz/abducted_child_alert_issued_for_6_year_old/" target="_blank">Abducted child alert issued for 6 year old | Mississippi News Group</a></div><br></div>
<div id="11-22-01-36-00" class="rssdiv"><div class="rssdate" id="rl11-22">11-22 01:36</div><div class="rsslink" id="rl11-22"><a href="https://www.reddit.com/r/news/comments/qz9twj/illinois_supreme_court_upholds_deerfields_assault/" target="_blank">Illinois Supreme Court upholds Deerfield's assault weapons ban in divided ruling</a></div><br></div>
<div id="11-22-01-01-14" class="rssdiv"><div class="rssdate" id="rl11-22">11-22 01:01</div><div class="rsslink" id="rl11-22"><a href="https://www.reddit.com/r/news/comments/qz96hu/megachurch_leader_who_calls_himself_the_son_of/" target="_blank">Megachurch leader who calls himself the 'son of God' charged with sex trafficking</a></div><br></div>
<div id="11-22-00-05-22" class="rssdiv"><div class="rssdate" id="rl11-22">11-22 00:05</div><div class="rsslink" id="rl11-22"><a href="https://www.reddit.com/r/news/comments/qz83o4/epic_bust_state_police_in_oregon_seize_500000/" target="_blank">'Epic' bust: State police in Oregon seize 500,000 pounds of marijuana</a></div><br></div>
<div id="11-22-00-04-13" class="rssdiv"><div class="rssdate" id="rl11-22">11-22 00:04</div><div class="rsslink" id="rl11-22"><a href="https://www.reddit.com/r/news/comments/qz82u8/texas_grid_vulnerable_to_blackouts_during_severe/" target="_blank">Texas grid vulnerable to blackouts during severe winter weather, even with new preparations, ERCOT estimates show</a></div><br></div>
<div id="11-21-23-17-56" class="rssdiv"><div class="rssdate" id="rl11-21">11-21 23:17</div><div class="rsslink" id="rl11-21"><a href="https://www.reddit.com/r/news/comments/qz75pk/waukesha_holiday_parade_evacuated_following/" target="_blank">Waukesha Holiday parade evacuated following emergency event involving gunshots, speeding vehicle</a></div><br></div>
<div id="11-21-22-14-08" class="rssdiv"><div class="rssdate" id="rl11-21">11-21 22:14</div><div class="rsslink" id="rl11-21"><a href="https://www.reddit.com/r/news/comments/qz5ud1/delta_variant_linked_to_increased_risk_of/" target="_blank">Delta variant linked to increased risk of stillbirth, CDC study finds</a></div><br></div>
<div id="11-21-19-04-54" class="rssdiv"><div class="rssdate" id="rl11-21">11-21 19:04</div><div class="rsslink" id="rl11-21"><a href="https://www.reddit.com/r/news/comments/qz1vzm/dozens_of_looters_rush_california_nordstrom_store/" target="_blank">Dozens of looters rush California Nordstrom store</a></div><br></div>
<div id="11-21-18-51-44" class="rssdiv"><div class="rssdate" id="rl11-21">11-21 18:51</div><div class="rsslink" id="rl11-21"><a href="https://www.reddit.com/r/news/comments/qz1ldy/pregnant_woman_shot_in_philadelphia_while_leaving/" target="_blank">Pregnant woman shot in Philadelphia while leaving baby shower later dies</a></div><br></div>
<div id="11-21-16-22-56" class="rssdiv"><div class="rssdate" id="rl11-21">11-21 16:22</div><div class="rsslink" id="rl11-21"><a href="https://www.reddit.com/r/news/comments/qyyep5/ghislaine_maxwell_trial_federal_judge_to_question/" target="_blank">Ghislaine Maxwell trial: Federal judge to question more than 200 potential jurors</a></div><br></div>
<div id="11-21-15-34-02" class="rssdiv"><div class="rssdate" id="rl11-21">11-21 15:34</div><div class="rsslink" id="rl11-21"><a href="https://www.reddit.com/r/news/comments/qyxdsd/video_9yearold_florida_girl_fights_off_suspected/" target="_blank">VIDEO: 9-year-old Florida girl fights off suspected robber to protect mom</a></div><br></div>
<div id="11-21-15-13-37" class="rssdiv"><div class="rssdate" id="rl11-21">11-21 15:13</div><div class="rsslink" id="rl11-21"><a href="https://www.reddit.com/r/news/comments/qywyvi/tesla_electric_suvs_get_poor_scores_from_consumer/" target="_blank">Tesla, electric SUVs get poor scores from Consumer Reports</a></div><br></div>
```

Jquery code to add html to webpage and format css by the last hour/day/older:
```
var rmonth = moment().format('M');
var rday = moment().format('D');
var rtoday = moment().format(rmonth + "-" + rday);
var rtom = (parseInt(rday) + 1);
var rtomi = rtom.toString();
var rtomf = moment().format(rmonth + "-" + rtomi);
var ryest = moment().format(rmonth + "-" + (rday - 1));
$("<style type='text/css'> #rl"+ rtoday +"{color:#b8ffcb; } </style>").appendTo("head");
$("<style type='text/css'> #rl"+ rtoday +" a:link {color:#b8ffcb;} </style>").appendTo("head");
$("<style type='text/css'> #rl"+ rtoday +" a:visited {color:#002914;} </style>").appendTo("head");
$("<style type='text/css'> #rl"+ rtoday +" a:hover {color:white; text-decoration: underline;}</style>").appendTo("head");
$("<style type='text/css'> #rn"+ rtoday +"{color:#6bff93;} </style>").appendTo("head");
$("<style type='text/css'> #rn"+ rtoday +" a:link {color:#6bff93;} </style>").appendTo("head");
$("<style type='text/css'> #rn"+ rtoday +" a:visited {color:#002914;} </style>").appendTo("head");
$("<style type='text/css'> #rn"+ rtoday +" a:hover {color:white; text-decoration: underline;}</style>").appendTo("head");
$("<style type='text/css'> #rl"+ rtomf +"{color:#6bff93;} </style>").appendTo("head");
$("<style type='text/css'> #rl"+ rtomf +" a:link {color:#6bff93;} </style>").appendTo("head");
$("<style type='text/css'> #rl"+ rtomf +" a:visited {color:#002914;} </style>").appendTo("head");
$("<style type='text/css'> #rl"+ rtomf +" a:hover {color:white; text-decoration: underline;}</style>").appendTo("head");
$("#rss-feeds").load("feeds/redditrnewshot.html");
```
