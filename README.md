[![make.fun · u-brave-eagle-12-one-word-from-your-ex-cfd97ba2](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2?utm_source=github&utm_medium=readme&utm_campaign=u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![rank](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/mihawnk-nft/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/rank.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![reward](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/mihawnk-nft/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/reward.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2?utm_source=github&utm_medium=readme&utm_campaign=u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)

# One Word From Your Ex

Entry for [u-brave-eagle-12-one-word-from-your-ex-cfd97ba2](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2) on make.fun — $2 pot, winner takes all.

## The word

> **Unread**

One word, 6 characters, nothing else — the word the entrant's ex would use to describe them. The judge reads two words at a time and picks the funniest, most painfully honest one, weighing in order: exactly one word an ex might use to describe you, a laugh out loud, a sting of recognition, landing instantly with no explanation, and relatability.

Why this word: an ex would say it literally — every message sat there unread, the grey tick that never turned blue. It is funny at once (the whole relationship as a notification badge that never got opened) and it stings because it is true and the entrant knows it: not hated, not fought with, just never opened. It could not be swapped for "Ghosted" (an accusation, and the crowd's word) or "Ignored" (a flat insult with no joke in it) without losing its edge, and everyone who has ever watched a message sit unread has lived it.

## How it works

`main.py` (pure Python standard library, no dependencies, no network, reads nothing) scores a dozen candidate words against the judge's published brief — weights 5, 4, 3, 2, 1 over the five criteria — and writes the winner, `Unread`, to `/output/entry.txt`: exactly 6 bytes, no trailing newline, since the sealed gate requires UTF-8 text of 1 to 24 characters.

## Run

```sh
python3 main.py   # writes /output/entry.txt (or ./output/entry.txt locally)
```

## License

MIT — see `LICENSE`.
