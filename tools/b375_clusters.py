# -*- coding: utf-8 -*-
"""b375_clusters.py -- COMPONENT 2: THE CLUSTERS THE CORPUS ACTUALLY HAS.

### ### **ENUMERATED FROM TWO SOURCES THE ORDER NAMES, AND FROM NEITHER ALONE:** ### the cluster
### documents themselves, and ### **THE REGISTRY'S OWN SECTION HEADINGS AND ROWS.**
### ### **DIRECTORY NAMES ARE NOT A SOURCE**, and the order says so.
### ### ### **MEMBERSHIP COMES FROM THE REGISTRY'S OWN ROWS** -- a row names a document and sits in a
### section, and that is the registry assigning, not this seat.
### ### ### **BUT A KEYSTONE'S CLUSTER COMES FROM THE KEYSTONE'S OWN TEXT**, and where its own text
### does not name one it is ### **`UNASSIGNED`, NEVER ASSIGNED BY RESEMBLANCE** -- the order's own
### instruction, and the rule `b367` and `b372` both paid for.
### ### **A CLUSTER WITH NO KEYSTONE IS A FINDING AND IS REPORTED AS ONE.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
REGY = os.path.join(PP, 'REGISTRY.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SECTION = re.compile(r'^#{2,3}\s+(.+?)\s*$')
ROWPATH = re.compile(r'`([A-Za-z0-9_\-./]+\.md)`')
CLUSNAME = re.compile(r'^([A-Z0-9_]+?)_CLUSTER_SYNTHESIS')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(*a):
    return subprocess.run(['git', '-C', PP] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def registry_sections():
    """### **THE REGISTRY'S OWN SECTIONS AND THE DOCUMENTS ITS ROWS NAME IN EACH.**"""
    txt = io.open(REGY, encoding='utf-8', errors='replace').read()
    out, cur = {}, None
    for i, ln in enumerate(txt.split(chr(10)), 1):
        m = SECTION.match(ln)
        if m:
            cur = m.group(1).strip()
            out.setdefault(cur, dict(line=i, docs=[]))
            continue
        if cur and ln.lstrip().startswith('|'):
            for p in ROWPATH.findall(ln):
                if p.endswith('.md') and p not in out[cur]['docs']:
                    out[cur]['docs'].append(p)
    return out


