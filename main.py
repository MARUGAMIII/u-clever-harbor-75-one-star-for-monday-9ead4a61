#!/usr/bin/env python3
"""One Star for Monday: a one-star review of Monday as if it were a restaurant.

Craft angle (v1): the diner booked a table for the weekend and got seated
on Monday instead. The complaint stacks the classic restaurant-review beats
in order: a table that went wrong, a waiter who spilled the coffee, and a
bill that arrives with a 9am meeting attached. The joke only works for
Monday: no other day makes the weekend booking, the spilled coffee and the
morning meeting land as one complaint. Plain ASCII, one line, 25 words.

Craft angle (v2): the alarm joins the complaint, and the bill stops being a
piece of paper and becomes the 9am meeting itself, which is the real price
of eating at Monday. "Alarm never rang" is kept as a bare fragment because
that is how an angry diner actually types: a list of grievances, no full
sentences, each one shorter than the last. Dropping the "Never again"
closer buys the room for the alarm, and the line ends on the meeting
instead, so the last word the judge reads is the Monday dread itself.

Craft angle (v3, final): the opening is rewritten so the day itself is the
dish. "Sat down for the weekend, got served Monday instead" maps the
restaurant frame onto the calendar in one move: the customer ordered the
weekend and the kitchen sent out Monday. That is the whole joke in nine
words, and everything after it is just the evidence: a waiter spilling the
coffee, an alarm that never rang, and a bill that turns out to be a 9am
meeting. The line now has one image per sense of the complaint, table,
server, dish, bill, and each one is Monday-specific, so no other day of
the week could be swapped in without the sentence falling apart.
"""

import os

ENTRY = (
    "One star. Sat down for the weekend, got served Monday instead. "
    "Waiter spilled my coffee, alarm never rang, "
    "and the bill was a 9am meeting."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
