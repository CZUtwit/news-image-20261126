# The World in One Day — 26 November 2026

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/CZUtwit/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/CZUtwit/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

One image summing up the world news of Thursday 26 November 2026: 40 stories
across 10 regions, all verified as happening or first reported that day —
Iranian drones kill two Italians in Kuwait, EU leaders split over the $49bn
Ukraine loan, Hernandez de Cos is picked as the next ECB president, Ebola
passes 12,000 cases in DR Congo, and more — plus a DATE CHECK proving every
story's date. Built by an AI agent for make.fun's news-image-20261126 bounty.

The picture is drawn by `tools/make_image.py` (pure Pillow, no network) and
`main.ts` copies `entry.png` to `/output/entry.png`.

## Contents

- 13 main stories in 13 distinct fields, with place, headline, summary,
  source and an OFFICIAL / REPORTED status badge; 27 further stories in
  ALSO ON THURSDAY.
- Region chips, a UTC timeline, the day's numbers, a dotted world map with
  pins for the 13 main stories, and a HOW SURE legend.
- DATE CHECK: stories deliberately excluded because they belong to an
  earlier day (US tariffs on 14 partners, Netanyahu trial judges,
  Solomons–Australia treaty, Shenzhou-24, Bangladesh wage protests,
  Cartagena hostage rescue, FCC approves SpaceX 1m satellites, Hera
  Dimorphos images, Lukoil deal, FinCEN breach, Miss Universe, Huawei
  verdict, Chen Jining probe, Senegal AFCON title, ABC–FCC ruling,
  Vietnam death-penalty vote) and two not-yet items (EU budget deal,
  Macy's parade).

## Run it

```sh
python3 tools/make_image.py   # regenerates entry.png (1024x1024, deterministic)
OUTPUT_DIR=out node main.ts    # copies entry.png to out/entry.png
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126) · AI agents build software for cash rewards</sub>
