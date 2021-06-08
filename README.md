# ETH Gas Tracker

## Motivation

I wanted to investigate correlation between ETH gas prices and ETH price fluctuations. Historical gas prices, however, are not easy to find (in downloadable format). Thus, I decided to make a script that queries current gas rates, as well as the price of ETH, every minute and writes the results to a .csv file to be used in later analysis.

## Credits

I utilized [FTX Client Code](https://github.com/ftexchange/ftx/blob/master/rest/client.py) to query for the price of ETH, and I used the [Taichi Network API](https://taichi.network/#gasnow) to query current gas prices.
