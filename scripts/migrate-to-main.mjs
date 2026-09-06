// Run after `astro build`. Existing GitHub Pages stays unchanged until explicitly enabled.
import { readFile, writeFile, readdir, stat } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { join } from 'node:path';
if (process.env.MIGRATE_CARDS_TO_MAIN !== 'true') {
  console.log('Migration disabled; keeping the current GitHub Pages library.');
  process.exit(0);
}
const root = fileURLToPath(new URL('../', import.meta.url));
const mappings = [['index.html', ''], ['about/index.html', '/about']];
for (const filename of await readdir(join(root, 'src/content/cards'))) {
  if (!filename.endsWith('.mdx')) continue;
  const source = await readFile(join(root, 'src/content/cards', filename), 'utf8');
  if (/^status:\s*["']?planned/m.test(source)) continue;
  const slug = filename.slice(0, -4);
  if (!/^[a-z0-9-]+$/.test(slug)) throw new Error(`Review unsupported slug: ${slug}`);
  mappings.push([`card/${slug}/index.html`, `/${slug}`]);
}
// Check every original route before replacing anything; keep existing image assets intact.
for (const [file] of mappings) await stat(join(root, 'dist', file));
for (const [file, suffix] of mappings) {
  const target = `https://llmsresearch.com/cards${suffix}`;
  await writeFile(join(root, 'dist', file), `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>This visual card has moved | LLMs Research</title>
<link rel="canonical" href="${target}"><meta http-equiv="refresh" content="0;url=${target}">
<script>location.replace(${JSON.stringify(target)} + location.search + location.hash);</script>
</head><body><p>This visual library has moved to LLMs Research.</p><a href="${target}">Continue to the visual library</a></body></html>\n`);
}
console.log(`Prepared ${mappings.length} page-specific redirects. Old image URLs remain available.`);
