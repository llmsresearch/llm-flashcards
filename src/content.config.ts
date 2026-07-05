import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

// Each card is one MDX file. Frontmatter carries the structural data
// (seeded from topics_v3.csv); the MDX body is hand-written prose.
const cards = defineCollection({
  loader: glob({ pattern: "**/*.mdx", base: "./src/content/cards" }),
  schema: z.object({
    seq: z.number(),
    title: z.string(),
    part: z.string(),
    partNumber: z.number(),
    chapter: z.string(),
    category: z.string(),
    // Short, plain description used for the meta tag and card listings.
    summary: z.string(),
    image: z.string(),
    status: z.enum(["done", "planned"]).default("done"),
    // Optional hand-picked related concepts (slugs).
    related: z.array(z.string()).default([]),
  }),
});

export const collections = { cards };
