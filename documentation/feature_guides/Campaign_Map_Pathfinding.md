# Designing Campaign Maps the AI Can Navigate

This guide explains, in plain terms, how the game works out where armies, agents and other characters can walk on the campaign map, why the AI sometimes gets "stuck", and what the pathfinding-related messages in your logs are trying to tell you. It deals **only with the campaign (strategy) map** — battle-map navigation is a completely separate system and is not covered here.

---

## 1. The two layers of campaign navigation

The game does not think about the campaign map as one big grid. It plans movement on **two layers at once**, and a map can be broken on either one.

### Layer 1 — Tiles (the fine grid)
This is the square-by-square layer. When a character actually walks somewhere, the game steps from one tile to the next, choosing from the eight surrounding tiles (the four orthogonal neighbours plus the four diagonals). Each step has a **movement cost**, and the game tries to find the cheapest legal chain of tiles from start to destination.

This is the layer that decides things like *"can this army physically get from this tile to that tile?"*

### Layer 2 — Regions (the big-picture map)
Regions are connected to their neighbours by **frontiers** — think of a frontier as a recognised border crossing between two regions. The AI uses this layer to reason at a strategic level: *"to get an army from Region A to Region D, it must pass through B and C."* It then falls back to the tile layer to actually walk each leg.

Crucially:
- The region layer **only connects land regions to land regions**. Sea regions are skipped entirely when planning a land march.
- A frontier can be **blocked**. A blocked frontier is invisible to strategic planning — the AI will act as if that crossing does not exist.

