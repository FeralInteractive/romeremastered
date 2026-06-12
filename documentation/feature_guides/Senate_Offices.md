![Workshop_header_template](/Workshop_header_template.png)
# Senate Offices: Adding and Modding Offices and Senators

## Table Of Contents

* [1. What the senate offices system is](#1-what-the-senate-offices-system-is)
   * [What changed from original Rome (OG)](#what-changed-from-original-rome-og)
* [2. Where it all lives: `descr_senate.txt`](#2-where-it-all-lives-descr_senatetxt)
* [3. Anatomy of an office](#3-anatomy-of-an-office)
* [4. Restrictions — who is allowed to hold an office](#4-restrictions--who-is-allowed-to-hold-an-office)
* [5. Senate benefits](#5-senate-benefits)
* [6. Worked example: adding a brand-new office](#6-worked-example-adding-a-brand-new-office)
* [7. Where senators come from, and "more senators"](#7-where-senators-come-from-and-more-senators)
* [8. Limitations and gotchas](#8-limitations-and-gotchas)
* [9. Error and log messages](#9-error-and-log-messages)
* [10. Modder's checklist](#10-modders-checklist)
* [11. Quick diagnosis table](#11-quick-diagnosis-table)
* [Related guides](#related-guides)

This guide explains how senate offices work in ROME REMASTERED, how to add your own offices (and tune how many "senator" seats exist), and the limitations to watch out for. It is written for non-programmers; everything described here is controlled from data files you can edit.

It pairs with the example mod that ships in this repository — [`super_faction/data/descr_senate.txt`](/example_mods/super_faction/data/descr_senate.txt) — which contains a complete, working senate definition you can copy from.

---

## 1. What the senate offices system is

The senate is a special institution attached to the Roman side of the campaign. It hands out **offices** (Quaestor, Aedile, Praetor, Consul, Censor, Pontifex Maximus in the stock game) to eligible characters, issues **missions** to its member factions, and can reward them with **units**. Holding an office gives a character a title and, in some cases, protective benefits.

The single most important thing to know for ROME REMASTERED is this:

> **The senate is now fully data-driven.** In the original game the offices were hard-wired — the same six, in a fixed order, with a fixed set of rules. In Remastered there are **no fixed offices baked into the game**. Every office — its name, how many seats it has, how long it's held, who qualifies, and what perks it grants — is read from `descr_senate.txt`. You are free to rename them, reorder them, add new ones, or remove them.

A second important change: senates are now defined **per faction**. The file can hold more than one senate definition, each tied to a specific faction, rather than one global Roman senate.

### What changed from original Rome (OG)

If you've modded the senate in the original game, almost everything you knew about its *limits* has been lifted. Remastered reads the same `descr_senate.txt` but treats far more of it as data:

| Aspect | Original Rome (OG) | ROME REMASTERED (RR) |
|---|---|---|
| **Which offices exist** | A **fixed set of six**, recognised by hard-coded name: Quaestor, Aedile, Praetor, Consul, Censor, Pontifex Maximus. Any other office name was rejected as `Unrecognised office`. | **Unlimited and fully custom.** Offices are read in order and identified by whatever name you give them. Add, remove, rename freely. |
| **Number of offices** | Fixed by the game (10 in early versions, later 6). | **As many as you define.** |
| **Office titles & descriptions** | Came from a **fixed internal list** of built-in text entries — you couldn't add new ones. | Looked up as **keys in your `expanded_bi` text table**, so any office can have its own custom name and description. |
| **Entry restrictions** | Only `not_consecutively` and the four **fixed** tenure rules (`quaestor_tenure`, `aedile_tenure`, `praetor_tenure`, `consul_tenure`). Anything else was `Unrecognised office restriction`. | `not_consecutively`, **`<any office>_tenure`** (reference any office you've defined), **and `trait_<name> <level>`** (require a character trait). |
| **Character traits as a requirement** | Not possible. | **Supported** via `trait_…`. |
| **Senate scope** | A **single, global** Roman senate. | **Per-faction senates** — multiple `Begin_Offices <faction>` blocks, one per faction that should have one. |
| **Senate benefits** | `censor_immunity`, `no_censor_suicide`. | Those **plus** `quaestor_immunity`. |
| **Senate positions** | A fixed internal list of ranks (Consul, Quaestor, Censor, …). | No fixed ranks — positions are whatever your offices define. |

The short version: in OG the file mostly *tuned* a fixed system; in RR the file *defines* the system. The rest of this guide describes the RR behaviour, and flags **OG vs RR** inline where a difference bites.

---

## 2. Where it all lives: `descr_senate.txt`

Everything is in a single file, `descr_senate.txt`, in your mod's `data` folder. It has four parts:

1. **Attitude settings** at the top — coefficients and boundaries that control how the senate's mood toward a faction is calculated.
2. **`Begin_Offices … End_Offices`** — the office definitions. **This is the part this guide focuses on.**
3. **`Begin_Unit_Rewards … End_Unit_Rewards`** — the pools of units the senate can gift as mission rewards.
4. **The missions** — the senate's mission types and their penalty/reward matrices.

The offices and unit-reward blocks are **tied to a faction by name**. The block header is the faction's senate identifier, for example:

```
Begin_Offices romans_senate
    … office definitions …
End_Offices
```

When the game sets up a faction's senate, it scans the file for the `Begin_Offices` block whose name matches that faction, and reads the offices from there. The matching unit-reward block (`Begin_Unit_Rewards romans_senate`) is found the same way. If the game can't find a block for a faction that should have one, it logs `Unable to find offices for faction <name>` and the senate won't set up correctly.

---

## 3. Anatomy of an office

Each office is a block ending in `End`. Here is the stock Quaestor, annotated:

```
Quaestor                                         ; the office's internal name
Title           SMT_SENATE_OFFICE_QUAESTOR_TITLE        ; text key for the displayed name
Description     SMT_SENATE_OFFICE_QUAESTOR_DESCRIPTION   ; text key for the description

Rank            10        ; (unused — see below)
Quantity        1         ; how many seats of this office exist
Duration        8         ; how many turns a holder serves
Sittings        1         ; (unused — see below)
Restrictions
End_restrictions          ; no entry requirements
Senate_benefits
    quaestor_immunity     ; perk granted to the holder's faction
End_senate_benefits
End
```

Field by field:

| Field | What it does |
|---|---|
| **(name)** | The office's **internal name**, on its own line at the top of the block (e.g. `Quaestor`). This is the name other offices use in `_tenure` restrictions, so keep it unique and without spaces. |
| **Title** | A **text key** for the name shown in-game. This key must exist in your expanded text (`expanded_bi`) table — see [§8](#8-limitations-and-gotchas). |
| **Description** | A **text key** for the office's description, again from your text table. |
| **Rank** | Intended as a pecking-order value. **Currently unused** by the game logic — set it for your own readability, but it changes nothing. |
| **Quantity** | **How many seats this office has.** `Quantity 3` means three characters can hold this office at once (the stock Consul is 3). This is the number to raise if you want "more senators" in a given role. |
| **Duration** | **How many turns** a character holds the office before the seat is up for reappointment. |
| **Sittings** | Intended as a cap on how many times one character may hold the office. **Currently unused.** |
| **Restrictions … End_restrictions** | Entry requirements — who is allowed to take the office. See [§4](#4-restrictions--who-is-allowed-to-hold-an-office). Leave the block empty for "anyone eligible". |
| **Senate_benefits … End_senate_benefits** | Perks the office grants. See [§5](#5-senate-benefits). Leave empty for none. |
| **End** | Closes the office block. |

> **Note on `Rank` and `Sittings`:** both are still **required to be present** (the parser reads them and will fail if they're missing), but their values currently have no effect on gameplay. Include them; don't rely on them.

> **OG vs RR:** The `Title` and `Description` keys behave differently across versions. In the original game they had to be **one of a fixed set of built-in text entries** — you couldn't introduce a new office name. In Remastered they're looked up in your **`expanded_bi` text table**, so any custom key works once you've added the text (see [§8](#8-limitations-and-gotchas)).

---

## 4. Restrictions — who is allowed to hold an office

Restrictions are the heart of the senate's career ladder. Each line inside `Restrictions … End_restrictions` adds one requirement a candidate must meet. ROME REMASTERED supports three kinds:

| Restriction | Meaning |
|---|---|
| `not_consecutively` | The same character **cannot hold this office two terms in a row**. They must sit out at least one term before returning. |
| `<officename>_tenure` | The candidate must have **previously served** in the named office. For example `Quaestor_tenure` means "must have been a Quaestor first". This is how you build a ladder of promotion. |
| `trait_<traitname> <level>` | The candidate must have the named character **trait** at the given level or higher. For example `trait_GoodCommander 2`. The trait must exist in your traits data. |

A few rules that matter:

- **You can stack several restrictions.** A Consul with both `not_consecutively` and `Praetor_tenure` requires a character who has been a Praetor *and* isn't currently coming straight off a Consulship.
- **`_tenure` can name *any* office you've defined** — not just the stock ones. This is what makes custom career ladders possible.
- **Order matters.** A `_tenure` restriction can only refer to an office that appears **earlier in the file**. If you write `Praetor_tenure` before the Praetor office has been defined, the game rejects it with `'<name>' does not contain a valid office name`. Define lower offices first, higher ones later.

> **OG vs RR:** In the original game, tenure restrictions were limited to the **four fixed** offices (`quaestor_tenure`, `aedile_tenure`, `praetor_tenure`, `consul_tenure`) and anything else was rejected. In Remastered, `_tenure` works against **any office you define**, and the **`trait_…`** form is entirely new — neither was possible in OG, and together they're the biggest new lever for building custom career ladders.

---

## 5. Senate benefits

Inside `Senate_benefits … End_senate_benefits` you may list any of three perks. They protect the office-holder's faction from the senate's investigative powers:

| Benefit | Effect |
|---|---|
| `quaestor_immunity` | The faction is **immune to Quaestor investigations**. |
| `censor_immunity` | The faction is **immune to Censor investigations**. |
| `no_censor_suicide` | A Censor investigation against the faction **will not end in a forced suicide**. |

Anything else here is rejected with `Unrecognised senate benefit`.

> **OG vs RR:** `quaestor_immunity` is **new to Remastered**. The original game offered only `censor_immunity` and `no_censor_suicide`.

---

## 6. Worked example: adding a brand-new office

Say you want to add a **Tribune** office that sits between Quaestor and Aedile: two seats, held for six turns, only open to former Quaestors, and granting Quaestor immunity.

1. **Add the text.** In your expanded text (`expanded_bi`) files, add a title and description entry — e.g. keys `SMT_SENATE_OFFICE_TRIBUNE_TITLE` and `SMT_SENATE_OFFICE_TRIBUNE_DESCRIPTION` — with the words players will see. (See the [string overrides guide](/documentation/data_file_guides/string_overrides.md) for how the text tables work.)

2. **Add the office block** to `descr_senate.txt`, **after** the Quaestor (because it references `Quaestor_tenure`) and before any office that will require `Tribune_tenure`:

```
Tribune
Title           SMT_SENATE_OFFICE_TRIBUNE_TITLE
Description     SMT_SENATE_OFFICE_TRIBUNE_DESCRIPTION

Rank            15
Quantity        2
Duration        6
Sittings        0
Restrictions
    Quaestor_tenure
End_restrictions
Senate_benefits
    quaestor_immunity
End_senate_benefits
End
```

3. **Optionally chain it.** If you want the Aedile to now require a Tribune first, change the Aedile's restriction from `Quaestor_tenure` to `Tribune_tenure`. Because the Tribune is defined above the Aedile, the reference resolves.

That's the whole process — there is no separate registration step and no code change. The number of offices is not fixed, so the new office simply takes the next slot.

> **"More offices" vs "more senators":** adding a new office block gives you a new *kind* of office. To put **more people in the senate** in an existing role, raise that office's **`Quantity`**. Both are valid ways to enlarge the senate.

---

## 7. Where senators come from, and "more senators"

Senators aren't a separate unit you recruit — they are the **characters of the senate's member factions**. When a seat needs filling, the game gathers candidates from across the **superfaction** (the senate faction plus the factions subservient to it), then filters that list down to those who satisfy the office's restrictions. The highest-suitability eligible character is appointed.

This has two practical consequences for modders:

- **To enlarge the senate, raise office `Quantity`** (more seats) and/or add new office blocks (more roles). The pool of people who *can* fill them is your faction characters.
- **If there aren't enough eligible characters, seats sit empty.** The game can create a senate officer character when one is needed, but if your **restrictions are too demanding** for the characters that actually exist, offices go unfilled and the game warns of an **insufficiency of senators**. A Consul that requires `Praetor_tenure` is useless if nothing in the campaign ever becomes a Praetor first.

So the realistic limit on "how many senators" is not a hard number in the game — it's **how many of your characters can meet the entry requirements**. Loosen restrictions or shorten the ladder if you want a bigger, busier senate.

---

## 8. Limitations and gotchas

- **Titles and descriptions must exist as text keys.** The `Title` and `Description` values are looked up in your expanded text (`expanded_bi`) table. If the key is missing, loading fails with `Couldn't find senate office title '<key>' in expanded string table` (or the equivalent for the description). Add the text **before** referencing it.

- **`_tenure` references must point at an office defined earlier in the file.** Forward references don't resolve. Order your offices from lowest to highest. A bad reference gives `'<name>' does not contain a valid office name`.

- **`trait_…` restrictions must name a real trait.** An unknown trait gives `'<name>' does not contain a valid trait name`. See the [traits and ancillaries list](/documentation/data_file_guides/traits_and_ancillaries.md).

- **Over-restrictive offices stay empty.** There is no automatic relaxing of rules. If nobody qualifies, the seat is vacant and you'll see senator-insufficiency warnings. Test your career ladder actually fills in a real campaign.

- **`Rank` and `Sittings` are read but unused.** Don't build a design around them having an effect — they don't, currently.

- **Each senate block is matched to a faction by name.** The `Begin_Offices <faction>` header must match a faction that is set up to have a senate. Renaming the block to a faction that isn't a senate faction won't give that faction a working senate on its own.

- **Changing office counts can break existing save games.** This is a long-standing caveat: the **number of offices isn't stored in the save**, it's taken from `descr_senate.txt` each time. If you change how many offices exist and load an older save made with a different count, that save can be left in a broken state. **Treat office-count changes as new-campaign-only**, and tell your users to start fresh.

- **Keep office internal names unique and space-free.** They're used as identifiers in `_tenure` restrictions; duplicates or spaces will cause matching problems.

---

## 9. Error and log messages

If `descr_senate.txt` has a problem, the game reports it while loading. The most useful messages:

### `Issue when attempting to read descr_senate.txt`
The file couldn't be read or parsed at all. Usually a missing file, a missing required field, or a block that isn't closed properly (`End`, `End_restrictions`, `End_senate_benefits`, `End_Offices`).

### `Unable to find offices for faction <name>`
The game looked for a `Begin_Offices <name>` block for a faction that should have a senate and didn't find one. Check the block header spelling matches the faction.

### `Couldn't find senate office title '<key>' in expanded string table`
(and the matching `…office description…` message) — the `Title`/`Description` key isn't present in your text data. Add the text entry.

### `'<name>' does not contain a valid office name`
A `_tenure` restriction refers to an office that hasn't been defined yet (or is misspelled). Move the referenced office earlier, or fix the name.

### `'<name>' does not contain a valid trait name`
A `trait_…` restriction names a trait the game doesn't know. Check spelling against your traits data.

### `Expected either 'not_consecutively', 'trait_<trait_name>' or '<office name>_tenure' for restriction, not '<name>'`
A line inside `Restrictions` isn't one of the three supported forms. Fix the keyword.

### `Unrecognised senate benefit`
A line inside `Senate_benefits` isn't one of `quaestor_immunity`, `censor_immunity`, or `no_censor_suicide`.

---

## 10. Modder's checklist

- [ ] **Add the text first.** Every office's `Title` and `Description` key exists in your `expanded_bi` text before you reference it.
- [ ] **Order offices low-to-high.** Any office used in a `_tenure` restriction is defined **above** the office that requires it.
- [ ] **Unique, space-free office names.**
- [ ] **`Rank`, `Quantity`, `Duration`, `Sittings`** are all present in every block (even though Rank/Sittings do nothing).
- [ ] **Restrictions are achievable** by the characters that actually exist — test that every office fills in a real campaign.
- [ ] **Benefits use only the three valid keywords.**
- [ ] **Block header matches the faction** that should own the senate.
- [ ] **Treat office-count changes as new-campaign-only** and warn users about save compatibility.
- [ ] **Match the working example** in [`super_faction/data/descr_senate.txt`](/example_mods/super_faction/data/descr_senate.txt) when in doubt.

---

## 11. Quick diagnosis table

| Symptom | Most likely cause | Where to look |
|---|---|---|
| Senate doesn't load / file rejected | Missing field, unclosed block, or bad syntax | [§9](#9-error-and-log-messages) `Issue when attempting to read…` |
| One faction has no working senate | No `Begin_Offices` block matching that faction | [§2](#2-where-it-all-lives-descr_senatetxt), [§9](#9-error-and-log-messages) |
| Office name/description shows as a code or blank | `Title`/`Description` key missing from text data | [§8](#8-limitations-and-gotchas) |
| Load fails citing an office name | A `_tenure` restriction points at an office defined later (or misspelled) | [§4](#4-restrictions--who-is-allowed-to-hold-an-office) |
| Load fails citing a trait name | `trait_…` restriction names an unknown trait | [§4](#4-restrictions--who-is-allowed-to-hold-an-office) |
| Offices keep sitting empty / "not enough senators" | Restrictions too strict for the characters available | [§7](#7-where-senators-come-from-and-more-senators) |
| Want more senators in a role | Raise that office's `Quantity` | [§3](#3-anatomy-of-an-office), [§6](#6-worked-example-adding-a-brand-new-office) |
| Old save broken after editing the file | Office count changed; counts aren't saved | [§8](#8-limitations-and-gotchas) |

---

## Related guides

- [`super_faction` example mod — `descr_senate.txt`](/example_mods/super_faction/data/descr_senate.txt) — a complete, working senate definition to copy from.
- [String overrides](/documentation/data_file_guides/string_overrides.md) — how to add the `Title`/`Description` text your offices reference.
- [Traits and ancillaries](/documentation/data_file_guides/traits_and_ancillaries.md) — valid trait names for `trait_…` restrictions.

---
