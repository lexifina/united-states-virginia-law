"""Virginia Law Library CSV (one file per Code title): rows -> section units, in force on a given day. Cache only."""
import csv
import hashlib
import html
import io
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
CACHE = HERE / '.hcache'
BASE = 'https://law.lis.virginia.gov'
MON = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']
HISTORY = re.compile(r'^(\d{4}\b|Acts? \d{4}|Code 19\d\d|Code \d{4}|R\. ?P\. 1948|\d{4}, c\.)')


def cached(url):
    return (CACHE / hashlib.sha256(url.encode()).hexdigest()).read_bytes()


def clean(s):
    s = html.unescape(re.sub(r'<[^>]+>', '', s)).replace('\xa0', ' ').replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('–', '-').replace('—', '-')
    return re.sub(r'\s+', ' ', s).strip()


def pad(seg):
    m = re.match(r'^(\d+)(.*)$', seg)
    return f'{int(m.group(1)):03d}{m.group(2)}' if m else seg


def ukey(disp):
    segs = [p for p in re.split(r'[-.:]', disp.lower().replace(' ', '')) if p]
    return '-'.join(pad(p) if i < 3 else p for i, p in enumerate(segs))


def date_in(txt):
    m = re.search(r'(' + '|'.join(MON) + r') (\d{1,2}), (\d{4})', txt.upper())
    return f'{int(m.group(3)):04d}-{MON.index(m.group(1)) + 1:02d}-{int(m.group(2)):02d}' if m else None


def in_force(cap, day):
    """(keep, caption without the status parenthetical, reason)."""
    c = cap.strip()
    m = re.match(r'^\(([^)]*)\)\s*(.*)$', c)
    par, rest = (m.group(1), m.group(2)) if m else ('', c)
    p = par.upper()
    if re.fullmatch(r'NOT IN EFFECT\.?', rest.strip().upper()) and not par:
        return False, rest, 'not in effect'
    if not par:
        return True, c, ''
    d = date_in(par)
    if 'CONTINGENT' in p:
        return ('EXPIRATION' in p), rest, 'contingent'
    if p.startswith('EFFECTIVE UNTIL') or p.startswith('REPEALED EFFECTIVE') or p.startswith('EXPIRES'):
        return (d is None or d > day), rest, 'until'
    if p.startswith('EFFECTIVE'):
        return (d is None or d <= day), rest, 'from'
    return True, c, ''


def caption(cap):
    c = clean(cap)
    return c if not c or c.endswith(('.', '?', '!')) else c + '.'


def title_rows(title):
    raw = cached(f'{BASE}/CSV/CoVTitle_{title}.csv')
    return raw, list(csv.DictReader(io.StringIO(raw.decode('utf-8-sig'))))


def paras(body):
    ps = [clean(p) for p in re.findall(r'<p[^>]*>(.*?)</p>', body, flags=re.S)]
    if not ps and body.strip():
        ps = [clean(body)]
    ps = [p for p in ps if p]
    if ps and HISTORY.match(ps[-1]):
        ps = ps[:-1]
    return ps


def units_of(title, day):
    raw, rows = title_rows(title)
    units, dropped = {}, 0
    for r in rows:
        num = r['Section'].strip()
        keep, cap, _ = in_force(r['Title'], day)
        ps = paras(r['Body'])
        if not keep or not ps:
            dropped += 1
            continue
        k = ukey(num)
        if k in units:
            k += '-dup'
        units[k] = {'label': f'Section {num}', 'kind': 'section', 'text': f'# § {num}. {caption(cap)}'.rstrip() + '\n' + '\n'.join(ps) + '\n'}
    name = rows[0]['TitleName'].strip() if rows else ''
    return raw, dict(sorted(units.items())), dropped, name
