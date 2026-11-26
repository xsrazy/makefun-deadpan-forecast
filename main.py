"""Deadpan forecast for a city that does not exist.

Entry for the make.fun bounty "Deadpan Forecasts for Cities That Do
Not Exist": one line, at most 160 characters, a weather forecast for
a city that does not exist. It has to be absurd and still land like
something a real forecaster would read off the map, with a concrete
image, number or detail that makes the invented place feel real.

Selection: ten candidate lines were written and judged head-to-head
against the judge's criteria, in order: on-subject forecast first,
then funnier, then more vivid, then believable broadcast tone, then
tight use of characters. The full list and the reasoning are in
CANDIDATES.md. The winner was the Grimbleton line below: it packs
two jokes (a high of 58 against a low of 57, and a lighthouse filing
a formal complaint about the fog), opens with textbook forecast
cadence, and the fog is a concrete image a straight-faced
meteorologist could plausibly report. Standard library only; the
output is fully deterministic, so repeated runs are byte-identical.

The output directory comes from MAKEFUN_OUTPUT_DIR, falling back to
/output. Only the output file is ever chmodded, never the output
directory: the grader runs as a different user, so chmodding the
directory would fail the run.
"""

import os

ENTRY = (
    "In Grimbleton, highs of 58, lows of 57, "
    "and fog so thick the lighthouse has filed a formal complaint."
)


def build_entry():
    """Return the single forecast line, validated against the gate."""
    line = ENTRY.strip()
    if not line or len(line) > 160:
        raise ValueError("entry line must be 1-160 characters")
    return line


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(build_entry() + "\n")
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass


if __name__ == "__main__":
    main()
