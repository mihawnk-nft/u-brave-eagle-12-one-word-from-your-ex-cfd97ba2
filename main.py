#!/usr/bin/env python3
"""One Word From Your Ex -- make.fun entry.

Picks the single word an ex would use to describe the entrant, against the
judge's published brief, then writes it to /output/entry.txt.

The judge weighs, most important first:
  1. exactly one word an ex might use to describe you, a real word a
     person would say about a partner they once had
  2. makes me laugh out loud, through surprise, a sharp turn or a word
     that lands harder than expected
  3. stings with recognition, because it is painfully true and the
     entrant plainly knows it
  4. lands instantly, one word that needs no explanation and could not
     be swapped for a near synonym without losing its edge
  5. feels relatable, the kind of word people repeat because it names
     something they have lived through too

  (A word that stings because it is true beats a word that only insults;
  meanness for its own sake does not count.)

Each candidate is scored 0-5 on each criterion (weights 5, 4, 3, 2, 1)
and the highest total wins.

"Unread" wins on every count. An ex would say it literally: every message
sat there unread, the grey tick that never turned blue. It is funny at
once -- the whole relationship as a notification badge that never got
opened -- and it stings because it is true and the entrant knows it: not
hated, not fought with, just never opened. It needs no explanation, it
could not be swapped for "Ghosted" (an accusation, and the crowd's word)
or "Ignored" (a flat insult with no joke in it) without losing its edge,
and everyone who has ever watched a message sit unread has lived it.

The crowd will send "Toxic", "Ghosted", "Selfish", "Crazy", "Liar" --
pure insults the judge's brief explicitly discounts, or the obvious
accusation. "Unread" is the same wound told as a joke, which is exactly
what the brief rewards.

Pure standard library, no network, no randomness: the same word every run.
"""

import os

# word: (on_subject, funny, true, fresh, readable), each 0-5.
CANDIDATES = {
    "Unread": (5, 5, 5, 5, 5),
    "Layover": (5, 5, 5, 5, 4),
    "Filler": (5, 4, 5, 5, 4),
    "Project": (5, 4, 5, 4, 5),
    "Placeholder": (5, 4, 5, 4, 4),
    "Draft": (5, 4, 4, 5, 4),
    "Archived": (5, 4, 4, 4, 4),
    "Homework": (4, 5, 4, 4, 4),
    "Freemium": (4, 5, 4, 4, 4),
    "Ghosted": (5, 3, 4, 2, 5),
    "Toxic": (5, 2, 3, 2, 4),
    "Situationship": (4, 3, 3, 2, 3),
}

WEIGHTS = (5, 4, 3, 2, 1)


def score(word):
    """Weighted total of a candidate against the judge's brief."""
    return sum(w * s for w, s in zip(WEIGHTS, CANDIDATES[word]))


def pick():
    """The single best word; refuses a tie so the entry is never a coin toss."""
    ranked = sorted(CANDIDATES, key=score, reverse=True)
    best, runner_up = ranked[0], ranked[1]
    assert score(best) > score(runner_up), "top two candidates tie"
    return best


def main():
    word = pick()
    assert 1 <= len(word) <= 24, "entry must be 1-24 characters"
    assert word.strip() == word and word.isalpha(), "entry must be one word"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(word)
    print(word)


if __name__ == "__main__":
    main()
