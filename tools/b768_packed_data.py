# -*- coding: utf-8 -*-
"""tools/b768_packed_data.py -- (R378)(4)(a): THE FAR SUM'S PACKED DATA, GENERATED FROM THE KERNEL'S OWN NUMERATORS.

The numerators are read from SIDE-explicit-formula's SIDEExplicitFormula/Window/Coeffs.lean in the kernel's working tree, its blob
read equal to the blob at the branch's base 89fd5b54 and at HEAD before any use; its 64 lists parsed in the order coeffList joins
them (16,365 numerators). Nothing of the window is printed: counts, lengths of literals in decimal digits, truth values and sha256
digests alone. Each generated Lean file is written into the kernel's working tree, edited by no hand, and is committed by the
one-call tool; this tool commits nothing and dispatches nothing.

  trial      SIDEExplicitFormula/Window/PackedTrial.lean: the seat's trial at small size ((R378)(4)(a), data/b768_ferry.txt :21):
             the first two lists of Coeffs.lean (512 numerators), the same list turned in two chunks of 256, the convolution sums
             in four chunks of 256 (the last place 0), the packed value of each chunk, the joined product, the sizes, and the
             convolution sums read from the general lemmas of Packed.lean (conv_of_packedL); every identity checked here first
  control    the tool's own controls, planted and printed

THE BASE: 2^133 (the navigator's sizing, data/b768_ferry.txt :19, data/b768_plan.txt :31). THE BOUND on each numerator's absolute
value: 4 x 10^17, a round figure read against the numerators here (each at most it) and against the base (2 n M^2 below it at
n = 16,365); it is no numerator and no figure of the window (data/b768_plan.txt (A3)).
"""
import hashlib
import io
import os
import re
import subprocess
import sys

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
for p_ in (T, os.path.join(T, 'standing')):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)   # ### the packed values run to some 10,000 digits; Python's text limit is 4,300 (the first run, 16:16:00Z)
import commit as CT              # noqa: E402  (KERNELS: the kernels' keys and folders, the one source)

NL = '\n'
EF = 'SIDE-explicit-formula'
KPATH = CT.KERNELS[EF]
BASE_REV = '89fd5b54941b246d707bd2e9708a8a24e222ba5c'   # ### push-b768-proof's base, main ((R378)(4), (9))
COEFFS = 'SIDEExplicitFormula/Window/Coeffs.lean'
TRIAL_OUT = 'SIDEExplicitFormula/Window/PackedTrial.lean'
BASE = 2 ** 133
BOUND = 4 * 10 ** 17
CHUNK = 256
N_ALL = 16365
BARRED = re.compile(r'frequen|ordinate|riemannZeta', re.I)
DECIMAL = re.compile(r'\d\.\d')


