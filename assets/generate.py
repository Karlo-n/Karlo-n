import math
import os
OUT = os.path.dirname(os.path.abspath(__file__))
FONT = "ui-monospace,SFMono-Regular,'DejaVu Sans Mono',Menlo,Consolas,monospace"
T = {
 "dark":  dict(bg="#0d1117", panel="#161b22", line="#30363d", fg="#c9d1d9", dim="#7d8590", acc="#d29922", alt="#8b949e"),
 "light": dict(bg="#ffffff", panel="#f6f8fa", line="#d0d7de", fg="#1f2328", dim="#656d76", acc="#9a6700", alt="#57606a"),
}
ART = [
"██╗  ██╗ ██████╗ ██╗     ██████╗ ",
"██║ ██╔╝██╔═══██╗██║     ██╔══██╗",
"█████╔╝ ██║   ██║██║     ██║  ██║",
"██╔═██╗ ██║   ██║██║     ██║  ██║",
"██║  ██╗╚██████╔╝███████╗██████╔╝",
"╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═════╝ ",
]
DOTS = lambda t, y=20: f'<circle cx="24" cy="{y}" r="5.5" fill="{t["line"]}"/><circle cx="42" cy="{y}" r="5.5" fill="{t["line"]}"/><circle cx="60" cy="{y}" r="5.5" fill="{t["line"]}"/>'

def banner(t):
    cw, lh = 13.2, 22
    art = "".join(f'<text xml:space="preserve" x="40" y="{114+i*lh}" textLength="{len(l)*cw:.0f}" lengthAdjust="spacingAndGlyphs" font-size="21" fill="{t["acc"] if i < 5 else t["dim"]}">{l}</text>' for i, l in enumerate(ART))
    info = [("alias", "kold"), ("carrera", "TPSI"), ("foco", "backend"), ("", "ciberseguridad"), ("shell", "bash"), ("os", "linux")]
    rows = "".join(f'<text xml:space="preserve" x="0" y="{i*24}"><tspan fill="{t["acc"]}">{k:<8}</tspan><tspan fill="{t["fg"]}">{v}</tspan></text>' for i, (k, v) in enumerate(info))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="300" viewBox="0 0 960 300">
<style>text{{font-family:{FONT}}} .c{{animation:b 1.1s steps(1) infinite}} @keyframes b{{50%{{opacity:0}}}}</style>
<rect x=".5" y=".5" width="959" height="299" rx="10" fill="{t['bg']}" stroke="{t['line']}"/>
<path d="M.5 40 H959.5" stroke="{t['line']}"/>{DOTS(t)}
<text x="480" y="25" font-size="13" fill="{t['dim']}" text-anchor="middle">kold@tpsi: ~</text>
<text x="40" y="70" font-size="14" fill="{t['dim']}">$ <tspan fill="{t['fg']}">figlet kold</tspan></text>
{art}
<text x="40" y="268" font-size="14" fill="{t['dim']}">$ <tspan class="c" fill="{t['acc']}">█</tspan></text>
<line x1="560" y1="70" x2="560" y2="260" stroke="{t['line']}"/>
<g transform="translate(596,92)" font-size="15">{rows}</g>
</svg>'''

def whoami(t):
    P = lambda cmd: f'<tspan fill="{t["acc"]}">kold@tpsi</tspan><tspan fill="{t["dim"]}">:~$ </tspan><tspan fill="{t["fg"]}">{cmd}</tspan>'
    KV = lambda k, v: f'<tspan fill="{t["alt"]}">{k:<11}</tspan><tspan fill="{t["fg"]}">{v}</tspan>'
    lines = [P("whoami"), KV("usuario", "kold"), KV("estudia", "Tecnólogo en Sistemas Informáticos"),
             KV("le_gusta", "entender cómo funcionan las cosas por dentro"), "",
             P("cat ahora.txt"), f'<tspan fill="{t["fg"]}">- montando un servidor linux en casa para practicar</tspan>',
             f'<tspan fill="{t["fg"]}">- haciendo máquinas de TryHackMe</tspan>',
             f'<tspan fill="{t["fg"]}">- construyendo una API REST con Node y PostgreSQL</tspan>', "",
             P('<tspan class="c" fill="' + t["acc"] + '">█</tspan>')]
    y, out, d = 76, "", 0.0
    for l in lines:
        if l: out += f'<text xml:space="preserve" class="r" style="animation-delay:{d:.2f}s" x="28" y="{y}">{l}</text>'
        y += 26; d += 0.25
    h = y + 6
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="{h}" viewBox="0 0 960 {h}">
<style>text{{font-family:{FONT};font-size:15px}} .r{{opacity:0;animation:in .2s forwards}} @keyframes in{{to{{opacity:1}}}} .c{{animation:b 1.1s steps(1) infinite}} @keyframes b{{50%{{opacity:0}}}}</style>
<rect x=".5" y=".5" width="959" height="{h-1}" rx="10" fill="{t['bg']}" stroke="{t['line']}"/>
<path d="M.5 40 H959.5" stroke="{t['line']}"/>{DOTS(t)}
<text x="480" y="25" font-size="13" fill="{t['dim']}" text-anchor="middle">bash — 96x{len(lines)}</text>
{out}</svg>'''