def main():
    rec('=' * 100)
    rec('b375 -- COMPONENT 2: THE CLUSTERS. ### **FROM THE DOCUMENTS AND THE REGISTRY, NOT FROM PATHS.**')
    rec('=' * 100)
    rec('')
    pop = json.load(io.open(os.path.join(D, 'b375_population.json'), encoding='utf-8'))
    rows = {r['file']: r for r in pop['rows']}
    rels = list(rows)

    # ---- SOURCE ONE: the cluster documents name their own clusters ---------------------------------
    rec('-' * 100)
    rec('  ### (1) SOURCE ONE -- THE CLUSTER DOCUMENTS THEMSELVES.')
    rec('-' * 100)
    doc_clusters = {}
    for rel in rels:
        base = os.path.basename(rel)
        m = CLUSNAME.match(base)
        if m:
            doc_clusters.setdefault(m.group(1), []).append(rel)
    for k in sorted(doc_clusters):
        rec('    %-40s named by %d document(s)' % (k, len(doc_clusters[k])))
        for f in doc_clusters[k]:
            rec('        %s%s' % (f, '   ### ARCHIVED SNAPSHOT' if f.startswith('archive/') else ''))
    rec('    ### ### **CLUSTERS NAMED BY A CLUSTER-SYNTHESIS DOCUMENT : %d**' % len(doc_clusters))

    # ---- SOURCE TWO: the registry's own sections and rows -------------------------------------------
    secs = registry_sections()
    rec('')
    rec('-' * 100)
    rec("  ### (2) SOURCE TWO -- THE REGISTRY'S OWN SECTIONS AND THE DOCUMENTS ITS ROWS NAME.")
    rec('-' * 100)
    subject = {k: v for k, v in secs.items() if v['docs']}
    rec('    sections in `REGISTRY.md` : %d ; ### **SECTIONS WHOSE ROWS NAME A DOCUMENT : %d**'
        % (len(secs), len(subject)))
    for k in sorted(subject, key=lambda x: secs[x]['line']):
        rec('    REGISTRY.md:%-6d %-52s %3d document(s) named'
            % (secs[k]['line'], k[:52], len(subject[k]['docs'])))

    # ---- THE KEYSTONES, AND THE CLUSTER EACH ONE'S OWN TEXT NAMES -----------------------------------
    rec('')
    rec('-' * 100)
    rec("  ### (3) EACH KEYSTONE, AND THE CLUSTER ITS OWN TEXT NAMES.")
    rec('  ### ### **UNASSIGNED IS AN ANSWER. ### RESEMBLANCE IS NOT.**')
    rec('-' * 100)
    ks = [f for f in rels if rows[f]['order_class'] == 'KEYSTONE']
    names = sorted(set(list(doc_clusters) + [k for k in subject]))
    assigned, unassigned = {}, []
    for f in ks:
        p = os.path.join(PP, f.replace('/', os.sep))
        try:
            txt = io.open(p, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        hit = None
        # ### a cluster-synthesis basename in the keystone's own text
        for cn in sorted(doc_clusters, key=len, reverse=True):
            if cn in txt:
                hit = (cn, 'its own text names the cluster `%s`' % cn)
                break
        if hit is None:
            # ### a registry section title quoted in the keystone's own text
            for sec in sorted(subject, key=len, reverse=True):
                core = re.sub(r'^[0-9.]+[A-Z]?:\s*', '', sec).strip()
                if len(core) >= 10 and core in txt:
                    hit = (sec, 'its own text names the registry section `%s`' % sec)
                    break
        if hit:
            assigned.setdefault(hit[0], []).append((f, hit[1]))
        else:
            unassigned.append(f)
    for cn in sorted(assigned):
        rec('')
        rec('    ### CLUSTER `%s` ### -- %d keystone(s)' % (cn, len(assigned[cn])))
        for f, why in assigned[cn]:
            rec('        %-62s ### %s' % (f[:62], why))
    rec('')
    rec('    ### ### **UNASSIGNED KEYSTONES : %d** ### -- their own text names no cluster this act'
        % len(unassigned))
    rec('    ### ### can enumerate, and ### **NONE IS ASSIGNED BY RESEMBLANCE.**')
    for f in unassigned:
        rec('        %s' % f)

    # ---- CLUSTERS WITH SUPPORT AND NO KEYSTONE -----------------------------------------------------
    rec('')
    rec('-' * 100)
    rec('  ### (4) THE CLUSTERS, WITH THEIR SUPPORT AND WHETHER A KEYSTONE EXISTS AT ALL.')
    rec('-' * 100)
    table = []
    for sec in sorted(subject, key=lambda x: secs[x]['line']):
        docs = subject[sec]['docs']
        present = [d2 for d2 in docs if d2 in rows]
        sup = [d2 for d2 in present if rows[d2]['order_class'] == 'SUPPORT']
        key = [d2 for d2 in present if rows[d2]['order_class'] == 'KEYSTONE']
        oth = [d2 for d2 in present if rows[d2]['order_class'] == 'OTHER']
        table.append(dict(cluster=sec, registry_line=secs[sec]['line'], named=len(docs),
                          resolved=len(present), support=sup, keystones=key, other=len(oth),
                          has_keystone=bool(key)))
    rec('    %-54s %6s %6s %6s %6s  %s' % ('cluster (registry section)', 'named', 'found',
                                           'KEY', 'SUP', 'keystone?'))
    for t2 in table:
        rec('    %-54s %6d %6d %6d %6d  %s'
            % (t2['cluster'][:54], t2['named'], t2['resolved'], len(t2['keystones']),
               len(t2['support']), 'yes' if t2['has_keystone'] else '### **NO KEYSTONE**'))
    # ### ### **A REGISTRY MAINTENANCE BLOCK IS NOT A SUBJECT CLUSTER**, and the order asks for the
    # ### ### SUBJECT clusters the corpus actually has. ### The partition is by the heading's own
    # ### shape -- a dated `Row addition`, `Version-log addition`, `Deposit gates` or a titles table
    # ### is the registry maintaining itself -- and ### **BOTH HALVES ARE REPORTED**, because a rule
    # ### that quietly discarded sections would be choosing the census's own answer.
    ADDENDUM = re.compile(r'^(Row addition|Version-log addition|Deposit gates|VERSION LOG|'
                          r'RATIFIED PUBLIC TITLES|PATENT STATE)', re.I)
    for t2 in table:
        t2['subject_cluster'] = not bool(ADDENDUM.match(t2['cluster']))
    nokey = [t2 for t2 in table if not t2['has_keystone'] and t2['resolved'] > 0]
    subj_nokey = [t2 for t2 in nokey if t2['subject_cluster']]
    withsup = [t2 for t2 in nokey if t2['support']]
    rec('')
    rec('    ### ### **SECTIONS WITH DOCUMENTS AND NO KEYSTONE : %d**' % len(nokey))
    rec('    ### ### **AND THE PARTITION THAT MATTERS, BY THE HEADING`S OWN SHAPE:** ### a dated')
    rec('    ### ### `Row addition`, `Version-log addition`, `Deposit gates`, a version log or a titles')
    rec('    ### ### table is ### **THE REGISTRY MAINTAINING ITSELF, NOT A SUBJECT CLUSTER.**')
    rec('    ### ### ### **SUBJECT CLUSTERS WITH DOCUMENTS AND NO KEYSTONE : %d**' % len(subj_nokey))
    for t2 in subj_nokey:
        rec('        `%s`' % t2['cluster'])
        rec('            %d document(s) resolved, %d SUPPORT, %d OTHER, ### **NO KEYSTONE**'
            % (t2['resolved'], len(t2['support']), t2['other']))
        for s in t2['support']:
            rec('            SUPPORT : %s' % s)
    rec('')
    rec('    ### **AND ACROSS BOTH HALVES, SECTIONS CARRYING AT LEAST ONE `SUPPORT` DOCUMENT AND NO')
    rec('    ### KEYSTONE : %d**' % len(withsup))
    for t2 in withsup:
        rec('        `%s` ### -- %d support document(s)%s'
            % (t2['cluster'][:70], len(t2['support']),
               '' if t2['subject_cluster'] else '   ### REGISTRY ADDENDUM, NOT A SUBJECT CLUSTER'))
        for s in t2['support']:
            rec('            %s' % s)
    rec('    ### ### **A CLUSTER WITH NO KEYSTONE IS A FINDING AND IS REPORTED AS ONE**, not as a hole')
    rec('    ### in the sweep.')

    rec('')
    rec('=' * 100)
    rec('  ### **NO CLUSTER WAS ENUMERATED FROM A DIRECTORY NAME.**')
    rec('  ### **NO KEYSTONE WAS ASSIGNED TO A CLUSTER BY RESEMBLANCE.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b375_clusters_notes', LINES)
    io.open(os.path.join(D, 'b375_clusters.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(doc_clusters=doc_clusters,
                        registry_sections={k: dict(line=v['line'], docs=v['docs'])
                                           for k, v in subject.items()},
                        keystones=len(ks), assigned={k: [f for f, _w in v]
                                                     for k, v in assigned.items()},
                        unassigned=unassigned, table=table,
                        clusters_without_keystone=[t2['cluster'] for t2 in nokey],
                        subject_clusters_without_keystone=[t2['cluster'] for t2 in subj_nokey],
                        with_support_no_keystone=[t2['cluster'] for t2 in withsup],
                        assigned_by_resemblance=0, enumerated_from_directories=0,
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
                   indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
