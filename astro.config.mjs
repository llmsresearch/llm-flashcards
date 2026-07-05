import { defineConfig } from "astro/config";
import mdx from "@astrojs/mdx";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://llmsresearch.github.io",
  base: "/llm-flashcards",
  integrations: [mdx(), sitemap()],
});
