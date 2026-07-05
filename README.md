# LLMs Visual Card

Large language models are easier to use than to understand. You can write a
prompt, call an API, or read a model card long before you have a stable picture
of what tokens, attention, context windows, retrieval, alignment, and inference
are doing together.

LLMs Visual Card is a visual map for building that picture. It breaks the LLM
stack into 180 focused cards, each explaining one concept with a diagram and a
short written note. The sequence starts with tokenization and moves toward the
practical questions that appear when models are used in real systems: cost,
latency, retrieval, evaluation, safety, and deployment.

Public site: <https://llmsresearch.github.io/llm-flashcards/>

Use it when you want a mental model, not just a definition. Open the public site
and follow the map from the beginning, or jump to a single card when a term keeps
showing up in papers, docs, product work, or engineering discussions.

## Who It Is For

This is for readers who use or study LLMs and want a clearer picture of how the
main pieces fit together:

- developers building with LLM APIs
- students and self-learners trying to connect scattered concepts
- product and research readers who need enough technical depth to reason clearly
- engineers moving from application use toward model behavior, retrieval,
  evaluation, or deployment

It is not meant to replace a textbook or a paper. It is meant to give you the
map you wish you had beside you while reading them.

## How To Use It

Read the cards in order if you want a curriculum. Each section builds on the
last: text becomes tokens, tokens become vectors, transformers process those
vectors, training shapes the model, and inference turns the trained model into
responses.

Use the map non-linearly if you are debugging a specific gap. For example, if
you are working on RAG, start with embeddings, vector search, chunking, reranking,
and citation. If you are trying to reduce cost or latency, start with tokens,
KV cache, quantization, rate limits, and streaming.

## What Is Inside

The visual cards are organized around the main layers of modern LLM systems:

- Representing language: tokenization and embeddings
- The transformer: attention, normalization, position encodings, and model variants
- Training: objectives, losses, optimizers, scaling laws, and fine-tuning
- Adaptation and alignment: SFT, RLHF, DPO, preference data, and guardrails
- Running the model: decoding, inference latency, KV cache, and quantization
- Talking to the model: prompting, reasoning, and context management
- Knowledge and tools: retrieval, RAG, agents, and function calling
- Beyond text: multimodal models and CLIP
- Measuring: benchmarks, human evaluation, and contamination
- Governing: grounding, bias, sycophancy, memorization, and safety behavior
- Shipping: APIs, streaming, costs, rate limits, and latency optimization

## Run Locally

Install dependencies.

```bash
npm install
```

Start the development server.

```bash
npm run dev
```

Build the static site.

```bash
npm run build
```

Preview the production build.

```bash
npm run preview
```

## Deploy

The site is configured for GitHub Pages at
`https://llmsresearch.github.io/llm-flashcards/`.

Pushes to `main` run `.github/workflows/deploy.yml`, which installs dependencies,
builds the Astro site, and publishes `dist/` with GitHub Pages. In the repository
settings, set Pages to use GitHub Actions as the build and deployment source.

## Repository Layout

```text
src/content/cards/   Card explanations in MDX, one file per card
src/pages/           Astro routes for the map, card pages, and about page
src/layouts/         Shared page layout
src/styles/          Global CSS
public/cards/        Card image assets
```

Generated and local-only folders such as `node_modules/`, `dist/`, and `.astro/`
are ignored.

## Card Content

Each card has two parts:

- an image in `public/cards/`
- an MDX explanation in `src/content/cards/`

The MDX frontmatter stores the card order, title, chapter, category, summary,
image path, and related-card links. The body text explains the concept in a few
paragraphs and is rendered on the card page.

## Contributing

If a card is wrong, unclear, or missing an important nuance, open an issue with
the card title and the proposed correction. Text corrections should be small and
factual. Image changes are handled separately because the card images are licensed
under NoDerivatives terms.

## License

See [LICENSE](LICENSE). The card images are licensed under CC BY-NC-ND 4.0.
