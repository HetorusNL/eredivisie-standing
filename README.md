# Eredivisie standing

Repository to show a table with scores for predictions of the standing in the eredivisie

## Eredivisie Standing Frontend

The frontend shows the data fetched from the Eredivisie Standing API.
The apiUrl can be overridden (defaults to `http://127.0.0.1:5000`) by mounting a `config.js` file with the following content (changing the url/port to where the API is hosted):

```js
const apiUrl = "http://127.0.0.1:5000/";
```

## Eredivisie Standing API

The Eredivisie Standing API combines the live data from the `football-data.org` API, and the predictions.
Make sure to go to https://www.football-data.org and get a token (for free), and add the token to the `FOOTBALL_DATA_TOKEN` environment variable for the API to use.
Also make sure to mount a `scores/` folder with files with the predictions.
The files should only contain the 18 eredivisie teams (with **exact** names!), in the predicted order.

## Example

An example docker compose file, with the file/directory mounts and other required files/folders/environment, can be found in the examples/ folder.
