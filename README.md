# Eredivisie standing

Repository to show a table with scores for predictions of the standing in the eredivisie

## Frontend

The frontend shows the data fetched from the API.
Make sure to mount a `scores/` folder with files with the predictions.
The files should only contain the 18 eredivisie teams (with **exact** names!), in the predicted order.

## API

The API combines the live data from the `football-data.org` API, and the predictions.
Make sure to go to https://www.football-data.org and get a token (for free), and add the token to the `FOOTBALL_DATA_TOKEN` environment variable for the API to use.
