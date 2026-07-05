# Contributing

Thanks for taking an interest in LLMs Visual Card. This repository is an Astro
knowledge bank, so contributions are mostly about accuracy, clarity, and coverage.

## Found a mistake?

If a card is wrong, misleading, or unclear, please [open an issue](../../issues/new).
Include the card title, the URL or filename if possible, and what you think is off.
Accuracy matters more than polish.

## Want a topic covered?

Open an issue describing the concept you would like to see added. A good request
names the concept, explains where it fits in the curriculum, and gives one or two
sources if the topic is technical or easy to misstate.

## Editing card text

Card explanations live in `src/content/cards/*.mdx`. Keep edits small and factual.
Preserve the existing frontmatter fields, especially `seq`, `title`, `chapter`,
`category`, `summary`, and `image`.

Before proposing a change, run:

```bash
npm run build
```

## A note on the images

The card images are released under [CC BY-NC-ND 4.0](LICENSE). Because the license
is NoDerivatives, we cannot accept pull requests that modify the card images
themselves. If an image is wrong, open an issue and describe the correction.

LLMs Visual Card
