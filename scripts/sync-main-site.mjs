// A deploy-only hook avoids sharing a general Vercel account token with CI.
import { setTimeout as wait } from 'node:timers/promises';
if (process.env.MIGRATE_CARDS_TO_MAIN !== 'true') {
  console.log('Main-domain synchronization is not enabled yet.');
  process.exit(0);
}
const hook = process.env.MAIN_SITE_DEPLOY_HOOK;
const revision = process.env.GITHUB_SHA;
if (!hook || !/^[a-f0-9]{40}$/.test(revision || '')) throw new Error('Missing deployment hook or source revision');
const hookUrl = new URL(hook);
if (hookUrl.origin !== 'https://api.vercel.com' || !hookUrl.pathname.startsWith('/v1/integrations/deploy/')) {
  throw new Error('Unexpected deployment hook host or path');
}
try {
  const response = await fetch(hook, { method: 'POST', signal: AbortSignal.timeout(30000) });
  if (!response.ok) throw new Error('Hook rejected');
} catch { throw new Error('Could not trigger the main website build. Hook URL redacted.'); }
console.log('Website rebuild requested. Waiting for the public card revision to be live.');
for (let attempt = 0; attempt < 48; attempt++) {
  try {
    const response = await fetch(`https://llmsresearch.com/cards/content-version.json?revision=${revision}&attempt=${attempt}`, { cache: 'no-store', signal: AbortSignal.timeout(15000) });
    if (response.ok) {
      const published = await response.json();
      let ready = published.commit === revision;
      // Concurrent pushes may publish a newer revision; never wait for an obsolete one.
      if (!ready && /^[a-f0-9]{40}$/.test(published.commit || '')) {
        const comparison = await fetch(`https://api.github.com/repos/llmsresearch/llm-flashcards/compare/${revision}...${published.commit}`, {
          headers: { Accept: 'application/vnd.github+json', Authorization: `Bearer ${process.env.GITHUB_TOKEN}` },
          signal: AbortSignal.timeout(15000),
        });
        if (comparison.ok) ready = ['ahead', 'identical'].includes((await comparison.json()).status);
      }
      if (ready) { console.log(`Website is live with revision ${published.commit}. Safe to publish redirects.`); process.exit(0); }
    }
  } catch { /* Retry transient failures without exposing request credentials. */ }
  await wait(15000);
}
throw new Error('The website did not publish the new content within 12 minutes. Existing GitHub Pages is retained.');
