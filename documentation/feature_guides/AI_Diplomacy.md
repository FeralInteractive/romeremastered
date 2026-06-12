# How the AI Conducts Diplomacy

This guide explains, in plain terms, how an AI faction decides what diplomatic deals to seek, how it puts a price on what's on the table, and why it accepts, refuses or haggles over an offer. The aim is to help modders understand *why* the AI behaves the way it does at the diplomacy table, and which data files to reach for when you want to change that behaviour.

---

## 1. The AI's "diplomatic department"

It helps to picture each AI faction as running a small diplomatic department with four distinct jobs. They work together every turn:

| Role | What it does |
|---|---|
| **Director / Manager** | Sets the faction's diplomatic **goals** for the turn — who it wants to ally with, who it wants to threaten, who it wants help against. These goals are called **missions**. |
| **Analyser** | Puts a **cash value** (in denarii) on every individual item in a proposed deal, from this faction's point of view. |
| **Negotiator** | Takes an incoming offer, weighs it up using the analyser's values, and decides whether to **accept, decline, or counter** — and builds the faction's own outgoing offers. |
| **Diplomat controller** | Handles the physical side: sending an actual diplomat character across the map to make contact with the target faction. |

The key thing to take away is that diplomacy is **goal-driven and value-driven**. The AI isn't reacting at random — it has a list of things it wants, and it runs the numbers on every deal. If you understand what feeds those goals and those numbers, you understand the behaviour.

---

## 2. Missions: what the AI is trying to achieve

Each turn the AI assigns itself **diplomatic missions** aimed at specific factions. Each mission has a **priority**, and missions that contradict each other are resolved so the faction isn't pulling in two directions at once. The main mission types are:

- **Trade** — establish trade rights.
- **Alliance** — form an alliance.
- **Neutral** — de-escalate to a neutral footing.
- **War** — move toward (or commit to) war.
- **Attack** — get another faction to **join** an attack on a shared target.
- **Access** — obtain military access (often to reach a target).
- **Protectorate** — make another faction a client kingdom.
- **Threat** — extort money under threat of attack.
- **Bribe** — bribe a settlement or character.

ROME REMASTERED adds several **survival- and relationship-driven** missions, such as seeking protection when facing eradication, asking a stronger faction to redirect its aggression elsewhere, leaning on a trusted protector, reacting to being encircled, and (for protectorates) seeking funding or a path back to independence.

### Hidden missions
Some missions are flagged **hidden**. The AI will **not** actively chase a hidden mission, but it **will accept** a deal that satisfies one if another faction happens to offer it. This is how the AI can be "open to" something — say, a ceasefire — without spending diplomats actively pursuing it. It's worth knowing this exists, because it's why an AI sometimes accepts an offer it never seemed to be working toward.

---

## 3. Putting a price on a deal

Every diplomatic offer is broken down into individual **items**, and the analyser values each one in **denarii, from the receiving faction's perspective**. A positive value means the item is worth something **to the faction being offered it**; a negative value means it only really benefits the *proposer*.

Items that get valued include:

- Alliance / nullifying an alliance
- Ceasefire
- Trade rights / cancelling trade rights
- Military access / cancelling military access
- Map information
- Ceding a region
- A yearly payment (tribute) for a number of turns, or a one-off sum
- Agreeing to attack a particular faction
- Becoming, or taking on, a protectorate
- A threat of attack
- Settling debts / compensation

The negotiator adds up the values on both sides of the proposed deal and works out the **balance**. Broadly: if the deal comes out in the AI's favour (once trust, the diplomat's skill, and a little randomness are taken into account), it leans toward **accepting**; if it's lopsided against the AI, it **declines or counters** to claw back the difference.

> **Designer's takeaway:** the AI is essentially a shrewd merchant. To make it say yes, the *numbers* have to work for it. The two biggest things that move those numbers are **trust** and **reputation** — covered next.

---

## 4. Trust and reputation — the master levers

This is the single most important section for anyone trying to influence AI diplomacy.

Before the AI values a deal, it works out how much it **trusts** the faction it's dealing with. Trust comes from **aggression** — a running measure of how much the other faction has wronged this one — combined with that faction's **global reputation** (its standing with the world at large). Crucially, **global reputation is weighted more heavily than the one-to-one history**: a faction with a terrible worldwide reputation gets treated with suspicion by *everyone*, even factions it has never personally crossed.

That trust level becomes a **modifier applied to the value of nearly every item in a deal**, swinging it by a substantial margin in either direction — penalising offers from distrusted factions and sweetening offers from trusted ones. Below a certain trust threshold the AI simply regards the proposer as **dishonest**, and that triggers a set of defensive behaviours:

- **It won't accept tribute paid over several years** from a faction it doesn't trust — only a lump sum it can bank immediately. A distrusted faction's promise of "100 per turn for ten turns" is treated as worthless, because the AI assumes it won't be paid.
- **It's reluctant to grant or accept military access**, because access can be revoked or abused.
- **It demands more** to compensate for the risk — the price it asks for the same item goes **up** when trust is low.
- **It's wary of one-sided "gifts"**, treating an over-generous offer as a possible trap.

### Why this matters to modders
Most "the AI is being unreasonable" reports trace back to trust and reputation:

- A faction that **refuses every offer** usually has very low trust toward the proposer — often because the proposer's **global reputation** is in the gutter, not because of anything between those two specific factions.
- A faction that **demands enormous sums** for a simple ceasefire is reacting to low trust inflating its asking price.
- A faction that **won't take yearly tribute** isn't bugged — it doesn't trust the payer to keep paying.

