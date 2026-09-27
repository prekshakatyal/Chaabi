# Chaabi Roops FAQ Assistant — Setup Guide

A working AI chat assistant demo for a "DM to order" Instagram business
(handcrafted sarees + silver jewellery). Built to be shown to the real
business owner as a free demo.

## Total time estimate: 6-9 hours, spread across a weekend

| Step | What you do | Time |
|---|---|---|
| 1. Get API access | Sign up at console.anthropic.com, create an API key | 15 min |
| 2. Local setup | Install Python deps, run the server, confirm it works with the placeholder FAQs below | 30-45 min |
| 3. Real research | Scroll the business's Instagram bio, posts, and comments to collect their ACTUAL FAQs — prices, sizing, shipping, returns, silver purity claims, etc. | 45-60 min |
| 4. Customize | Replace `BUSINESS_INFO` in `server.py` with the real FAQs and tone | 30-45 min |
| 5. Test & refine | Ask it 15-20 realistic customer questions, fix answers that are wrong, vague, or off-tone | 1-1.5 hrs |
| 6. Polish UI | Tweak colors/copy in `static/index.html` if you want it to feel more "theirs" (e.g. swap the maroon for their actual brand color) | 30-60 min |
| 7. Deploy so it's shareable | Put it on a free host (Render, Railway, or PythonAnywhere) so you can send a link, not "run this on your laptop" | 1-2 hrs |
| 8. Record a 2-3 min demo video/GIF | Screen-record you asking it 3-4 real questions, so she doesn't even need to click a link to see the value | 30-45 min |

Steps 1-2 are one sitting. Steps 3-6 are the "weekend afternoon." Step 7
is optional for the very first pitch (a video demo is often enough) but
worth doing once she's interested, since a live link she can play with
herself converts better than a video.

## Local setup (do this first)

```bash
cd saree-faq-bot
pip install flask anthropic
export ANTHROPIC_API_KEY="sk-ant-your-key-here"
python server.py
```

Open **http://localhost:5000** — you'll see the chat widget already
wired up with placeholder Chaabi Roops FAQs. Ask it something like
"is the jewellery real silver?" to confirm it's working end to end
before you customize anything.

## What to actually edit

Everything that matters is in **`server.py`**, in the `BUSINESS_INFO`
string. Don't touch the HTML/CSS unless you want to restyle it — the
logic and the FAQ content are what make the demo convincing or not.

## Deploying so you can send a link (Step 7)

The easiest free options for a small demo like this:
- **Render.com** — free tier, connects to a GitHub repo, auto-deploys
- **Railway.app** — similarly simple, generous free tier
- **PythonAnywhere** — good for very simple Flask apps

Any of these: push this folder to a GitHub repo, connect it, set the
`ANTHROPIC_API_KEY` environment variable in their dashboard (never
commit it to the repo), and you'll get a public URL.

## Pitching it once it's ready

Send Roopali a short message with the link (or the demo video if not
deployed yet): "Built this for Chaabi Roops over the weekend — a quick
assistant for common questions like sizing/shipping/silver purity.
Take a look, no pressure either way!"
