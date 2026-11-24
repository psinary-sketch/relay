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
  full       L9c1's data ((R378)(4)(a), (b); data/b768_plan.txt :67-:70): the seven files SIDEExplicitFormula/Window/AutoData0.lean,
             AutoData1.lean (the autocorrelation A(d), d = 0 to 16,364, from the balanced digits of P x Q), AutoP.lean and AutoQ.lean (the
             numerators and their turn packed chunk by chunk), AutoR0.lean and AutoR1.lean (the convolution sums, A laid symmetrically
             about the place 16,364, packed chunk by chunk) and AutoConv.lean (the joins, the product, the lengths and sizes, and auto_conv
             by conv_of_packedL); each kernel evaluation 16 chunks, 4,096 places at most; every identity checked here first
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
import time

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


FULL_DIR = 'SIDEExplicitFormula/Window/'
BLK = 16        # ### chunks per kernel evaluation: 16 x 256 = 4,096 places, within the 4,100 of the seat's rule ((R378)(4), KT_CAP)
NB = 133        # ### the base 2^133 by its bits


def bits_pack(digs, nb=NB):
    """sum digs[k] (2^nb)^k for digits each in [-2^(nb-1), 2^(nb-1)), by one binary text (linear in the places)."""
    h = 1 << (nb - 1)
    s = ''.join(format(d + h, '0%db' % nb) for d in reversed(digs))
    return int(s, 2) - int(('1' + '0' * (nb - 1)) * len(digs), 2)


def bits_digits(R, n, nb=NB):
    """the n balanced digits of R in the base 2^nb, each in [-2^(nb-1), 2^(nb-1)), or None where R has no such n places."""
    h = 1 << (nb - 1)
    Rp = R + int(('1' + '0' * (nb - 1)) * n, 2)
    if Rp < 0 or Rp >> (nb * n):
        return None
    s = format(Rp, 'b').zfill(nb * n)
    L = len(s)
    return [int(s[L - nb * (k + 1): L - nb * k], 2) - h for k in range(n)]


def join_g(infos, nb=NB):
    v = 0
    for x, n in reversed(infos):
        v = x + (v << (nb * n))
    return v


def full_data(lists):
    """the data of L9c1 from Coeffs.lean's 64 lists: the numerators l, their turn r, the product's balanced digits D (the convolution sums),
    the autocorrelation A (A[d] = D[N - 1 + d]), and the chunks of P, Q and D in the order the Lean joins them."""
    l = [v for c in lists for v in c]
    N = len(l)
    r = l[::-1]
    P, Q = bits_pack(l), bits_pack(r)
    D = bits_digits(P * Q, 2 * N) or []
    A = D[N - 1:2 * N - 1]
    aC = [A[256 * k:256 * (k + 1)] for k in range(64)]
    head, t00 = A[:1], A[1:256]
    pch = [('coeffChunk%02d' % k, lists[k]) for k in range(64)]
    qch = [('coeffChunk%02d.reverse' % k, list(reversed(lists[k]))) for k in range(63, -1, -1)]
    dch = ([('autoC%02d.reverse' % k, list(reversed(aC[k]))) for k in range(63, 0, -1)] + [('autoT00.reverse', list(reversed(t00))),
           ('autoHead', head), ('autoT00', t00)] + [('autoC%02d' % k, aC[k]) for k in range(1, 64)] + [('autoZero', [0])])
    info = lambda ch: [(pack(BASE, c), len(c)) for _n, c in ch]
    pi, qi, di = info(pch), info(qch), info(dch)
    chk = dict(
        lengths=(N == N_ALL and len(D) == 2 * N and len(dch) == 130 and sum(len(c) for _n, c in dch) == 2 * N and max(len(c) for _n, c in dch) <= CHUNK),
        digits=(bool(D) and bits_pack(D) == P * Q),
        flat_d=([v for _n, c in dch for v in c] == D),
        flat_q=([v for _n, c in qch for v in c] == r),
        top_zero=(bool(D) and D[-1] == 0),
        symmetric=(bool(D) and all(D[k] == D[2 * N - 2 - k] for k in range(2 * N - 1))),
        sizes=(bool(D) and all(-BASE < 2 * x < BASE for x in D)),
        bound=all(-BOUND <= x <= BOUND for x in l),
        base_bound=(2 * (N * BOUND * BOUND) < BASE),
        auto_direct=(bool(A) and all(A[d] == sum(l[i] * l[i + d] for i in range(N - d)) for d in (0, 1, 2, 3, 255, 256, 8191, 16363, 16364))),
        joined=(join_g(pi) == P and join_g(qi) == Q and join_g(di) == P * Q),
        joined_product=(join_g(pi) * join_g(qi) == join_g(di)))
    return dict(N=N, D=D, A=A, aC=aC, head=head, t00=t00, pch=pch, qch=qch, dch=dch, pi=pi, qi=qi, di=di), chk


