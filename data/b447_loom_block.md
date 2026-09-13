
<!-- b447 loom entry -->

### **THE ARM THAT BITES — noted once, 2026-09-12 (b447)**

`relay/tools/noise_floor.py` gives every verdict two arms: a FLOOR arm (`|value| <= sqrt(machine epsilon) = 1.49e-08`) and a DRIFT arm (relative change under refinement against `1e-3`). Its own header, written at b272, already said which one carries the weight: *"A MAGNITUDE TEST ALONE WOULD HAVE PASSED ALL FOUR OF b264's FLOOR MODES"* and *"IT IS THE DRIFT ARM THAT BITES, NOT THE FLOOR ARM."*

b446 counted it (`relay/data/b446_floor_census.txt`). There were **553** banked comparisons against the floor, and **547** of them were of a kind other than the spectral or modal quantities it was measured on. The floor arm fired **56** times, in structured records, **every one on a value of exactly zero, which any positive floor refuses. The floor's size decided no banked verdict.**

**So the gate's verdicts are the drift arm's, and a closing that reads "resolved against the floor" names the arm that did not decide.** This note is the whole of the record's response. Nothing is re-verdicted and no closing is edited: the sites are not repairable, and no verdict among them is wrong. It is filed once, here, so that a reader knows which arm carried the weight.

*Its rule's other face is filed with the bar-floor rule (TECHNE `BAR_FLOOR_RULE.md`, local). Nothing deposits.*