def git(*a):
    r = subprocess.run(['git', '-C', KPATH] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')
    if r.returncode != 0:
        sys.exit('### git %s: exit %d' % (' '.join(a[:2]), r.returncode))
    return r.stdout.strip()


def read_coeffs():
    """The 64 lists of Coeffs.lean in coeffList's order, the blob read equal at the base and at HEAD first."""
    p = os.path.join(KPATH, COEFFS)
    raw = open(p, 'rb').read()
    blob = git('hash-object', p)
    at_base = git('rev-parse', '%s:%s' % (BASE_REV, COEFFS))
    at_head = git('rev-parse', 'HEAD:%s' % COEFFS)
    text = raw.decode('utf-8').replace('\r\n', '\n')   # ### the working tree's line ends read as the blob's
    chunks = re.findall(r'def coeffChunk(\d\d) : List ℤ := \[(.*?)\]', text, re.S)
    names = [c[0] for c in chunks]
    lists = [[int(x) for x in re.findall(r'-?\d+', body)] for _, body in chunks]
    m = re.search(r'def coeffList : List ℤ :=(.*?)\n\n', text, re.S)
    order = re.findall(r'coeffChunk(\d\d)', m.group(1)) if m else []
    rep = dict(blob=blob, at_base=at_base, at_head=at_head, equal=(blob == at_base == at_head), chunks=len(lists),
               names_in_order=(names == ['%02d' % i for i in range(64)]), joined_in_order=(order == names),
               total=sum(len(x) for x in lists), lengths=sorted(set(len(x) for x in lists)),
               within_bound=all(abs(v) <= BOUND for x in lists for v in x))
    return lists, rep


def pack(b, l):
    v = 0
    for x in reversed(l):
        v = x + b * v
    return v


def join(B, vs):
    v = 0
    for x in reversed(vs):
        v = x + B * v
    return v


def conv(l, r):
    n = len(l)
    out = [0] * (2 * n)
    for i, x in enumerate(l):
        if x:
            for j, y in enumerate(r):
                out[i + j] += x * y
    return out


def lean_list(name, doc, xs):
    rows = [', '.join(str(v) for v in xs[i:i + 16]) for i in range(0, len(xs), 16)]
    return ['/-- %s -/' % doc, 'def %s : List ℤ := [' % name] + ['  ' + r + (',' if k < len(rows) - 1 else '') for k, r in enumerate(rows)] + [']', '']


def trial_text(lists, rep):
    l = lists[0] + lists[1]
    r = list(reversed(l))
    d = conv(l, r)
    n = len(l)
    B = BASE ** CHUNK
    pv = [pack(BASE, lists[0]), pack(BASE, lists[1])]
    rc = [r[i:i + CHUNK] for i in range(0, n, CHUNK)]
    qv = [pack(BASE, c) for c in rc]
    dc = [d[i:i + CHUNK] for i in range(0, 2 * n, CHUNK)]
    dv = [pack(BASE, c) for c in dc]
    chk = dict(
        lengths=(n == 512 and len(r) == 512 and len(d) == 1024 and all(len(c) == CHUNK for c in rc + dc + lists[:2])),
        top_zero=(d[-1] == 0),
        symmetric=all(d[k] == d[2 * n - 2 - k] for k in range(2 * n - 1)),
        product=(pack(BASE, l) * pack(BASE, r) == pack(BASE, d)),
        joined=(join(B, pv) == pack(BASE, l) and join(B, qv) == pack(BASE, r) and join(B, dv) == pack(BASE, d)),
        joined_product=(join(B, pv) * join(B, qv) == join(B, dv)),
        sizes=all(-BASE < 2 * x < BASE for x in d),
        bound=all(-BOUND <= x <= BOUND for x in l + r),
        base_bound=(2 * (n * BOUND * BOUND) < BASE),
        conv_direct=all(d[k] == sum(l[i] * r[k - i] for i in range(n) if 0 <= k - i < n) for k in (0, 1, 255, 511, 767, 1022, 1023)))
    L = ['import SIDEExplicitFormula.Window.Packed', 'import SIDEExplicitFormula.Window.Coeffs', '',
         '/-!',
         '# The trial at small size of the far sum`s route',
         '',
         'The first two lists of Coeffs.lean, 512 numerators, packed in the base `2 ^ 133`; the same list turned, in two chunks of',
         '256; their convolution sums, in four chunks of 256, the last place `0`. Each chunk`s packed value is checked against its',
         'list by the kernel`s evaluation, the joined product checked against the joined sums, and each sum checked below half the',
         'base in absolute value; the general lemmas of Packed.lean then read each convolution sum as its place in the data',
         '(`trial_conv`). Written by relay tools/b768_packed_data.py from Coeffs.lean as its blob stands at the branch`s base',
         '(blob %s); edited by no hand. No figure here is printed elsewhere by the generator.' % rep['blob'][:16],
         '-/', '',
         'namespace SIDEExplicitFormula', 'namespace Window', '',
         '/-- The base of the trial`s packings. -/', 'def trialBase : ℤ := 2 ^ 133', '',
         '/-- A round bound on the absolute value of each numerator. -/', 'def trialBound : ℤ := 4 * 10 ^ 17', '']
    L += lean_list('trialR0', 'The trial`s list turned, its places 0 to 255.', rc[0])
    L += lean_list('trialR1', 'The trial`s list turned, its places 256 to 511.', rc[1])
    for i in range(4):
        L += lean_list('trialD%d' % i, 'The convolution sums of the trial, places %d to %d.' % (CHUNK * i, CHUNK * i + CHUNK - 1), dc[i])
    L += ['/-- The trial`s list: the numerators for `j` from 16 to 527. -/', 'def trialL : List ℤ := [coeffChunk00, coeffChunk01].flatten', '',
          '/-- The trial`s list turned. -/', 'def trialR : List ℤ := [trialR0, trialR1].flatten', '',
          '/-- The convolution sums of the trial. -/', 'def trialD : List ℤ := [trialD0, trialD1, trialD2, trialD3].flatten', '']
    vals = [('trialPv0', 'coeffChunk00', pv[0]), ('trialPv1', 'coeffChunk01', pv[1]), ('trialQv0', 'trialR0', qv[0]),
            ('trialQv1', 'trialR1', qv[1])] + [('trialDv%d' % i, 'trialD%d' % i, dv[i]) for i in range(4)]
    for nm, src, v in vals:
        L += ['/-- The packed value of `%s`. -/' % src, 'def %s : ℤ := %d' % (nm, v), '']
    for nm, src, _v in vals:
        L += ['set_option maxHeartbeats 0 in', 'theorem %s_ok : packL trialBase %s = %s := by decide +kernel' % (nm, src, nm), '']
    L += ['theorem trialBase_ge : 2 ≤ trialBase := by decide +kernel', '',
          'theorem trialL_chunks : ∀ c ∈ [coeffChunk00, coeffChunk01], c.length = 256 := by decide +kernel', '',
          'theorem trialR_chunks : ∀ c ∈ [trialR0, trialR1], c.length = 256 := by decide +kernel', '',
          'theorem trialD_chunks : ∀ c ∈ [trialD0, trialD1, trialD2, trialD3], c.length = 256 := by decide +kernel', '',
          'theorem trialR_len : trialR.length = trialL.length := by decide +kernel', '',
          'theorem trialD_len : trialD.length = 2 * trialL.length := by decide +kernel', '',
          'theorem trial_bM : 2 * ((trialL.length : ℤ) * (trialBound * trialBound)) < trialBase := by decide +kernel', '',
          'set_option maxHeartbeats 0 in',
          'theorem trial_join_ok : joinV (trialBase ^ 256) [trialPv0, trialPv1] * joinV (trialBase ^ 256) [trialQv0, trialQv1] =',
          '    joinV (trialBase ^ 256) [trialDv0, trialDv1, trialDv2, trialDv3] := by decide +kernel', '',
          '/-- The product of the packed trial list and the packed list turned is the packed convolution sums. -/',
          'theorem trial_prod : packL trialBase trialL * packL trialBase trialR = packL trialBase trialD := by',
          '  unfold trialL trialR trialD',
          '  rw [packL_flatten trialBase 256 _ trialL_chunks, packL_flatten trialBase 256 _ trialR_chunks,',
          '    packL_flatten trialBase 256 _ trialD_chunks]',
          '  simp only [List.map_cons, List.map_nil, trialPv0_ok, trialPv1_ok, trialQv0_ok, trialQv1_ok, trialDv0_ok, trialDv1_ok,',
          '    trialDv2_ok, trialDv3_ok]',
          '  exact trial_join_ok', '',
          'set_option maxHeartbeats 0 in',
          'theorem trialL_bd : ∀ x ∈ trialL, -trialBound ≤ x ∧ x ≤ trialBound :=',
          '  forall_of_all (P := fun x => -trialBound ≤ x ∧ x ≤ trialBound) trialL (by decide +kernel)', '',
          'set_option maxHeartbeats 0 in',
          'theorem trialR_bd : ∀ x ∈ trialR, -trialBound ≤ x ∧ x ≤ trialBound :=',
          '  forall_of_all (P := fun x => -trialBound ≤ x ∧ x ≤ trialBound) trialR (by decide +kernel)', '',
          'set_option maxHeartbeats 0 in',
          'theorem trialD_bd : ∀ x ∈ trialD, -trialBase < 2 * x ∧ 2 * x < trialBase :=',
          '  forall_of_all (P := fun x => -trialBase < 2 * x ∧ 2 * x < trialBase) trialD (by decide +kernel)', '',
          '/-- **The trial**: each convolution sum of the trial list and its turn is the place of the data at its index. -/',
          'theorem trial_conv : ∀ k < 2 * trialL.length,',
          '    convR trialL.length (fun i => trialL.getD i 0) (fun j => trialR.getD j 0) k = trialD.getD k 0 :=',
          '  conv_of_packedL (M := trialBound) trialBase_ge trialL trialR trialD trialR_len trialD_len trialL_bd trialR_bd trial_bM',
          '    trialD_bd trial_prod', '',
          'end Window', 'end SIDEExplicitFormula', '']
    digits = max(len(str(abs(v))) for _, _, v in vals)
    return NL.join(L), chk, digits


def text_checks(t):
    lines = t.split(NL)
    first = next((l for l in lines if l.strip() and not l.startswith('--')), '')
    longest = max([len(re.findall(r'-?\d+', b)) for b in re.findall(r':= \[(.*?)\]', t, re.S)] + [0])
    return dict(decimal=len(DECIMAL.findall(t)), barred=len(BARRED.findall(t)), import_first=first.startswith('import '),
                longest_list=longest, lines=t.count(NL), bytes=len(t.encode('utf-8')),
                sha256=hashlib.sha256(t.encode('utf-8')).hexdigest()[:16])


def decl_lines(t):
    out = []
    for i, l in enumerate(t.split(NL), 1):
        m = re.match(r'(theorem|def) (\w+)', l)
        if m and not (m.group(1) == 'def' and re.match(r'trial(R|D)\d$', m.group(2))):
            out.append('%s:%d' % (m.group(2), i))
    return out


def cmd_trial(mode='dry'):
    lists, rep = read_coeffs()
    print('  Coeffs.lean: blob %s, at the base %s, at HEAD %s -> EQUAL %s ; lists %d, named in order %s, joined in coeffList`s order %s ; '
          'numerators %d ; list lengths %s ; each within the round bound %s' % (rep['blob'][:12], rep['at_base'][:12], rep['at_head'][:12],
                                                                           rep['equal'], rep['chunks'], rep['names_in_order'],
                                                                           rep['joined_in_order'], rep['total'], rep['lengths'],
                                                                           rep['within_bound']))
    if not (rep['equal'] and rep['chunks'] == 64 and rep['names_in_order'] and rep['joined_in_order'] and rep['total'] == N_ALL
            and rep['within_bound']):
        sys.exit('### NOT WRITTEN: Coeffs.lean is not read as the base holds it')
    t, chk, digits = trial_text(lists, rep)
    tc = text_checks(t)
    print('  the checks before the write: %s' % ' ; '.join('%s %s' % kv for kv in chk.items()))
    print('  the text: lines %d, bytes %d, sha256 %s ; decimal literals %d ; barred words %d ; imports first %s ; the longest list %d ; '
          'the longest packed literal %d digits' % (tc['lines'], tc['bytes'], tc['sha256'], tc['decimal'], tc['barred'], tc['import_first'],
                                                    tc['longest_list'], digits))
    print('  declarations (name:line), the lists of data left out: %s' % ', '.join(decl_lines(t)))
    ok = all(chk.values()) and not tc['decimal'] and not tc['barred'] and tc['import_first'] and tc['longest_list'] <= CHUNK
    if not ok:
        sys.exit('### NOT WRITTEN: a check failed')
    if mode != 'write':
        print('### DRY: nothing written')
        return
    out = os.path.join(KPATH, TRIAL_OUT)
    with io.open(out, 'w', encoding='utf-8', newline='\n') as f:
        f.write(t)
    back = open(out, 'rb').read()
    print('### WRITTEN %s: %d bytes, sha256 %s, read back EQUAL %s' % (TRIAL_OUT, len(back), hashlib.sha256(back).hexdigest()[:16],
                                                                     back == t.encode('utf-8')))


def cmd_control():
    res = []

    def c(name, got, ok):
        res.append(ok)
        print('  (%d) %s: %s -> %s' % (len(res), name, got, 'AS WANTED' if ok else 'NOT AS WANTED'))
    l, r = [3, -1, 4, 1, -5], [2, 7, -1, 8, 2]
    d = conv(l, r)
    b = 2 ** 20
    c('pack, conv and the product on a planted list (the product of the packings the packing of the sums)',
      pack(b, l) * pack(b, r) == pack(b, d), pack(b, l) * pack(b, r) == pack(b, d))
    d2 = list(d)
    d2[3] += 1
    c('A PLANTED FAULT: one sum moved by 1, the product check reads it', pack(b, l) * pack(b, r) == pack(b, d2),
      pack(b, l) * pack(b, r) != pack(b, d2))
    big = [10 ** 6] * 4
    db = conv(big, big)
    c('A PLANTED FAULT: a base below twice the largest sum, the size check reads it', all(-16 < 2 * x < 16 for x in db),
      not all(-16 < 2 * x < 16 for x in db))
    c('the join of chunks: the packed value of a list the joined values of its chunks of 2',
      join(b ** 2, [pack(b, l[0:2]), pack(b, l[2:4]), pack(b, l[4:])]) == pack(b, l),
      join(b ** 2, [pack(b, l[0:2]), pack(b, l[2:4]), pack(b, l[4:])]) == pack(b, l))
    lists, rep = read_coeffs()
    c('Coeffs.lean read: the blob equal at the base and HEAD, 64 lists in order, 16,365 numerators, each within the round bound',
      (rep['equal'], rep['chunks'], rep['names_in_order'], rep['joined_in_order'], rep['total'], rep['within_bound']),
      rep['equal'] and rep['chunks'] == 64 and rep['names_in_order'] and rep['joined_in_order'] and rep['total'] == N_ALL and rep['within_bound'])
    c('the base against the bound at the full list: 2 n M^2 below 2^133 at n = 16,365', 2 * (N_ALL * BOUND * BOUND) < BASE,
      2 * (N_ALL * BOUND * BOUND) < BASE)
    t, chk, _ = trial_text(lists, rep)
    tc = text_checks(t)
    c('the trial`s checks and text (each identity, no decimal literal, no barred word, imports first, lists of 256 at most)',
      (all(chk.values()), tc['decimal'], tc['barred'], tc['import_first'], tc['longest_list']),
      all(chk.values()) and not tc['decimal'] and not tc['barred'] and tc['import_first'] and tc['longest_list'] <= CHUNK)
    c('THE TEXT CHECK`S POSITIVE CONTROL: a planted decimal literal and a barred word read', text_checks('import X\n-- 1.5 frequency\n'),
      text_checks('import X\n-- 1.5 frequency\n')['decimal'] == 1 and text_checks('import X\n-- 1.5 frequency\n')['barred'] == 1)
    print('### THE TOOL`S CONTROLS: %d OF %d AS WANTED' % (sum(res), len(res)))


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['trial']:
        cmd_trial(*(a[1:2] or ['dry']))
    elif a[:1] == ['control']:
        cmd_control()
    else:
        sys.exit(__doc__)
