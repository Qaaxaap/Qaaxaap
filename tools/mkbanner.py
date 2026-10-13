#!/usr/bin/env python3
"""Generate assets/terminal.svg: a faithful copy of Qaaxaap's powerlevel11k prompt.

Glyphs are outlined from Maple Mono NF CN (the font his kitty uses), so the banner
renders identically for every viewer without depending on their fonts.

Vertical geometry follows the font's own metrics -- hhea ascent 1020 / descent -300,
i.e. a 1.32em terminal cell -- so the segment background blocks align with the glyphs
and the powerline separators sit exactly inside their block, as in a real terminal.

Colours are the 256-colour values from ~/.config/p11k/p11k.kdl.
"""
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

REG = '/home/Qaaxaap/.nix-profile/share/fonts/truetype/MapleMono-NF-CN-Regular.ttf'
BOLD = '/home/Qaaxaap/.nix-profile/share/fonts/truetype/MapleMono-NF-CN-Bold.ttf'
OUT = '/home/Qaaxaap/Projects/Qaaxaap/assets/terminal.svg'

SIZE, SIZE_SMALL = 15, 13

fonts = {False: TTFont(REG), True: TTFont(BOLD)}
glyphsets = {k: f.getGlyphSet() for k, f in fonts.items()}
cmaps = {k: f.getBestCmap() for k, f in fonts.items()}
hmtx = fonts[False]['hmtx']

UPEM = fonts[False]['head'].unitsPerEm
ASC = fonts[False]['hhea'].ascent           # 1020
DESC = fonts[False]['hhea'].descent         # -300
S, S_SMALL = SIZE / UPEM, SIZE_SMALL / UPEM
CELL = (ASC - DESC) * S                     # 19.8px terminal cell at 15px
CELL_SMALL = (ASC - DESC) * S_SMALL

def adv(ch):
    g = cmaps[False].get(ord(ch))
    return (hmtx[g][0] if g else 600) * S

SEP1, ENDT, RST, RSUB = '\ue0b1', '\ue0b0', '\ue0b2', '\ue0b3'
LINUX, FOLDER, CLOCK = '\uf17c', '\uf07c', '\uf017'


