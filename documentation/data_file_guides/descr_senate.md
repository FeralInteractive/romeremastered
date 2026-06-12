![Workshop_header_template](/Workshop_header_template.png)
# descr_senate.txt

## Table Of Contents

* [Introduction](#introduction)
* [File structure at a glance](#file-structure-at-a-glance)
* [1. Attitude settings](#1-attitude-settings)
* [2. Offices](#2-offices)
* [3. Unit rewards](#3-unit-rewards)
* [4. Fines and rewards](#4-fines-and-rewards)
* [5. Missions and the penalty/reward matrix](#5-missions-and-the-penaltyreward-matrix)
* [What changed from original Rome (OG)](#what-changed-from-original-rome-og)
* [Limitations and notes](#limitations-and-notes)
* [Related guides](#related-guides)

## Introduction

`descr_senate.txt` (in your mod's `data` folder) defines everything about the senate: the **offices** it grants, the **missions** it hands out and their rewards and penalties, the **units** it can gift, and the coefficients that drive its **attitude** toward each faction.

In ROME REMASTERED this file does far more than it did in the original game. Offices are no longer a fixed set baked into the executable — they are read entirely from here — and senates are defined **per faction** rather than as a single global institution. See the [What changed from original Rome (OG)](#what-changed-from-original-rome-og) section for the full list of differences.

> This guide is the **file-format reference** for `descr_senate.txt` as a whole. For an in-depth, worked walkthrough of **adding offices and senators** specifically, see the companion feature guide: [Senate Offices: Adding and Modding Offices and Senators](/documentation/feature_guides/Senate_Offices.md).

A complete, working example ships in this repository: [`super_faction/data/descr_senate.txt`](/example_mods/super_faction/data/descr_senate.txt). The snippets below are taken from it.

## File structure at a glance

The file is read top to bottom in this order:

1. **Attitude settings** — coefficients and boundaries controlling the senate's mood toward each faction.
2. **`Begin_Offices … End_Offices`** — the offices, one block per faction.
3. **`Begin_Unit_Rewards … End_Unit_Rewards`** — the unit pools the senate can gift, one block per faction.
4. **Fines, rewards, and the missions** — the global fine/reward amounts followed by each mission's duration and its penalty/reward matrix.

---

## 1. Attitude settings

These appear at the very top of the file and tune how the senate feels about a faction and how often it acts.

```
appreciation_duration           10
displeasure_duration            10

probability_of_random_mission   15

turn_coefficient                200
strength_coefficient            25
relative_strength_coefficient   25
combined_strength_coefficient   25

attitude_boundary_1             30000
attitude_boundary_2             60000
attitude_boundary_3             90000
attitude_boundary_4             120000
attitude_boundary_5             150000
attitude_boundary_6             180000
```

| Setting | Meaning |
|---|---|
| `appreciation_duration` | How many turns the senate's **approval** lasts after a faction pleases it. (10 turns = 5 years.) |
| `displeasure_duration` | How many turns the senate's **displeasure** lasts after a faction angers it. |
| `probability_of_random_mission` | Percentage chance, per opportunity, of issuing a **random** mission when nothing else is generated. |
| `turn_coefficient` | Weights how much the **passage of time** feeds into the senate's attitude calculation. |
| `strength_coefficient` | Weights the faction's **own military strength**. |
| `relative_strength_coefficient` | Weights the faction's strength **relative to** the senate. |
| `combined_strength_coefficient` | Weights **combined** strength considerations. |
| `attitude_boundary_1` … `_6` | The thresholds that divide the attitude score into bands (from most favourable to most hostile). All six must be present and should increase in order. |

The coefficients and boundaries are deliberately abstract — they feed a scoring formula, and the stock values are the result of tuning. Change them in moderate steps and test; large changes can make the senate permanently delighted or permanently furious.

---

## 2. Offices

Offices are defined in one or more `Begin_Offices <faction> … End_Offices` blocks. The block name must match the faction the senate belongs to (e.g. `romans_senate`).

```
Begin_Offices romans_senate

Quaestor
Title           SMT_SENATE_OFFICE_QUAESTOR_TITLE
Description     SMT_SENATE_OFFICE_QUAESTOR_DESCRIPTION
Rank            10
Quantity        1
Duration        8
Sittings        1
Restrictions
End_restrictions
Senate_benefits
    quaestor_immunity
End_senate_benefits
End

… more offices …

End_Offices
```

In brief, each office block carries: a unique **internal name** (first line), a **Title** and **Description** text key, **Rank** (currently unused), **Quantity** (number of seats), **Duration** (turns served), **Sittings** (currently unused), a **Restrictions** block (entry requirements: `not_consecutively`, `<office>_tenure`, `trait_<name> <level>`), and a **Senate_benefits** block (`quaestor_immunity`, `censor_immunity`, `no_censor_suicide`).

> Offices are the most heavily reworked part of this file in Remastered and have their own dedicated guide. For the field-by-field breakdown, restriction rules, a worked "add a new office" example, where senators come from, and the save-game caveats, see **[Senate Offices: Adding and Modding Offices and Senators](/documentation/feature_guides/Senate_Offices.md)**.

---

## 3. Unit rewards

The units the senate can gift as mission rewards are listed in `Begin_Unit_Rewards <faction> … End_Unit_Rewards`, grouped into named pools:

```
Begin_Unit_Rewards romans_senate
    minor_exotic_unit
    {
        roman velite gladiator
        merc rhodian slingers
        …
    }
    major_exotic_unit
    {
        roman arcani
        …
        roman legionary first cohort i, requires_event marian_reforms
    }
    eagle_units
    {
        roman legionary first cohort i, requires_event marian_reforms
        roman legionary first cohort ii, requires_event marian_reforms
    }
    triarii
    {
        roman triarii
    }
End_Unit_Rewards
```

- Each pool (`minor_exotic_unit`, `major_exotic_unit`, `eagle_units`, `triarii`) holds a list of unit entries the senate may pick from when that class of reward is granted.
- A unit name must match a unit defined in your `export_descr_unit` data — see the [EDU guide](/documentation/data_file_guides/EDU.md).
- Append `, requires_event <event>` to gate a unit behind a campaign event (e.g. `requires_event marian_reforms`), so it can only be awarded once that event has fired.

---

## 4. Fines and rewards

Before the missions, three fine and three reward magnitudes are defined globally and referenced by the mission matrices:

```
; Fines are expressed as percentages of current annual income
major_fine          10
moderate_fine       5
minor_fine          1

; Rewards are expressed as direct denari payments
major_reward        10000
moderate_reward     5000
minor_reward        1000
```

- **Fines** are a **percentage of the faction's annual income** — so they scale with how rich the faction is.
- **Rewards** are **flat denarii payments**.

These six values are what the `p1`/`p2`/`p3` and `r1`/`r2`/`r3` codes in the mission matrices resolve to (see next section).

---

## 5. Missions and the penalty/reward matrix

Each mission is a block headed by its name and closed with `End`. Every mission has a **`Duration`** (in turns; `0` means a straight yes/no with no ongoing timer) and a **matrix** of outcomes.

```
Make_Trade_Agreement
Duration    10
-3 E        p3
-3 M        p2
-2 E        p2
-2 M        p1
-1 E        p1
-1 M        p1
0 E         r1
0 M         r1
1 E         r1
1 M         r2
2 E         r2
2 M         r2
3 E         r3
3 M         r3
End
```

### Reading a matrix line

Each line is: **`<attitude> <difficulty> <outcome>`**.

- **Attitude** — a number from **`-3` to `+3`**, representing the senate's current mood toward the faction (−3 = most hostile, +3 = most favourable).
- **Difficulty** — a single letter for how hard the mission is judged to be:
  - **`E`** = Easy
  - **`M`** = Medium
  - **`D`** = Difficult
- **Outcome** — what the faction gets for **completing** the mission in that attitude/difficulty cell:

| Code | Meaning |
|---|---|
| `r1` / `r2` / `r3` | A **reward** — minor / moderate / major (resolves to the reward amounts in §4). |
| `p1` / `p2` / `p3` | A **penalty (fine)** — minor / moderate / major (resolves to the fine percentages in §4). Yes, completing a mission can still carry a penalty in some attitude bands — typically when the senate is hostile and resents you succeeding. |
| `Outlaw` | The faction is **outlawed** by the senate. |

A cell you don't list defaults to **no outcome**. You don't have to fill every combination — only the attitude/difficulty pairs a mission can actually present.

### Optional per-mission settings

Some missions carry extra tuning lines before or alongside the matrix:

| Setting | Meaning |
|---|---|
| `difficulty_boundaries_0` / `_1` / `_2` | Thresholds (e.g. percentages) used to classify a particular instance of the mission as Easy / Medium / Difficult. Seen on missions like `Assassinate`. |
| `reissue_delay_in_turns` | Minimum turns before the same mission may be issued again (stops the senate spamming it). |
| `max_region_traversal` | A distance limit, in regions, for missions such as `Take_City` (how far afield the target may be). |
| `<mission>_lower_boundary` / `_higher_boundary` | Mission-specific tuning ranges (e.g. `take_city_lower_boundary`, `rebel_city_higher_boundary`) controlling target selection. |

### The mission set

The stock file defines matrices for missions including: `Help_Player`, `Demand_Suicide`, `Attack_Outlaw_Faction`, `Assassinate`, `Break_Alliance`, `Cease_Hostilities`, `Declare_War`, `Give_Back_City`, `Exact_Tribute`, `Subjugate`, `Broker_Peace`, `Make_Trade_Agreement`, `Get_Map_Info`, `Appease`, `Make_Alliance`, `Give_Cash`, `Annex_City`, `Blockade_Port`, `Capture_Rebel_City`, `Destroy_Rebel_City`, and `Take_City`.

> **Important:** these mission **types are defined by the game engine** — each one drives specific in-game behaviour. You can freely **retune** any mission's duration, difficulty banding, reissue delay and its full reward/penalty matrix, but you **cannot invent a wholly new mission type** by adding a new block here; an unrecognised mission name has no engine behaviour to attach to. This is the opposite of offices, which *are* fully data-defined.

---

## What changed from original Rome (OG)

| Aspect | Original Rome (OG) | ROME REMASTERED (RR) |
|---|---|---|
| **Offices** | A **fixed set of six**, recognised by hard-coded name; no others allowed. | **Unlimited and fully custom** — any names, any number, read in order. |
| **Office count** | Fixed by the game (10 in early versions, later 6). | As many as you define. |
| **Office titles/descriptions** | From a **fixed built-in** text list. | From your **`expanded_bi`** text table — any custom key. |
| **Office restrictions** | `not_consecutively` plus four **fixed** tenure rules only. | `not_consecutively`, **any `<office>_tenure`**, and **`trait_<name> <level>`**. |
| **Senate scope** | A **single global** Roman senate. | **Per-faction senates** — multiple `Begin_Offices`/`Begin_Unit_Rewards` blocks keyed by faction. |
| **Senate benefits** | `censor_immunity`, `no_censor_suicide`. | Those **plus** `quaestor_immunity`. |
| **Reward units** | Hard-coded unit lists. | **Data-defined pools** in `Begin_Unit_Rewards`, with `requires_event` gating. |
| **Attitude settings, fines/rewards, mission matrices** | Already data-driven and tuned here. | **Unchanged in spirit** — same format, still fully editable. |

The headline: in OG this file mostly *tuned* a fixed senate; in RR it *defines* the offices and reward units outright, per faction, while the attitude/mission tuning works as it always did.

---

## Limitations and notes

- **Office `Title`/`Description` keys must exist** in your `expanded_bi` text before you reference them, or loading fails. See [String overrides](/documentation/data_file_guides/string_overrides.md).
- **`_tenure` restrictions must reference an office defined earlier** in the same block. Order offices low-to-high.
- **`trait_…` restrictions must name a real trait** — see [Traits and ancillaries](/documentation/data_file_guides/traits_and_ancillaries.md).
- **Changing how many offices exist can break existing save games** — office counts aren't stored in saves. Treat such changes as new-campaign-only.
- **Mission types are engine-defined** — retune their matrices, don't expect new names to do anything.
- **Reward unit names must match your EDU** data, and any `requires_event` must be a real campaign event.
- If the file can't be parsed the game logs `Issue when attempting to read descr_senate.txt`; if a faction's office block is missing it logs `Unable to find offices for faction <name>`. The [Senate Offices feature guide](/documentation/feature_guides/Senate_Offices.md#9-error-and-log-messages) lists the full set of parser messages.

---

## Related guides

- [Senate Offices: Adding and Modding Offices and Senators](/documentation/feature_guides/Senate_Offices.md) — the deep-dive companion to this reference.
- [`super_faction` example mod — `descr_senate.txt`](/example_mods/super_faction/data/descr_senate.txt) — a complete working file.
- [EDU — export_descr_unit](/documentation/data_file_guides/EDU.md) — for valid reward-unit names.
- [String overrides](/documentation/data_file_guides/string_overrides.md) — for office title/description text.
- [Traits and ancillaries](/documentation/data_file_guides/traits_and_ancillaries.md) — for `trait_…` restriction names.
