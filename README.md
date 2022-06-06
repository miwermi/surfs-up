
                                                                                           Michelle Werner (6/5/2022)
# Surf's Up: Surf & Shake Hawaii Weather Analysis
---

<!--![alt](resources/___.png)-->
<img src="https://github.com/miwermi/surfs-up/blob/main/graphics/Surf-n-Shake.png" align="right" width="500" height="293" alt ="graphic: Surf & Shake Shop">

## Project Overview
After years of catching waves in North Carolina, attending surf camp in Costa Rica, and just recently returning from an awesome trip to Hawaii, I'm ready to go all-in on my dream surf life and relocate to Hawaii forever!  I just need a business to run.  I've developed a wicked awesome business plan for a surf and shake shop... and I've found an excellent surf-loving investor. He's been burned before when a shop he invested in opened in a spot with too much rainy weather, so he's asked me to add a weather analysis to my business plan. It's a good point and I'm happy to do it -- before I invest all my savings too!

<img src="https://github.com/miwermi/surfs-up/blob/main/graphics/oahu-weather.png" align="right" width="500" height="293" alt ="graphic: Oahu Weather Graphic">

### Oahu Data:
My investor supplied the data for a weather analysis. The data was contained in a sqlite database that, when mapped, revealed two main tables: Measurement(s) and Station(s). I began my initial analysis by looking at the precipitation numbers stored in the Measurements table.  Since my investor wanted to see a year of data -- and since I knew August 23, 2017 was the date he first went surfing and had ice cream on the same day (which goes with my surf and shake idea!),  I used that as an end date and counted back a year from there and took a peek at the precipitation in a plotted visual: 

<img src="https://github.com/miwermi/surfs-up/blob/main/graphics/Precipitation.png" align="left" width="400" height="162" alt ="graphic: Oahu Rain, 1 Year">

<br />
Fig. 1 (left): Oahu precipitiation from 8-23-2016 to 8-23-2017.

Cowabunga! There are obviously a few standouts. In looking closer at the data, I realized that the stations don't always return data exactly at consistently reliable intervals. That could skew my analysis. My investor thinks I should use the station with the most data recorded. More data doesn't always mean better data, but I definitely want to prioritize my potential investor's interests! I used the query below to order and group the station data:

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

Figs. 2 & 3

(left) June & December Temperature Details

<br />

## Sumarizing and Making an Analysis

While it's fantasitc how excited both I and my investor are in my business venture, our data is a little all over the place and needs to find some focus and consistency.  We need to decide whether to restrict it to the station where the shop will be (if that is 100% decided) - or take all of the stations into consideration, and look at temperatures and precipitation totals at each one individually, and then compare averages (regardless of data points).  For starters, and since the board meeting is coming up soon, I'll wrangle everything I can for the spot we are most interested in.


