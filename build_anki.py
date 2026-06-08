"""Build the free LLM Flashcards Anki deck (.apkg) from the 19 cards in cards/.

Front: concept name. Back: the full card image.

These IDs are independent of the paid deck. Do NOT change MODEL_ID/DECK_ID
after release: Anki uses them (and each note's guid) to preserve a user's
review history across updates. The guid is derived from the filename, so
renaming a card file is the only thing that resets that card's history.

Run:  python build_anki.py     (needs `pip install genanki`)
Out:  llm-flashcards.apkg
"""

from pathlib import Path

import genanki

ROOT = Path(__file__).resolve().parent
CARDS_DIR = ROOT / "cards"
OUT = ROOT / "llm-flashcards.apkg"

MODEL_ID = 1980321457
DECK_ID = 1980321458

# (filename, topic, concept) — titles/topics taken from README.md
CARDS = [
    ("01-what-is-a-transformer.jpg", "Transformer architecture", "What is a Transformer?"),
    ("02-what-is-tokenization.jpg", "Tokenization", "What is Tokenization?"),
    ("03-what-is-an-embedding.jpg", "Embeddings", "What is an Embedding?"),
    ("04-language-modeling-objective.jpg", "Training", "Language Modeling Objective"),
    ("05-full-finetuning-vs-peft.jpg", "Fine-tuning", "Full Fine-tuning vs PEFT"),
    ("06-rlhf-overview.jpg", "RLHF and alignment", "RLHF Overview"),
    ("07-system-vs-user-prompt.jpg", "Prompting", "System vs User Prompt"),
    ("08-what-is-rag.jpg", "Retrieval (RAG)", "What is RAG?"),
    ("09-what-is-an-llm-agent.jpg", "Agents and tools", "What is an LLM Agent?"),
    ("10-autoregressive-generation.jpg", "Inference", "Autoregressive Generation"),
    ("11-scaling-laws.jpg", "Scaling laws", "Scaling Laws"),
    ("12-gpt-vs-bert-vs-t5.jpg", "Architectures", "GPT vs BERT vs T5"),
    ("13-what-is-quantization.jpg", "Quantization", "What is Quantization?"),
    ("14-perplexity-as-a-metric.jpg", "Evaluation", "Perplexity as a Metric"),
    ("15-lost-in-the-middle.jpg", "Context management", "Lost in the Middle"),
    ("16-hallucination.jpg", "Safety and ethics", "Hallucination"),
    ("17-chat-completion-api.jpg", "APIs and practical", "Chat Completion API"),
    ("18-multimodal-llms.jpg", "Multimodal", "Multimodal LLMs"),
    ("19-reasoning-in-llms.jpg", "Reasoning", "Reasoning in LLMs"),
    ("20-reasoning-models.jpg", "Reasoning", "Reasoning Models (o1/R1)"),
    ("21-state-space-models-mamba.jpg", "Architectures", "State Space Models and Mamba"),
    ("22-mixture-of-experts-routing.jpg", "Architectures", "Mixture of Experts Routing"),
    ("23-model-context-protocol.jpg", "Agents and tools", "Model Context Protocol (MCP)"),
    ("24-vision-transformer.jpg", "Multimodal", "Vision Transformer (ViT)"),
    ("25-sparse-autoencoders.jpg", "Interpretability", "Sparse Autoencoders (SAEs)"),
    ("26-tree-of-thoughts.jpg", "Prompting", "Tree of Thoughts"),
    ("27-double-descent.jpg", "Training", "Double Descent"),
    ("28-activation-functions.jpg", "Training", "Activation Functions"),
    ("29-gpqa.jpg", "Evaluation", "GPQA"),
    ("30-matryoshka-embeddings.jpg", "Embeddings", "Matryoshka Embeddings"),
]

CSS = """
.card {
  font-family: -apple-system, system-ui, "Helvetica Neue", Arial, sans-serif;
  background: #F5F3EE;
  color: #2D2A28;
  text-align: center;
  padding: 24px;
}
.concept {
  font-size: 28px;
  font-weight: 700;
  color: #2A9D8F;
  margin: 32px 12px;
  line-height: 1.3;
}
.topic {
  font-size: 14px;
  color: #999999;
  text-transform: lowercase;
  letter-spacing: 0.5px;
  margin-top: 8px;
}
.card-image img {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
}
hr#answer {
  border: 0;
  border-top: 1px solid #DDD8CE;
  margin: 24px 0;
}
"""

QFMT = """
<div class="concept">{{Concept}}</div>
<div class="topic">{{Topic}}</div>
"""

AFMT = """
{{FrontSide}}
<hr id="answer">
<div class="card-image">{{Card}}</div>
"""


def main() -> None:
    model = genanki.Model(
        MODEL_ID,
        "LLM Flashcards Card",
        fields=[{"name": "Concept"}, {"name": "Topic"}, {"name": "Card"}],
        templates=[{"name": "Visual", "qfmt": QFMT, "afmt": AFMT}],
        css=CSS,
    )

    deck = genanki.Deck(DECK_ID, "LLM Flashcards")
    media_files: list[str] = []

    for filename, topic, concept in CARDS:
        path = CARDS_DIR / filename
        if not path.exists():
            raise SystemExit(f"missing card: {path}")
        note = genanki.Note(
            model=model,
            fields=[concept, topic, f'<img src="{filename}">'],
            guid=genanki.guid_for(filename),
        )
        deck.add_note(note)
        media_files.append(str(path))

    package = genanki.Package(deck)
    package.media_files = media_files
    package.write_to_file(str(OUT))

    size_mb = OUT.stat().st_size / (1024 * 1024)
    print(f"wrote {OUT.name} ({len(media_files)} cards, {size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
