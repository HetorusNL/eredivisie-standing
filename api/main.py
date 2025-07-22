from flask import Flask
from flask import jsonify
from flask import Response
import os
from pathlib import Path
import requests
from typing import Any

# first fetch the token from the environment, or die as the first thing to do
TOKEN: str | None = os.getenv("FOOTBALL_DATA_TOKEN")
assert TOKEN, "error: add the token to the FOOTBALL_DATA API to the environment!"

API_ENDPOINT: str = "http://api.football-data.org/v4/competitions/DED/standings"
HEADERS: dict[str, str] = {"X-Auth-Token": TOKEN}

# some constants used in the code
# mapping between place-difference and score
SCORES: dict[int, int] = {
    0: 11,
    1: 7,
    2: 4,
    3: 2,
    4: 1,
}

api = Flask(__name__)


@api.route("/")
def get_standing() -> Response:
    # pass it to an internal function for error handling purposes
    try:
        return _get_standing()
    except BaseException as e:
        print(e)
        return jsonify()


def _get_standing() -> Response:
    data: dict[str, Any] = requests.get(API_ENDPOINT, headers=HEADERS).json()
    table: list[dict[str, Any]] = data["standings"][0]["table"]

    # create a dictionary with team: place
    teams: dict[str, int] = {}

    for index, row in enumerate(table):
        place: int = index + 1
        team = row["team"]["shortName"]
        # print(place, team)
        teams[team] = place

    print("current teams:place")
    print(teams)

    # for all local files, calculate the total score
    scores_folder: Path = Path(__file__).parent / "scores"
    scores: list[dict[str, Any]] = []
    for file in scores_folder.rglob("*"):
        print(f"\nprocessing file: {file.name}")
        # open the file and make sure it's valid
        lines: list[str]
        try:
            with open(file) as f:
                lines: list[str] = [line.strip() for line in f.readlines()]
                assert len(lines) == 18, f"error: invalid file: {file}!"
        except AssertionError as e:
            print(e)
            continue

        # formulate the team: place combinations
        prediction: dict[str, int] = {}
        for index, team in enumerate(lines):
            prediction[team] = index + 1

        # calculate the score for all teams in the prediction
        score: int = 0
        for team, place in prediction.items():
            difference: int = abs(place - teams[team])
            # print(difference)
            score += SCORES.get(difference, 0)
        print(prediction)
        print(f"score: {score}")
        scores.append({"name": file.name, "score": score})

    # sort the scores with decending score
    scores.sort(key=lambda obj: obj["score"], reverse=True)

    # add ranking to the scores
    for index in range(len(scores)):
        # ranking is the index + 1
        scores[index]["ranking"] = index + 1

    print(scores)

    return jsonify(scores)


if __name__ == "__main__":
    # run the api as a blocking call
    api.run(host="0.0.0.0")
