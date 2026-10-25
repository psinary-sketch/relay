# -*- coding: utf-8 -*-
"""b710_order.py -- THE AUTHOR'S ORDER AT THE ROOT'S PROMPT, LANDED (b710, after the seal, before the root).

### The author's word of 2026-10-24 at the root's prompt ("Root: 1, proceed, as the ferry orders ... Entered for b711 ...
### W-ORD-READING5-INDEPENDENCE, a supplement to data/b710_reading5.txt section (i) at b711's step zero"), checked before it was acted on
### (data/b710_citation_check.txt, the mid-act checks of 23:57Z, VACUOUS by the reader's span, and the terminals' files listed, defect (h)).
### The order is landed by the record tool's own landing function, b698's land through tools/b710_record.py (sealed, imported unedited,
### its screens run), appended to PLACE-papers OPEN_TRAILS beneath W-ORD-MOVES-BY-LOCUS; its landing bank data/b710_order_lines.json.
### This tool is not sealed (written after the seal at the author's word); it writes no other file. Written by the Write tool.
### `python -X utf8 tools/b710_order.py [dry]`.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b710_record as REC   # noqa: E402  ### the sealed record tool, imported unedited
import b710_worklist as K   # noqa: E402

NL = chr(10)
ORDER_REC = ('*Appended 2026-10-24 by b710 beneath W-ORD-MOVES-BY-LOCUS (:15804), under `(R320)` and the author’s word of 2026-10-24 at the '
             'root’s prompt -- THE ORDER **`W-ORD-READING5-INDEPENDENCE`**, FOR b711’S STEP ZERO:* a supplement to relay data/b710_reading5.txt '
             'section (i) (:34-:52, the principle I read as compiled by definitions alone), in the author’s words “‘Independent’ characteristics '
             'have been theorem proven and machine verified within the program … more than we’ve reminded ourselves”. Each named terminal is read '
             'at its kernel and tag through the Read tool, its statement printed, its grade taken from the statement (and from EXCLUSION_ENGINE’s '
             'table where it grades it), and the principle’s row restated from those reads: SIDEBijection.identity_formation_bijection with its '
             'Independence lemma (SIDE-bijection); T3.T3prime_shared_witness and T3.T3doubleprime_general_commutation_fails (SIDE-lv-conservation); '
             'productLemma_holds (v0.18), family_theorem (v0.21), h2_sign_cfg_iff_target (v0.15) and h2_sign_sum_iff_rh (v0.36) '
             '(SIDE-explicit-formula); lam_add (SIDE-li-map); kappa_zero_of_no_mechanism, parametric_mechanism_theorem and interface_split '
             '(SIDE-interfaces); silence_universal (SIDE-kernel Kernel/SilenceTheorem.lean :74); offLine_of_codim_two (SIDE-kernel Voice3b) and the '
             'codimension terminals of SIDE-simplicity. The search that read Independence as definitions alone (relay data/b710_r5_search.txt '
             ':70-:131 and :586-:598) is printed beside the supplement, so the miss is located by its query. b710’s sealed banks and its landed '
             'entry are not edited; the files declaring each named terminal were located at b710 by a file listing, their statements not read '
             '(relay data/b710_defects.txt (h)). Status OPEN, trigger b711.')


def main(argv):
    dry = 'dry' in argv
    REC.land([('OPEN_TRAILS.md', ORDER_REC, NL + ORDER_REC + NL)], 'b710_order_lines.json', 'order', entry=None,
             check=[('OPEN_TRAILS.md', K.ORDER_MOVES, '*Appended 2026-10-24 by b710 beneath b709'), ('FINDINGS.md', 10246, '## Reading 5: the four principles')],
             dry=dry)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
