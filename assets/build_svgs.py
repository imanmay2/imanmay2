#!/usr/bin/env python3
"""Regenerate the self-hosted SVGs: portrait.svg, langs.svg, footer.svg.

    python3 assets/build_svgs.py

Nothing here calls a third-party image service — every SVG the README shows for
these is generated once and committed, so it can't 403 on someone else's dyno.
"""
import json, os, pathlib

HERE = pathlib.Path(__file__).parent
MONO = 'ui-monospace, "SF Mono", SFMono-Regular, Menlo, Consolas, "DejaVu Sans Mono", monospace'


def portrait_svg():
    lines = (HERE / "portrait.txt").read_text().rstrip("\n").split("\n")
    # the top rows are near-black hair against a night background, so they carry
    # almost no ink -- drop them rather than frame a band of empty space
    ink = lambda l: len(l) - l.count(" ")
    while lines and ink(lines[0]) < 12:
        lines.pop(0)
    while lines and ink(lines[-1]) < 6:
        lines.pop()
    fs, lh, padx, pady, bar = 10.0, 10.4, 22, 16, 34
    cols = max(len(l) for l in lines)
    w = round(cols * fs * 0.6 + padx * 2)
    h = round(bar + pady * 2 + len(lines) * lh)

    body = "\n".join(
        f'      <text x="{padx}" y="{bar + pady + lh * (i + 0.82):.1f}" xml:space="preserve">'
        f'{l}</text>' for i, l in enumerate(lines))

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="ASCII portrait of Manmay Chakraborty">
  <title>portrait.ascii</title>
  <defs>
    <linearGradient id="ink" x1="0" y1="0" x2="0.35" y2="1">
      <stop offset="0%"   stop-color="#9df7e5"/>
      <stop offset="38%"  stop-color="#64ffda"/>
      <stop offset="72%"  stop-color="#57b6f5"/>
      <stop offset="100%" stop-color="#a78bfa"/>
    </linearGradient>
    <linearGradient id="scan" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%"   stop-color="#64ffda" stop-opacity="0"/>
      <stop offset="50%"  stop-color="#64ffda" stop-opacity=".16"/>
      <stop offset="100%" stop-color="#64ffda" stop-opacity="0"/>
    </linearGradient>
    <filter id="bloom" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur stdDeviation="1.1" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="win"><rect width="{w}" height="{h}" rx="10"/></clipPath>
    <clipPath id="screen"><rect y="{bar}" width="{w}" height="{h - bar}"/></clipPath>
  </defs>

  <g clip-path="url(#win)">
    <rect width="{w}" height="{h}" fill="#0b1018"/>
    <rect width="{w}" height="{bar}" fill="#111a27"/>
    <line x1="0" y1="{bar}" x2="{w}" y2="{bar}" stroke="#64ffda" stroke-opacity=".22"/>
    <g>
      <circle cx="18" cy="{bar/2}" r="4.5" fill="#ff5f57" fill-opacity=".85"/>
      <circle cx="34" cy="{bar/2}" r="4.5" fill="#febc2e" fill-opacity=".85"/>
      <circle cx="50" cy="{bar/2}" r="4.5" fill="#28c840" fill-opacity=".85"/>
    </g>
    <text x="{w/2}" y="{bar/2 + 3.6}" text-anchor="middle" font-family='{MONO}'
          font-size="10.5" fill="#64ffda" fill-opacity=".72" letter-spacing=".6">portrait.ascii</text>

    <g font-family='{MONO}' font-size="{fs}" fill="url(#ink)" filter="url(#bloom)">
{body}
    </g>

    <g clip-path="url(#screen)">
      <rect x="0" y="{bar}" width="{w}" height="46" fill="url(#scan)">
        <animate attributeName="y" values="{bar};{h}" dur="5.5s" repeatCount="indefinite"/>
      </rect>
    </g>
    <rect width="{w}" height="{h}" rx="10" fill="none" stroke="#64ffda" stroke-opacity=".28"/>
  </g>
