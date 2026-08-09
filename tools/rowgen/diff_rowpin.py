"""The pin-correct differ — resolves each terminal against ITS OWN repo's pin.

THREE ITERATIONS, AND THE FIRST TWO WERE WRONG IN THE SAME WAY.

  (1) sitting 1: an `os.walk` resolver read checked-out working trees, and declared three real
      terminals missing because they live on a branch.
  (2) sitting 2: the config stamped every terminal with its kernel's current HEAD, producing sixty
      "stale pin" flags that were artifacts of the config.
  (3) sitting 3, first cut: pins were taken from the row but paired with whatever repo the terminal
      mapped to — so a row citing SIDE-kernel `691295b` alongside terminals in SIDE-archimedean,
      SIDE-frobenius, SIDE-rcurve and SIDE-spinor produced ten false STALE-PINs. The declarations
      are all present at their own repos' pins.

All three are the IMPOSED-PRESENT / MISPAIRED-PIN class: **the tool asked a different question from
the one the row answers.**

HOW THE CORPUS ACTUALLY RECORDS PINS, which is what a correct differ must follow: a Correspondence
row names its terminal and often a pin, but the authoritative per-repo pins live in a per-paper
AUDIT FOOTER — e.g. *"Kernels audited at: SIDE-kernel `ce5d7bd` …; SIDE-archimedean `8019d9d`,
SIDE-frobenius `2efe9f2`, SIDE-rcurve `d5f33b4`, SIDE-spinor `b235bc6` (all v0.1.0)."*

So resolution is: **the terminal's own repo → that repo's pin from the footer → `git show`**, with
in-row pins and the branch/HEAD as ordered fallbacks. A STALE-PIN survives only if the declaration
is absent at EVERY pin the paper offers for that terminal's repo.
"""
import io, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rowgen

HEX = re.compile(r"`([0-9a-f]{7,40})`")
NAME = re.compile(r"`([A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z0-9_']+)+)`")
REPO_PIN = re.compile(r"(SIDE-[a-z0-9-]+)[^`]{0,40}`([0-9a-f]{7,40})`")


def footer_pins(md):
    """repo -> [pins], from every 'SIDE-xxx `pin`' pairing anywhere in the paper."""
    out = {}
    for repo, pin in REPO_PIN.findall(md):
        out.setdefault(repo, [])
        if pin not in out[repo]:
            out[repo].append(pin)
    return out


def decl_at(repo_dir, pin, path, last):
    src = rowgen.git_show(repo_dir, pin, path)
    if not src:
        return False
    for ln in src.splitlines():
        s = ln.strip()
        for k in ("theorem", "lemma", "def", "abbrev", "structure", "instance",
                  "noncomputable def"):
            head = k + " " + last
            if s.startswith(head):
                tail = s[len(head):len(head) + 1]
                if tail == "" or not (tail.isalnum() or tail == "_"):
                    return True
    return False


def main(map_path, papers):
    m = json.load(io.open(map_path, encoding="utf-8"))
    G = {"checked": 0, "ok": 0, "stale": 0, "unmapped": 0}
    for p in papers:
        md = io.open(p, encoding="utf-8").read()
        fp = footer_pins(md)
        base = os.path.basename(p)
        rows = [ln for ln in md.split("\n") if ln.strip().startswith("|") and "`" in ln]
        checked = ok = 0
        stale, unmapped = [], []
        seen = set()
        for ln in rows:
            inrow = HEX.findall(ln)
            for n in NAME.findall(ln):
                if n.split(".")[-1] in ("md", "lean", "py") or (n, base) in seen:
                    continue
                seen.add((n, base))
                hits = m.get(n)
                if not hits:
                    unmapped.append(n)
                    continue
                repo, path = hits[0][0], hits[0][1]
                repo_dir = "D:" + os.sep + repo
                last = n.split(".")[-1]
                pins = list(fp.get(repo, [])) + [q for q in inrow if q not in fp.get(repo, [])]
                pins += ["HEAD"]
                checked += 1
                if any(decl_at(repo_dir, q, path, last) for q in pins):
                    ok += 1
                else:
                    stale.append((n, repo, path, pins[:4]))
        print("=== %-40s checked %3d | present-at-a-paper-pin %3d | STALE %d | unmapped %d ==="
              % (base, checked, ok, len(stale), len(unmapped)))
        for n, repo, path, pins in stale:
            print("   STALE  %-46s %s :: %s   tried %s" % (n, repo, path, ",".join(pins)))
        G["checked"] += checked; G["ok"] += ok
        G["stale"] += len(stale); G["unmapped"] += len(unmapped)
    print()
    print("TOTALS  checked %d | present %d | STALE %d | unmapped %d"
          % (G["checked"], G["ok"], G["stale"], G["unmapped"]))
    print("STALE now means: absent at EVERY pin the paper offers for that terminal's own repo.")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
