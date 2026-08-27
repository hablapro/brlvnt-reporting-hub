#!/usr/bin/env python3
"""GGMI scenario recompute + self-check, RECONCILED to the live draft's spend
decisions (main-session rewrite, Bing funded to $30k both scenarios, Azerion halved
in Controlled) but re-baselined to the PLANNED SEPTEMBER $205,000 plan per mission
cc0a693f. Run: python3 verify_scenarios.py (asserts every headline; non-zero on drift).
Measured figures carried verbatim from figures.json (2026-08-27f, Azerion resolved);
only new content is the Sep-plan denominator arithmetic.
"""
# Approved plan (client tracker 08/06/2026)
aug_plan = {"Bing":30000,"Quantcast":35000,"Azerion":35000,"Native":25000,"DOOH":7000,"Meta":0}
sep_plan = {"Bing":30000,"Quantcast":35000,"Azerion":35000,"Native":25000,
            "Meta":30000,"TikTok":10000,"DOOH":0,"Partnerships":40000}
# August actual client-facing tracking (figures.json 2026-08-27f)
aug_track = {"Bing":18533,"Quantcast":31387,"Azerion":42956,"Native":28682}
# Scenario proposed spend, per line — matches live draft §4
controlled = {"Bing":30000,"Quantcast":10968,"Azerion":21478,"Native":0,"Meta":0,"TikTok":0,"Partnerships":0}
deep       = {"Bing":30000,"Quantcast":0,"Azerion":0,"Native":0,"Meta":0,"TikTok":0,"Partnerships":0}

aug_working=sum(aug_plan.values()); aug_active=aug_working-aug_plan["DOOH"]-aug_plan["Meta"]
aug_track_total=sum(aug_track.values()); sep_total=sum(sep_plan.values())
c=sum(controlled.values()); d=sum(deep.values())
def pct(p,w): return round(100*p/w,1)

assert aug_working==132000 and aug_active==125000
assert aug_track_total==121558 and sep_total==205000
assert pct(aug_track_total,aug_active)==97.2
assert c==62446 and d==30000, (c,d)
assert controlled["Azerion"]==round(aug_track["Azerion"]/2)  # halved current weight
assert c-d==32446                                            # Azerion 21478 + Quantcast 10968
ramp=sep_total-aug_working; new_lines=sep_plan["Meta"]+sep_plan["TikTok"]+sep_plan["Partnerships"]
assert ramp==73000 and new_lines==80000 and pct(sep_total,aug_working)==155.3

print("AUGUST (transition month) client-facing vs approved:")
for k in ["Bing","Quantcast","Azerion","Native"]:
    print(f"  {k:11} approved {aug_plan[k]:>6} track {aug_track[k]:>6} pace {pct(aug_track[k],aug_plan[k]):>5}%")
print(f"  ACTIVE      approved {aug_active} track {aug_track_total} pace {pct(aug_track_total,aug_active)}%  (working media {pct(aug_track_total,aug_working)}%)")
print("\nSEPTEMBER scenarios vs PLANNED $205,000 (spend = live draft §4):")
print(f"  {'Line':13}{'Plan Sep':>10}{'Controlled':>12}{'Deep':>8}")
for k in ["Bing","Quantcast","Azerion","Native","Meta","TikTok","Partnerships"]:
    print(f"  {k:13}{sep_plan.get(k,0):>10}{controlled[k]:>12}{deep[k]:>8}")
print(f"  {'DOOH':13}{0:>10}{0:>12}{0:>8}")
print(f"  {'TOTAL':13}{sep_total:>10}{c:>12}{d:>8}")
print(f"\n  Controlled ${c:,}/mo -> vs planned Sep: -${sep_total-c:,} ({pct(sep_total-c,sep_total)}%) | vs Aug in-market: -${aug_track_total-c:,} ({pct(aug_track_total-c,aug_track_total)}%)")
print(f"  Deep       ${d:,}/mo -> vs planned Sep: -${sep_total-d:,} ({pct(sep_total-d,sep_total)}%) | vs Aug in-market: -${aug_track_total-d:,} ({pct(aug_track_total-d,aug_track_total)}%)")
print(f"  Scenario difference ${c-d:,}/mo (Azerion halved 21478 + Quantcast 10968)")
print(f"  Held ramp: Sep +${ramp:,} over Aug working media = ${new_lines:,} of new/returning lines held at $0 in both scenarios")
print("\nALL ASSERTS PASSED")
