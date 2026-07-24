# LLMs Visual Card

Preparing for an AI engineering interview often means revising a lot of LLM
concepts quickly: tokenization, attention, transformers, training, alignment,
RAG, agents, evaluation, and deployment. You may already know pieces of the
system, but connecting them under interview pressure is harder than recognizing
them in isolation.

LLMs Visual Card is built for that revision loop. It gives you a visual way to
refresh core large language model concepts without rereading long docs or
tutorials. Each card explains one idea with a diagram and a short note, so the
concept is easier to recall when you are answering technical questions.

Public site: <https://llmsresearch.github.io/llm-flashcards/>

This repository hosts the free open-source foundation: 193+ visual cards covering
the core mechanics of modern LLM systems. The sequence starts with text becoming
tokens and moves through transformers, training, inference, retrieval, agents,
safety, evaluation, APIs, and production tradeoffs.

## Who It Is For

This is for readers preparing for AI, ML, or LLM-heavy technical interviews who
need a fast way to reconnect concepts before a screen or onsite:

- developers building with LLM APIs
- engineers moving into AI product or platform work
- students and self-learners preparing for technical rounds
- ML practitioners revising architecture, RAG, agents, or deployment concepts
- product and research readers who need enough technical depth to speak clearly

It is not meant to replace papers, docs, or textbooks. It is meant to give you a
high-signal visual map when you need to revise quickly.

## How To Use It

Treat the map as your interview revision curriculum. Read it in order if you want
the full system path: text becomes tokens, tokens become vectors, transformers
process those vectors, training shapes the model, and inference turns the trained
model into responses.

Use it non-linearly when you need to refresh a specific gap. For RAG interviews,
start with embeddings, vector search, chunking, reranking, and citation. For
systems and production rounds, start with tokens, KV cache, quantization, rate
limits, streaming, and latency.

Visual frameworks are easier to recall than text blocks when you are explaining
architecture tradeoffs out loud.

## Free Foundation And Complete Collection

The public site contains the free foundation: 193+ cards that cover the core LLM
concepts you should be able to discuss with confidence.

The complete living collection on Gumroad contains 330+ cards and keeps growing
as new agentic workflows, model patterns, and LLM research become relevant. It
includes lifetime updates, so it can stay useful as an interview and reference
tool over time.

Complete collection: <https://llmsresearch.com/flashcards>

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
