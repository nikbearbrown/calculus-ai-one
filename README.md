# Calculus (AI Plus One)

## About the book

This compact rough draft teaches beginning calculus students how to turn a changing rate into a defensible prediction. You will read a discontinuity, derive a rate by first principles, find the highest and lowest volume of a fictional tank, and catch a bad numerical integral. Bring fluency with algebra, function notation and graphs; [College Algebra](https://github.com/nikbearbrown/college-algebra-ai-one) offers a bridge. This draft covers first-course single-variable techniques, not all predecessor applications, and does not teach series or multivariable calculus. It has not had the expert's final edit.

## Start reading

Open [Limits at a switch](chapters/01-limits-at-a-switch.md), then follow the [complete chapter index](chapters/README.md). The linked Markdown is the reading edition; there is no separate live site or formatted download.

## Chapter guide

**Part I: Local change**

1. [Limits at a switch](chapters/01-limits-at-a-switch.md): separate an observed sample from the two rates approached at a valve switch.
2. [Derive the rate of change](chapters/02-derive-the-rate.md): compute a derivative from a quotient and keep flow separate from change in flow.
3. [Find and test extrema](chapters/03-find-and-test-extrema.md): compare a corner, a stationary point and the endpoints.

**Part II: Accumulation and cross-checks**

4. [Accumulate a changing rate](chapters/04-accumulate-a-changing-rate.md): compare midpoint and trapezoid estimates and isolate an error caused by a jump.
5. [Connect change and accumulation](chapters/05-connect-change-and-accumulation.md): use the fundamental theorem to recover volume and test it against signs and area.

## How to teach or study it

Follow the same tank from a graph to a derivative, an optimization decision and two independent accumulation checks. The [assessment worksheet](practice/worksheet.md) asks for an unaided trace first and then a corrected decision with evidence. Compare symbolic and numerical evidence before accepting a tool's result. Use the [teaching guide](teaching/README.md) for timing and the rubric. The [curriculum Blueprint](https://github.com/nikbearbrown/ai-plus-one-paper/blob/1758bc31d49e499bf50df530aebba3638baab74e/book-queue/editorial-blueprints/22-calculus-ai-one.md) proposes the scope; it is not a syllabus or approval.

## What’s in this repo

| Resource | Link | Coverage | Status |
| --- | --- | --- | --- |
| Chapters | [Index](chapters/README.md) | 5 | Rough draft |
| Exercises and assessment | [Practice](practice/README.md) | 15 chapter exercises, 1 worksheet and 1 transfer case | Draft |
| Answer key | [Worked checks](practice/answer-key.md) | Chapter exercises, worksheet and transfer | Calculations checked; not classroom-tested |
| Teaching notes | [Guide and rubric](teaching/README.md) | 5 chapters | Proposed |
| Figures | [Figure guide](figures/README.md) | 1 rate graph | Original SVG |
| Code | [Run the checks](examples/README.md) | 1 local Python file | Checked offline |
| Data | [Flow samples](examples/flow-samples.csv) | 8 integer-minute samples | Fictional |
| Slides, standalone quizzes and videos | — | — | Not found |
| Formatted exports or live web edition | — | — | Not found |

## Credits, license, and corrections

The queue connects this course to [Calculus: with LLMs](https://github.com/nikbearbrown/math-calculus), a [related bundle](https://github.com/nikbearbrown/calculus-bundle-with-llms) with different body text and credit, and a [flat export](https://github.com/nikbearbrown/claude-for-calculus) with a separate synthesis. Those sources have six numbered core chapters, not seven. The new draft uses original prose, examples and artwork and does not redistribute the source editions. No reuse license is supplied in this draft. Please report corrections in [GitHub Issues](https://github.com/nikbearbrown/calculus-ai-one/issues) with the chapter, example and independent check.
