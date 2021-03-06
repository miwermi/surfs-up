
                                                                                           Michelle Werner (6/5/2022)
# Surf's Up: Surf & Shake Hawaii Weather Analysis
---

<!--![alt](resources/___.png)-->
<img src="https://github.com/miwermi/surfs-up/blob/main/graphics/Surf-n-Shake.png" align="right" width="500" height="293" alt ="graphic: Surf & Shake Shop">

## Project Overview

After years of catching waves in North Carolina, attending surf camp in Costa Rica, and just recently returning from an awesome trip to Hawaii, I'm ready to go all-in on my dream surf life and relocate to Hawaii forever!  I just need a business to run.  I've developed a wicked awesome business plan for a surf and shake shop... and I've found an excellent surf-loving investor. He's been burned before when a shop he invested in opened in a spot with too much rainy weather, so he's asked me to add a weather analysis to my business plan. It's a good point and I'm happy to do it -- before I invest all my savings too!

<img src="https://github.com/miwermi/surfs-up/blob/main/graphics/oahu-weather.png" align="right" width="500" height="293" alt ="graphic: Oahu Weather Graphic">

### Oahu Data:

My investor supplied the data for a weather analysis consisting of observed weather readings from stations all over Oahu. The data was contained in a sqlite database that, when mapped, revealed two main tables: Measurement(s) and Station(s). I began my initial analysis by looking at the precipitation numbers stored in the Measurements table.  Since my investor wanted to see a year of data -- and since I knew August 23, 2017 was the date he first went surfing and had ice cream on the same day (which goes with my surf and shake idea!) --  I used that date as an end date, counted back a year from there, and took a peek at the precipitation in a plotted visual: 

<br />
<img src="https://github.com/miwermi/surfs-up/blob/main/graphics/PrecipitationReadings.png" align="left" width="400" height="162" alt ="graphic: Oahu Rain, 1 Year">

Fig. 1 (left): All Oahu precipitation readings from 8-23-2016 to 8-23-2017.

Cowabunga! There are obviously a few standouts. Looking more closely at the data, I realized that the stations don't always exactly return data at consistently reliable intervals. That could skew my analysis. 
<br clear="all" />

My investor thinks I should use the station with the most data recorded. More data doesn't always mean better data, but I definitely want to prioritize my potential investor's interests! I used the query below to order and group the station data:

    SELECT measurement.station AS measurement_station, count(measurement.station) AS count_1 
    FROM measurement GROUP BY measurement.station ORDER BY count(measurement.station) DESC

but since I was writing in python, it looked like this:

    session.query(Measurement.station, func.count(Measurement.station)).\
    group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()
    
The query revealed exactly what I wanted to see, a list of station ids and the number of data points reported by each in descending order:

    [('USC00519281', 2772),
     ('USC00519397', 2724),
     ('USC00513117', 2709),
     ('USC00519523', 2669),
     ('USC00516128', 2612),
     ('USC00514830', 2202),
     ('USC00511918', 1979),
     ('USC00517948', 1372),
     ('USC00518838', 511)]

Station USC00519281, with 2772 points of data, is the station with the most points of data - AND it's a great surf spot! This is where we want to open the Surf & Shake Shop.  Next, my investor wanted me to created some temperature charts.  

First we looked at June and December averages from the entire Oahu dataset:

<img src="https://github.com/miwermi/surfs-up/blob/main/graphics/JuneTemps.png" align="left" width="186" height="262" alt ="graphic: June Temps">
<img src="https://github.com/miwermi/surfs-up/blob/main/graphics/DecemberTemps.png" align="left" width="186" height="262" alt ="graphic: Dec Temps">

<br />
Figs. 2 & 3 (left): June & December Temperature Details for all Oahu Stations (full dataset, not limited to one year)



<br clear="all" />

## Location Specific Analysis

While it's fantastic how excited both I and my investor are in my business venture, our data results need some focus and consistency.  We need to decide whether to restrict it to the station where the shop will be (if that is 100% decided) - or take all of the stations into consideration and look at temperatures and precipitation totals at each one individually, and then compare averages (regardless of data points).  For starters, and since the board meeting is coming up soon, I'll wrangle everything I can for the spot we are most interested in.


<img src="https://github.com/miwermi/surfs-up/blob/main/graphics/Station81-TobsFreq.png" align="right" width="277" height="181" alt ="graphic: Station 81 Temp Frequencies">

### Station 81 Data:

The reported June and December temperature information above was tallied from the entire dataset which contained multiple entries per day from each of the 9 stations on Oahu. The number of data points was inconsistent across the entire set (some of the 9 stations reported every day, some didn't), but probably still gave us pretty good overall averages.  If we look at just the entries from Station 81 (USC00519281), we find that last year's temps ranged from a min temp of 59 to a max temp of 83 with a daily average of 73 degrees. The frequency of each temp is charted in Fig. 4 on the right.

<img src="https://github.com/miwermi/surfs-up/blob/main/graphics/Station81-PrcpFreq.png" align="right" width="277" height="181" alt ="graphic: Station 81 Precipitation Frequencies">

The Station 81 (USC00519281) average daily precipitation for the past year was .2, with a max of 2.98 and a zero prcp minimum. Frequencies of those numbers are charted in Fig 5 on the right.

At right: Figures 5 and 6, Station 81 (USC00519281) reported observed temps and precipitation (binned).

Furthermore, limiting and charting the reported precipitation for each day in the past year at our target station reveals a clearer picture of rainfall in this location:

<br clear="all" />
<img src="https://github.com/miwermi/surfs-up/blob/main/graphics/Precipitation81.png" align="left" width="636" height="150" alt ="graphic: Station 81 Precipitation">

Fig 6. Station 81 (USC00519281): Reported Daily Precipitation from 8/23/2016 - 8/23/2017

<br clear="all" />

## Initial Analysis Summary & Further Considerations

The analysis so far has revealed some great information about the station location we are most interested in for the Surf & Shake Shop and about Oahu weather conditions in general.  So far, there are no alarming issues. Rainfall is typical of beach locations with a minimal amount falling often, but most likely not ruining the day. For further consideration for our business plan though, we might also want to consider not just the dates, but also the times of the reported information and water temperatures - that way we could make comparisons to tide times.  These are the killer stats for surf enthusiasts!  If we drilled down enough on those stats, we might find ways to tailor our business plan for even greater success - everyone loves ice cream for sure, and shake shops... but coffee, donuts, and wet suit sales and/or rentals might also be great things to offer.  If the tide times match the rain times and the water hasn't yet heated up, we'll need more than ice cream! 

