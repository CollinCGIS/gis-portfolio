"""Build the portfolio site from the parts in src/ and code/.

Run:  python3 build.py

Outputs two files:
  index.html     a complete standalone web page -- this is what you host
  artifact.html  the same page without the <html>/<head> wrapper, for
                 republishing inside Claude, which adds its own wrapper
"""
import json
import pathlib

src = pathlib.Path("src")
code = pathlib.Path("code")

TITLE = "Environmental GIS Portfolio"
DESCRIPTION = ("Environmental GIS analysis portfolio: urban heat, water quality, wildfire risk, "
               "sea level rise and air quality, with interactive method demos and browser GIS tools.")

# 1. fold every snippet file into a data file the Code page reads
manifest = json.loads((src / "manifest.json").read_text())
snippets = []
for entry in manifest:
    item = dict(entry)
    item["code"] = (code / entry["file"]).read_text().rstrip("\n")
    snippets.append(item)
# escaping "</" keeps a "</script>" inside any snippet from closing the tag early
payload = json.dumps(snippets, ensure_ascii=False).replace("</", "<\\/")
(src / "code-data.js").write_text("window.SNIPPETS=" + payload + ";\n")

# 2. assemble styles, markup and scripts in dependency order
fonts = ("https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;"
         "12..96,700&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap")
head = (f"<title>{TITLE}</title>\n"
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        f'<link rel="stylesheet" href="{fonts}">\n')
css = (src / "style.css").read_text() + (src / "style2.css").read_text()
order = ["lib.js", "maps-data.js", "demos.js", "common.js", "gismath.js", "code-data.js",
         "resume-data.js", "tools.js", "code.js", "resume.js", "home.js", "router.js"]
scripts = "".join("<script>\n" + (src / f).read_text() + "\n</script>\n" for f in order)
body = head + "<style>\n" + css + "\n</style>\n" + (src / "body.html").read_text() + "\n" + scripts

# 3a. standalone page for an ordinary web host
reset = ("""<style>
:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
body{margin:0;font:14px system-ui,-apple-system,"Segoe UI",sans-serif}
img{max-width:100%}
[hidden]{display:none!important}
</style>""")
standalone = ('<!doctype html>\n<html lang="en">\n<head>\n'
              '<meta charset="utf-8">\n'
              '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
              f'<meta name="description" content="{DESCRIPTION}">\n'
              '<meta name="color-scheme" content="light dark">\n'
              f"{reset}\n</head>\n<body>\n{body}</body>\n</html>\n")
pathlib.Path("index.html").write_text(standalone)

# 3b. unwrapped page for republishing inside Claude
pathlib.Path("artifact.html").write_text(body)

kb = len(standalone) // 1024
print(f"built index.html ({kb} KB) and artifact.html; {len(snippets)} snippets")
