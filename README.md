
                                                                                           Michelle Werner (6/5/2022)
# Surf's Up: Surf & Shake Hawaii Weather Analysis
---

<!--![alt](resources/___.png)-->
<img src="https://github.com/miwermi/surfs-up/blob/main/graphics/Surf-n-Shake.png" align="right" width="500" height="293" alt ="graphic: Surf & Shake Shop">

## Project Overview
After years of catching waves in North Carolina, attending surf camp in Costa Rica, and just recently returning from an awesome trip to Hawaii, I'm ready to go all-in on my dream surf life and relocate to Hawaii forever!  I just need a business to run.  I've developed a wicked awesome business plan for a surf and shake shop... and I've found an excellent surf-loving investor. He's been burned before when a shop he invested in opened in a spot with too much rainy weather, so he's asked me to add a weather analysis to my business plan. It's a good point and I'm happy to do it -- before I invest all my savings too!

<img src="https://github.com/miwermi/surfs-up/blob/main/graphics/oahu-weather.png" align="right" width="500" height="293" alt ="graphic: Oahu Weather Graphic">

### Oahu Data:
My investor supplied the data for a weather analysis. The data was contained in a sqlite database that, when mapped, revealed two main tables: Measurement(s) and Station(s). I began my initial analysis by looking at the precipitaion numbers stored in the Measurements table.  Since my investor wanted to see a year of data -- and since I knew August 23, 2017 was the date he first went surfing and had ice cream on the same day (which goes with my surf and shake idea!),  I used that as an end date and counted back a year from there and took a peek at the precipitation in a plotted visual: 

<img src="https://github.com/miwermi/surfs-up/blob/main/graphics/Precipitation.png" align="left" width="400" height="162" alt ="graphic: Oahu Rain, 1 Year">

Fig. 1 (left): Oahu preciptiation from 8-23-2016 to 8-23-2017.

Kowabunga! There are obviously a few standouts. In looking closer at the data, I realized that the stations don't always return data exactly at consistently reliable intervals. That could skew my analysis. I decided to see which station had the most data points and go from there.
