# 🐍 Your Portfolio — Editing Guide

This is your personal portfolio website. **Everything is in one file**: `index.html`.
You don't need any special tools — just a text editor (VS Code is great, but even
Notepad works) and a web browser.

---

## 🚀 Quick Start (3 ways to view)

### A. Just open it
Double-click `index.html` — opens in your default browser. Works offline.

### B. Local server (recommended for development)
Open a terminal in this folder and run:
```bash
python3 -m http.server 8000
```
Then visit `http://localhost:8000` in your browser.

### C. Host it free (when ready)
- **Netlify** — drag the folder onto https://app.netlify.com/drop
- **GitHub Pages** — push to a repo, enable Pages
- **Vercel / Cloudflare Pages** — all work great with one folder

---

## ✏️ How to Edit Stuff (find these in `index.html`)
Open the file in any editor, then **Ctrl+F / Cmd+F** to search for things to change.

| Want to change... | Search for | Where it appears |
|---|---|---|
| Your name | `Your Name` | Nav brand, footer, manifest author |
| The big hero headline | `Building software that feels like` | Top of page |
| The tagline / sub-copy | `Self-taught developer shipping` | Hero sub-paragraph |
| Your email | `hello@example.com` | Big italic contact link |
| GitHub / Twitter / etc links | `href="#"` | Social icons + nav |
| The accent color (violet) | `--accent: #a78bfa` | The top `:root` block in `<style>` |
| Stats (numbers + labels) | `Projects shipped` | "BY THE NUMBERS" section |

### 🎨 Want a different accent color?
At the top of the file, inside `<style>`, the first `:root` block has:
```
--accent: #a78bfa;     /* 👈 try changing this */
```
Try: `#22d3ee` (cyan), `#34d399` (green), `#fbbf24` (amber), `#f472b6` (pink).
Save → refresh → entire re-theme.

---

## ➕ How to Add a New Project (the important one)

1. Open `index.html` in any text editor
2. Scroll to the `04 — SELECTED WORK` section (search for `<!-- ====== PROJECT 01 ======`)
3. Find any `<article class="project">...</article>` block
4. **Copy** the whole block
5. **Paste** it right before the `▶ PASTE NEW PROJECTS HERE ▼` comment at the bottom
6. Edit inside the new block:

| To change | Look for inside the block |
|---|---|
| Number (01, 02, 03...) | `<div class="project-num">01 /</div>` |
| Project name | `<h3 class="project-title">...</h3>` |
| Description | `<p class="project-desc">...</p>` |
| GitHub link | The first `<a href="#">` (Source icon) |
| Live demo link | The second `<a href="#">` (External icon, or delete it if no demo) |
| Tech stack pills | Inside `<div class="project-stack">`, add/remove `<span>name</span>` |

### Quick template — just copy-paste this:
```html
<article class="project reveal">
    <div class="project-num">04 /</div>
    <div class="project-body">
        <div class="project-head">
            <h3 class="project-title">My New Project</h3>
            <div class="project-links">
                <a href="https://github.com/you/my-project" target="_blank" rel="noopener" aria-label="Source">
                    <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 .5C5.4.5 0 5.9 0 12.6c0 5.3 3.4 9.8 8.2 11.4.6.1.8-.3.8-.6v-2.2c-3.3.7-4-1.6-4-1.6-.6-1.4-1.4-1.8-1.4-1.8-1.1-.8.1-.8.1-.8 1.2.1 1.9 1.3 1.9 1.3 1.1 1.9 2.9 1.4 3.6 1 .1-.8.4-1.4.8-1.7-2.7-.3-5.5-1.3-5.5-6 0-1.3.5-2.4 1.3-3.3-.1-.3-.6-1.6.1-3.3 0 0 1-.3 3.3 1.3.9-.3 2-.4 3-.4s2 .1 3 .4c2.3-1.6 3.3-1.3 3.3-1.3.7 1.7.2 3 .1 3.3.8.9 1.3 2 1.3 3.3 0 4.7-2.8 5.7-5.5 6 .4.4.8 1.1.8 2.2v3.3c0 .3.2.7.8.6 4.8-1.6 8.2-6.1 8.2-11.4C24 5.9 18.6.5 12 .5z"/></svg>
                </a>
                <a href="https://myproject.com" target="_blank" rel="noopener" aria-label="Live demo">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
                </a>
            </div>
        </div>
        <p class="project-desc">
            Short description of what this project does.
        </p>
        <div class="project-stack">
            <span>Python</span>
            <span>FastAPI</span>
        </div>
    </div>
</article>
```

Save the file, refresh the browser — done. 🎉

---

## 🖼️ Want to add project screenshots later?

When you have images, add this line at the top of `.project-body`, right after the `<div class="project-num">` row:

```html
<img src="images/project.png"
     alt="My project screenshot"
     style="width:100%;border-radius:12px;margin:0 0 20px;border:1px solid var(--card-border);" />
```

Then create an `images/` folder next to `index.html` and drop your screenshots in.

---

## 🛠️ Recommended Editor

**[VS Code](https://code.visualstudio.com/)** — free, lightweight.

Install the "Live Server" extension — every time you save `index.html`,
the browser auto-refreshes. Makes editing feel instant.

---

## 📁 File Structure

```
portfolio/
├── index.html       ← the entire website (yes, really)
├── README.md        ← this guide
└── (optional) images/   ← create when adding project screenshots
```

---

## 💡 Tips

- **Test on mobile**: open Chrome DevTools (F12) → click the phone icon → resize
- **Backup before big changes**: just copy `index.html` to `index-backup.html`
- **Sanity-check your HTML**: paste into https://validator.w3.org if anything looks broken

Now go make it yours. 🚀