def _ns(body):
    return ['namespace SIDEExplicitFormula', 'namespace Window', ''] + body + ['end Window', 'end SIDEExplicitFormula', '']


def _blocks(prefix, ch, vals, letter, imports_doc):
    """the value defs, the block lists, the info lists and the block checks of one packing's chunks."""
    L = []
    for i, ((nm, _c), (v, n)) in enumerate(zip(ch, vals)):
        L += ['/-- The packed value of `%s`, %d places. -/' % (nm, n), 'def %s%s : ℤ := %d' % (prefix, vals_name(i), v), '']
    nb = (len(ch) + BLK - 1) // BLK
    for b in range(nb):
        part = list(range(b * BLK, min(len(ch), (b + 1) * BLK)))
        L += ['/-- The chunks %d to %d of the %s packing. -/' % (part[0], part[-1], letter),
              'def %sBlk%d : List (List ℤ) := [%s]' % (prefix, b, ', '.join(ch[i][0] for i in part)), '',
              '/-- Their packed values with their lengths. -/',
              'def %sI%d : List (ℤ × ℕ) := [%s]' % (prefix, b, ', '.join('(%s%s, %d)' % (prefix, vals_name(i), vals[i][1]) for i in part)), '',
              'set_option maxHeartbeats 0 in',
              'theorem %s_info%d : %sBlk%d.map (chunkInfo packBase) = %sI%d := by decide +kernel' % (prefix, b, prefix, b, prefix, b), '']
    return L, nb


def vals_name(i):
    return 'v%03d' % i