def radar(t, title, axes):
    cx, cy, R, n = 190, 210, 115, len(axes)
    pt = lambda i, r: (cx + r*math.sin(2*math.pi*i/n), cy - r*math.cos(2*math.pi*i/n))
    ring = lambda k: " ".join(f"{x:.1f},{y:.1f}" for x, y in (pt(i, R*k/4) for i in range(n)))
    g = "".join(f'<polygon points="{ring(k)}" fill="none" stroke="{t["line"]}" stroke-dasharray="{"" if k == 4 else "2 3"}"/>' for k in range(1, 5))
    g += "".join(f'<line x1="{cx}" y1="{cy}" x2="{pt(i,R)[0]:.1f}" y2="{pt(i,R)[1]:.1f}" stroke="{t["line"]}"/>' for i in range(n))
    poly = " ".join(f"{pt(i,R*v/100)[0]:.1f},{pt(i,R*v/100)[1]:.1f}" for i, (_, v) in enumerate(axes))
    dots = "".join(f'<rect x="{pt(i,R*v/100)[0]-3:.1f}" y="{pt(i,R*v/100)[1]-3:.1f}" width="6" height="6" fill="{t["acc"]}"/>' for i, (_, v) in enumerate(axes))
    lab = ""
    for i, (name, v) in enumerate(axes):
        x, y = pt(i, R + 20)
        a = "middle" if abs(x - cx) < 5 else ("start" if x > cx else "end")
        lab += f'<text x="{x:.1f}" y="{y+4:.1f}" text-anchor="{a}" fill="{t["fg"]}">{name}</text>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="380" height="370" viewBox="0 0 380 370">
<style>text{{font-family:{FONT};font-size:12px}}</style>
<rect x=".5" y=".5" width="379" height="369" rx="10" fill="{t['bg']}" stroke="{t['line']}"/>
<text x="20" y="30" fill="{t['dim']}">$ <tspan fill="{t['fg']}">{title}</tspan></text>
{g}<polygon points="{poly}" fill="{t['acc']}" fill-opacity=".15" stroke="{t['acc']}" stroke-width="1.5"/>{dots}{lab}
</svg>'''

# Autoevaluación 0-100: editar con valores reales.
SYS = [("linux", 65), ("redes", 55), ("seguridad", 50), ("bases de datos", 60), ("git", 70), ("docker", 40)]
DEV = [("javascript", 65), ("python", 60), ("java", 55), ("sql", 60), ("html/css", 75), ("bash", 50)]
for m, t in T.items():
    for name, svg in {"banner": banner(t), "whoami": whoami(t),
                      "radar-sys": radar(t, "skills --sistemas", SYS),
                      "radar-dev": radar(t, "skills --lenguajes", DEV)}.items():
        open(f"{OUT}/{name}-{m}.svg", "w").write(svg)