You influence all of this primarily through reputation and starting relations, not by trying to script individual deals. See [`feral_descr_reputations_and_relations.txt`](/documentation/data_file_guides/feral_descr_reputations_and_relations.md), which lets you tune exactly how much each in-game action (honouring alliances, breaking treaties, bribing rebels, and so on) moves reputation up or down. That file is the intended tool for keeping factions' reputations from drifting permanently too high or too low.

---

## 5. Diplomatic stance

The relationship between any two factions sits at one of a series of **stances**, running from friendliest to most hostile:

**Allied → Suspicious → Neutral → Hostile → At War**

These are points on a scale rather than just labels, and the AI sends **warning signals** as a relationship slides into the suspicious or hostile range — its way of telling a player (or another faction) that patience is running out before it tips into war. The current stance feeds directly into how deals are valued: an ally and an enemy will price the very same offer quite differently.

---

## 6. Haggling: how counter-offers play out

When the AI doesn't outright accept or decline, it **counters**. A few things shape how that back-and-forth goes:

- **Patience is limited.** Each pairing of factions gets a limited number of counter-offers/rejections before the AI loses patience for that turn. Push past it and the deal is rejected outright — internally flagged as something like *"too many counters"* or *"unsure of intentions."* This is deliberate: it stops endless haggling and models a faction getting fed up.
- **There's deliberate randomness.** A small random bias is added to each evaluation, and the AI's patience limit itself varies. This is **by design** — it stops diplomacy being perfectly predictable, so the same offer won't always produce an identical response. If you're testing changes, expect some run-to-run variation and test more than once.
- **The diplomat matters.** A more capable diplomat character improves the terms the AI is willing to offer, which is why sending a skilled diplomat genuinely helps.

---

## 7. Personality shapes everything upstream

Which missions a faction pursues — how expansionist, how aggressive, how alliance-minded it is — is driven by its **AI personality**. This is the upstream dial that decides whether a faction is forever scheming for war or generally content to trade and ally. If you want a faction to *behave* differently at the diplomacy table as a baseline, its personality is usually the right place to start, ahead of fine-tuning individual values.

See [`feral_descr_ai_personality.txt`](/documentation/data_file_guides/feral_descr_ai_personality.md) for the full set of personality controls.

---

## 8. Protectorates and breaking away

Protectorates (client kingdoms) have some specific behaviour worth calling out, because it surprises people:

- A protectorate that grows **strong relative to its protector** may push for **independence** — and the protector AI may decide it's worth **risking war** to keep it in line, rather than letting it walk away, when the protectorate isn't strong enough to make that costly.
- The AI weighs a protectorate offer in the context of its **other alliances**: it will be reluctant to take on (or stay loyal to) a protectorate that is the enemy of a faction it already trusts, because that would just force a betrayal later.

These behaviours are balanced around relative **military strength** and existing relationships, so they shift naturally as a campaign develops.

---

## 9. Modder's checklist for diplomacy

When the AI's diplomacy isn't behaving the way you intended, work down this list:

- [ ] **Check global reputation first.** A faction refusing all deals is usually distrusted because of poor worldwide standing, not a specific feud. Tune this via [`feral_descr_reputations_and_relations.txt`](/documentation/data_file_guides/feral_descr_reputations_and_relations.md).
- [ ] **Check starting relations and stance.** Two factions that start as enemies will price everything through that lens. Set the intended opening relationships in your campaign's setup data.
- [ ] **Check the AI personality** of a faction that is too passive or too warlike — see [`feral_descr_ai_personality.txt`](/documentation/data_file_guides/feral_descr_ai_personality.md).
- [ ] **Remember trust gates.** If the AI won't accept tribute-over-time or military access, that's low trust by design — raise trust/reputation rather than expecting it to agree.
- [ ] **Expect demanded prices to rise when trust is low.** A "too expensive" ceasefire is usually a trust symptom.
- [ ] **Test more than once.** Built-in randomness means a single test isn't conclusive; repeat before deciding a change didn't work.
- [ ] **Use a skilled diplomat** when judging the *best* terms the AI will offer — a poor diplomat understates what's achievable.

---

## 10. Quick diagnosis table

| Symptom | Most likely cause | Where to look |
|---|---|---|
| AI refuses every offer from a particular faction | That faction's **global reputation** / trust is very low | [§4](#4-trust-and-reputation--the-master-levers), reputations file |
| AI demands a huge sum for a minor concession | Low trust inflating its asking price | [§4](#4-trust-and-reputation--the-master-levers) |
| AI won't accept payment spread over several turns | It doesn't trust the payer to keep paying | [§4](#4-trust-and-reputation--the-master-levers) |
| AI won't grant or accept military access | Trust gate — access seen as exploitable | [§4](#4-trust-and-reputation--the-master-levers) |
| AI is far too warlike / far too passive | AI personality settings | [§7](#7-personality-shapes-everything-upstream), personality file |
| Two factions that should be friendly start hostile | Starting relations / stance in campaign setup | [§5](#5-diplomatic-stance) |
| A protectorate keeps trying to break away | It has grown strong relative to its protector | [§8](#8-protectorates-and-breaking-away) |
| Same offer gives different answers on repeat tests | Deliberate randomness in evaluation and patience | [§6](#6-haggling-how-counter-offers-play-out) |
| AI accepts something it never seemed to pursue | A **hidden mission** it was willing to accept but not chase | [§2](#2-missions-what-the-ai-is-trying-to-achieve) |

---

## Related data-file guides

- [`feral_descr_reputations_and_relations.txt`](/documentation/data_file_guides/feral_descr_reputations_and_relations.md) — tune how actions change reputation and relations. **The primary tool for shaping AI diplomacy.**
- [`feral_descr_ai_personality.txt`](/documentation/data_file_guides/feral_descr_ai_personality.md) — set how aggressive, expansionist or alliance-minded each faction is.

---