def full_texts(fd, rep):
    head = lambda doc: ['/-!', doc, '', 'Written by relay tools/b768_packed_data.py from Coeffs.lean as its blob stands at the branch`s base (blob %s);'
                        % rep['blob'][:16], 'edited by no hand.', '-/', '']
    out = {}
    aC, A = fd['aC'], fd['A']
    d0 = lean_list('autoHead', 'The autocorrelation at the lag 0.', fd['head']) + lean_list('autoT00', 'The autocorrelation at the lags 1 to 255.', fd['t00'])
    for k in range(1, 32):
        d0 += lean_list('autoC%02d' % k, 'The autocorrelation at the lags %d to %d.' % (256 * k, 256 * k + len(aC[k]) - 1), aC[k])
    out['AutoData0'] = (['import SIDEExplicitFormula.Window.PackedJoin', ''] +
                        head('# The autocorrelation of the window`s numerators, the lags 0 to 8191, as data') + _ns(d0))
    d1 = []
    for k in range(32, 64):
        d1 += lean_list('autoC%02d' % k, 'The autocorrelation at the lags %d to %d.' % (256 * k, 256 * k + len(aC[k]) - 1), aC[k])
    d1 += lean_list('autoZero', 'The place past the last lag.', [0])
    out['AutoData1'] = (['import SIDEExplicitFormula.Window.PackedJoin', ''] +
                        head('# The autocorrelation of the window`s numerators, the lags 8192 to 16364, as data') + _ns(d1))
    pb, _ = _blocks('autoP', fd['pch'], fd['pi'], 'numerators`', None)
    for b in range(4):
        pb += ['set_option maxHeartbeats 0 in',
               'theorem autoP_bd%d : (autoPBlk%d.all fun c => c.all fun x => decide (-numBound ≤ x ∧ x ≤ numBound)) = true := by' % (b, b),
               '  decide +kernel', '']
    out['AutoP'] = (['import SIDEExplicitFormula.Window.PackedJoin', 'import SIDEExplicitFormula.Window.Coeffs', ''] +
                    head('# The numerators packed in the base `2 ^ 133`, chunk by chunk, each value checked by the kernel') + _ns(pb))
    qb, _ = _blocks('autoQ', fd['qch'], fd['qi'], 'turned', None)
    for b in range(4):
        qb += ['set_option maxHeartbeats 0 in',
               'theorem autoQ_bd%d : (autoQBlk%d.all fun c => c.all fun x => decide (-numBound ≤ x ∧ x ≤ numBound)) = true := by' % (b, b),
               '  decide +kernel', '']
    out['AutoQ'] = (['import SIDEExplicitFormula.Window.PackedJoin', 'import SIDEExplicitFormula.Window.Coeffs', ''] +
                    head('# The numerators turned, packed in the base `2 ^ 133`, chunk by chunk, each value checked by the kernel') + _ns(qb))
    dch, di = fd['dch'], fd['di']
    for part, lo, hi, blo in (('AutoR0', 0, 64, 0), ('AutoR1', 64, 130, 4)):
        L = []
        for i in range(lo, hi):
            L += ['/-- The packed value of `%s`, %d places. -/' % (dch[i][0], di[i][1]), 'def autoR%s : ℤ := %d' % (vals_name(i), di[i][0]), '']
        for b in range(blo, (hi + BLK - 1) // BLK if hi < 130 else 9):
            idx = list(range(b * BLK, min(130, (b + 1) * BLK)))
            idx = [i for i in idx if lo <= i < hi]
            if not idx:
                continue
            L += ['/-- The chunks %d to %d of the convolution sums. -/' % (idx[0], idx[-1]),
                  'def autoRBlk%d : List (List ℤ) := [%s]' % (b, ', '.join(dch[i][0] for i in idx)), '',
                  '/-- Their packed values with their lengths. -/',
                  'def autoRI%d : List (ℤ × ℕ) := [%s]' % (b, ', '.join('(autoR%s, %d)' % (vals_name(i), di[i][1]) for i in idx)), '',
                  'set_option maxHeartbeats 0 in',
                  'theorem autoR_info%d : autoRBlk%d.map (chunkInfo packBase) = autoRI%d := by decide +kernel' % (b, b, b), '',
                  'set_option maxHeartbeats 0 in',
                  'theorem autoR_bd%d : (autoRBlk%d.all fun c => c.all fun x => decide (-packBase < 2 * x ∧ 2 * x < packBase)) = true := by' % (b, b),
                  '  decide +kernel', '']
        out[part] = (['import SIDEExplicitFormula.Window.AutoData0', 'import SIDEExplicitFormula.Window.AutoData1', ''] +
                     head('# The convolution sums packed in the base `2 ^ 133`, chunk by chunk, each value checked by the kernel') + _ns(L))
    pB = ' ++ '.join('autoPBlk%d' % b for b in range(4))
    qB = ' ++ '.join('autoQBlk%d' % b for b in range(4))
    rB = ' ++ '.join('autoRBlk%d' % b for b in range(9))
    pI = ' ++ '.join('autoPI%d' % b for b in range(4))
    qI = ' ++ '.join('autoQI%d' % b for b in range(4))
    rI = ' ++ '.join('autoRI%d' % b for b in range(9))
    ma = lambda n: ', '.join(['List.map_append'] * n)
    infos = lambda pre, n: ', '.join('%s_info%d' % (pre, b) for b in range(n))
    bds = lambda pre, n: ', '.join('%s_bd%d' % (pre, b) for b in range(n))
    blks = lambda pre, n: ', '.join('%sBlk%d' % (pre, b) for b in range(n))
    C = ['/-- The convolution sums of the numerators and their turn: the autocorrelation laid symmetrically about the place 16364,',
         'the last place `0`. -/', 'def autoD : List ℤ := (%s).flatten' % rB, '',
         'theorem coeffList_blocks : coeffList = (%s).flatten := by' % pB,
         '  simp only [coeffList, %s, List.cons_append, List.nil_append, List.flatten_cons, List.flatten_nil,' % blks('autoP', 4),
         '    List.append_nil, List.append_assoc]', '',
         'theorem coeffList_rev_blocks : coeffList.reverse = (%s).flatten := by' % qB,
         '  simp only [coeffList, %s, List.reverse_append, List.cons_append, List.nil_append, List.flatten_cons,' % blks('autoQ', 4),
         '    List.flatten_nil, List.append_nil, List.append_assoc]', '',
         'theorem auto_P : packL packBase coeffList = joinG packBase (%s) := by' % pI,
         '  rw [coeffList_blocks, packL_flatten_gen, %s, %s]' % (ma(3), infos('autoP', 4)), '',
         'theorem auto_Q : packL packBase coeffList.reverse = joinG packBase (%s) := by' % qI,
         '  rw [coeffList_rev_blocks, packL_flatten_gen, %s, %s]' % (ma(3), infos('autoQ', 4)), '',
         'theorem auto_R : packL packBase autoD = joinG packBase (%s) := by' % rI,
         '  unfold autoD', '  rw [packL_flatten_gen, %s, %s]' % (ma(8), infos('autoR', 9)), '',
         'set_option maxHeartbeats 0 in',
         'theorem auto_join_ok : joinG packBase (%s) * joinG packBase (%s) =' % (pI, qI), '    joinG packBase (%s) := by decide +kernel' % rI, '',
         '/-- The product of the packed numerators and the packed numerators turned is the packed convolution sums. -/',
         'theorem auto_prod : packL packBase coeffList * packL packBase coeffList.reverse = packL packBase autoD := by',
         '  rw [auto_P, auto_Q, auto_R]', '  exact auto_join_ok', '',
         'theorem coeffList_len : coeffList.length = 16365 := by',
         '  rw [coeffList_blocks, length_flatten_gen packBase, %s, %s]' % (ma(3), infos('autoP', 4)), '  decide +kernel', '',
         'theorem coeffList_rev_len : coeffList.reverse.length = coeffList.length := by',
         '  first', '  | exact List.length_reverse _', '  | exact List.length_reverse', '  | simp', '',
         'theorem autoD_len : autoD.length = 2 * coeffList.length := by',
         '  rw [coeffList_len]', '  unfold autoD', '  rw [length_flatten_gen packBase, %s, %s]' % (ma(8), infos('autoR', 9)), '  decide +kernel', '',
         'theorem coeffList_bd : ∀ x ∈ coeffList, -numBound ≤ x ∧ x ≤ numBound := by',
         '  rw [coeffList_blocks]', '  refine all_flatten (P := fun x => -numBound ≤ x ∧ x ≤ numBound) _ ?_',
         '  simp only [List.all_append, %s, Bool.and_self]' % bds('autoP', 4), '',
         'theorem coeffList_rev_bd : ∀ x ∈ coeffList.reverse, -numBound ≤ x ∧ x ≤ numBound := by',
         '  rw [coeffList_rev_blocks]', '  refine all_flatten (P := fun x => -numBound ≤ x ∧ x ≤ numBound) _ ?_',
         '  simp only [List.all_append, %s, Bool.and_self]' % bds('autoQ', 4), '',
         'theorem autoD_bd : ∀ x ∈ autoD, -packBase < 2 * x ∧ 2 * x < packBase := by',
         '  unfold autoD', '  refine all_flatten (P := fun x => -packBase < 2 * x ∧ 2 * x < packBase) _ ?_',
         '  simp only [List.all_append, %s, Bool.and_self]' % bds('autoR', 9), '',
         'theorem auto_bM : 2 * ((coeffList.length : ℤ) * (numBound * numBound)) < packBase := by',
         '  rw [coeffList_len]', '  decide +kernel', '',
         '/-- **L9c1**: each convolution sum of the numerators and their turn is the place of `autoD` at its index. -/',
         'theorem auto_conv : ∀ k < 2 * coeffList.length,',
         '    convR coeffList.length (fun i => coeffList.getD i 0) (fun j => coeffList.reverse.getD j 0) k = autoD.getD k 0 :=',
         '  conv_of_packedL (M := numBound) packBase_ge coeffList coeffList.reverse autoD coeffList_rev_len autoD_len coeffList_bd',
         '    coeffList_rev_bd auto_bM autoD_bd auto_prod', '']
    out['AutoConv'] = (['import SIDEExplicitFormula.Window.AutoP', 'import SIDEExplicitFormula.Window.AutoQ',
                        'import SIDEExplicitFormula.Window.AutoR0', 'import SIDEExplicitFormula.Window.AutoR1', ''] +
                       head('# L9c1: the autocorrelation of the window`s numerators, by one product of packed integers') + _ns(C))
    return dict((k, NL.join(v)) for k, v in out.items())


def cmd_full(mode='dry'):
    lists, rep = read_coeffs()
    print('  Coeffs.lean: blob %s, at the base %s, at HEAD %s -> EQUAL %s ; lists %d ; numerators %d ; each within the round bound %s' % (
        rep['blob'][:12], rep['at_base'][:12], rep['at_head'][:12], rep['equal'], rep['chunks'], rep['total'], rep['within_bound']))
    if not (rep['equal'] and rep['chunks'] == 64 and rep['names_in_order'] and rep['joined_in_order'] and rep['total'] == N_ALL
            and rep['within_bound']):
        sys.exit('### NOT WRITTEN: Coeffs.lean is not read as the base holds it')
    t0 = time.time()
    fd, chk = full_data(lists)
    print('  the checks before the write (%.1f s): %s' % (time.time() - t0, ' ; '.join('%s %s' % kv for kv in chk.items())))
    texts = full_texts(fd, rep)
    ok = all(chk.values())
    for k in ('AutoData0', 'AutoData1', 'AutoP', 'AutoQ', 'AutoR0', 'AutoR1', 'AutoConv'):
        tc = text_checks(texts[k])
        good = not tc['decimal'] and not tc['barred'] and tc['import_first'] and tc['longest_list'] <= CHUNK
        ok = ok and good
        print('  %s.lean: lines %d, bytes %d, sha256 %s ; decimal literals %d ; barred words %d ; imports first %s ; the longest list %d -> %s' % (
            k, tc['lines'], tc['bytes'], tc['sha256'], tc['decimal'], tc['barred'], tc['import_first'], tc['longest_list'], 'OK' if good else 'REFUSED'))
        dl = [x for x in decl_lines(texts[k]) if not re.match(r'auto(C\d\d|T00|Head|Zero|[PQR]v\d{3}|Rv\d{3}):', x)]
        print('    declarations (name:line), the data and the values left out: %s' % ', '.join(dl))
    if not ok:
        sys.exit('### NOT WRITTEN: a check failed')
    if mode != 'write':
        print('### DRY: nothing written')
        return
    for k, t in sorted(texts.items()):
        out = os.path.join(KPATH, FULL_DIR + k + '.lean')
        with io.open(out, 'w', encoding='utf-8', newline='\n') as f:
            f.write(t)
        back = open(out, 'rb').read()
        print('### WRITTEN %s%s.lean: %d bytes, sha256 %s, read back EQUAL %s' % (FULL_DIR, k, len(back), hashlib.sha256(back).hexdigest()[:16],
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
    dg = [5, -7, 0, 2 ** 131, -(2 ** 132), 1]
    rt = bits_digits(bits_pack(dg), len(dg))
    c('the balanced packing and its digits by binary text, on planted digits at both ends of the range: the digits read back', rt == dg, rt == dg)
    c('A PLANTED FAULT: a value past the places asked, no digits read', bits_digits(bits_pack(dg) << NB, len(dg)),
      bits_digits(bits_pack(dg) << NB, len(dg)) is None)
    ch = [[3, -1, 4], [1], [-5, 9, 2, 6]]
    c('the join of chunks of uneven lengths: the packed value of the flattened list', join_g([(pack(BASE, x), len(x)) for x in ch]) == pack(BASE, [v for x in ch for v in x]),
      join_g([(pack(BASE, x), len(x)) for x in ch]) == pack(BASE, [v for x in ch for v in x]))
    fd, fchk = full_data(lists)
    texts = full_texts(fd, rep)
    tcs = [text_checks(texts[k]) for k in sorted(texts)]
    c('the full data`s checks and its seven texts (each identity ; no decimal literal, no barred word, imports first, lists of 256 at most)',
      (all(fchk.values()), len(texts), sum(t['decimal'] + t['barred'] for t in tcs), all(t['import_first'] for t in tcs), max(t['longest_list'] for t in tcs)),
      all(fchk.values()) and len(texts) == 7 and not sum(t['decimal'] + t['barred'] for t in tcs) and all(t['import_first'] for t in tcs)
      and max(t['longest_list'] for t in tcs) <= CHUNK)
    di2 = list(fd['di'])
    di2[70] = (di2[70][0] + 1, di2[70][1])
    c('A PLANTED FAULT: one chunk value of the convolution sums moved by 1, the joined product check reads it',
      join_g(fd['pi']) * join_g(fd['qi']) == join_g(di2), join_g(fd['pi']) * join_g(fd['qi']) != join_g(di2))
    print('### THE TOOL`S CONTROLS: %d OF %d AS WANTED' % (sum(res), len(res)))


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['trial']:
        cmd_trial(*(a[1:2] or ['dry']))
    elif a[:1] == ['full']:
        cmd_full(*(a[1:2] or ['dry']))
    elif a[:1] == ['control']:
        cmd_control()
    else:
        sys.exit(__doc__)