</svg>
'''


LANG_COLOR = {"TypeScript": "#3178c6", "Python": "#3572A5", "JavaScript": "#f1e05a",
              "C++": "#f34b7d", "Go": "#00ADD8", "EJS": "#a91e50", "Java": "#b07219",
              "C": "#555555", "HTML": "#e34c26", "Roff": "#ecdebe"}


def langs_svg(data, top=5):
    items = sorted(data.items(), key=lambda kv: -kv[1])[:top]
    total = sum(data.values())
    w, rowh, padx, head = 460, 30, 22, 56
    h = head + rowh * len(items) + 16

    rows = []
    for i, (lang, b) in enumerate(items):
        pct = 100 * b / total
        y = head + i * rowh
        barw = round((w - padx * 2 - 150) * pct / 100, 1)
        col = LANG_COLOR.get(lang, "#8892b0")
        rows.append(f'''    <g>
      <text class="lbl" x="{padx}" y="{y + 11}" font-size="11.5">{lang}</text>
      <rect class="trk" x="{padx + 96}" y="{y + 2}" width="{w - padx*2 - 150}" height="9" rx="4.5"/>
      <rect x="{padx + 96}" y="{y + 2}" width="{barw}" height="9" rx="4.5" fill="{col}"/>
      <text class="pct" x="{w - padx}" y="{y + 11}" font-size="11.5" text-anchor="end">{pct:.1f}%</text>
    </g>''')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Most used languages">
  <title>Most used languages</title>
  <style>
    .card {{ fill: #0d1117; stroke: #64ffda; stroke-opacity: .22 }}
    .ttl {{ fill: #64ffda }} .sub {{ fill: #54607a }}
    .lbl {{ fill: #ccd6f6 }} .pct {{ fill: #8892b0 }} .trk {{ fill: #1b2635 }}
    @media (prefers-color-scheme: light) {{
      .card {{ fill: #ffffff; stroke: #0a7f6b; stroke-opacity: .30 }}
      .ttl {{ fill: #0a7f6b }} .sub {{ fill: #8b949e }}
      .lbl {{ fill: #24292f }} .pct {{ fill: #57606a }} .trk {{ fill: #eaeef2 }}
    }}
  </style>
  <rect class="card" width="{w}" height="{h}" rx="10"/>
  <g font-family='{MONO}'>
    <text class="ttl" x="{padx}" y="26" font-size="13" letter-spacing=".4">Most used languages</text>
    <text class="sub" x="{padx}" y="41" font-size="9.5">by bytes, across my 15 largest repos</text>
{chr(10).join(rows)}
  </g>
</svg>
'''


def footer_svg():
    w, h = 1200, 120
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="">
  <defs>
    <linearGradient id="fg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%"   stop-color="#112240"/>
      <stop offset="55%"  stop-color="#0a192f"/>
      <stop offset="100%" stop-color="#0d1117"/>
    </linearGradient>
    <linearGradient id="fl" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%"   stop-color="#64ffda" stop-opacity="0"/>
      <stop offset="50%"  stop-color="#64ffda" stop-opacity=".7"/>
      <stop offset="100%" stop-color="#64ffda" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect width="{w}" height="{h}" fill="url(#fg)"/>
  <path fill="#64ffda" fill-opacity=".10"
        d="M0 62 C 150 26, 300 98, 450 62 S 750 26, 900 62 S 1200 98, 1350 62 L1350 {h} L0 {h} Z">
    <animateTransform attributeName="transform" type="translate" values="0 0;-450 0" dur="11s" repeatCount="indefinite"/>
  </path>
  <path fill="#4f9cf9" fill-opacity=".09"
        d="M0 78 C 150 46, 300 110, 450 78 S 750 46, 900 78 S 1200 110, 1350 78 L1350 {h} L0 {h} Z">
    <animateTransform attributeName="transform" type="translate" values="-450 0;0 0" dur="15s" repeatCount="indefinite"/>
  </path>
  <rect y="0" width="{w}" height="1.5" fill="url(#fl)"/>
</svg>
'''


if __name__ == "__main__":
    (HERE / "portrait.svg").write_text(portrait_svg())
    langs = json.load(open(HERE / "langs.json"))
    (HERE / "langs.svg").write_text(langs_svg(langs))
    (HERE / "footer.svg").write_text(footer_svg())
    for f in ("portrait.svg", "langs.svg", "footer.svg"):
        print(f"{f:16} {os.path.getsize(HERE / f):>7} bytes")
