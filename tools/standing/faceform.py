# -*- coding: utf-8 -*-
"""standing/faceform.py -- v1.8.0, (R338)(2)(iv)(a), (c) AND (vii): THE FACE'S FIELDS AND THE CLAUSES THE CLOSING IS COMPOSED FROM.

(a) THE FIELD OF PRE-FACE COMMITS: a sitting act's commits made before its face stand on the face by hash, one line, so G-NOTHING-RAN-AHEAD reads
    a field and not a hash somewhere in the prose (b727 event (4): seven PLACE-papers commits stood in the sitting bank and on no face).
(c) THE CLOSING'S OUTBOUND SENTENCE: one clause, written here, the face and the closing composing it, so no rewrite of a closing section drops a
    phrase G-CLOSING-SENTENCE reads (b727 event (6): "plain requests to github.com").
(vii) THE KERNEL-FILES CLAUSE OF N5: README.md, and AGENTS.md beside it on the kernels whose AGENTS item a ruling passes by number (b727 (g): N5's
    words named README.md alone while [20] and [22], passed, wrote SIDE-cosmo's AGENTS.md).
Pure in its arguments; nothing written.
"""
import re

PRE_FACE_TITLE = '### THE PRE-FACE COMMITS, BY HASH:'
PRE_FACE = re.compile(r'^' + re.escape(PRE_FACE_TITLE) + r'(.*)$', re.M)
HEX = re.compile(r'\b[0-9a-f]{7,40}\b')
SECTION = re.compile(r'^### \([0-9A-Za-z]+\) ', re.M)
OUTBOUND_HEAD = ('no identifier of the author in any outbound request header, URL, input or payload, or in any workflow file ; no secret added ; '
                 'the outbound reads: the seat`s plain requests to github.com')


def pre_face_field(face):
    """the hashes of the face's field, or None where the face carries no field (a face before v1.8.0)."""
    m = PRE_FACE.search(face or '')
    return HEX.findall(m.group(1)) if m else None


def declared(h, face):
    """a commit declared on the face: by the field where the face carries one (or in the section of what ran ahead, step zero's), else by its
    7-hex prefix anywhere on the face, the reading before v1.8.0."""
    f = pre_face_field(face)
    if f is None:
        return h[:7] in (face or '')
    i = max((face or '').find('WHAT RAN AHEAD OF THIS SEAL'), 0)
    m = SECTION.search(face or '', i)
    return any(x.startswith(h[:7]) or h.startswith(x[:7]) for x in f) or h[:7] in (face or '')[i:m.start() if m else i]


def outbound_clause(tail=''):
    """the closing's outbound sentence: the standing words, the act's own reads appended."""
    return OUTBOUND_HEAD + ((' ; ' + tail) if tail else '')


def n5_kernel_clause(agents=()):
    """N5's clause for the kernels' files: `agents` [(kernel, item)] the AGENTS items a ruling passes by number."""
    s = 'README.md alone on each kernel named'
    if agents:
        s += ', AGENTS.md beside it on %s' % ' and '.join('%s by %s' % (k, i) for k, i in agents)
    return s + ' ; no .lean file, no workflow file, no tag'


def readme_writes(write_list):
    """v1.9.0, (R339)(2)(vi): N5's count of kernel README writes, derived from the (W) list and carried as no number: the kernels (W) names with a README.md."""
    out = set()
    for l in (write_list or '').split('\n'):
        i = l.find('README.md')
        if i >= 0:
            out.update(re.findall(r'SIDE-[\w-]+', l[i:]))
    return sorted(out)


def n5_count_sentence(write_list):
    r = readme_writes(write_list)
    return '%d kernel README write%s by the (W) list%s' % (len(r), '' if len(r) == 1 else 's', (': ' + ', '.join(r)) if r else '')


def kernel_file_allowed(kernel, path, agents=()):
    return path == 'README.md' or (path == 'AGENTS.md' and any(k == kernel for k, _i in agents))
