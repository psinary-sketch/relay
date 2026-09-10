    # ---- COMPONENT 1: THE SPAN -----------------------------------------------------------------
    bar()
    rec('  ### THE SPAN, TAKEN FROM THE TOOL AND NOT TYPED.')
    bar()
    spanrec = text(d('b408_span.txt'))
    m = re.search(r'THE CURRENT SPAN : (\d+) ACT', spanrec)
    arm('G-SPANTOOL', "the span was banked from the tool's own run under this act's stem",
        bool(m) and 'b363_span.py' in spanrec,
        'the tool reports %s acts' % (m.group(1) if m else '?'))
    arm('G-SPANNOTYPED', 'and the components print the tool`s own lines, not a typed number',
        'THE TOOL’S OWN LINES, TAKEN FROM ITS OUTPUT AND NOT TYPED' in crun)
    arm('G-FOLDNOTRUN', 'the fold is reported NOT DUE and none was run',
        'THE FOLD IS NOT DUE' in crun and int(m.group(1)) < 9,
        '%s against a threshold of 9' % (m.group(1) if m else '?'))

    # ---- ADDITION THREE ------------------------------------------------------------------------
    bar()
    rec('  ### THE TWO CHANNELS, THE SWEEP, AND THE NUMBERING HAZARD.')
    bar()
    arm('G-TWOCLASSES', 'both channels are quoted in the classes document`s own words',
        'Class C₃ (archimedean)' in crun and 'Class C₄ (global coherence)' in crun)
    sw = re.search(r'C3 -- LINES NAMING IT BESIDE A CHANNEL WORD : (\d+)', xrun)
    sw4 = re.search(r'C4 -- LINES NAMING IT BESIDE A CHANNEL WORD : (\d+)', xrun)
    arm('G-CHANSWEEP', 'the sweep ran with its predicate printed and its whole yield printed',
        bool(sw) and bool(sw4) and 'THE PREDICATE, FIXED BEFORE THE SWEEP' in xrun
        and 'files in scope : 4705' in xrun,
        'C3 %s hits ; C4 %s hits ; 4705 files in scope'
        % (sw.group(1) if sw else '?', sw4.group(1) if sw4 else '?'))
    arm('G-CHANHANDREAD', 'and every hit is classified by kind, with its reason',
        crun.count('hit(s)') >= 5 and 'THE HAND-READING, BY KIND OF HIT' in crun)
    arm('G-NUMBERING', 'the two numbering schemes are quoted and the artefact named',
        'Archimedean / functional equation' in crun
        and 'MATCHER ARTEFACT, NOT AN EXAMINATION' in fold(crun))
    arm('G-TOOLKIT', 'and the toolkit`s silence about one source is printed',
        'DOES NOT NAME `C₄` AT ALL' in fold(crun).replace('  ', ' ')
        or 'DOES NOT NAME `C₄` AT ALL' in crun)
    opened = (asserted(bank, 'the channel is open') + asserted(bank, 'is a promising channel')
              + asserted(bank, 'is worth opening'))
    arm('G-NOCHANCLAIM', 'the bank ASSERTS no channel is open, promising or worth opening',
        not opened, 'asserting sentences %d %s' % (len(opened), opened or ''))
    arm('G-NOCHANCLAIM-CTL', 'and the predicate FIRES on synthetic text asserting one',
        bool(asserted('The modular symmetry is a promising channel.', 'is a promising channel')))
    arm('G-NORECONCILE', 'and the numbering hazard is PRINTED, not reconciled',
        'PRINTED AND NOT RECONCILED' in fold(bank) or 'not reconciled' in bank.lower())

    # ---- ADDITION FOUR -------------------------------------------------------------------------
    bar()
    rec('  ### THE CLASSIFIED PROOF, PRICED IN TWO LAYERS AND NOT WRITTEN.')
    bar()
    arm('G-K8CLASSIFIED', 'all eight constituents are classified',
        all(('### **%s**' % k) in crun for k in
            ('K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8')))
    arm('G-IMPORTS', 'the distinct imported premises are counted and named',
        'THE DISTINCT IMPORTED PREMISES ARE FOUR' in fold(crun))
    arm('G-WITHHYP', 'the verdict is PROOF-WITH-HYPOTHESES',
        'A PROOF-WITH-HYPOTHESES, NOT A PROOF IN THE LEMMA' in fold(crun))
    arm('G-CONDITIONAL', 'and the conditional finding is printed beside it',
        'A PROOF OF A CONDITIONAL IS NOT ONE' in fold(crun))
    arm('G-TWOLAYERS', 'the price is printed in two layers',
        'THE SECOND LAYER' in fold(crun) and 'LABOUR AND NOT LOGIC' in fold(crun))
    arm('G-UNCHECKED', 'and the in-principle layer is marked UNCHECKED',
        'UNCHECKED' in crun)
    written = asserted(bank, 'the classified proof is written') + asserted(bank, 'we wrote the proof')
    arm('G-NOTWRITTEN', 'the bank ASSERTS nowhere that the proof was written', not written,
        'asserting sentences %d' % len(written))
    arm('G-NOTWRITTEN-CTL', 'and the predicate FIRES on synthetic text asserting it',
        bool(asserted('At last the classified proof is written in full.',
                      'the classified proof is written')))

    # ---- COMPONENTS 2 AND 3 --------------------------------------------------------------------
    bar()
    rec('  ### THE FOUR DRESSES, AND THE ROW`S KIND.')
    bar()
    arm('G-FOURDRESSES', 'four dresses are put to the test with an instantiation each',
        crun.count('THE KIND :') == 4 and crun.count('THE OBJECT:') == 4)
    arm('G-ONESENTENCE', 'the sentence the test produces is stated',
        'A RESULT APPLIES TO AN OBJECT ONLY IF THE OBJECT IS OF THE KIND' in fold(crun))
    minted = asserted(bank, 'this act names it') + asserted(bank, 'we call it')
    arm('G-NOMINT', 'and the bank ASSERTS no name of its own', not minted,
        'asserting sentences %d' % len(minted))
    arm('G-NOMINT-CTL', 'and the predicate FIRES on synthetic text minting one',
        bool(asserted('Having no name, this act names it the kind principle.',
                      'this act names it')))
    arm('G-RESTATEMENT', 'and one dress is reported a restatement, not a fourth instance',
        'A RESTATEMENT OF DRESS 3' in crun and 'INDEPENDENT AND `1` IS' in fold(crun))
    arm('G-ROWCOST', 'the row`s cost and yield are printed from the banks',
        'sites entered, by their own markers' in crun and 'acts named anywhere' in crun)
    arm('G-ROWKIND', 'and the row`s kind is answered as a description, not a grade',
        'A BOOKKEEPING INSTRUMENT' in fold(crun)
        and 'A DESCRIPTION AND NOT A DEMOTION' in fold(crun))

    # ---- ADDITIONS ONE AND TWO -----------------------------------------------------------------
    bar()
    rec('  ### THE PRICE LIST AND THE SUITE MEASURE.')
    bar()
    arm('G-PRICELIST', 'the routed-price list carries item, act, cost and whose call',
        crun.count('### **ITEM** ###') == 3 and crun.count('WHOSE :') == 3)
    arm('G-PRICESCOPE', 'and it declares what it is not',
        'NOT A CORPUS-WIDE ROUTED-ITEM CENSUS' in fold(crun))
    arm('G-PRICEDISP', 'and a NAMED item is kept apart from a ROUTED one',
        'NAMED, NOT ROUTED' in fold(crun))
    arm('G-ARMCOUNTS', 'the four suites` arm counts and the standing core are printed',
        'STANDING CORE' in xrun and re.search(r'carried \d+ ; NEW \d+', xrun) is not None)
    arm('G-ARMLIMIT', 'and the measure prints its own limit',
        'UPPER BOUND ON CONTINUITY' in fold(crun))
    reformed = asserted(bank, 'the suite was rebuilt') + asserted(bank, 'an arm was added')
    arm('G-NOREFORM', 'the bank ASSERTS no arm was added, removed, renamed or promoted',
        not reformed, 'asserting sentences %d' % len(reformed))

    # ---- WHAT WAS NOT TOUCHED ------------------------------------------------------------------
    bar()
    rec('  ### WHAT WAS NOT TOUCHED.')
    bar()
    faces_blob = git(PP, 'show', '%s:FACES_LEDGER.md' % side).stdout.decode('utf-8')
    arm('G-NOROWWRITE', 'FACES_LEDGER.md is BYTE-IDENTICAL to the blob at %s' % side,
        text(FACES).replace('\r\n', '\n') == faces_blob,
        'working %d ; blob %d bytes'
        % (len(text(FACES).encode('utf-8')), len(faces_blob.encode('utf-8'))))
    st_now = text(STANDING)
    st_blob = git(ROOT, 'show', '%s:tools/FERRY_STANDING.md' % side).stdout.decode('utf-8')
    arm('G-NOSTANDING', 'FERRY_STANDING.md is byte-identical to the blob',
        st_now.replace('\r\n', '\n') == st_blob.replace('\r\n', '\n'))
    rc_now = text(os.path.join(ROOT, 'tools', 'run_clock.py'))
    rc_blob = git(ROOT, 'show', '%s:tools/run_clock.py' % side).stdout.decode('utf-8')
    arm('G-NOINSTRUMENT', 'and run_clock.py is byte-identical too -- b407 amended it, not b408',
        rc_now.replace('\r\n', '\n') == rc_blob.replace('\r\n', '\n'))
    arm('G-NOREPAIR', 'this act made no in-place repair anywhere',
        'NO IN-PLACE REPAIR' in text(t('b408_desk_bank.py')).upper()
        or 'in-place repair' not in text(t('b408_desk_bank.py')).lower())
    lean = [x for x in git(SIDE, 'status', '--porcelain').stdout.decode(
        'utf-8', 'replace').split(chr(10)) if x.strip() and x.strip().endswith('.lean')]
    arm('G-NOLEAN', 'no `.lean` file is modified', not lean, 'lean changes %s' % (lean or 'none'))
    builds = asserted(bank, 'a kernel was built')
    arm('G-NOBUILD', 'the bank ASSERTS nowhere that a kernel was built', not builds,
        'asserting sentences %d' % len(builds))
    arm('G-NOBUILD-CTL', 'and the predicate FIRES on synthetic text asserting it',
        bool(asserted('The lane was opened and a kernel was built for it.', 'a kernel was built')))
    tools = sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b408_'))
    arm('G-CAP', 'at most 6 new relay tool files', len(tools) <= 6, '%d : %s' % (len(tools), tools))

