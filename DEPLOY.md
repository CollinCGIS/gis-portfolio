# Putting this site online for free

The site is one self-contained HTML file, so any static host will serve it with no
configuration. Pick one of the three below.

---

## Option 1 — GitHub Pages (recommended)

Free for public repositories, with free HTTPS and custom domains. Worth picking for a
GIS job search specifically: the repository itself becomes part of the portfolio, since a
hiring manager can read your analysis code next to the maps it produced.

### Through the website, no command line

1. Sign up at [github.com](https://github.com) if you have not already.
2. Click **New repository**. Name it `gis-portfolio`. Set it to **Public**. Create it.
3. On the empty repository page, click **uploading an existing file**.
4. Drag in everything from this folder, including the `src` and `code` folders.
   - `.nojekyll` starts with a dot, so your file manager may hide it. On macOS press
     `Cmd + Shift + .` in Finder to show hidden files; on Windows, tick **Hidden items**
     in the File Explorer View tab. The site works without it, but including it avoids
     surprises later.
5. Click **Commit changes**.
6. Go to **Settings → Pages**. Under **Source** choose **Deploy from a branch**, pick
   branch `main` and folder `/ (root)`. Click **Save**.
7. Wait one or two minutes. Your site is at `https://YOURNAME.github.io/gis-portfolio/`.

### Through the command line

```bash
cd gis-portfolio
git init
git add .
git commit -m "Environmental GIS portfolio"
git branch -M main
git remote add origin https://github.com/YOURNAME/gis-portfolio.git
git push -u origin main
```

Then do step 6 above.

### Getting a shorter URL

Name the repository `YOURNAME.github.io` instead, and the site is served at
`https://YOURNAME.github.io/` with nothing after the slash. You get one of these per
account.

### Updating it later

Replace the changed files and commit again. The site redeploys in about a minute.

---

## Option 2 — Cloudflare Pages

Fastest route if you do not want a GitHub account. No bandwidth cap on the free plan.

1. Sign up at [pages.cloudflare.com](https://pages.cloudflare.com).
2. Choose **Upload assets** rather than connecting a repository.
3. Drag in this whole folder.
4. You get a `your-project.pages.dev` URL straight away.

It can also connect to a GitHub repository and redeploy on each push, if you would
rather have both.

---

## Option 3 — Netlify Drop

The quickest possible version: open [app.netlify.com/drop](https://app.netlify.com/drop)
and drag the folder onto the page. You get a live URL in seconds, and can claim it to a
free account afterwards to keep it.

One caution: Netlify's free plan now runs on a monthly credit allowance, and exceeding it
pauses the site until the next cycle. For a portfolio that is unlikely to matter, but
Cloudflare Pages has no such cap.

---

## Using your own domain name

A domain costs roughly $10–15 a year — the hosting stays free. Something like
`yourname.dev` or `yourname.com` reads better on a resume than a `github.io` address.

Registrars worth looking at: Cloudflare Registrar (sells at cost), Namecheap, Porkbun.

Once you own it:

- **GitHub Pages:** Settings → Pages → Custom domain. Add the domain, then at your
  registrar create a `CNAME` record pointing `www` at `YOURNAME.github.io`. Tick
  **Enforce HTTPS** once the certificate is issued, which takes up to an hour.
- **Cloudflare Pages:** Custom domains → Set up a domain. If the domain is registered
  with Cloudflare the DNS is configured for you.

---

## Before you send the link out

- Open the site on a phone as well as a laptop.
- Check the Resume page — the `[bracketed]` placeholders are visible until you fill in
  `src/resume-data.js` and rebuild.
- Click through all five pages and open a couple of tools, to confirm the upload
  completed.
- Search for your own name plus "GIS portfolio" after a week, to see whether it is
  indexed.

## A note on what gets served

`index.html` is the complete standalone page and is the file a host serves. `artifact.html`
is the same page without the outer `<html>` and `<head>` wrapper, which only exists for
republishing inside Claude — hosting that one directly would render the page in quirks
mode. If you only ever edit through `build.py`, both stay in sync.