def c256(n):
    lv = [0, 95, 135, 175, 215, 255]
    if n < 16:
        r, g, b = [(0,0,0),(128,0,0),(0,128,0),(128,128,0),(0,0,128),(128,0,128),(0,128,128),(192,192,192),
                   (128,128,128),(255,0,0),(0,255,0),(255,255,0),(0,0,255),(255,0,255),(0,255,255),(255,255,255)][n]
    elif n < 232:
        n -= 16
        r, g, b = lv[n // 36], lv[(n % 36) // 6], lv[n % 6]
    else:
        r = g = b = 8 + (n - 232) * 10
    return '#%02x%02x%02x' % (r, g, b)


C = dict(frame=c256(240), sep=c256(244), dirn=c256(31), dira=c256(39), prompt=c256(76), time=c256(66),
         ok=c256(70), bg=c256(236), gap=c256(240), white=c256(255), sapphire=c256(74),
         text='#cdd6f4', out='#a6adc8', name='#89b4fa', quote='#cba6f7',
         peach='#fab387', blue='#89b4fa', teal='#94e2d5', hdr='#6c7086')

L_PLAIN = [('╭─', C['frame'], 0, 0),
           (' ', C['white'], 0, 1),                    # space before the os icon
           (LINUX, C['white'], 0, 1),
           (' ', C['white'], 0, 1),                    # space after the os icon
           (SEP1, C['sep'], 0, 1),
           (' ', C['dirn'], 0, 1),                     # space before the dir segment
           (FOLDER + ' ', C['dirn'], 0, 1),
           ('~', C['dira'], 1, 1), ('/Projects/', C['dirn'], 0, 1),
           ('Qaaxaap', C['dira'], 1, 1),
           (' ', C['dirn'], 0, 1),                     # space before the closing triangle
           (ENDT, C['bg'], 0, 0)]


def right_stat(clock):
    """right line: <start] ␣ ✔ ␣ [rsub ␣ clock ␣ [clock ␣ -- spaces as p11k emits them"""
    return [(RST, C['bg'], 0, 0),
            (' ', C['text'], 0, 1), ('✔', C['ok'], 0, 1), (' ', C['text'], 0, 1),
            (RSUB, C['sep'], 0, 1), (' ', C['time'], 0, 1),
            (clock, C['time'], 0, 1), (' ', C['time'], 0, 1),
            (CLOCK, C['time'], 0, 1), (' ', C['time'], 0, 1)]


TITLE = 'qaaxaap@lfs: ~/Projects/Qaaxaap'

from ff_rows import LOGO_ROWS as FF_LOGO, FIELD_ROWS as FF_FIELDS   # real capture, bare pty

FF_CMD = ' fastfetch'

# the capture carries the colours the terminal emitted against black. The logo's
# body colour was lifted for that black terminal, so it goes back to pure black
# here: on this banner it reads as the darker part of the mark, which is enough.
FF_LIFT = {'#333333': '#000000', None: C['text']}

ROWS = [
    ('header', L_PLAIN, right_stat('18:36:50')),
    ('text', [('╰─', C['frame'], 0, 0), ('❯', C['prompt'], 0, 0), (' whoami', C['text'], 0, 0)]),
    ('text', [('Qaaxaap', C['name'], 1, 0), (' — Rust · C++ · Nix · Wayland', C['out'], 0, 0)]),
    ('blank',),
    ('header', L_PLAIN, right_stat('18:36:51')),
    ('text', [('╰─', C['frame'], 0, 0), ('❯', C['prompt'], 0, 0), (FF_CMD, C['text'], 0, 0)]),
    ('ffblock',),
    ('blank',),
    ('header', L_PLAIN, right_stat('18:36:52')),
    ('text', [('╰─', C['frame'], 0, 0), ('❯', C['prompt'], 0, 0), (' ls ~/projects', C['text'], 0, 0)]),
    ('text', [('powerlevel11k', C['peach'], 0, 0), ('  Tuack-GUI', C['blue'], 0, 0),
              ('  tuack-vscode', C['teal'], 0, 0), ('  d2l-learning', C['sapphire'], 0, 0)]),
]

X0, Y0, X_END = 30, 46 + 6 + ASC * S, 970


def place(segs, x0):
    """char stream + background spans (exact cell edges) for one row"""
    out, spans, cur, x = [], [], None, x0
    for text, fill, bold, bgflag in segs:
        for ch in text:
            w = adv(ch)
            out.append((ch, x, fill, bold))
            if bgflag:
                if cur is None:
                    cur = [x, x + w]
                else:
                    cur[1] = x + w
            elif cur is not None:
                spans.append(tuple(cur))
                cur = None
            x += w
    if cur is not None:
        spans.append(tuple(cur))
    return out, spans, x


FF_X = X0 + 41 * adv(' ')          # module list starts where the logo region ends

rects, used, body, y = [], {}, [], Y0
for row in ROWS:
    if row[0] == 'blank':
        y += CELL
        continue
    if row[0] == 'header':
        left, lspans, lx_end = place(row[1], X0)
        rx = X_END - sum(adv(c) for c in ''.join(s[0] for s in row[2]))
        right, rspans, _ = place(row[2], rx)
        for sx, ex in lspans + rspans:
            rects.append(f'<rect x="{sx:.2f}" y="{y - ASC * S:.2f}" width="{ex - sx:.2f}" height="{CELL:.2f}" fill="{C["bg"]}"/>')
        g0, g1 = lx_end, rx
        n = max(1, int((g1 - g0) / adv('·')))
        gx = g0 + ((g1 - g0) - n * adv('·')) / 2
        line = left + [(ch, gx + i * adv('·'), C['gap'], 0) for i, ch in enumerate('·' * n)] + right
    elif row[0] == 'ffblock':
        # logo on the left, module list on the right; the shorter column is
        # padded with blank lines so the two stay vertically centred
        n_ff = max(len(FF_LOGO), len(FF_FIELDS))
        for i, r in enumerate(FF_LOGO):
            ys = y + (n_ff - len(FF_LOGO)) / 2 * CELL + i * CELL
            for ch, x, fill, bold in place([(t, FF_LIFT.get(c, c), b, 0) for t, c, b in r], X0)[0]:
                if ch != ' ':
                    used[(ch, bold)] = None
                    body.append((ys, ch, x, fill, bold))
        for i, r in enumerate(FF_FIELDS):
            ys = y + (n_ff - len(FF_FIELDS)) / 2 * CELL + i * CELL
            for ch, x, fill, bold in place([(t, FF_LIFT.get(c, c), b, 0) for t, c, b in r], FF_X)[0]:
                if ch != ' ':
                    used[(ch, bold)] = None
                    body.append((ys, ch, x, fill, bold))
        y += n_ff * CELL
        continue
    else:
        line, _, _ = place(row[1], X0)
    for ch, x, fill, bold in line:
        if ch == ' ':
            continue
        used[(ch, bold)] = None
        body.append((y, ch, x, fill, bold))
    y += CELL

title_x = (1000 - len(TITLE) * adv('Q')) / 2
for ch in TITLE:
    used[(ch, False)] = None

paths, missing = {}, []
for (ch, bold) in used:
    gname = cmaps[bold].get(ord(ch))
    if gname is None:
        missing.append(ch)
        continue
    pen = SVGPathPen(glyphsets[bold], ntos=lambda v: f'{v:.0f}')
    glyphsets[bold][gname].draw(pen)
    paths[(ch, bold)] = pen.getCommands()
if missing:
    raise SystemExit(f'missing glyphs: {missing}')


def pid(ch, bold):
    return ('g' if not bold else 'gb') + format(ord(ch), 'x')


defs = '\n'.join(f'    <path id="{pid(c, b)}" d="{d}"/>' for (c, b), d in sorted(paths.items()))

rows_svg, i = [], 0
while i < len(body):
    yl, seg, j = body[i][0], [], i
    while j < len(body) and body[j][0] == yl:
        _, ch, x, fill, bold = body[j]
        seg.append(f'<use xlink:href="#{pid(ch, bold)}" x="{x / S:.0f}" fill="{fill}"/>')
        j += 1
    rows_svg.append(f'  <g transform="translate(0 {yl:.2f}) scale({S} {-S})">' + ''.join(seg) + '</g>')
    i = j

title_baseline = (46 - CELL_SMALL) / 2 + ASC * S_SMALL
title_svg = (f'  <g transform="translate({title_x / S_SMALL:.0f} {title_baseline / S_SMALL:.0f}) scale({S_SMALL} {-S_SMALL})">'
             + ''.join(f'<use xlink:href="#{pid(ch, False)}" x="{j * 600}" fill="{C["hdr"]}"/>'
                       for j, ch in enumerate(TITLE) if ch != ' ') + '</g>')

H = int(round(y - CELL + (-DESC) * S + 24))
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1000 {H}" width="1000" height="{H}" role="img" aria-labelledby="ttl dsc">
  <title id="ttl">Qaaxaap — powerlevel11k prompt in Maple Mono NF CN</title>
  <desc id="dsc">Qaaxaap's real powerlevel11k prompt, drawn as glyph outlines: a framed header in ~/Projects/Qaaxaap with a check mark and clock on the right, then whoami, fastfetch -l none -s OS:WM:Terminal, and ls ~/projects.</desc>
  <defs>
    <linearGradient id="win" x1="0" y1="0" x2="0.6" y2="1"><stop offset="0" stop-color="#1e1e2e"/><stop offset="1" stop-color="#181825"/></linearGradient>
    <linearGradient id="bar" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#11111b"/><stop offset="1" stop-color="#1e1e2e"/></linearGradient>
    <radialGradient id="glowA" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#89b4fa" stop-opacity="0.20"/><stop offset="1" stop-color="#89b4fa" stop-opacity="0"/></radialGradient>
    <radialGradient id="glowB" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#cba6f7" stop-opacity="0.18"/><stop offset="1" stop-color="#cba6f7" stop-opacity="0"/></radialGradient>
    <clipPath id="winClip"><rect width="1000" height="{H}" rx="16"/></clipPath>
{defs}
  </defs>
  <g clip-path="url(#winClip)">
    <rect width="1000" height="{H}" fill="url(#win)"/>
    <ellipse cx="110" cy="140" rx="380" ry="240" fill="url(#glowA)"/>
    <ellipse cx="910" cy="260" rx="400" ry="260" fill="url(#glowB)"/>
    <rect width="1000" height="46" fill="url(#bar)"/>
    <circle cx="28" cy="23" r="6.5" fill="#f38ba8"/><circle cx="50" cy="23" r="6.5" fill="#f9e2af"/><circle cx="72" cy="23" r="6.5" fill="#a6e3a1"/>
{title_svg}
{chr(10).join('    ' + r for r in rects)}
{chr(10).join(rows_svg)}
    <rect x="0.5" y="0.5" width="999" height="{H - 1}" rx="16" fill="none" stroke="#313244"/>
  </g>
</svg>
'''
open(OUT, 'w').write(svg)
print(f'glyphs={len(paths)} uses={len(body)} rects={len(rects)} cell={CELL:.2f}px height={H} bytes={len(svg)}')