**Why this matters:** A map can *look* perfectly connected to a human eye and still be broken because the two layers disagree. The most common "stuck AI" bugs come from a region that looks reachable on screen but has no usable frontier, or a corridor that exists on the tile layer but is too long or twisted for the planner to follow (see [Section 5](#5-why-the-ai-gets-stuck-the-iteration-budget)).

There is also a third, supporting calculation — **movement extents** — which is what paints the reachable-tiles overlay when you select an army (the tiles it can reach this turn / next turn). It uses the same rules as the tile layer, so if normal pathing is broken in an area, the movement overlay will usually look wrong there too. That overlay is a handy free diagnostic tool.

---

## 2. What makes a tile impassable

A tile is treated as **impassable** (no character may stand on it or walk through it) for any of the following reasons. When you design terrain, every one of these is effectively a wall:

| Terrain feature | Passable? | Notes |
|---|---|---|
| Sea / ocean | **No** for land units | Only passable to a fleet, or to a land army that is embarked on a ship. Admirals/fleets, conversely, may **only** be on sea tiles. |
| River and river source | **No** | …unless a **road crosses it** (a bridge) or it is a **ford**. A river with no crossing splits the land in two. |
| Low mountains & high mountains | **No** | Solid barrier. |
| Thick / dense forest (the densest forest level) | **No** | Lighter forest is passable but costs more to cross. |
| Flooded tiles | **No** | |
| Landmarks & volcanoes | **No** | Decorative impassable features. |
| Walls without a road | **No** | A wall tile is only passable where a road runs through it (a gate). |
| Cliffs | **Directional** | See below — cliffs can block movement from only *some* directions. |
| Tiles flagged "impassable from all directions" | **No** | A hard, total block, regardless of approach. |

### Cliffs and "directional" impassability
Cliffs are special: a tile can be passable from some sides but not others. The game stores, per tile, **which directions are blocked**. You cannot step from a cliff tile straight onto a coast tile, or vice versa — the height difference is treated as a sheer drop.

Two consequences that catch map makers out:
1. **Diagonal moves around a cliff corner are checked against the tiles on both sides of the corner.** If either neighbour forms a cliff edge, the diagonal is refused. So two tiles can be touching at a corner and still not be walkable between.
2. A tile that is **impassable from all directions** is a complete block — useful for sealing off scenery, but lethal if one sits in the only corridor between two areas.

---

## 3. Settlements, ports and forts must sit on reachable ground

When the game places (or validates) a settlement, port or fort, it refuses tiles that are:

- Sea
- Dense forest
- Flooded
- Low or high mountains
- On a cliff
- On an internal (non-coastal) border between regions
- On a landmark or volcano
- On a wall with no road through it
- On a river or ford

A settlement is also kept a minimum distance from its own region's existing settlement and port, so they can't be stacked on top of one another.

**The trap:** the validity check stops the *placement* being on bad terrain, but it does **not** guarantee the settlement is *reachable*. If you ring a valid settlement tile with impassable terrain (mountains, dense forest, uncrossed river), you can create a city the AI owns but can never march an army to or from. This is one of the most common causes of an AI faction that "does nothing" — its capital is effectively a sealed box.

> **Rule of thumb:** every settlement, port and fort needs at least one *passable* land tile leading out of it that eventually connects, tile by tile, to the rest of its landmass.

---

## 4. Movement cost, roads and fog of war

Finding *a* path is not enough — the game looks for the **cheapest** path, measured in movement (action) points.

- Every tile step costs movement points. The cost depends on the terrain being entered and whether a **road** is present. Roads make tiles cheaper to cross, which is why armies naturally prefer them.
- **Diagonal steps** are available (so movement isn't restricted to a plus-shaped grid), but the planner can be told to ignore diagonals for certain calculations.
- For the **human player only**, tiles hidden in unexplored fog of war carry a heavy extra cost. This nudges the player's suggested routes toward ground they've actually scouted. It does not apply to the AI's own strategic reasoning or to road-building.

### A note on costs going wrong
Movement costs must always be **zero or positive**. If a map's terrain or road data somehow produces a **negative** step cost, the planner's maths breaks down and it can fail to find a route it should easily find. If you are editing terrain-cost or road data and start seeing the `The g value has gone negative` message (see [Section 6](#6-log-messages-and-what-they-mean)), that is the cause — a movement cost has come out below zero.

---

## 5. Why the AI gets stuck: the iteration budget

This is the single most important concept for diagnosing a "stuck AI" map.

When the game searches for a path, it does **not** search forever. Each search is given a **budget** — a maximum number of steps it is allowed to explore before it gives up and reports **no path found**. The budget is generous but finite, and it is **deliberately smaller** for the AI's routine character movement than for, say, the long preview line drawn when a *human* drags an army across the whole map.

What this means in practice:

- If the destination is genuinely **unreachable** (sealed off by terrain), the search burns through its budget and returns nothing. The army stays put.
- Even if a path **technically exists**, a very **long, narrow or maze-like** corridor can force the search to explore so many dead-end tiles that it exhausts the budget *before* it stumbles onto the route. The result is identical: the AI behaves as if there is no path.

So a map can be "connected" in the strict sense and **still** defeat the AI, simply because the only route is too convoluted to find within the budget. A single-tile-wide goat track winding through a huge mountain range is the classic offender.

### Design implications
- **Keep the main arteries between regions reasonably wide and reasonably direct.** A corridor a few tiles wide and roughly straight is found instantly; a one-tile zig-zag over a long distance may not be found at all.
- **Avoid large mazes of impassable terrain.** Every dead end the search has to rule out eats into the budget.
- **Don't rely on a single chokepoint tile** to connect two big landmasses. If anything ever blocks that tile (an enemy army sitting in a zone of control, a flood, a scripted obstruction), the whole connection collapses.

---

## 6. Zones of control (ZOC)

Enemy armies and settlements project a **zone of control** over the tiles around them. The campaign AI has two modes of path search:

- **Avoiding zones of control** — the normal mode. The planner treats enemy-controlled tiles as something to route *around*, and a character that steps into a ZOC is brought to a halt (this is the rule that stops armies sliding straight past an enemy stack).
- **Ignoring zones of control** — used for certain calculations where ZOC shouldn't matter.

For map design, the thing to remember is that a ZOC can **temporarily** close a corridor. If your only route between two areas is one tile wide, a single enemy army parked beside it can seal the border completely, because every alternative tile is impassable terrain. Give the AI room to manoeuvre: alternative tiles, or a corridor wide enough that one enemy can't cover all of it.

---

## 7. Map-maker's checklist for AI-friendly campaign maps

Run through this before shipping a map:

- [ ] **Every land region connects to its neighbours by at least one usable (unblocked) land frontier.** A land region whose only connections are sea, or whose frontiers are all blocked, is a marooned pocket — armies inside it can never strategically path out.
- [ ] **No region is an accidental island.** If a landmass is meant to be reachable on foot, confirm there is an unbroken chain of passable tiles to it — not just a frontier line on the region map.
- [ ] **Every settlement, port and fort has a passable land exit** that connects to the rest of its landmass.
- [ ] **Rivers that are meant to be crossable have a bridge (road) or ford.** A river with no crossing permanently splits the land.
- [ ] **Main routes between regions are a few tiles wide and not excessively winding.** Avoid long, single-tile, maze-like corridors — they can exceed the search budget even when technically passable.
- [ ] **No critical connection depends on a single tile** that an enemy ZOC, flood, or other obstruction could close.
- [ ] **Check cliff and coast boundaries.** Remember cliff-to-coast steps are blocked, and diagonal moves around cliff corners are refused. A coastline can look walkable and not be.
- [ ] **Sea regions are flagged as sea, and land regions as land.** A land region mistakenly treated as sea (or vice versa) will break strategic pathing into and out of it.
- [ ] **Watch the movement-extents overlay.** Select an army in a suspect area and look at the reachable-tiles highlight. If it stops short of where it obviously should reach, you've found a barrier.

---

## 8. Quick diagnosis table

| Symptom | Most likely cause | Where to look |
|---|---|---|
| An AI faction never expands or moves its main army | Its capital/region is sealed off by impassable terrain, or its only frontier is blocked | [§3](#3-settlements-ports-and-forts-must-sit-on-reachable-ground), [§7](#7-map-makers-checklist-for-ai-friendly-campaign-maps) |
| Armies refuse to take an obvious-looking route | Corridor too long/narrow/winding for the search budget, or a cliff/diagonal block | [§5](#5-why-the-ai-gets-stuck-the-iteration-budget), [§2](#2-what-makes-a-tile-impassable) |
| `too many iterations to handle` in the log | Search budget exhausted — unreachable or over-convoluted route | [§5](#5-why-the-ai-gets-stuck-the-iteration-budget) |
| `A_STAR_SEARCH no open nodes` in the log | Destination genuinely unreachable | [§8](#8-log-messages-and-what-they-mean) |
| `...region is a sea` in the log | Land/sea region mis-flagged in region data | [§1](#1-the-two-layers-of-campaign-navigation), [§8](#8-log-messages-and-what-they-mean) |
| `The g value has gone negative` in the log | Negative movement cost in edited terrain/road data | [§4](#4-movement-cost-roads-and-fog-of-war) |
| Units can't cross what looks like a passable river | River has no bridge (road) or ford | [§2](#2-what-makes-a-tile-impassable) |
| Movement-range overlay stops short for no clear reason | A hidden barrier (cliff, directional block, dense forest) in the way | [§1](#1-the-two-layers-of-campaign-navigation), [§2](#2-what-makes-a-tile-impassable) |

