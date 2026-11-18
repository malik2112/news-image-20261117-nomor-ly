# news-image-20261117-nomor-ly — "WORLD IN BRIEF: Tuesday 17 November 2026"

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/malik2112/news-image-20261117-nomor-ly/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/malik2112/news-image-20261117-nomor-ly/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

One image summing up the world news of Tuesday 17 November 2026, as a
newspaper front page under the masthead WORLD IN BRIEF. The program
(`main.py`, Python 3.13, standard library only) copies the bundled image
to `/output/entry.png`. No network; both runs write the same bytes.

## The day's news in the image

Researched 18 November 2026 from same-day news roundups (asaspress World
News Digest 17 Nov 2026; Foreign Exchanges world roundup 17 Nov 2026;
NPR News Now 5pm ET 17 Nov 2026; Arab News 6pm GMT bulletin 17 Nov 2026;
The Daily 10, 17 Nov 2026; One Turn News, 17 Nov 2026):

1. **Two fronts, one day** — U.S. jets strike an IRGC missile launch site
   on Qeshm Island while Iran fires drones at the U.S. base in Bahrain
   (Sheikh Isa, home of the U.S. 5th Fleet), its third attack there in five
   days; and Ukraine hits the Kerch Bridge a second day, a road span
   collapsing into the strait.
2. **Shenzhen summit set** — Trump, Xi and Putin to meet Thursday 19 Nov on
   the APEC sidelines, the first-ever trilateral summit of the three leaders.
3. **Gaza aid plea** — the UK, Australia, Canada and Italy urge Israel to
   open aid crossings; Britain sanctions Israeli settlement firms.
4. **Quad in Manila** — Trump opens his Asia trip with a Quad summit;
   critical-minerals deals and joint maritime patrols agreed.

Ticker: Nasdaq falls 2.5% ahead of Nvidia earnings; Geneva debates a ban on
killer robots; Mongolia's president resigns.

## Files

- `main.py` — entrypoint; copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`
  (defaults to `/output/entry.png`).
- `entry.png` — the front-page image, 1024×1024, 569,647 bytes (PNG).
- `LICENSE` — MIT.

## Local check

```sh
mkdir -p out1 out2
MAKEFUN_OUTPUT_DIR=out1 python3 main.py
MAKEFUN_OUTPUT_DIR=out2 python3 main.py
sha256sum out1/entry.png out2/entry.png  # identical
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=pwfn5nwa&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
