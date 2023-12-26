import os
import shutil
import requests
from glob import glob
from rich import print
from rich.progress import track


SRC = "./backjun/"
DST = "./백준/"
URL = "https://solved.ac/api/v3/problem/show"
TIERS = {
    0: "Unrated",
    1: "Bronze V",
    2: "Bronze IV",
    3: "Bronze III",
    4: "Bronze II",
    5: "Bronze I",
    6: "Silver V",
    7: "Silver IV",
    8: "Silver III",
    9: "Silver II",
    10: "Silver I",
    11: "Gold V",
    12: "Gold IV",
}


def get_prob_info(prob_id):
    api_url = "https://solved.ac/api/v3/problem/show"
    args = {"problemId": prob_id}
    headers = {"Content-Type": "application/json"}
    res = requests.get(api_url, params=args, headers=headers)

    if res.status_code == 200:
        prob_info = res.json()
        return prob_info
    else:
        return None


def write_markdown(level, prob_id, title):
    content = f"""
# [{level}] {title} - {prob_id}
[문제 링크](https://www.acmicpc.net/problem/{prob_id})

"""
    return content


if __name__ == "__main__":
    src = glob(SRC + "*.py")

    for s in track(src):
        prob_id = s.split("/")[-1].split(".")[0]

        if (info := get_prob_info(prob_id)) is None:
            continue

        level = info["level"]
        title = info["titleKo"]
        level = TIERS[level]
        tier, _level = level.split(" ")

        dst = DST + f"{tier}/{prob_id}. {title}"
        os.makedirs(dst, exist_ok=True)

        print(f"{s} -> {dst}")
        shutil.copy(s, f"{dst}/{title}.py")
        with open(f"{dst}/README.md", "w") as f:
            f.write(write_markdown(level, prob_id, title))
