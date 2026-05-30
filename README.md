# LLM Flashcards

**Hand-drawn flashcards for learning how large language models actually work.**

One concept per card: a clean diagram and a short, plain-English explanation. This repository holds **19 free sample cards**, one from each topic in the full deck, covering the LLM stack from tokenization and attention through RAG, agents, and inference.

Made by [LLMs Research](https://llmsresearch.com), an independent applied research lab.

---

## The cards

<table>
  <tr>
    <td width="33%"><a href="cards/01-what-is-a-transformer.jpg"><img src="cards/01-what-is-a-transformer.jpg" alt="What is a Transformer?"/></a><p align="center"><b>Transformer architecture</b></p></td>
    <td width="33%"><a href="cards/02-what-is-tokenization.jpg"><img src="cards/02-what-is-tokenization.jpg" alt="What is Tokenization?"/></a><p align="center"><b>Tokenization</b></p></td>
    <td width="33%"><a href="cards/03-what-is-an-embedding.jpg"><img src="cards/03-what-is-an-embedding.jpg" alt="What is an Embedding?"/></a><p align="center"><b>Embeddings</b></p></td>
  </tr>
  <tr>
    <td><a href="cards/04-language-modeling-objective.jpg"><img src="cards/04-language-modeling-objective.jpg" alt="Language Modeling Objective"/></a><p align="center"><b>Training</b></p></td>
    <td><a href="cards/05-full-finetuning-vs-peft.jpg"><img src="cards/05-full-finetuning-vs-peft.jpg" alt="Full Fine-tuning vs PEFT"/></a><p align="center"><b>Fine-tuning</b></p></td>
    <td><a href="cards/06-rlhf-overview.jpg"><img src="cards/06-rlhf-overview.jpg" alt="RLHF Overview"/></a><p align="center"><b>RLHF &amp; alignment</b></p></td>
  </tr>
  <tr>
    <td><a href="cards/07-system-vs-user-prompt.jpg"><img src="cards/07-system-vs-user-prompt.jpg" alt="System vs User Prompt"/></a><p align="center"><b>Prompting</b></p></td>
    <td><a href="cards/08-what-is-rag.jpg"><img src="cards/08-what-is-rag.jpg" alt="What is RAG?"/></a><p align="center"><b>Retrieval (RAG)</b></p></td>
    <td><a href="cards/09-what-is-an-llm-agent.jpg"><img src="cards/09-what-is-an-llm-agent.jpg" alt="What is an LLM Agent?"/></a><p align="center"><b>Agents &amp; tools</b></p></td>
  </tr>
  <tr>
    <td><a href="cards/10-autoregressive-generation.jpg"><img src="cards/10-autoregressive-generation.jpg" alt="Autoregressive Generation"/></a><p align="center"><b>Inference</b></p></td>
    <td><a href="cards/11-scaling-laws.jpg"><img src="cards/11-scaling-laws.jpg" alt="Scaling Laws"/></a><p align="center"><b>Scaling laws</b></p></td>
    <td><a href="cards/12-gpt-vs-bert-vs-t5.jpg"><img src="cards/12-gpt-vs-bert-vs-t5.jpg" alt="GPT vs BERT vs T5"/></a><p align="center"><b>Architectures</b></p></td>
  </tr>
  <tr>
    <td><a href="cards/13-what-is-quantization.jpg"><img src="cards/13-what-is-quantization.jpg" alt="What is Quantization?"/></a><p align="center"><b>Quantization</b></p></td>
    <td><a href="cards/14-perplexity-as-a-metric.jpg"><img src="cards/14-perplexity-as-a-metric.jpg" alt="Perplexity as a Metric"/></a><p align="center"><b>Evaluation</b></p></td>
    <td><a href="cards/15-lost-in-the-middle.jpg"><img src="cards/15-lost-in-the-middle.jpg" alt="Lost in the Middle"/></a><p align="center"><b>Context management</b></p></td>
  </tr>
  <tr>
    <td><a href="cards/16-hallucination.jpg"><img src="cards/16-hallucination.jpg" alt="Hallucination"/></a><p align="center"><b>Safety &amp; ethics</b></p></td>
    <td><a href="cards/17-chat-completion-api.jpg"><img src="cards/17-chat-completion-api.jpg" alt="Chat Completion API"/></a><p align="center"><b>APIs &amp; practical</b></p></td>
    <td><a href="cards/18-multimodal-llms.jpg"><img src="cards/18-multimodal-llms.jpg" alt="Multimodal LLMs"/></a><p align="center"><b>Multimodal</b></p></td>
  </tr>
  <tr>
    <td><a href="cards/19-reasoning-in-llms.jpg"><img src="cards/19-reasoning-in-llms.jpg" alt="Reasoning in LLMs"/></a><p align="center"><b>Reasoning</b></p></td>
    <td></td>
    <td></td>
  </tr>
</table>

> Click any card to open it full size.

---

## Why these exist

I started drawing these while building [LLMs Research](https://llmsresearch.com). Every time I had to explain a piece of LLM internals on a whiteboard, a diagram worked better than any paragraph. After enough whiteboards it was clear there was a deck hiding in there.

The cards are made for the moment between "I have used an LLM API" and "I understand what is actually happening underneath." They assume some technical background but no heavy mathematics. They work for revising before an interview, building a first-principles mental model, or keeping open as a reference while reading a paper.

## How to use them

- **Browse** them right here, or click any card to open it full size.
- **Print** them for physical study.
- **Read along** with the longer write-ups in our [visual guides](https://llmsresearch.com/learn): the transformer, attention with a worked example, the KV cache, and RAG vs fine-tuning.

## The full deck

These 19 are a sample. The complete deck is **180 hand-drawn cards across 19 topics**, delivered as a high-resolution PDF and an **Anki deck** (`.apkg`) for spaced-repetition review. Lifetime updates are included as new cards are added.

**→ [Get the full deck](https://llmsresearch.com/flashcards?utm_source=github&utm_medium=repo&utm_campaign=flashcards_launch)**

## License

The cards in this repository are released under **[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)**.

You are welcome to **share** them, including in slides, classes, study groups, and social posts, as long as you **credit LLMs Research** and link back. Commercial use, reselling, repackaging, and modified versions are not permitted. See [LICENSE](LICENSE) for details.

## Contributing

Spotted something wrong or confusing on a card? Want to suggest a concept for a future card? Open an [issue](../../issues). Corrections and topic requests genuinely shape what gets drawn next.

## About

[LLMs Research](https://llmsresearch.com) is an independent applied research lab working on LLM efficiency: inference, KV cache compression, adaptive compute, and multi-agent systems. The deck grows alongside the research.

[Website](https://llmsresearch.com) · [Visual guides](https://llmsresearch.com/learn) · [Newsletter](https://llmsresearch.substack.com) · [X](https://x.com/llmsresearch) · [LinkedIn](https://www.linkedin.com/company/llmsresearch)
