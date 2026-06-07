# LLM Flashcards

Hand-drawn flashcards on how LLMs work.

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
    <td><a href="cards/06-rlhf-overview.jpg"><img src="cards/06-rlhf-overview.jpg" alt="RLHF Overview"/></a><p align="center"><b>RLHF and alignment</b></p></td>
  </tr>
  <tr>
    <td><a href="cards/07-system-vs-user-prompt.jpg"><img src="cards/07-system-vs-user-prompt.jpg" alt="System vs User Prompt"/></a><p align="center"><b>Prompting</b></p></td>
    <td><a href="cards/08-what-is-rag.jpg"><img src="cards/08-what-is-rag.jpg" alt="What is RAG?"/></a><p align="center"><b>Retrieval (RAG)</b></p></td>
    <td><a href="cards/09-what-is-an-llm-agent.jpg"><img src="cards/09-what-is-an-llm-agent.jpg" alt="What is an LLM Agent?"/></a><p align="center"><b>Agents and tools</b></p></td>
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
    <td><a href="cards/16-hallucination.jpg"><img src="cards/16-hallucination.jpg" alt="Hallucination"/></a><p align="center"><b>Safety and ethics</b></p></td>
    <td><a href="cards/17-chat-completion-api.jpg"><img src="cards/17-chat-completion-api.jpg" alt="Chat Completion API"/></a><p align="center"><b>APIs and practical</b></p></td>
    <td><a href="cards/18-multimodal-llms.jpg"><img src="cards/18-multimodal-llms.jpg" alt="Multimodal LLMs"/></a><p align="center"><b>Multimodal</b></p></td>
  </tr>
  <tr>
    <td><a href="cards/19-reasoning-in-llms.jpg"><img src="cards/19-reasoning-in-llms.jpg" alt="Reasoning in LLMs"/></a><p align="center"><b>Reasoning</b></p></td>
    <td></td>
    <td></td>
  </tr>
</table>

Click any card to open it full size.

**Study in Anki:** download [`llm-flashcards.apkg`](llm-flashcards.apkg) (these 19 cards) and import it into [Anki](https://apps.ankiweb.net/). Front is the concept, back is the card.

## Why I made them

I work on LLM efficiency at LLMs Research, and a lot of that work happens on a whiteboard. Drawing a thing forces you to know what you're drawing. A vague hand-wave on a slide hides confusion. A diagram doesn't.

After enough whiteboards I had a stack of diagrams. The stack turned into a study deck for myself. I tightened the lines, kept the labels honest, and put them on cards. That's the deck.

The cards are for someone who has used an LLM API and wants the layer underneath. Some technical background helps. No heavy math.

## What's in the full deck

180 cards across 19 topics:

| | | |
|---|---|---|
| Transformer architecture (27) | Tokenization (8) | Embeddings (7) |
| Training (10) | Fine-tuning (9) | RLHF and alignment (11) |
| Prompting (11) | RAG (12) | Agents and tools (11) |
| Inference and decoding (11) | Scaling laws (7) | Architecture variants (8) |
| Quantization (7) | Evaluation (8) | Context management (6) |
| Safety (8) | APIs and practical use (6) | Multimodal (6) |
| Reasoning (7) | | |

Two formats: a PDF (180 pages, printable) and an `.apkg` for Anki spaced-repetition review. New cards get added every few weeks. Past buyers get the updates by email.

[llmsresearch.com/flashcards](https://llmsresearch.com/flashcards?utm_source=github&utm_medium=repo&utm_campaign=flashcards_launch)

## License

CC BY-NC-ND 4.0. Share the cards with credit and a link back to this repo. No repackaging, no reselling, no modified versions, no commercial use. Full text in [LICENSE](LICENSE).

## Contributing

If something on a card is wrong or unclear, [open an issue](../../issues/new). If you want a card on a concept that is not in the deck yet, open one too. I read them.

## About

[LLMs Research](https://llmsresearch.com) is an independent applied research lab. We work on LLM efficiency: inference, KV cache compression, adaptive compute, multi-agent systems. The deck started as study notes for that work.

[Website](https://llmsresearch.com) · [Newsletter](https://llmsresearch.substack.com) · [X](https://x.com/llmsresearch) · [LinkedIn](https://www.linkedin.com/company/llmsresearch)
