# Posting runbook — arXiv only, no venue

Decision: both papers go to arXiv as preprints. No peer review, no workshop, no conference.
That is a legitimate route — arXiv assigns a DOI, Google Scholar indexes it automatically, and
the papers are citable from the day they post.

## What posts, and what does not

| | Paper | Posts? |
|---|---|---|
| 1 | `paper/` — *Betting Against the Benchmark* (40 pp) | **Yes** |
| 2 | `paper-equity/` — *A Century Is Not Enough* (15 pp) | **Yes** |
| 3 | `paper-workshop/` — 4-page note | **No** |

**Why not the third.** It was written to fit a 4-page workshop limit. Its content — the
drift failure and the certificate construction — is a strict condensation of paper 1, which
carries the same result in **closed form** rather than by simulation alone. With the workshop
dropped, posting it beside its own source is redundant publication, and it is the kind that is
obvious to anyone reading an author profile. Keep it in the repository; do not post it.

## Order matters

Paper 2 cites paper 1 five times, currently as `arXiv preprint` with no identifier. So:

1. Post **paper 1**. Wait for the arXiv ID (`arXiv:2608.XXXXX`), usually next business day.
2. Put that ID into paper 2's bibliography:

   ```bibtex
   @article{guven2026,
     title   = {Betting Against the Benchmark: Drift-Robust, Anytime-Valid Certificates
                of Out-of-Sample Predictive Ability},
     author  = {Guven, Mehmet Demir},
     journal = {arXiv preprint arXiv:2608.XXXXX},
     year    = {2026}
   }
   ```

3. Rebuild: `cd paper-equity && ./build_arxiv.sh`
4. Post **paper 2**.

Posting them in the other order leaves paper 2 citing a phantom.

---

## Paper 1 — *Betting Against the Benchmark*

- **Upload**: `paper/arxiv-submission.tar.gz` — verified: extracts clean, compiles from
  scratch, 40 pages, 0 errors, 0 undefined references
- **Abstract**: paste `paper/abstract-plain.txt`
- **Primary**: `q-fin.ST` · **Cross-list**: `stat.ME`, `econ.EM`
- **Comments**: `40 pages. Code, pinned data, and one script per reported number: https://github.com/ITheClixs/crypto-return-predictability`

## Paper 2 — *A Century Is Not Enough*

- **Upload**: `paper-equity/arxiv-submission.tar.gz` — verified the same way, 15 pages
- **Abstract**: paste `paper-equity/abstract-plain.txt`
- **Primary**: `q-fin.ST` · **Cross-list**: `stat.ME`, `econ.EM`
- **Comments**: `15 pages, 2 figures. Companion to arXiv:2608.XXXXX. Code and data: https://github.com/ITheClixs/crypto-return-predictability`

## Both

- **License**: CC BY-NC-SA 4.0, matching the repository. arXiv's grant is **irrevocable** —
  you cannot narrow it later, so choose deliberately.
- **Author name**: exactly as you want it cited forever. Google Scholar clusters on it.
- **Affiliation footnote**: states the work was independent, unfunded, unsupervised,
  uncommissioned and unendorsed. Confirm ETH's policy allows naming the department this way for
  independent work — the only item here that is a policy question, not a technical one.

---

## After both are live

### Google Scholar

1. <https://scholar.google.com> → **My profile** → sign in
2. Name, affiliation, institutional email if you have one, areas of interest
3. Scholar usually finds arXiv papers within days. If it does not: **+ → Add article manually**,
   then fill title, author, year, and the arXiv URL as the source
4. Set **Article updates → automatic** so later arXiv versions merge instead of duplicating

Both papers will appear as separate entries with the second citing the first. That internal
citation does not count toward your h-index; Scholar excludes self-citations from some metrics
and not others, and either way it is not worth engineering.

### GitHub repository description

Repository name stays `crypto-return-predictability` — renaming breaks the URL printed in both
papers. Set the description to:

```
Anytime-valid certificates of out-of-sample predictive ability. Papers: arXiv:2608.XXXXX (method) and arXiv:2608.YYYYY (equity premium). Reproducible: one script per reported number.
```

Add both arXiv links to the **Website** field and to the README header.

### Optional

- Add a `CITATION.cff` so GitHub shows a "Cite this repository" button
- `dist-alphacert/` builds the library standalone (numpy + scipy only) if you ever want it on
  PyPI; nothing about posting depends on that

---

## What to expect

Neither paper is a landmark and neither claims to be. Paper 1 documents a real failure of a
widely-used test and supplies a construction that avoids it; paper 2 is an honest null result
with an interval attached. Expect modest attention. The durable value is that both are correct,
reproducible, and say plainly what they do not establish.
