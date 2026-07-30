# Wiki Operations Log

Chronological record of all ingest, update, and maintenance operations.

---

## 2026-07-30 ingest | 15 Hannah Ritchie myths — heat pumps, meat substitutes, hard-to-abate industry, minerals

Fourth big Ritchie batch. 15 new myth pages from `raw/myths/`. Routing pass done first — all 15 confirmed as genuine standalone claims, no merges, one duplicate skipped.

### Routing decisions

- **15 files → 15 new myth pages, no merges**
- `heat-pumps-summary 2.md` was byte-for-byte identical to `heat-pumps-summary.md` — skipped and logged
- `03-heat-pumps-air-conditioning-demand.md` is really about air-conditioning demand, not heat pumps — treated as its own myth (verdict: "AC is not a luxury we can't afford")
- No overlap with the existing 27 myths that would merit merging

### Heat pumps + cooling cluster (3 pages)

| Raw file | New page | Verdict | Topic |
|---|---|---|---|
| heat-pumps-summary.md | heat-pumps-dont-work-in-cold.md | false | energy |
| 02-heat-pumps-cost.md | heat-pumps-too-expensive.md | mostly-false | energy |
| 03-heat-pumps-air-conditioning-demand.md | air-conditioning-luxury.md | false | energy |

Key numbers: COP 2.7 in UK cold, gas boiler 0.7-0.8; Nesta 2,500 users 3/4 happy; £12,000 install vs £2,750 boiler; £7,500 UK grant; 2bn AC units today → 6bn by 2050; efficient units cut demand from 6,200 to 3,400 TWh by 2050 (EU-sized saving); heating causes 4× more emissions than cooling.

### Meat substitutes / plant-based diets cluster (4 pages, Ritchie chapters 41-44)

| Raw file | New page | Verdict | Topic |
|---|---|---|---|
| Chapter-41-Plant-Based-Diets-and-Land.md | not-enough-land-for-plant-based.md | false | food |
| Chapter-42-Meat-Substitutes-and-Carbon.md | meat-substitutes-worse-for-climate.md | false | food |
| Chapter-43-Cost-of-Meat-Substitutes.md | meat-substitutes-too-expensive.md | mostly-false | food |
| Chapter-44-Meat-Substitutes-and-Health.md | meat-substitutes-unhealthy.md | false | food |

Key numbers: 75% of world farmland supports livestock; 75% of soy fed to animals; cow returns 3 cal per 100 fed; fully plant-based diet needs 1bn ha vs current 4bn ha; meat substitutes 10× lower emissions than pork; lab-grown meat cost fell 50,000× since 2013 to $10-100/kg; plant burgers tick 3/8 UPF markers vs 6/8 for processed meat; 1 in 5 UK support a meat tax.

### Hard-to-abate industry cluster (3 pages, Ritchie ch 45-47)

| Raw file | New page | Verdict | Topic |
|---|---|---|---|
| Low-Carbon-Cement-Summary.md | low-carbon-cement-impossible.md | false | materials |
| Low-Carbon-Steel-Summary.md | low-carbon-steel-impossible.md | false | materials |
| Low-Carbon-Aviation-Shipping-Summary.md | flying-shipping-hopeless.md | mostly-false | transport |

Key numbers: cement 7% of global emissions, ~1 tonne CO2 per tonne concrete, +$100-200/tonne with CCS but tiny impact on finished house cost; steel 7% of emissions, 0.8 tonnes coal per tonne steel, 5,200 TWh globally for all-green steel (~⅕ of world electricity), +25% cost = $150 on a car / $400 on a house; aviation + shipping each 2-3% of emissions, Norway 60+ e-ferries, Maersk 18 methanol ships, hydrogen aviation would need 4,000 TWh (15-20% of world electricity).

### Minerals cluster (5 pages)

| Raw file | New page | Verdict | Topic |
|---|---|---|---|
| Minerals-Running-Out-Summary.md | running-out-of-minerals.md | false | materials |
| Minerals-More-Mining-Summary.md | renewables-more-mining.md | false | materials |
| Minerals-Human-Exploitation-Summary.md | clean-energy-child-labour.md | mostly-false | materials |
| Minerals-and-Supply-Dependency-Summary.md | mineral-dependency-same-as-oil.md | mostly-false | materials |
| Minerals-and-Water-Use-Summary.md | clean-energy-uses-too-much-water.md | mostly-false | materials |

Key numbers: lithium production 30k → 150k tonnes/yr (2008-2022), reserves grew even faster (few million → 20m+); coal needs 30× more mining than renewables and 100× more than nuclear per TWh; 74% of world cobalt from DRC (74% of it), 45% of use goes to EVs (26% to electronics), Tesla LFP >50% of new cars; China refines >80% of world rare earths; 92% of world's population would be energy-secure on renewables; 16% of critical mineral mines in high water stress; Chile mining 4% of water vs farming 72%; EV vs petrol water use China 262 vs 137 m³ (EV loses on fossil grid, wins two-thirds on solar/wind).

### Files created

- 15 new pages in `wiki/myths/`
- 0 source summaries (myth workflow)
- 0 pages updated elsewhere
- `wiki/index.md` — 15 new rows in Myths section; date bumped to 2026-07-30
- `wiki/log.md` — this entry

### Cross-linking

All three clusters (heat pumps/AC, meat substitutes, industry, minerals) cross-link tightly within themselves and to relevant existing wiki pages. Notable outward links:
- Heat pumps → `home-cooling-heatwaves`
- Meat substitutes → `eat-lancet-planetary-diet-2025`, `beef-and-climate-change`, `lab-grown-meat`
- Cement → existing `Cement and Concrete - A Hidden Climate Problem`, `bio-based-resins-composites`, `bamboo` (all as alternative building materials)
- Steel/aviation → `renewables-need-fossil-fuels-to-build`, `carbon-capture-will-fix-it`
- Minerals cluster → `ariana-mine-santander` (as a concrete case), `Fossil Fuel Banking`, `Smaller EVs Are Better`

### Overall Myths section state

Wiki now has **42 myth pages**.

Ritchie is still the primary source, roughly on track with the book's chapter count (which appears to have ~47 questions based on the filenames). If Fabien keeps going, we're maybe another 5-10 pages away from covering the whole book.

### Process notes

- The routing pass caught one duplicate (heat-pumps 2), no borderline cases this time
- Meat-substitutes cluster was written carefully to distinguish from the existing `beef-and-climate-change` page — those focus on beef and dietary transition; these focus on the substitutes themselves
- Cement/steel/aviation pages deliberately reference the existing `carbon-capture-will-fix-it` myth so readers can see how CCS fits (and where it doesn't) inside the wider industrial decarbonisation picture
- The `clean-energy-child-labour` page took the most care on tone — the underlying problem (cobalt exploitation) is real and serious. The verdict is "mostly false" because the claim's generalisation ("clean energy relies on it") ignores that the same cobalt is in phones and used to be in petrol catalytic converters, and that the industry is already moving off cobalt

---

## 2026-07-29 ingest | 18 Hannah Ritchie myths — EV, nuclear and renewables clusters

Largest myth batch to date. All 18 from `raw/myths/`, all summarising Hannah Ritchie's *Not the End of the World*. Followed the routing workflow: read all files, produced routing report, user approved "all 18 as new pages, no merges."

### Routing decisions

- **18 files → 18 new myth pages, no merges, no source summaries in `wiki/sources/`** (myth workflow)
- `EV-Grid-Charging-Summary 2.md` was a **byte-for-byte duplicate** of the original — skipped (only wrote 8 EV pages, not 9)
- The **storage/intermittency** myth was flagged as a borderline case (partial overlap with the existing `not-enough-clean-energy` page); user chose Option A → standalone new page

### EV cluster (8 pages)

| Raw file | New page | Verdict | Topic |
|---|---|---|---|
| EV-Carbon-Footprint-Summary.md | evs-just-as-bad-for-climate.md | false | transport |
| EV-Cost-Summary.md | evs-too-expensive.md | mostly-false | transport |
| EV-Cold-Weather-Summary.md | evs-dont-work-in-cold.md | mostly-false | transport |
| EV-Range-Summary.md | evs-only-good-for-short-trips.md | false | transport |
| EV-Charging-Points-Summary.md | not-enough-ev-chargers.md | mostly-false | transport |
| EV-Grid-Charging-Summary.md | evs-will-break-the-grid.md | false | transport |
| EV-Fires-Summary.md | evs-catch-fire-all-the-time.md | false | transport |
| EV-Air-Pollution-Summary.md | evs-still-pollute.md | mostly-false | transport |

Key numbers: EV lifecycle emissions 66-70% lower (UK/EU), still 37-45% lower in coal-heavy China; 100 miles ~£6 (home) vs £12-18 petrol; NAF winter test 19% avg range drop, Tesla 11% best, Skoda 32% worst; Norwegian fire data 4/100,000 EVs/yr, petrol 19× higher; National Grid 25-29% peak rise if all UK cars electric.

### Nuclear cluster (4 pages)

| Raw file | New page | Verdict | Topic |
|---|---|---|---|
| Nuclear-Power-Safety-Summary.md | nuclear-too-dangerous.md | false | energy |
| Nuclear-Power-Waste-Summary.md | nuclear-waste-unsolved.md | mostly-false | energy |
| Nuclear-Power-Build-Time-Summary.md | nuclear-takes-too-long-to-build.md | mostly-false | energy |
| Nuclear-Power-Cost-Summary.md | nuclear-too-expensive.md | mostly-false | energy |

Key numbers: nuclear <0.1 deaths/TWh vs coal 25, gas 2.8, brown coal 33; Fukushima ~2,314 deaths (mostly evacuation-related); Chernobyl ~300-500 confirmed; global average 6-8 years to build; South Korea nuclear at £2.24m/MW vs US £10.23m/MW; Finland's Onkalo repository opening (100,000-year design life).

### Renewables + jobs + wildlife cluster (6 pages)

| Raw file | New page | Verdict | Topic |
|---|---|---|---|
| renewable-energy-costs-summary.md | renewables-too-expensive.md | false | energy |
| renewable-energy-land-use-summary.md | renewables-take-too-much-land.md | mostly-false | energy |
| renewable-energy-storage-summary.md | intermittency-storage-problem.md | mostly-false | energy |
| renewable-energy-waste-summary.md | renewables-produce-too-much-waste.md | false | energy |
| energy-jobs-transition-summary.md | energy-transition-kills-jobs.md | mostly-false | systemic |
| wind-farms-and-birds-summary.md | wind-farms-kill-birds.md | mostly-false | energy |

Key numbers: solar cost down 85% since 2010; 96% of new solar/wind cheaper than new coal/gas; ~$6tn/yr hidden air-pollution cost of fossil fuels; solar at 0.5% of global land; three storage windows (batteries/hydro/hydrogen); Chris Goodall £3tn/yr batteries-only vs billions with hydrogen; coal 89 kg waste/MWh vs solar 2, wind 0.2; 68m global energy jobs 2023 up from 63m in 2019; cats kill 2.4bn US birds/yr vs turbines 1.2m; painting one blade black cut deaths 70%+ (Norway trial).

### Files created

- 18 new pages in `wiki/myths/`
- 0 source summaries (myth workflow)
- 0 pages updated elsewhere
- `wiki/index.md` — added all 18 rows to the Myths section; date bumped to 2026-07-29
- `wiki/log.md` — this entry

### Cross-linking

Each cluster is now heavily cross-linked internally via Connected topics. Notable inter-cluster links:
- EV pages link to Smaller EVs, CARS Life Cycle, EV Progress in the main wiki
- Nuclear pages link to each other and to `intermittency-storage-problem` (firm backup argument)
- Renewables pages cross-link to `poor-countries-need-fossil-fuels` (cost of capital), `bio-based-resins-composites` (blade recycling), `solar-on-peatland`, `Taiwan offshore wind reef fish` source, and the existing `not-enough-clean-energy` and `renewables-not-replacing-fossil-fuels` myths

### Process note

Routing pass before writing was worth it. All 18 files turned out to be genuinely distinct claims — no merges needed — but confirming that up front (with the user's explicit approval on the storage/intermittency borderline case) meant no rework. Storage/intermittency page ended up with 3-time-windows framing, Chris Goodall's £3tn number, and cross-links to nuclear and V2G, which it wouldn't have got as a "Go deeper" append.

### Overall Myths section state

Wiki now has **27 myth pages**. Cluster sizes:
- Framing / systemic (5): its-too-late, not-enough-public-support, poor-countries-need-fossil-fuels, energy-transition-kills-jobs, ai-needs-fossil-fuels
- Renewables / energy transition (7): not-enough-clean-energy, renewables-not-replacing-fossil-fuels, renewables-need-fossil-fuels-to-build, renewables-too-expensive, renewables-take-too-much-land, intermittency-storage-problem, renewables-produce-too-much-waste
- CCS / carbon capture (1): carbon-capture-will-fix-it
- EVs (8): evs-just-as-bad-for-climate, evs-too-expensive, evs-dont-work-in-cold, evs-only-good-for-short-trips, not-enough-ev-chargers, evs-will-break-the-grid, evs-catch-fire-all-the-time, evs-still-pollute
- Nuclear (4): nuclear-too-dangerous, nuclear-waste-unsolved, nuclear-takes-too-long-to-build, nuclear-too-expensive
- Wildlife (1): wind-farms-kill-birds
- (Renewables-need-fossil-fuels-to-build already listed above under renewables)

Ritchie book has been the workhorse throughout. Filenames suggest more chapters ("Question 12", "Question 16"…) — book has ~30 questions, so this pipeline still has runway.

---

## 2026-07-28 ingest (batch 2) | Two more Ritchie myths — AI energy demand + EROI

Second Ritchie batch of the day. Two new myth pages from `raw/myths/`.

### 1. AI energy demand

**Source file:** `raw/myths/AI-and-Energy-Demand-Summary.md`
**Original source:** Hannah Ritchie, *Not the End of the World* (Chatto & Windus, 2024) — Question 12 of the Fossil Fuels chapter ("Won't we need more fossil fuels to keep up with artificial intelligence?")

- Created new myth page: `wiki/myths/ai-needs-fossil-fuels.md`
- Verdict: mostly-false; topic: energy
- Data centres = 1-3% of world electricity today; even under pessimistic AI scenarios, ~6% by 2030
- IEA: world electricity demand grows ~6,000 TWh by 2030; data centres = ~3% of that growth
- Bigger drivers: industry, buildings, EVs, air conditioning, heating
- Local hotspots: Ireland 17%, five+ US states above 10%
- Koomey's Law: 2010-2018 compute grew 550%, energy grew 6%
- Personal AI use is negligible (100 ChatGPT queries ≈ 20 minutes of streaming)
- Real problem is not physics, it is executives dashing for gas (Meta Hyperion Louisiana, Microsoft/Chevron West Texas)
- Cross-references existing wiki pages on data centres, PFAS cooling, Meta RE100 exit

### 2. EROI myth — "we need fossil fuels to build renewables"

**Source file:** `raw/myths/energy-transition-summary 2.md`
**Original source:** Hannah Ritchie, *Not the End of the World* (Chatto & Windus, 2024) — extract on EROI

**Filename note:** the file name looks like a duplicate of `energy-transition-summary.md` (already ingested as `renewables-not-replacing-fossil-fuels.md`), but the content is a completely different myth about **EROI (Energy Return on Investment)** — "you need fossil fuels to build solar and wind." Both were ingested as separate myth pages.

- Created new myth page: `wiki/myths/renewables-need-fossil-fuels-to-build.md`
- Verdict: false; topic: energy
- Solar panels pay back build energy in <1 year, run 25-30 years, produce ~25× the energy they cost
- Wind and nuclear pay back in months
- "Energy cliff": above an EROI of 10, extra gains barely matter for society; solar/wind/nuclear all comfortably above 10
- Every past energy transition used the old system to build the new — this is normal, not a flaw
- Honest caveat noted for biofuels (some pathways have EROI close to 1)

### Overall

- 2 new myth pages
- Updated `wiki/index.md` — added 2 new Myths entries under the existing Myths section
- No source-summary files in `wiki/sources/` (per the myth workflow)
- No index date bump needed — already at 2026-07-28

### Meta observation

The Ritchie book keeps producing high-quality myth pages because it is **structured as a Q&A** with sourced numbers. That is much easier to convert to the Myth template than long-form journalism. If you keep working through the book, this pipeline will keep running smoothly.

---

## 2026-07-28 ingest | Five Hannah Ritchie myths + PFAS in datacentre cooling

Six-file batch — one article (data centres + PFAS) plus five book-summary myths (all from Hannah Ritchie, *Not the End of the World*).

### 1. Article — PFAS in datacentre cooling (Guardian, 27 July 2026)

**Source file:** `raw/articles/US environmental groups urge EPA to reject new Pfas to cool datacenters.md`
**Original source:** The Guardian, Tom Perkins, 27 July 2026 — https://www.theguardian.com/us-news/2026/jul/27/pfas-datacenter-cooling-epa

- Created source summary: `wiki/sources/pfas-datacentre-cooling-guardian-2026.md`
- Updated `wiki/sectors/digital/DRAFT - ai-data-centre-energy-crisis.md` — added "The chemistry of 'waterless' cooling — PFAS in the pipes" section; bumped date to 2026-07-28
- 17 environmental groups led by Earthjustice have asked EPA to reject Chemours' Opteon 2P50, first PFAS coolant fast-tracked under Trump's datacentre executive order
- Two-phase cooling systems (marketed as low-water) use PFAS gas as refrigerant; TFA breakdown product classified as hazardous by ECHA July 2026 (thyroid, sperm quality, liver)
- Adds a third dimension (chemistry) to the existing water/heat framing for data centres

### 2-6. Five Hannah Ritchie myth pages

All from `raw/myths/` — book-summary notes turned into Myth-template pages. No separate source summaries in `wiki/sources/` per the myth workflow.

**`raw/myths/CCS-summary.md` → `wiki/myths/carbon-capture-will-fix-it.md`**
- Verdict: mostly-false; topic: energy
- CCS captures ~0.1% of global emissions today; optimistic 2030 scenario = 2%; realistic role narrow (cement, steel, fertiliser)
- Track record poor: >100 of 149 projects cancelled; ~80% US CCS projects failed
- Oxford: high-CCS pathway costs $1tn+/yr more than low-CCS

**`raw/myths/clean-energy-summary.md` → `wiki/myths/not-enough-clean-energy.md`**
- Verdict: false; topic: energy
- Coal 1/3 efficient, gas ~50%, solar/wind waste nothing → 1 unit renewables replaces 2-3 units coal
- EV 80% efficient vs petrol 20%; full electrification cuts total energy demand by ~40% (416 EJ → 247 EJ)
- 92% of new global electricity demand in 2022 came from renewables

**`raw/myths/climate-support-summary.md` → `wiki/myths/not-enough-public-support.md`**
- Verdict: false; topic: systemic
- 86% of 59,000-person 63-country survey say humans cause climate change; 89% of 130,000-person 125-country survey want more political action
- US: 74% support joining international climate action, 71% say Americans already harmed
- EU: 93% see it as serious problem
- Perception gap (pluralistic ignorance): Americans guessed a third support action; real figure ~two thirds

**`raw/myths/energy-transition-summary.md` → `wiki/myths/renewables-not-replacing-fossil-fuels.md`**
- Verdict: mostly-false; topic: energy
- Three-way split: addition (no clear real-world example), displacement (China), transition (Denmark, UK, Finland)
- UK -50% fossil fuel electricity since 2008 peak; Denmark -80% since 2000; Finland -2/3 since 2000
- More than half of world's countries past "peak fossil fuels" in electricity sector
- Coal, oil, gas each expected to peak globally within ~5 years

**`raw/myths/fossil-fuels-poverty-summary.md` → `wiki/myths/poor-countries-need-fossil-fuels.md`**
- Verdict: mostly-false; topic: systemic
- Sub-Saharan Africa (ex-South Africa): 14% of world population, 0.6% of global CO2 emissions
- Tripling their electricity on gas would raise world emissions by only ~0.6%
- Bottleneck is finance, not technology: solar loans cost ~12% in South Africa/India/Mexico vs ~5% in rich countries
- Rich-country hypocrisy documented: G7 blocked African fossil fuel finance while restarting own coal; EU delayed African fertiliser support on environmental grounds while using 5-10× more per hectare
- Namibia, Brazil, Chile, Morocco already ahead of EU/US on renewable electricity share

### What was done overall

- Created 1 source summary (PFAS)
- Updated 1 wiki page (ai-data-centre-energy-crisis)
- Created 5 new myth pages
- Updated `wiki/index.md` — added PFAS source, expanded ai-data-centre-energy-crisis description, added 5 new Myths entries; bumped last-updated to 2026-07-28

### Process notes

- Second run of the raw/myths/ workflow; smooth
- All 5 myths came from the same author (Hannah Ritchie, *Not the End of the World*), so tone and framing are consistent — "concede first, correct second" was easy to apply because Ritchie herself writes that way
- Where Ritchie is cited for specific numbers, I noted the source in the myth-page Sources block; where the numbers ultimately trace to other bodies (IEA, IPCC, WMO, Yale Program, Nature Climate Change surveys), I named those as well

---

## 2026-07-27 ingest | Myth: it's too late, we're heading for 5 or 6 degrees (first myth ingest)

**Source file:** `raw/myths/Isittoolate.md`
**Original source:** Fabien's notes summarising Hannah Ritchie, *Not the End of the World* (Chatto & Windus, 2024)

**What was done:**
- Created new myth page: `wiki/myths/its-too-late.md` — following the Myth template (six mandatory headings, claim_id matches filename, verdict "mostly-false", topic "systemic")
- Updated `wiki/index.md` — added a new "Myths" section header and the first entry; bumped last-updated to 2026-07-27
- No separate source summary in `wiki/sources/` — per the updated CLAUDE.md, myths do not get one

**Key content:**
- Realistic warming range on current trajectories: **1.8-3°C**, not 5-6°C (UNEP Emissions Gap 2024, IEA WEO 2024)
- Current policies: ~2.5-3°C; 2030 targets met: ~2.4°C; net-zero pledges delivered: ~1.8°C
- 1.5°C is out of reach; even 2°C looks unlikely; but every fraction of a degree still matters
- RCP8.5 flagged as an implausible upper bound that still gets misused in headlines
- Tipping points are real for specific systems but do not form one global switch
- Concede-first tone throughout; no "you're wrong" framing
- Moral licensing warning surfaced in the Go deeper section (reusable bag full of beef example)

**Process note:** first ingest under the new raw/myths/ workflow. Folder was created earlier today; CLAUDE.md Directory Structure and Ingest sections were updated to include it before this ingest ran.

---

## 2026-07-26 ingest | Can Everyone Live a 'Good Life' Within Planetary Limits? (New Scientist / Guimarães)

**Source file:** `raw/papers/LiveGoodLife-NS.pdf`
**Original source:** New Scientist, April Reese, 14 July 2026 (updated 15 July 2026) — *Can everyone live a 'good life' without destroying the planet?*

**What was done:**
- Created source summary: `wiki/sources/live-good-life-guimaraes-newscientist-2026.md`
- Created new wiki page: `wiki/concepts/key-ideas/live-good-life-planetary-boundaries.md`
- Updated `wiki/index.md` — added source and new key-ideas page entries

**Key content added:**
- Humanity has now crossed 7 of 9 planetary boundaries (Rockström 2009 framework)
- Millward-Hopkins (Lausanne, 2025): consumption growth rate 4× higher in surplus-consumption countries than in countries below decent living standards
- "Useless overconsumption" and "consumption corridor" concepts
- Guimarães, Portugal as a working case: European Green Capital 2026; ~2.3 Earths footprint per resident; waste circularity 2.5× Portuguese average; –18% per-capita waste since 2018; 95 ha green space restored; sustainability codified into law
- Landscape Laboratory (Carlos Ribeiro) as the institutional backbone
- Wealthy environmentalists have larger footprints than wealthy peers (echoes high-income carbon paradox)
- World Inequality Lab Global Justice Report (June 2026): global wealth tax on billionaires; average per-capita income ~€5,000/month achievable within planetary limits by end of century

---

## 2026-07-26 ingest | Three New Routes to Global Geothermal (New Scientist)

**Source file:** `raw/papers/Geothermal-NS.pdf`
**Original source:** New Scientist, Katharine Sanderson, 21 July 2026 (updated 23 July 2026)

**What was done:**
- Created source summary: `wiki/sources/geothermal-newscientist-2026.md`
- Updated existing page: `wiki/solutions/renewables/DRAFT - Geothermal energy.md` — added substantial "July 2026: three new routes to geothermal, anywhere on Earth" section; updated frontmatter tags/summary/date/sources
- Updated `wiki/index.md` — added source entry; expanded Geothermal page description

**Key content added:**
- IEA: geothermal's technical potential is ~150× current global electricity demand at depths to 8 km
- Route 1: EGS (Enhanced Geothermal Systems) — 2-10 km depth; Pohang South Korea 2017 M5.5 quake, £148m damage; Iceland's slow-cooling mitigation approach at HS Orka
- Route 2: AGS (Advanced Geothermal Systems / closed-loop) — Eavor's Geretsried Germany plant (operational 2025); China Huaneng supercritical CO2 demo (Zhengzhou, May 2026)
- Route 3: superhot / supercritical geothermal (374°C+) — Iceland Deep Drilling Project's 4.7 km well (2017); Quaise Energy's millimetre-wave drilling plan (Oregon 2030 target; 10+ km by 2035); GA Drilling laser/plasma trials
- Key voices: Matt Houde (Quaise), Iain Staffell (Imperial), Bill Ellsworth (Stanford), Sanjeev Kumar (EGEC), Lilja Magnúsdóttir (HS Orka)

---

## 2026-07-26 ingest | Earthly's Nature Disclosure Frameworks Overview

**Source file:** `raw/articles/What the core sustainability disclosure frameworks require from your nature investments.md`
**Original source:** Earthly blog, Giacomo Bartoleschi and Faith Sayo, 23 July 2026 — https://earthly.org/blog/what-core-sustainability-disclosure-frameworks-require-from-your-nature-investments

**What was done:**
- Created source summary: `wiki/sources/nature-disclosure-frameworks-earthly-2026.md`
- Updated `wiki/index.md` — added source entry
- No new wiki page created — vendor piece; framework map is useful but reads as marketing

**Key content added (framework map):**
- SBTi V2 OER, TNFD (metrics A21.0-A24.4), IFRS S2, ESRS E1-7, SBTN, ISO 14068-1, GHG Protocol, CDP — what each requires from nature-investment disclosures
- EY 2025 Nature Action Barometer: 93% of companies mention nature; only 26% can evidence impact
- 8-in-10 companies reporting across multiple frameworks simultaneously
- MSCI: <30% of nature-based projects achieve BBB+ quality rating
- Vendor caveats noted for future readers

---

## 2026-07-26 ingest | SBTi Corporate Net-Zero Standard V2.0 (Earthly explainer)

**Source file:** `raw/articles/What the SBTi's Corporate Net-Zero Standard V2 means for your carbon credit strategy.md`
**Original source:** Earthly blog, Faith Sayo, 23 July 2026 — https://earthly.org/blog/what-sbti-corporate-net-zero-standard-v2-means-for-business-carbon-credit-strategy

**What was done:**
- Created source summary: `wiki/sources/sbti-net-zero-v2-earthly-2026.md`
- Updated existing page: `wiki/standards-labels/SBTI - sbti-science-based-targets.md` — added substantial "July 2026: SBTi publishes the final Corporate Net-Zero Standard V2.0" section; updated frontmatter tags/summary/date/sources
- Updated `wiki/index.md` — added source entry; expanded SBTi page description

**Key content added:**
- V2.0 takes effect 1 February 2027; new-rule target validation opens Q1 2027; V1.3.1 available until 31 January 2028
- BVCM replaced by Ongoing Emissions Responsibility (OER) framework — three public recognition tiers
- Two-tier classification: Category A (>€50m HIC / >€450m LIC) with strictest obligations, Category B (mostly SMEs) with lighter obligations
- Three formal roles for carbon credits (voluntary OER 2027-35, mandatory removals from 2035 for Category A, neutralisation of residual emissions at net-zero year)
- OER tiers: Engaged (1% + ~$20/tonne), Advanced (100% of scope 1&2 + 10% scope 1-3), Leadership (100% scope 1-3 + $80/tonne)
- $80/tonne clarified as Leadership contribution budget, not a market price
- Nature-based solutions can be up to 90% of the removal requirement in 2035
- Transparency: OER positions published on SBTi Dashboard; opt-outs require written justification

---

## 2026-07-26 ingest | Meta Quits RE100 Clean Energy Pledge (RTÉ)

**Source file:** `raw/articles/Meta quits clean energy pledge amid data centre expansion.md`
**Original source:** RTÉ News, 25 July 2026 — https://www.rte.ie/news/2026/0725/1585032-meta-pledge/ (originally Recharge News)

**What was done:**
- Created source summary: `wiki/sources/meta-quits-re100-rte-2026.md`
- Updated existing page: `wiki/sectors/digital/DRAFT - ai-data-centre-energy-crisis.md` — added "July 2026: Meta quits RE100 as tech pivots to gas" section; updated frontmatter date/summary; extended sources
- Updated `wiki/index.md` — added source entry; expanded ai-data-centre-energy-crisis description

**Key content added:**
- Meta withdrawn from RE100 (Climate Group's 444-member 100%-renewable-electricity pledge)
- Joined 2016; Climate Group explicit reason: "no longer able to meet the technical criteria due to investments made in new gas power"
- 10 new natural gas plants for Meta's Hyperion data centre in Louisiana alone
- Microsoft/Chevron deal for West Texas; Google linked to similar partnerships
- Annualised matching versus 24/7 hourly matching now the real fault line in corporate clean-energy accounting

---

## 2026-07-26 ingest | Puffer Jackets — a Fashion Case Study (Guardian)

**Source file:** `raw/articles/Lofty ambitions can puffer jackets be made more sustainable?.md`
**Original source:** The Guardian (Australia), Petra Stock, 25 July 2026 — https://www.theguardian.com/australia-news/2026/jul/25/lofty-ambitions-can-puffer-jackets-be-made-more-sustainable

**What was done:**
- Created source summary: `wiki/sources/puffer-jackets-guardian-2026.md`
- Updated existing page: `wiki/circularity-waste/DRAFT - The Environmental Impact of the FASHION industry.md` — added "Case study: puffer jackets" section; updated frontmatter tags/summary/date/sources
- Updated `wiki/index.md` — added source entry; expanded Fashion page description

**Key content added:**
- 83% of a puffer jacket's carbon/water footprint comes from producing the materials
- ~100 million puffer jackets made in China annually
- Down/wool/synthetic/plant-based filler comparison
- Down welfare: 1-2% still from live plucking; Responsible Down Standard
- Wool welfare: mulesing still legal in Australia; ZQ Merino, Responsible Wool Standard
- Adelaide University: 89% of garments bought new; padded jackets rarely worn
- Australia: 53% of unwanted clothes to landfill; 9% recycled; 1.5bn new items/year; 220,000 tonnes landfilled
- 1-in-10 items are repaired; repair extends useful life by 2.5 years on average

---

## 2026-07-26 ingest | Smaller EVs Are Better (WRI)

**Source file:** `raw/articles/For Electric Vehicles, Smaller Is Better.md`
**Original source:** WRI, Yiqian Zhang-Billert, Sarah Cassius & Cristina Albuquerque, 28 July 2025 — https://www.wri.org/insights/electric-vehicles-smaller-better

**What was done:**
- Created source summary: `wiki/sources/wri-smaller-evs-2025.md`
- Created new wiki page: `wiki/sectors/transport/smaller-evs-better.md`
- Updated `wiki/index.md` — added source and new transport page entries

**Key content added:**
- 2/3 of BEV models in 2023 were SUVs/pickups/large cars (up from 1/3 in 2017)
- Europe: <40% of BEVs are small/medium; US 25%; China 50%
- Larger EVs use up to 20% more electricity per vehicle
- T&E: prioritising smaller EVs in Europe could cut battery-mineral demand by 25%
- IEA: 18-20% cut in global mineral demand for EV batteries by 2050 with targeted measures
- Safety: 45% higher fatal pedestrian collision risk; +30% for cyclists/pedestrians per +300 kg
- Policy tools: France weight tax (>1600 kg), Paris tripled SUV parking, Norway EV weight+emissions tax, >320 European cities with low-emission zones
- BYD Seagull, Wuling Bingo entering Europe; VW/Renault/Stellantis rolling out sub-€25k EVs
- Average daily European travel: 12.4 km/person — well within compact EV range

---

## 2026-07-26 ingest | WRI Ocean Warming Synthesis

**Source file:** `raw/articles/As Temperatures Climb, the Ocean Takes the Brunt.md`
**Original source:** WRI, Tom Pickerell (Global Director, Ocean Program), 22 July 2026 — https://www.wri.org/insights/ocean-warming-climate-change-impacts

**What was done:**
- Created source summary: `wiki/sources/wri-ocean-warming-2026.md`
- Updated existing page: `wiki/climate-science/record-hot-ocean-el-nino-2026.md` — added "WRI's July 2026 update: the three big ocean numbers" section; updated frontmatter date
- Updated `wiki/index.md` — added source entry; expanded record-hot-ocean-el-nino description

**Key content added:**
- Ocean absorbs 91% of excess heat from GHGs (7.6 billion cups of tea per second)
- Upper 2,000 m: 9th consecutive record year for stored heat in 2025 (WMO)
- Rate of warming 2005-2025 more than double the rate 1960-2005
- Sea level: +11 cm since Jan 1993; rate up from 2.65 mm/yr to 4.75 mm/yr
- Arctic sea ice: record-low annual max March 2025 (~14.3m km²), tied 2026
- Antarctic sea ice: 3rd-lowest annual max in 2025; 2nd-lowest summer min
- Ocean absorbs ~25% of human CO2; surface acidity up ~30% since preindustrial
- Tuvalu-Australia Falepili Union Treaty (climate migration pathway)
- The Gambia salinity case; Pacific Northwest oyster hatcheries case
- IPCC: deep-ocean warming and interior acidification effectively irreversible on our timescales
- WRI's three policy asks: treat adaptation as essential; invest in blue-carbon ecosystems; make ocean data visible alongside emissions

---

## 2026-07-26 ingest | LSHTM–Cornell Nature Study on Healthier Global Diet

**Source file:** `raw/articles/A healthier global diet could cut farm emissions by 85%.md`
**Original source:** ScienceDaily / London School of Hygiene & Tropical Medicine, 23 July 2026 — https://www.sciencedaily.com/releases/2026/07/260716023557.htm
**Peer-reviewed study:** Gibson M et al. (2026), *Food systems transformation would reshape global agriculture*, *Nature*, DOI: 10.1038/s41586-026-10775-2

**What was done:**
- Created source summary: `wiki/sources/lshtm-healthy-diet-farm-emissions-2026.md`
- Updated existing page: `wiki/sectors/agriculture-food/eat-lancet-planetary-diet-2025.md` — added "July 2026 update: what the transformation would actually cost and reshape" section; updated frontmatter date
- Updated `wiki/index.md` — added source entry; expanded EAT-Lancet page description

**Key content added:**
- LSHTM–Cornell team + 10 modelling groups; foresight modelling based on EAT-Lancet 2025 pathway
- Global 2050 vs 2020: net CO2 from land-use change –85%; farmland use –6%; livestock production value –42% (–$630bn); ruminant sector alone –70% (–$274bn); ~400M fewer ruminants worldwide
- Vegetable/fruit/nut/legume value: +57% (+$890bn)
- Regional: USA –21% agri value (crops +20%, livestock –73%); India +46% (crops +65%, livestock –8%); Europe –35% (crops –8%, livestock –66%)
- Caveats: "costless preference shift" assumption; foresight scenarios not forecasts; severe local disruption possible without planning
- Just-transition framing: Matt Gibson quote on confronting "powerful groups that profit from the status quo"

---

## 2026-07-22 ingest | Jet Stream Patterns Behind Europe's Long Heatwaves (New Scientist)

**Source file:** `raw/papers/Jetstream-NS.pdf`
**Original source:** New Scientist, Alec Luhn, 13 July 2026
**Peer-reviewed study:** *Environmental Research Letters*, Pappert D. & Martius O. (University of Bern), DOI: 10.1088/1748-9326/ae7f34

**What was done:**
- Created source summary: `wiki/sources/jetstream-heatwave-patterns-newscientist-2026.md`
- Created new wiki page: `wiki/climate-science/jetstream-heatwave-patterns-2026.md`
- Updated `wiki/index.md` — added source and new climate-science page entries

**Key content added:**
- Only ~20 well-observed long heatwaves in the daily record; Bern team simulated 1,900 plausible hot spells with a climate model
- Two jet stream patterns identified: **Type I** (wavy jet stream tracing an omega block over western Europe; Atlantic storms reinforce the low pressure at the omega's base) and **Type II** (poleward-shifted straighter jet stream diverting storm track north of the UK)
- Both patterns produce a persistent high-pressure ridge over Europe; same feedback loop at ground level (dry compressed descending air, no clouds, drying land)
- June 2026 European heatwave killed ~20,000 people; started as Type II, morphed into Type I
- Trend in blocking patterns is not yet resolved — some studies find more, some no change
- Jet stream is shifting northwards in general, likely drying southern Europe
- Practical use: pattern-recognition tool for forecasters and grid operators to prepare for prolonged heat

---

## 2026-07-22 ingest | JBS $6bn Expansion — First Big Legal Challenge to a Meat Major

**Source file:** `raw/articles/​World largest meat company faces legal challenge over green credentials of $6bn global expansion.md`
**Original source:** The Guardian, Jonathan Watts, 22 July 2026 — https://www.theguardian.com/environment/2026/jul/22/meat-multinational-faces-legal-challenge-over-green-credentials-of-6bn-global-expansion-plan

**What was done:**
- Created source summary: `wiki/sources/jbs-6bn-legal-challenge-guardian-2026.md`
- Updated existing page: `wiki/concepts/key-ideas/Greenwashing lawsuits on the rise.md` — added "July 2026 update: the first big legal challenge against a meat major (JBS)" section; updated frontmatter tags/summary/date
- Updated `wiki/index.md` — added source entry; expanded Greenwashing lawsuits description

**Key content added:**
- Greenpeace International petitions Dutch courts to force JBS to disclose how its $6bn expansion is compatible with duty-of-care obligations
- Specifically targets $2.5bn plan for six meat plants in Nigeria; Niger State has promised 1.2m hectares
- JBS moved HQ to the Netherlands in 2025 to list on NYSE — now exposed to Dutch legal standards used against Shell
- Track record cited: broke Amazon deforestation cleanup pledge, scrapped "net zero by 2040", latest sustainability report excludes indirect emissions from cows
- Recent precedents: TotalEnergies ordered by Paris court to disclose climate risks (June 2026); Shell case in The Hague — ruling expected early 2027
- Key quote (Brown): "if you come to the Netherlands, you have to play by Dutch rules and be held to account to Dutch standards"

---

## 2026-07-22 ingest | UK Datacentre Water Shortage — Water UK Evidence to MPs (Guardian)

**Source file:** `raw/articles/Not enough water for UK's datacentre plans, trade body says.md`
**Original source:** The Guardian, Pippa Neill, 21 July 2026 — https://www.theguardian.com/environment/2026/jul/21/not-enough-water-for-uks-datacentre-plans-trade-body-says

**What was done:**
- Created source summary: `wiki/sources/uk-datacentre-water-shortage-guardian-2026.md`
- Updated existing page: `wiki/sectors/digital/DRAFT - ai-data-centre-energy-crisis.md` — added "UK data centres and water: 'fatally flawed' government forecasts" section; extended sources; updated frontmatter date/summary
- Updated `wiki/index.md` — added source entry; expanded ai-data-centre-energy-crisis description

**Key content added:**
- Water UK submission to MPs calls government forecasts "fatally flawed" for excluding datacentres
- 125 datacentres proposed or under construction in Affinity Water region alone (much under hosepipe ban)
- Individual datacentres requesting up to 3 million litres/day — the peak demand of 3,500 homes
- Environment Agency permitting requires datacentres to use drinking water only
- Current UK datacentre use ~6.6m L/day; tripling capacity by 2030 → ~19.8m L/day
- May 2026 House of Lords report: 5bn L/day public water shortfall by 2055
- Drought hierarchy still not published by ministers
- Datacentres designated critical national infrastructure — potentially prioritised over households in droughts
- Water UK's Jon Chappel: "unforgivable" and "a genuine failing of government"

---

## 2026-07-22 ingest | Europe Wetlands Map (Phys.org / University of Copenhagen / *Nature*)

**Source file:** `raw/articles/New study pinpoints Europe's most critical wetlands for climate action.md`
**Original source:** Phys.org / University of Copenhagen, 15 July 2026 — https://phys.org/news/2026-07-europe-critical-wetlands-climate-action.html
**Peer-reviewed study:** Kovács GM et al. (2026), *Nature*, DOI: 10.1038/s41586-026-10760-9

**What was done:**
- Created source summary: `wiki/sources/europe-wetlands-map-copenhagen-2026.md`
- Updated existing page: `wiki/biodiversity-land/The importance of Wetlands.md` — added "2026 update: Europe's wetlands finally get a harmonised 10-metre map" section; updated frontmatter tags/summary/date; added map viewer and DOI to sources
- Updated `wiki/index.md` — added source entry; expanded Wetlands page description

**Key content added:**
- First harmonised 10-metre resolution wetland map for 38 European countries (Global Wetland Center, University of Copenhagen)
- Six categories: inland marshes, peatbogs, salt marshes, salines, intertidal flats, moors & heathlands
- 27–33% of contiguous wetland area is in patches smaller than 25 ha; 7–11% under 1 ha — much of which was missed by coarser mapping
- ~1/5 of Europe's wetlands highly affected by human activities; inland marshes most disturbed
- Peatlands top climate priority — concentrated in Northern Europe, both biggest stores and biggest emitters when disturbed
- Up to 5 Gt CO2-eq soil carbon may already have been released — equivalent to ~1.5 years of total EU CO2 emissions
- Directly supports the EU Nature Restoration Law (30% by 2030 target)
- Kovács now working on a global version

---

## 2026-07-22 ingest | EU Ban on Destroying Unsold Clothes (DW)

**Source file:** `raw/articles/EU ban on destroying unsold clothes takes effect.md`
**Original source:** Deutsche Welle, Nik Martin, 19 July 2026 — https://www.dw.com/en/eu-ban-on-destroying-unsold-clothes-takes-effect/a-78024888

**What was done:**
- Created source summary: `wiki/sources/eu-unsold-clothes-ban-dw-2026.md`
- Updated existing page: `wiki/circularity-waste/DRAFT - The Environmental Impact of the FASHION industry.md` — added "2026 update: EU bans the destruction of unsold clothes" section; updated frontmatter tags/summary/date
- Updated `wiki/index.md` — added source entry; expanded fashion page description

**Key content added:**
- Ban took effect 19 July 2026 across the 27-member EU under the Ecodesign for Sustainable Products Regulation (ESPR)
- Applies to firms with >250 employees and >€50m turnover; extended to medium-sized firms in 2030
- Firms must find ways to sell products (discounts, alternative markets, charity); destruction only when unsafe, damaged, counterfeit, or rejected by charities
- Annual disposal reports and 5-year record retention required
- EEA: 4–9% of unsold textile products destroyed each year; 1 in 5 online returns not resold
- Only ~20% of apparel sold in the EU is produced in the EU — supply-chain vulnerability
- HDE welcomes consumer-side gains; flags "not all unsold goods can be resold or donated easily"

---

## 2026-07-22 ingest | Taiwan Offshore Wind — 86 Reef Fish Species on Formosa Foundations

**Source file:** `raw/articles/Divers went down to check on 69 offshore wind turbines off the coast of Taiwan, and the 86 species they found living in the steel had never been recorded there before.md`
**Original source:** EcoPortal, Hugo Rojas, 17 July 2026 — https://www.ecoportal.net/en/divers-went-check-offshore-wind-turbines/29373/
**Peer-reviewed study:** *Frontiers in Marine Science* (2026) — https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2026.1733177/full

**What was done:**
- Created source summary: `wiki/sources/taiwan-offshore-wind-reef-fish-2026.md`
- Updated existing page: `wiki/solutions/renewables/DRAFT - FACTS about Wind Energy.md` — added "2026: Offshore Wind as an Accidental Reef — 86 New Fish Species at Formosa (Taiwan)" section; updated frontmatter tags/summary/date/sources
- Updated `wiki/index.md` — added source entry; expanded Wind Energy page description

**Key content added:**
- Formosa Wind Farm: 69 turbines across ~90 km² of previously flat sandy seabed off Miaoli County, Taiwan
- SCUBA surveys in 2017, 2018 and 2025; 86 reef-associated fish species documented within 50 m of foundations in 2025, none previously recorded in the area
- Colonisation sequence: barnacles/sponges/corals within months → shrimp/crabs/gastropods → groupers/snappers/lobsters
- By 2025, species richness, diversity and trophic structure indistinguishable from established purpose-built artificial reefs
- Foundations act as "cliff face" habitat spanning surface to seabed — drawing full water column
- Wider literature caveat: attraction vs production debate; at Formosa the absence of prior records suggests real production
- Result generalises to fixed-bottom offshore wind on soft-bottom seabeds; other siting still needs its own evidence

---

## 2026-07-13 ingest | Nature at a Crossroads — ISSB Nature Practice Statement (Reuters Events)

**Source file:** `raw/papers/Nature&BiodiversityResearch-Reuters.pdf`
**Original source:** Reuters Events Sustainable Business, Catherine Early — *Nature at a Crossroads: The evolving architecture of nature disclosure* (2026)

**What was done:**
- Created source summary: `wiki/sources/nature-at-a-crossroads-reuters-2026.md`
- Created new wiki page: `wiki/standards-labels/issb-nature-practice-statement-2026.md`
- Updated `wiki/index.md` — added source and new standards-labels page entries

**Key content added:**
- ISSB decided (April 2026 leak) not to develop a mandatory standalone nature standard (IFRS S3); instead a non-mandatory "practice statement" attached to IFRS S1
- Pushback led by Nature Finance, WWF, BirdLife International, Nature Positive Initiative, Paul Polman, Johan Rockström, Pavan Sukhdev, Marco Lambertini
- Key McCarthy line: the ISSB is "actively maintaining a disclosure framework that instructs companies to report climate risk against a baseline that the board's own scientific advisors know to be false"
- $44tn annual output nature-dependent; PwC: 12–17% GDP erosion at risk; Sussex: $2tn/yr from partial ecosystem collapses
- TNFD 2025 Status Report: ~620 organisations across 50+ countries, ~$20tn AUM committed
- Japan largest single-country adopter (~130 orgs); China's Environmental and Ecological code effective 15 Aug 2026
- ISSB exposure-draft consultation planned October 2026 ahead of COP17 biodiversity negotiations

---

## 2026-07-13 ingest | A Record-Hot Ocean and the 2026 El Niño

**Source file:** `raw/articles/Why A Record-Hot Ocean Is Supercharging The El Niño Effect.md`
**Original source:** Forbes contributor column, Ingmar Rentzhog (CEO, We Don't Have Time), 9 July 2026 — https://www.forbes.com/sites/we-dont-have-time/2026/07/09/why-a-record-hot-ocean-is-supercharging-the-el-nio-effect/

**What was done:**
- Created source summary: `wiki/sources/record-hot-ocean-el-nino-forbes-2026.md`
- Created new wiki page: `wiki/climate-science/record-hot-ocean-el-nino-2026.md`
- Updated `wiki/index.md` — added source and climate-science page entries

**Key content added:**
- 21 June 2026: global sea surface temperature at 21.0°C (record for time of year, Copernicus)
- H1 2026: marine heatwaves touched ~82% of the global ocean; Mediterranean worst hit
- NOAA (June 2026) declared El Niño; 63% odds of very strong event at Nov–Jan peak
- Nature Communications (2024): deep-ocean warming alone could make extreme El Niños 40–80% more common
- 4th global mass coral bleaching event affected ~84% of world's reefs, 2023–mid-2025
- High Seas Treaty entered into force 17 January 2026 (80+ signatories)
- Ocean Observatories Initiative (~900 sensors, $386m) narrowly saved from shutdown in June 2026
- 2020 shipping-sulphur rule cut sulphate aerosols; may have contributed to 2023 ocean warming acceleration
- IEA: clean energy now ~2× fossil fuel investment; methane cuts could avoid ~0.5°C by mid-century

---

## 2026-07-13 ingest | Bamboo-Ready — Institution of Structural Engineers manual

**Source file:** `raw/articles/Schools, airports, high-rise towers architects urged to get 'bamboo-ready'.md`
**Original source:** The Guardian, Yassin El-Moudden, 22 January 2026 — https://www.theguardian.com/environment/2026/jan/22/bamboo-architecture-construction-engineering-schools-airports-towers

**What was done:**
- Created source summary: `wiki/sources/bamboo-construction-guardian-2026.md`
- Updated existing page: `wiki/solutions/nature-based-solutions/The incredible environmental properties of Bamboo.md` — added "2026 update: engineering bamboo for permanent buildings" section; corrected frontmatter tags; added sources; extended summary keywords
- Updated `wiki/index.md` — expanded Bamboo page description

**Key content added:**
- Institution of Structural Engineers published a new manual for permanent bamboo structures based on ISO 22156; lead author David Trujillo (Warwick)
- Concrete existing projects: Kempegowda Airport Bengaluru, Ninghai bamboo tower China (>20 m), Green School Bali
- Composite bamboo shear walls used for earthquake-resilient housing in Colombia and typhoon-resilient housing in the Philippines
- Bamboo is not appropriate above two storeys in general use
- Knowledge gaps traced partly to colonial-era technical education
- Portugal now growing larger bamboo varieties as a crop as Mediterranean shifts; Horizom, Fiboo building European supply chain
- Construction ~1/3 of global carbon emissions in 2022; more than half from cement

---

## 2026-07-13 ingest | Mass-Balance Recycled Plastic Greenwashing (Guardian / IJ4EU)

**Source file:** `raw/articles/Europe's supermarket shelves packed with 'misleading' claims about recycled plastic packaging.md`
**Original source:** The Guardian, Stefano Valentino, 27 January 2026 — https://www.theguardian.com/environment/2026/jan/27/recycled-plastic-packaging-claims-misleading-say-experts (part of an IJ4EU cross-border investigation)

**What was done:**
- Created source summary: `wiki/sources/eu-recycled-plastic-mass-balance-2026.md`
- Created new wiki page: `wiki/circularity-waste/plastic-mass-balance-greenwashing.md`
- Updated `wiki/index.md` — added source and circularity-waste page entries

**Key content added:**
- Pyrolysis oil = at most 5% of feedstock; 95% must be virgin naphtha
- Mass-balance bookkeeping lets 5% recycled input be assigned to 5 tonnes labelled "100% recycled" (all fossil chemistry)
- "Avoided emissions" credit turns a 6–8% worse process into apparent 2 kg CO2 savings per kg
- ISCC industry-led certification; Sabic used only 2,600 t of pyrolysis oil in 2022 vs ~4 Mt of naphtha
- Kraft Heinz, Mondelēz named brands; Saudi Aramco (Sabic parent) is world's largest corporate GHG emitter
- EU PPWR rules that accommodate mass balance take effect in 2026; UK equivalent in 2027
- IEA World Energy Outlook 2025: plastic set to become a critical growth engine for oil majors

---

## 2026-07-13 ingest | Dublin Sea Rise and the Data Centre Split (Irish Independent)

**Source file:** `raw/articles/Dublin faces complex emissions challenges as sea rises twice as fast as global average.md`
**Original source:** Irish Independent, Liam Coates and Azmia Riaz (with Shauna Corr), 29 January 2026 — https://www.independent.ie/county/dublin/dublin-faces-complex-emissions-challenges-as-sea-rises-twice-as-fast-as-global-average/a/126667590.html — funded by the Local Democracy Reporting Scheme

**What was done:**
- Created source summary: `wiki/sources/dublin-sea-rise-emissions-2026.md`
- Updated existing page: `wiki/ireland-hub/DRAFT - IRELAND Climate Adaptation.md` — added substantial "Dublin Bay: Sea Level Rise at Twice the Global Rate" section covering planned retreat, DART protection, inland flooding and decarbonisation zones; corrected frontmatter tags; expanded summary
- Updated existing page: `wiki/ireland-hub/DRAFT - IRELAND Data Centre Dilemna.md` — added "Dublin data-centre concentration and the SDCC ban motion (Jan 2026)" subsection with the 7%/46% shares
- Updated `wiki/index.md` — added source entry; expanded descriptions for both Ireland Hub pages

**Key content added:**
- Dublin Bay sea level rising at 7–8 mm/yr vs 3–4 mm/yr global (double the rate)
- Combined 2018 Dublin council emissions: 6.4 Mt CO2; 36% from transport
- Data centres = 7% of Dublin city emissions, 46% of south county Dublin
- Voluntary Homeowners Relocation Scheme: 174 potentially eligible, only 20 accepted by Sept 2024
- €230m East Coast Railway Infrastructure Protection Projects
- SDCC passed motion September 2025 calling for nationwide data-centre ban
- Micheál Martin: "demonisation of data centres" must end; Eamon Ryan: zero-emissions data centres as opportunity

---

## 2026-07-13 ingest | Construction Industry — the Reuse Target (own-research)

**Source file:** `raw/own-research/Construction industry - the reuse target.md`
**Original source:** Own research by Fabien Mossière, drawing on Ecologie360 (2025)

**What was done:**
- Filed directly (own-research — no summarising): `wiki/sectors/buildings/construction-industry-reuse-target.md`
- Added standard frontmatter, editorial summary blockquote and relative markdown links to Cement/Concrete, Bio-based resins and Bamboo pages
- Preserved original body content exactly
- Updated `wiki/index.md` — added entry under Buildings section

**Key content:**
- Reuse (not recycling) as a distinct approach: taking doors, tiles, sanitary ware straight from demolition to new build
- Ademe estimate: reuse could cut construction sector's carbon impact by 30–40%
- Construction = ~1/3 of French emissions
- Blanchemaille (Roubaix, La Redoute former HQ): 13,000 sqm, €600k saved, ~600 t CO2 avoided
- Concrete reuse: up to 500 kg CO2/tonne avoided; metal: 90% energy saving; wood: 1,000 L water saving per m³
- Under RE2020, reused materials count as zero carbon (up to 30% carbon intensity cut per sqm)
- Engie's La Garenne-Colombes HQ: 6,000 sqm reused panels, 600 reused glazed units (Saint-Gobain Clipper Coramine)
- Obstacles: selective removal takes longer, insurance and certification, matching supply and demand
- Cyneo (Bouygues), BTP Match, Recyclo'Bat as emerging platforms; Circable (Vinci) for electrical cables

---

## 2026-07-06 ingest | EAT-Lancet 2025 — The Planetary Health Diet Update

**Source file:** `raw/articles/EAT-Lancet report Three key takeaways on climate and diet change.md`
**Original source:** Carbon Brief Staff, 2 October 2025 — https://www.carbonbrief.org/eat-lancet-report-three-key-takeaways-on-climate-and-diet-change/
**Underlying report:** Rockström et al. (2025), *The EAT-Lancet Commission on healthy, sustainable and just food systems*, The Lancet Commissions, DOI: 10.1016/S0140-6736(25)01201-2

**What was done:**
- Created source summary: `wiki/sources/eat-lancet-2025-carbonbrief.md`
- Created new wiki page: `wiki/sectors/agriculture-food/eat-lancet-planetary-diet-2025.md`
- Updated `wiki/index.md` — added source entry and new agriculture-food page entry

**Key content added:**
- 2025 update of the 2019 planetary health diet, with improved food-system modelling and a new social-justice dimension
- Food systems = ~1/3 of human-driven GHG; even with full fossil phaseout, food alone can push past 1.5°C
- Recommended ~2,400 kcal/day, plant-rich, minimally processed — still allows ~1 glass milk/day, 2 meat + 2 egg servings/week
- Full dietary transformation cuts non-CO2 agri-emissions 20% vs 2020 and cuts agricultural land use by 3.4 million km² (India-sized)
- Dietary shift + ambitious mitigation policies cut non-CO2 agri-emissions 34%
- ~15 million avoidable deaths/year if adopted widely
- Richest 30% of the world's population = 70%+ of food-system environmental pressure
- Food systems are the largest driver of five of nine planetary boundaries being breached
- Rockström expects and is prepared for another meat-industry backlash (DeSmog documented the 2019 disinformation campaign)

---

## 2026-07-06 skip | Greenwashing, illegality and false claims 13 climate litigation wins in 2025 1.md

**Source file:** `raw/articles/Greenwashing, illegality and false claims 13 climate litigation wins in 2025 1.md`

**Decision:** Skipped. Duplicate of `raw/articles/Greenwashing, illegality and false claims 13 climate litigation wins in 2025.md`, which was ingested on 2026-06-12. Same Guardian article by Isabella Kaminski (31 December 2025); this copy differs only in the `created` timestamp and a trailing Guardian donation appeal, which is not substantive content.

---

## 2026-07-06 skip | How food and farming will determine the fate of planet Earth.md (re-download)

**Source file:** `raw/articles/How food and farming will determine the fate of planet Earth.md`

**Decision:** Skipped. Already ingested on 2026-06-04. Same Project Drawdown article by Jonathan Foley PhD (30 March 2024) at the same URL. The file is a fresh re-clip; the content is already reflected in `wiki/sectors/agriculture-food/agriculture-planetary-footprint.md` and the source summary `wiki/sources/foley-food-farming-fate-earth-2024.md`.

---

## 2026-07-06 ingest | Bio-Based Wood Resins Outperform Fossil Composites (University of Oulu)

**Source file:** `raw/articles/New wood-based resin beats fossil resin strength by 76%.md`
**Original source:** New Atlas, Etiido Uko (with Juha Heiskanen, University of Oulu), 8 March 2026 — https://newatlas.com/materials/bio-based-wooden-plastic-resins/
**Peer-reviewed study:** *Composites Part B: Engineering* (2026) — https://www.sciencedirect.com/science/article/pii/S1359836825011722

**What was done:**
- Created source summary: `wiki/sources/wood-based-resin-oulu-2026.md`
- Created new wiki page: `wiki/sectors/industry/bio-based-resins-composites.md`
- Updated `wiki/index.md` — added source entry and new industry page entry

**Key content added:**
- University of Oulu team (Salonen, Heiskanen et al.) has replaced petroleum-derived DGEBA with furfural-derived diepoxides made from lignocellulosic biomass (sawdust, straw)
- Bio-based polyester resin: 76% higher tensile strength than commercial fossil polyester
- Bio-based epoxy composites: improved toughness and higher tensile/flexural strength than DGEBA
- Furfural-based diepoxide has a degradable chemical structure — first bio-epoxy composite reported to combine high mechanical performance with chemical recyclability
- 90-day harbour weathering test passed
- Production compatible with existing chemical industry lines — no factory retool; price parity feasible once feedstocks scale
- Three patents filed; industrial partners being sought
- EU strategic autonomy angle: Europe has <2% of global oil reserves
- Applications: wind turbine blades, boat hulls, car body panels, aircraft, sporting goods, civil engineering

---

## 2026-07-06 ingest | BP Shareholder Rebellion — Triple Climate Defeat at April 2026 AGM

**Source file:** `raw/articles/BP board suffers triple climate rebellion from shareholders.md`
**Original source:** The Guardian, Jillian Ambrose, 23 April 2026 — https://www.theguardian.com/uk-news/2026/apr/23/bp-board-suffers-triple-climate-rebellion-from-shareholders

**What was done:**
- Created source summary: `wiki/sources/bp-shareholder-rebellion-2026.md`
- Created new wiki page: `wiki/climate-finance/bp-shareholder-rebellion-2026.md`
- Updated `wiki/index.md` — added source entry and new climate-finance page entry

**Key content added:**
- BP's first AGM under new chair Albert Manifold and new CEO Meg O'Neill (first female CEO of any oil major)
- >50% of votes opposed the plan to scrap existing climate reporting
- >50% opposed replacing in-person AGMs with online-only meetings
- 18% opposed re-election of chair — described as "unprecedented" less than a year into the role
- LGIM (UK's largest asset manager) voted against climate-reporting rollback and against Manifold
- Glass Lewis and ISS proxy advisers opposed the rollback; Glass Lewis also opposed Manifold personally, over exclusion of the Follow This resolution asking how BP's rising oil and gas output aligns with a world shifting away from fossil fuels
- Wider context: BP has walked back Bernard Looney's transition targets to close a market-value gap with Shell — investors not convinced
- Mark van Baal (Follow This): "How does BP plan to create value for shareholders as oil and gas demand declines? BP would rather antagonise its shareholders than answer it."
- Nick Mazan (ACCR): "Investors have communicated loud and clear that brushing shareholders aside is unacceptable in public markets."

---

## 2026-07-06 ingest | Oil Nations on Edge — TAFF Coalition at Bonn Intersessional

**Source file:** `raw/articles/Oil nations on edge in the face of new climate coalition.md`
**Original source:** DW (Deutsche Welle), Tim Schauenberg, 18 June 2026 — https://www.dw.com/en/oil-nations-on-edge-in-the-face-of-new-climate-coalition/a-77607010

**What was done:**
- Created source summary: `wiki/sources/dw-oil-nations-taff-2026.md`
- Updated existing page: `wiki/solutions/energy-transition/santa-marta-fossil-fuel-conference-2026.md` — added "June 2026 update: TAFF at the Bonn intersessional" section; corrected frontmatter tags to quoted hashtag form; added DW to sources; expanded summary keywords
- Updated existing page: `wiki/legislation-policy/DRAFT - COP30.md` — added "Update: Bonn intersessional and COP31 Turkey (June 2026)" subsection; quoted tags; updated date
- Updated `wiki/index.md` — added source entry; updated descriptions for both pages above

**Key content added:**
- Santa Marta coalition now has a working name: **Transition Away From Fossil Fuels (TAFF)**
- Iran war and resulting energy price shock have shifted political mood in Bonn
- UN climate chief Simon Stiell: fossil fuel dependence means "importing inflation and economic instability"
- African lead negotiator Antwi Boasiako Amoah cautions TAFF risks fragmenting the multilateral process; Africa cannot fund adaptation through additional debt
- COP31 will be held in Turkey, November 2026
- Adaptation finance tripling debate stuck on baseline year: ~$20bn (2019) vs ~$40bn (2025)
- Outgoing COP30 President André Correa do Lago: "moving from COPs focused on negotiations to COPs focused on implementation"

---

## 2026-07-06 ingest | Heatwaves and Sport (own-research)

**Source file:** `raw/own-research/Sports and Heatwave.md`
**Original source:** Own research by Fabien Mossière, based on Bloomberg Green Zero podcast episode "Is the world becoming too hot for summer sports?" (2 July 2026, Akshat Rathi with Jessica Murfree, UNC)

**What was done:**
- Filed directly (own-research — no summarising): `wiki/sectors/heatwaves-and-sport.md`
- Added standard frontmatter, editorial summary blockquote, tags and relative markdown links
- Preserved original body content exactly
- Updated `wiki/index.md` — added entry under Sport section

**Key content:**
- Sport-and-climate as a two-way problem: warming changes how sport is played; sport itself emits through travel, construction, sponsorship
- Health risk: elite athletes, humidity and wet-bulb; risks extend to farmers and construction workers
- Sports most exposed: baseball, football, soccer, track and field, cricket
- Current adaptations: hydration breaks, marathon relocation (Tokyo), rule changes, indoor ice hockey, lighter clothing
- Athlete activism: fossil fuel sponsorship protest by women's football players; David Pocock (rugby → senator)
- 2026 World Cup expected to emit ~7.8 Mt CO2, mostly fan travel; Qatar 2022 emissions dominated by stadium construction
- Options: rotation of hosts, fewer events, smaller formats, sponsorship transition, calendar shift

---

## 2026-07-06 ingest | Beef and Climate Change — WRI Six-Question Explainer

**Source file:** `raw/articles/6 Pressing Questions About Beef and Climate Change, Answered.md`
**Original source:** World Resources Institute — Waite, Searchinger, Ranganathan & Zionts (updated March 2022, originally 2019) — https://www.wri.org/insights/6-pressing-questions-about-beef-and-climate-change-answered

**What was done:**
- Created source summary: `wiki/sources/wri-beef-6-questions-2022.md`
- Created new wiki page: `wiki/sectors/agriculture-food/beef-and-climate-change.md` (Article template, follows WRI's six-question structure but rewritten in European accessible tone)
- Updated `wiki/index.md` — added source entry and new agriculture-food page entry

**Key content added:**
- Beef emissions come from enteric fermentation (methane), manure (N2O), and land-use change (CO2)
- ~3 billion tonnes CO2-eq in 2010 (~7% of global GHG, comparable to India)
- Beef requires ~20× more land and emits ~20× more GHG per gram of protein than beans
- WRI target: ~50 calories/day (~1.5 burgers/week) in high-consuming countries would eliminate the need for further ag land expansion by 2050
- US per capita beef consumption already down one-third since 1970s but decline needs to be 1.5× faster
- Silvopasture (Colombia): quadrupled cows/acre, cut methane per kg
- Kenya dairy trials: 8–60% methane per litre of milk via napier grass + Calliandra
- Feed additives: 3-NOP, seaweed
- COP26 methane pledge (30% by 2030) + deforestation pledge both hinge on beef

---

## 2026-07-01 ingest | Ariana Mine and Santander — $100m Loan vs Lima's Water Supply

**Source files:**
- `raw/articles/Ariana copper and zinc mine.md` (BankTrack Dodgy Deal dossier)
- `raw/articles/Santander stop the Ariana mining project.md` (Ekō petition)

**Original sources:**
- BankTrack — https://www.banktrack.org/project/ariana_copper_and_zinc_mine (project dossier, accessed July 2026)
- Ekō, 19 June 2026 — https://action.eko.org/a/santander-stop-the-ariana-mining-project

**What was done:**
- Created source summary: `wiki/sources/ariana-mine-banktrack-2026.md`
- Created source summary: `wiki/sources/ariana-mine-eko-petition-2026.md`
- Created new wiki page: `wiki/climate-finance/ariana-mine-santander.md`
- Updated existing page: `wiki/climate-finance/fossil-fuel-banking.md` — added cross-reference in Connected Topics
- Updated `wiki/index.md` — added two source entries, new climate-finance page entry, bumped last-updated date

**Key content added:**
- Ariana is an underground copper/zinc mining project in Marcapomacocha (Junín, Peru) owned by Alpayana since 2025
- Site sits inside the Marcapomacocha water system supplying ~60% of Lima and Callao's dry-season drinking water (10+ million people)
- Water utility SEDAPAL flagged four impact pathways: reduced groundwater flows, heavy metal contamination, vibration damage to the Cuevas-Milloc Trans-Andean Tunnel, and possible tailings dam collapse 100 m from the tunnel
- Constitutional Chamber of Lima ruled in 2025 that the project is a "certain and imminent threat" to the right to drinking water; ordered a Complementary EIA
- Alpayana bought the project for US$200m in March 2025 (LXG Capital advised)
- Banco Santander refinanced Alpayana with **US$100m in August 2025**
- Peru has recorded 18 tailings dam ruptures since 1952, mostly seismic
- Ekō petition targets Santander's Executive Chairman Ana Botín; explicitly rebuts the "critical minerals for the energy transition" defence
- Framed as a non-fossil test of European bank environmental & human rights policies

---

## 2026-06-29 ingest | First Attribution of Antarctic Glacier Retreat to Human Activity (Pine Island)

**Source file:** `raw/articles/Human activity has driven retreat of Antarctica's fastest melting glacier.md`
**Original source:** Phys.org press release based on King's College London / British Antarctic Survey research, 28 June 2026 — https://phys.org/news/2026-06-human-driven-retreat-antarctica-fastest.html
**Peer-reviewed study:** *The Cryosphere* (2026), Bradley et al.

**What was done:**
- Created source summary: `wiki/sources/pine-island-glacier-attribution-2026.md`
- Updated existing page: `wiki/biodiversity-land/Glaciers in Retreat -  Facts, Risks, and What Can Be Done.md` — added "June 2026: first attribution of Antarctic glacier retreat to human activity" subsection under "Weakness in Antarctica"; added Phys.org / KCL source
- Updated `wiki/index.md` — added source entry; expanded Glaciers in Retreat description with the new finding

**Key content added:**
- First direct attribution of a major Antarctic outlet glacier's retreat to human emissions
- Greenhouse-gas-driven ocean warming increased Pine Island Glacier's retreat by 18–20% since the 1940s
- ~4 km of additional landward grounding-line retreat by 2015 (≈ one-fifth of total observed)
- Pine Island started retreating rapidly in the 1940s due to warm ocean intrusions; human warming reinforced the trend from the 1960s
- A bedrock ridge may briefly stabilise the glacier later this century, but the pause is temporary if warming continues
- Human influence projected to be the dominant driver of Pine Island retreat in the 22nd century
- Bradley: "Ice sheets respond slowly. The impacts of today's emissions will continue to shape Antarctic ice loss for centuries."

---

## 2026-06-29 ingest | Slough Datacentre Hub Adds a Local Heat Island

**Source file:** `raw/articles/'Slough is like an experiment' Europe's largest datacentre hub leaves town sweltering.md`
**Original source:** The Guardian, Aisha Down, 26 June 2026 — https://www.theguardian.com/environment/2026/jun/26/slough-is-like-an-experiment-europes-largest-datacentre-hub-leaves-town-sweltering
**Cambridge preprint cited:** Marinoni et al., 2026 — https://arxiv.org/pdf/2603.20897

**What was done:**
- Created source summary: `wiki/sources/slough-datacentre-heat-island-2026.md`
- Updated existing page: `wiki/sectors/digital/DRAFT - ai-data-centre-energy-crisis.md` — added "Slough: a hyperscale heat island" section; added Slough/Cambridge facts to the Key Facts list; updated frontmatter summary and date; added two new sources
- Updated `wiki/index.md` — added source entry; updated description for the ai-data-centre-energy-crisis page

**Key content added:**
- Slough hosts 30–40 large data centres totalling ~1 GW — Europe's largest hub; tenants include Amazon, Google, Oracle, Microsoft
- Cambridge preprint: data centres push up local temperatures by 2°C on average, up to 9°C; Slough not yet measured but "almost like an experiment by itself" because of its scale
- 24 June 2026: 36.7°C at the weather station nearest the tech park — several degrees hotter than other Slough stations
- Heat source is the cooling systems for AI chips; UK has proposed waste-heat district heating but most heat is currently vented
- Reinforces the case for stricter siting standards and waste-heat recovery

---

## 2026-06-29 ingest | Swiss Glaciers Hit Second-Earliest "Glacier Loss Day" on Record

**Source file:** `raw/articles/Swiss glaciers facing 'enormous' loss from heatwave.md`
**Original source:** RTÉ News / AFP, 27 June 2026 — https://www.rte.ie/news/2026/0627/1580624-glaciers-heatwave/

**What was done:**
- Created source summary: `wiki/sources/swiss-glaciers-heatwave-2026.md`
- Updated existing page: `wiki/biodiversity-land/Glaciers in Retreat -  Facts, Risks, and What Can Be Done.md` — added "June 2026: second-earliest glacier loss day on record" subsection under Melting in the Alps; corrected frontmatter tags to quoted hashtag form; updated date; added RTÉ/AFP source
- Updated `wiki/index.md` — added source entry; updated description for the Glaciers in Retreat page (and removed two now-stale entries for the deleted FACTS about Glacier page)

**Note:** The FACTS about Glacier page was deleted by the user shortly after the initial ingest. The Swiss glacier content was redirected to the existing comprehensive "Glaciers in Retreat" page in biodiversity-land instead.

**Key content added:**
- 30 June 2026: snow accumulated during winter 2025–26 fully melted away — only 2022 (26 June) was earlier in 25 years of records
- Three months earlier than a "healthy state"; average loss day this century is mid-August
- Rhone Glacier: 1 metre of vertical ice loss in just 10 days during the heatwave
- 25% less winter snowfall vs 2010–2020; March Saharan dust accelerated melt
- Swiss glaciers shrank 38% in volume between 2000 and 2024; 1,200 glaciers lost in 50 years; only ~1,300 remain
- If warming continues, only small remnants will exist by 2100
- Threatens summer flow of the Rhine and Rhone — major water supply for Europe

---

## 2026-06-29 ingest | FIFA President's Private Jet: 27 Flights, 516 Tonnes CO₂e in 16 Days

**Source file:** `raw/articles/World Cup 2026 How Fifa president Gianni Infantino is jetting around.md`
**Original source:** BBC Verify / BBC Sport, Jake Horton et al., 28 June 2026 — https://www.bbc.com/sport/football/articles/cgev5wy0zg3o
**Source summary created:** `wiki/sources/infantino-private-jet-bbc-2026.md`
**Wiki pages updated:**
- `wiki/sectors/Environmental Impact of football world cups.md` — added "The President's Jet: A Case Study in Leadership Failure" section with full data: 27 flights, 31,144 miles, 516 tonnes CO₂e, equivalent to 78 people's annual footprint; updated frontmatter summary and date; added BBC Verify source

---

## 2026-06-29 ingest | UK Heatwave June 2026: First Ever Three Consecutive Red Warnings

**Source file:** `raw/articles/Climate sceptics cheering as they melt in record temperatures? This heatwave is where satire has come to die.md`
**Original source:** The Guardian (comment), Jonathan Freedland, 26 June 2026 — https://www.theguardian.com/commentisfree/2026/jun/26/climate-sceptics-record-temperatures-heatwave-ed-miliband-net-zero
**Source summary created:** `wiki/sources/uk-heatwave-june-2026-guardian.md`
**Wiki pages updated:**
- `wiki/climate-science/wildfires-climate-feedback.md` — added "June 2026: Record Heat Reaches Temperate Europe" section documenting UK's first-ever three consecutive red heat warnings, 35°C+, Derbyshire wildfire, and European 40°C heat; updated frontmatter summary and date
- `wiki/concepts/key-ideas/Greenwashing.md` — added "Political Denial as Greenwashing: The Anti-Woke Davos (June 2026)" example documenting fossil-fuel-backed conference attacking climate policy while delegates sweltered in 35°C+ heat

---

## 2026-06-28 ingest | Ireland Data Centre Boom — 107 Facilities, €18.5bn Invested

**Source file:** `raw/articles/Data-centre boom sees 107 facilities now operating in Ireland, with €18.5bn invested.md`
**Original source:** Irish Independent, John Burns, 26 June 2026 — https://www.independent.ie/irish-news/data-centre-boom-sees-107-facilities-now-operating-in-ireland-with-18.5bn-invested/a/157776762.html

**What was done:**
- Created source summary: `wiki/sources/ireland-datacentre-boom-2026.md`
- Updated existing page: `wiki/ireland-hub/DRAFT - IRELAND Data Centre Dilemna.md` — added "The Scale of the Sector (June 2026)" section with latest Bitpower figures and new CRU policy; updated frontmatter summary and date
- Updated `wiki/index.md`

**Key content added:**
- 107 data centres operating in Ireland (up from ~82); 9 under construction; 43 with planning permission
- Combined IT load: 1.3 GW; hyperscalers = ~75% of capacity; total investment €18.5bn
- EirGrid median forecast: 31% of national electricity by 2034 (up from 22% in 2024)
- CRU moratorium lifted December 2025; new rules: 80% renewables + energy neutral after 6 years
- Three environmental groups challenging new rules in High Court over six-year fossil fuel window
- AI hardware imports from Taiwan quadrupled in six months (€0.5bn → €2.2bn)

---

## 2026-06-28 ingest | Quantum Computer Mines Cryptocurrency With 100× Less Energy

**Source file:** `raw/papers/Crypto-Quantum.pdf`
**Original source:** New Scientist, Karmela Padavic-Callaghan, 12 June 2026 (updated 24 June 2026)

**What was done:**
- Created source summary: `wiki/sources/crypto-quantum-newscientist-2026.md`
- Updated existing page: `wiki/sectors/digital/Cryptocurrency and the environment.md` — added "2026 Update: Can Quantum Computing Clean Up Crypto Mining?" section; updated frontmatter summary and date
- Updated `wiki/index.md`

**Key content added:**
- D-Wave Advantage2 quantum computer mining Quip experimental blockchain (Postquant Labs)
- Uses optimisation proof-of-work problem rather than brute-force — suited to quantum machines
- Wins 92% of blocks it competes for (available only ~5 min/day); uses 12.5W vs 1,334W for conventional machine (~100× less power)
- A conventional machine to beat it would need ~300× the power
- Quip designed quantum-safe; most existing blockchains are not
- Caution: capital/manufacturing costs of quantum hardware may offset per-computation energy gains
- Longer-term vision: distributed worldwide quantum computer network via Quip

---

## 2026-06-28 ingest | Wildlife Thrives in Solar Farm Built on Restored Peatland

**Source file:** `raw/papers/nS-solar.pdf`
**Original source:** New Scientist, Alec Luhn, 8 June 2026 (updated 23 June 2026)
**Peer-reviewed study:** Ecological Solutions and Evidence, Hanna Rae Martens et al. — DOI: 10.1002/2688-8319.70259

**What was done:**
- Created source summary: `wiki/sources/solar-peatland-newscientist-2026.md`
- Created new wiki page: `wiki/biodiversity-land/solar-on-peatland.md`
- Updated existing page: `wiki/biodiversity-land/The importance of Wetlands.md` — added "Solar farms on rewetted peatland" section with link to new page; updated frontmatter summary and date
- Updated `wiki/index.md`

**Key content added:**
- Solar farm on rewetted peatland (Wattmanufactur, 30 ha, northern Germany) found to host more diverse bird species than nearby hay fields
- Wetland and woodland species attracted (white wagtail, reed bunting, grey heron, kestrel, buzzard); threatened meadow pipit also recorded
- Peatlands hold twice as much carbon as all forests; 95% of German and 80% of UK peatlands degraded
- Critical distinction: solar on drained (not rewetted) peat can release more GHGs than it displaces — some of 165 German peatland solar farms are net emitters
- Only 5 solar farms in Germany currently on rewetted peatland
- UK has restored only 2,500 km² — one-tenth of damaged area; Germany less
- Government incentives needed to scale peatland PV beyond pilot sites

---

## 2026-06-26 ingest | Greater Dublin Water Supply on a "Knife Edge"

**Source file:** `raw/articles/Greater Dublin water supply 'on knife edge', cttee told.md`
**Original source:** RTÉ News, Juliette Gash, 24 June 2026 — https://www.rte.ie/news/2026/0624/1580174-shannon-dublin-water/

**What was done:**
- Created source summary: `wiki/sources/dublin-water-supply-shannon-2026.md`
- Updated existing page: `wiki/ireland-hub/DRAFT - IRELAND Water Usage and Water Management.md` — added "Dublin Water Supply on a Knife Edge" section; updated frontmatter summary and updated date
- Updated `wiki/index.md`

**Key content added:**
- Greater Dublin water demand cannot be met sustainably without the Water Supply Project (Shannon diversion)
- Project: 2% of Shannon annual flow from Parteen Basin, piped east; supports up to 50% of Ireland's population
- Planning application submitted to An Coimisiún Pleanála, December 2025
- 80% of landowners along route have signed voluntary agreements; CPO available for remainder
- Dublin leakage reduced from 37% to 29%; parallel, not sequential, approach to leakage and new supply
- Lough Derg and Parteen Basin water levels and recreation unaffected

---

## 2026-06-26 skip | Food waste... blending 1.md

**Source file:** `raw/articles/Food waste can become jet fuel through simpler refining and 50-50 blending 1.md`

**Decision:** Skipped. Exact duplicate of `raw/articles/Food waste can become jet fuel through simpler refining and 50-50 blending.md`, which was ingested on 2026-06-23. Same source URL, same content, different creation timestamp only.

---

## 2026-06-23 ingest | Food Waste Can Become Jet Fuel

**Source file:** `raw/articles/Food waste can become jet fuel through simpler refining and 50-50 blending.md`
**Original source:** TechXplore, Marianne Stein, 22 June 2026 — https://techxplore.com/news/2026-06-food-jet-fuel-simpler-refining.html
**Peer-reviewed study:** Nature Sustainability, Buchun Si et al., 2026 — DOI: 10.1038/s41893-026-01848-1

**What was done:**
- Created source summary: `wiki/sources/food-waste-saf-illinois-2026.md`
- Updated existing page: `wiki/solutions/electrification/Sustainable Aviation Fuel - A Necessary but Complicated Solution.md` — added new section "New Feedstock Pathway: Food Waste as Jet Fuel"; updated frontmatter summary and updated date
- Updated `wiki/index.md`

**Key content added:**
- University of Illinois team converts food waste to SAF via hydrothermal liquefaction (HTL) + distillation-focused refining
- Simpler, lower-cost process than heavy catalytic refining; fuel quality lower but blendable
- 50-50 blend with conventional jet fuel meets ASTM/FAA standards; 10-20% blends also feasible
- Biggest bottleneck: logistics of collecting food waste from landfills and wastewater plants
- HTL works with treated wastewater as feedstock
- Lifecycle analysis: negative carbon emissions in both baseline and improved scenarios
- Still at small lab scale; next step is diesel engine tests, then jet engine tests

---

## 2026-06-22 ingest | Formula 1 Sustainability — On Track for Net Zero by 2030

**Source file:** `raw/articles/Formula 1 Sustainability changes put sport on track for net zero emissions by 2030.md`
**Original source:** BBC Sport, Andrew Benson, 17 June 2026 — https://www.bbc.com/sport/formula1/articles/cvgjp4rj2p5o

**What was done:**
- Created source summary: `wiki/sources/f1-sustainability-bbc-2026.md`
- Created new wiki page: `wiki/sectors/formula-1-sustainability-2026.md`
- Updated `wiki/index.md`

**Key content added:**
- Total CO₂ emissions: 228,793 tonnes (2018) → 148,805 tonnes (2025) — 35% reduction; 12% year on year
- Factory and facilities emissions down 64% vs 2018
- Logistics emissions down 21% year on year, 29% since 2018
- From 2026: sustainable fuels mandatory in races (80% fewer GHG vs fossil-fuel comparator)
- Calendar geographic clustering (e.g. Japan/Australia/China in spring) cuts freight and travel
- Net Zero by 2030 commitment = minimum 50% absolute reduction; remaining emissions offset

---

## 2026-06-22 ingest | Ireland 'Exposed' Over Fossil Fuels for Transport

**Source file:** `raw/articles/Ireland 'exposed' over use of fossil fuels for transport.md`
**Original source:** RTÉ News, Aaron McElroy, 17 June 2026 — https://www.rte.ie/news/ireland/2026/0617/1578833-climate-change-review/

**What was done:**
- Created source summary: `wiki/sources/ireland-transport-ccac-2026.md`
- Updated existing page: `wiki/ireland-hub/DRAFT - IRELAND Transport Emissions.md` — added 2026 CCAC Annual Review section; updated frontmatter tags and summary
- Updated `wiki/index.md`

**Key content added:**
- CCAC 2026 Annual Review: fossil fuel transport dependence leaves Ireland exposed to repeated price shocks
- TFI journeys +6%, Local Link +19% in 2025; but total public transport journeys largely unchanged (capacity constraints)
- Projects needed: DART+ South West, Luas Finglas, NTA Park and Ride
- CCAC calls for targeted support for lower-income, car-dependent households
- EV scrappage scheme welcomed; real-time charging maps needed

---

## 2026-06-22 ingest | No Improvement to Water Quality Standards in 2025

**Source file:** `raw/articles/No improvement to water quality standards in 2025.md`
**Original source:** RTÉ News, Pat McGrath, 17 June 2026 — https://www.rte.ie/news/environment/2026/0617/1578808-water-quality-report/

**What was done:**
- Created source summary: `wiki/sources/ireland-water-quality-epa-2026.md`
- Updated existing page: `wiki/ireland-hub/DRAFT - IRELAND Water Usage and Water Management.md` — added 2026 EPA water quality section; updated frontmatter tags and summary
- Updated `wiki/index.md`

**Key content added:**
- EPA 2025 water quality indicators: no major improvement achieved
- 43% of rivers have excess nitrates (east and south-east worst affected)
- Over 30% of lakes have excess phosphorous (border region worst)
- Just over half of rivers and lakes in good or better biological quality
- More rivers declined in quality class than improved in 2025
- Local success: six of 16 rivers in Ballyteigue Bannow, Co Wexford, improved in 2025

---

## 2026-06-22 ingest | Ranked: Europe's Most Forested Countries

**Source file:** `raw/articles/Ranked Europe's Most Forested Countries.md`
**Original source:** Visual Capitalist, Srijaa Chatterjee, 10 June 2026 — https://www.visualcapitalist.com/cp/europes-most-forested-countries/

**What was done:**
- Created source summary: `wiki/sources/europe-forested-countries-2026.md`
- Updated existing page: `wiki/biodiversity-land/Forests and Land - Our Most Important Carbon Sink.md` — added "Forest Cover Across Europe" section with State of Europe's Forests 2025 findings; updated sources
- Updated `wiki/index.md`

**Key content added:**
- Finland leads Europe at ~73% forest cover; Sweden close behind; Montenegro and Slovenia in top tier
- Iceland, Ireland, and UK have some of the lowest forest shares in Europe
- State of Europe's Forests 2025: European forest area expanding overall, but growth rates slowing
- EEA: forest resilience becoming critical policy issue as temperatures rise

---

## 2026-06-22 ingest | 'Forgotten' Pollutants Cause 15% of Global Warming

**Source file:** `raw/articles/'Forgotten' pollutants cause 15 per cent of global warming.md`
**Original source:** New Scientist, Alec Luhn, 11 June 2026 — https://appuk.newscientist.com/2026/06/11/2530049/content.html
**Peer-reviewed study:** Science, DOI: 10.1126/science.aee5790

**What was done:**
- Created source summary: `wiki/sources/indirect-greenhouse-gases-newscientist-2026.md`
- Created new wiki page: `wiki/climate-science/indirect-greenhouse-gases.md`
- Updated `wiki/index.md`

**Key content added:**
- Carbon monoxide, VOCs, and black carbon have caused ~15% of all warming since pre-industrial times — double the contribution of N₂O
- Together they have caused ~0.3°C of warming
- Mechanism: form low-level ozone + consume hydroxyl radicals that would otherwise break down methane
- Break down within hours to years — cutting them would quickly slow the rate of warming
- Almost no country includes them in Paris Agreement action plans
- Hydrogen transition risk: leakage could add 0.1°C by 2100 if combustion replaces batteries at scale
- Key researchers: Ilissa Ocko (Spark Climate Solutions), Alex Archibald (Cambridge), Alastair Lewis (York)

---

## 2026-06-15 ingest | AMOC Monitoring Under Threat

**Source file:** `raw/articles/Amoc collapse could change Europe's climate 10x faster than expected. We aren't ready.md`
**Original source:** The Guardian, Penny Holliday, Femke de Jong, Sjoerd Groeskamp, 14 June 2026 — https://www.theguardian.com/commentisfree/2026/jun/14/amoc-collapse-europe-climate

**What was done:**
- Created source summary: `wiki/sources/amoc-monitoring-guardian-2026.md`
- Updated existing page: `wiki/climate-science/amoc-collapse-carbon.md` — added new section "AMOC Monitoring Under Threat"; updated summary keywords and sources
- Updated `wiki/index.md`

**Key content added:**
- AMOC collapse could change Europe's climate 10× faster than the current rate
- Trump administration cuts to NASA, NOAA, NSF = ~50% of total AMOC monitoring budget
- US descoped Ocean Observatories Initiative (June 2026)
- EU OceanEye initiative: €50m committed but not yet operational
- Total AMOC monitoring cost: ~€25m/year (5 cents per EU citizen)
- Authors urge EU, UK, and international partners to fund long-term monitoring before continuity is broken

---

## 2026-06-15 ingest | Activists Push to Create a Climate Nobel Prize

**Source file:** `raw/articles/Activists push to create first-ever Climate Nobel Prize '$1M is ready to go if the Nobel Committee agrees'.md`
**Original source:** Good Good Good, Kamrin Baker, 11 December 2025 — https://www.goodgoodgood.co/articles/nobel-prize-in-climate-and-planetary-health-ecosia

**What was done:**
- Created source summary: `wiki/sources/climate-nobel-prize-ecosia-2025.md`
- Created new wiki page: `wiki/concepts/climate-nobel-prize.md`
- Updated `wiki/index.md`

**Key content added:**
- Ecosia CEO Christian Kroll notarised €1m commitment for the first prize endowment
- Proposal: 7th Nobel category — Climate and Planetary Health
- Three recognition areas: Pragmatic Governance, Scaling Prosperity and Markets, Building Common Ground
- Backed by Luisa Neubauer and Dr Claudia Kemfert
- Ecosia would have no influence over nominations or laureates

---

## 2026-06-15 ingest | SBTi Sets New Rules for Corporate Net Zero

**Source file:** `raw/articles/Climate Standard Setter SBTi Sets New Rules for Companies Seeking Net Zero.md`
**Original source:** Wall Street Journal, Yusuf Khan, 11 June 2026 — https://www.wsj.com/pro/sustainable-business/climate-standard-setter-sbti-sets-new-rules-for-companies-seeking-net-zero-43a38733

**What was done:**
- Created source summary: `wiki/sources/sbti-net-zero-rules-2026.md`
- Created new wiki page: `wiki/standards-labels/sbti-science-based-targets.md`
- Updated `wiki/index.md`

**Key content added:**
- SBTi 2026 update allows market-based environmental credits (SAF credits, RECs) for target-setting
- Carbon removals (DAC, reforestation credits) allowed from 2035 for hard-to-abate residual emissions
- PPAs now count; local preferred, cross-regional allowed if structural barriers exist
- Hourly electricity matching preferable but not mandated; tech companies must report hourly share
- Framed as "best-efforts framework" — recognising companies don't control everything

---

## 2026-06-15 ingest | Welcome to the Most Polluting Games Ever

**Source file:** `raw/articles/Welcome to the most polluting games ever.md`
**Original source:** We Don't Have Time, Markus Lutteman, June 2026 — https://app.wedonthavetime.org/posts/44991735-7f37-43f6-bca2-c677af540e95

**What was done:**
- Created source summary: `wiki/sources/world-cup-most-polluting-wdht-2026.md`
- Updated existing page: `wiki/sectors/Environmental Impact of football world cups.md` — added FIFA sportswashing section; updated frontmatter summary and sources
- Updated `wiki/index.md`

**Key content added:**
- University of Manchester: 2026 World Cup could be most polluting ever
- Queen's University Belfast: 14 of 16 venues exceed safety thresholds (heat, flooding, rain)
- FIFA signed 4-year deal with Saudi Aramco in 2024; Aramco CEO called phasing out oil "a fantasy"
- SGR research: Aramco sponsorship could induce additional 30 million tonnes CO₂e in 2026
- Dr Oscar Berglund (Bristol): "FIFA has made elite men's football the primary target of petrostate sportswashing"
- 2034 World Cup awarded to Saudi Arabia
- UK: matches increasingly cancelled due to flooding; winters projected 30% wetter by 2070

---

## 2026-06-15 ingest | Are Manure Digesters a Real Solution to Dairy Farm Emissions?

**Source file:** `raw/papers/New Scientist 3.pdf`
**Original source:** New Scientist, Alec Luhn, 7 April 2026 (updated 20 May 2026) — Environmental Research Letters, DOI: 10.1088/1748-9326/ae4fe4

**What was done:**
- Created source summary: `wiki/sources/manure-digesters-newscientist-2026.md`
- Updated existing page: `wiki/solutions/carbon-removal/Methane Digester - Project Drawdown 28.md` — added "2026 Update: The Limits of Digesters" section; updated frontmatter (title, tags, summary, sources)
- Updated `wiki/index.md`

**Key content added:**
- California study of 98 dairies: digesters cut point-source methane 91→68 kg/h at 2/3 of farms
- Some leaks exceeded 1,000 kg/h — turning those digesters into net emitters
- California Low Carbon Fuel Standard incentives increased dairy herd size by 860 cows on average
- Digesters accelerate ammonia formation — "pollution swapping" concern
- Overall bulk of research: well-run digesters can cut manure emissions by roughly half
- Brent Kim (Johns Hopkins): "taxpayer dollars are being used to inflate the value of manure"

---

## 2026-06-12 ingest | A Patagonia Story

**Source file:** `raw/own-research/a Patagonia story.md`
**Original source:** Own research by Fabien Mossière

**What was done:**
- Filed directly (own-research — no summarising): `wiki/concepts/company-evaluations/patagonia-story.md`
- Added standard frontmatter, editorial summary, and relative markdown links
- Updated `wiki/index.md`

**Key content:**
- Yvon Chouinard's journey from Californian climbing obsession to global outdoor brand
- 1972: stopped making pitons (his best-selling product) to protect rock faces — first act of putting planet before profit
- One Percent for the Planet (founded 1986); switch to organic cotton 1994; repair culture; "Don't Buy This Jacket" 2011
- 2017: Patagonia sued Trump over shrinking of Utah national monuments; protections restored in 2021
- 2022: gave entire company to an environmental trust — ~$100m/year in profit now goes to environmental causes
- Honest acknowledgement of contradictions: still manufactures in low-cost countries, faces greenwashing criticism

---

## 2026-06-12 ingest | Greenwashing, illegality and false claims: 13 climate litigation wins in 2025

**Source file:** `raw/articles/Greenwashing, illegality and false claims 13 climate litigation wins in 2025.md`
**Original source:** The Guardian, Isabella Kaminski, 31 December 2025 — https://www.theguardian.com/environment/2025/dec/31/greenwashing-illegality-false-claims-climate-litigation-wins-2025

**What was done:**
- Created source summary: `wiki/sources/climate-litigation-wins-2025.md`
- Updated existing page: `wiki/concepts/key-ideas/Greenwashing lawsuits on the rise.md` — added 2025 litigation section with 13 key wins; updated frontmatter tags and summary
- Updated `wiki/index.md`

**Key content added:**
- Rosebank and Jackdaw North Sea fields ruled illegal in the UK (scope 3 emissions not assessed)
- TotalEnergies convicted of greenwashing in France
- Apple Watch "carbon neutral" claim banned in Germany; dropped worldwide
- JBS ($1.1m settlement) and Tyson (dropped net zero claims) in the US
- EnergyAustralia settled — acknowledged offsets do not undo GHG damage
- Three Norwegian oilfields declared unlawful
- NSW coalmine expansion blocked on scope 3 grounds
- ICJ advisory opinion: states must prevent harm to the climate system
- UK forced to publish stronger climate delivery plan

---

## 2026-06-12 ingest | World's largest banks pledged $906bn to fossil fuel companies in 2025

**Source file:** `raw/articles/World's largest banks pledged $906bn to fossil fuel companies in 'unfathomable' increase in 2025, report finds.md`
**Original source:** The Guardian, Oliver Milman, 9 June 2026 — https://www.theguardian.com/environment/2026/jun/09/world-banks-pledge-billions-fossil-fuel-industry-2025

**What was done:**
- Created source summary: `wiki/sources/banking-on-climate-chaos-2025.md`
- Created new wiki page: `wiki/climate-finance/fossil-fuel-banking.md`
- Updated `wiki/index.md`

**Key content added:**
- $906bn committed by 65 largest banks to fossil fuels in 2025, up 8% on 2024
- $8.7 trillion total since the Paris Agreement (2015–2025)
- JPMorgan Chase leads at $58bn; Bank of America, MUFG, Mizuho, Citigroup follow
- $508bn for fossil fuel expansion specifically, up 27%
- "Dirty dozen" banks responsible for 40% of all industry fossil fuel funding
- Net-Zero Banking Alliance (UN-backed) disbanded in 2025 after mass departures
- 26 of 65 banks reduced fossil fuel financing; BNP Paribas, UBS, La Caixa led reductions

---

## 2026-06-12 ingest | Seaqual removes plastic from the Ocean and turns it into fashion

**Source file:** `raw/own-research/Seaqual removes plastic from the Ocean and turn it into fashion.md`
**Original source:** Own research by Fabien Mossière

**What was done:**
- Filed directly (own-research — no summarising): `wiki/circularity-waste/seaqual-ocean-plastic-fashion.md`
- Added standard frontmatter, editorial summary, and relative markdown links
- Updated `wiki/index.md`

**Key content:**
- Seaqual Initiative: industrial-scale marine plastic upcycling founded 2016 in Spain (Antex, Textil Santanderina, Ecoalf)
- SEAQUAL® YARN = 10% upcycled marine plastic + 90% land-based rPET (engineering constraint due to degraded marine polymer)
- LCA: 37% reduction in GWP vs virgin PET; identical to standard post-consumer rPET
- Sourcing from Spain/Mediterranean (PA6 fishing nets), North Africa, Latin America, Vietnam (PET bottles)
- Traceability via DNA tracers + AWARE blockchain system; certified GRS + Oeko-Tex
- SEAQUAL® YARN T2T: next-gen textile-to-textile chemical recycling
- Brand take-back programmes: Isomi, Duvaltex, Burlington Restora, Wetheknot

---

## 2026-06-12 ingest | Extreme weather in 2025 drove record wildfire emissions in Europe + Arctic fires releasing ancient carbon

**Source files:**
- `raw/papers/New Scientist 2.pdf` (contains both articles)
- `raw/papers/Artic-Fires.pdf` (companion file for the Arctic fires article)

**Original sources:**
- New Scientist, Alec Luhn, 29 April 2026 (updated 15 May 2026): Europe wildfires
- New Scientist, Michael Le Page, 13 May 2026 (updated 30 May 2026): Arctic fires

**What was done:**
- Created source summary: `wiki/sources/europe-wildfires-2025-newscientist.md`
- Created source summary: `wiki/sources/arctic-fires-ancient-carbon-2026.md`
- Created new wiki page: `wiki/climate-science/wildfires-climate-feedback.md` (covers both articles)
- Updated `wiki/index.md`

**Key content added:**
- Europe: fastest-warming continent, warming 2× global average; 2025 hottest year on record in UK, Iceland, Norway
- 3-week Arctic heatwave reaching 30°C inside the Arctic circle (typically 0–2 heat-stress days per year)
- European wildfires emitted 47 million tonnes of carbon in 2025 — a record
- Portugal and Spain fires made at least 40× more likely by climate change; 10,000+ sq km burned
- Arctic/boreal fires burning peat carbon up to 5,000 years old — not captured by climate models
- Smouldering of ancient soil organic matter releases CO₂ and black carbon (soot)
- Black carbon darkens ice/snow, accelerating melt
- Climate models systematically underestimate wildfire emissions

## 2026-06-12 skip | _TEMPLATE.md

**Source file:** `raw/articles/_TEMPLATE.md`

**Decision:** Skipped. File is an article clipping template, not content to ingest.

---

## 2026-06-11 ingest | Airline industry chiefs say 2050 net zero goal now unlikely

**Source file:** `raw/articles/Airline industry chiefs say 2050 net zero goal now unlikely.md`
**Original source:** The Guardian, Gwyn Topham, 8 June 2026 — https://www.theguardian.com/environment/2026/jun/08/airline-industry-chiefs-willie-walsh-2050-net-zero-unlikely

**What was done:**
- Created source summary: `wiki/sources/iata-netzero-unlikely-2026.md`
- Updated existing page: `wiki/sectors/transport/FACTS about Air Travel.md` — added 2026 Update section with IATA summit admission
- Updated `wiki/index.md`

**Key content added:**
- IATA boss Willie Walsh: 2050 net zero pledge "probably not now be achieved"
- SAF at 0.8% of airline fuel needs in 2026; target is 65% by 2050
- ICAO 5% reduction by 2030 via SAF: "no path to meet that outcome"
- CORSIA being "undermined" by government inaction
- UK just met 2% SAF minimum in 2025, mostly imported recycled cooking oil — no e-SAF at scale

---

## 2026-06-11 ingest | World Cup heat (two articles + podcast)

**Source files:**
- `raw/articles/Extreme Heat Breaks - The Climate story behind the 2026 World Cup.md`
- `raw/articles/Volatile summer weather threatens to turn World Cup into test of heat.md`

**Original sources:**
- Outrage+Optimism podcast, June 2026
- Reuters, Angelica Medina and Janina Rios, 10 June 2026 — https://www.reuters.com/business/environment/volatile-summer-weather-threatens-turn-world-cup-into-test-heat-2026-06-10/

**What was done:**
- Created source summary: `wiki/sources/world-cup-heat-outrage-optimism-2026.md`
- Created source summary: `wiki/sources/world-cup-heat-reuters-2026.md`
- Updated and completed existing draft: `wiki/sectors/Environmental Impact of football world cups.md` — fixed frontmatter, added heat impacts section
- Updated `wiki/index.md` — added Sport section and page entry

**Key content added:**
- Mandatory three-minute hydration breaks in every half: first time in football history
- Climate Central: climate change increased performance-impairing heat risk at 97 of 104 matches
- Heat risk at 2026 World Cup is twice that of the 1994 World Cup in the same country
- A quarter of matches projected in conditions exceeding recommended safety limits
- WBGT above 28°C linked to declines in sprinting, distance, and recovery
- NJ Transit surge-priced return tickets to MetLife Stadium to $150 (from under $15)
- "Climate change is now outpacing athletes' ability to adapt" — Christiana Figueres

---

## 2026-06-11 ingest | 'Severe' stress on oceans as rate of sea level rise doubles, UN warns

**Source file:** `raw/articles/'Severe' stress on oceans as rate of sea level rise doubles in 10 years, UN warns.md`
**Original source:** The Guardian, Karen McVeigh, 8 June 2026 — https://www.theguardian.com/environment/2026/jun/08/un-world-ocean-assessment-severe-stress-sea-level-rise-doubles-pollution-fishing-climate

**What was done:**
- Created source summary: `wiki/sources/un-world-ocean-assessment-2026.md`
- Updated existing page: `wiki/biodiversity-land/FACTS about the Ocean.md` — added 2026 Update section
- Updated `wiki/index.md`

**Key content added:**
- Sea level rise rate doubled: 2mm/year (pre-2015) to 4.3mm/year (2023)
- 16% of all ocean heat absorbed since 1955 happened after 2018
- 52.1 million tonnes of plastic enter the ocean annually; 24.4 trillion microplastic particles
- Only 27% of ocean floor mapped by 2025
- High seas treaty came into force 2026 — protection for two-thirds of global ocean
- Ocean governance described as "fragmented"

---

## 2026-06-11 ingest | What floats and what sinks — ocean-based climate solutions

**Source file:** `raw/articles/What floats and what sinks when it comes to ocean-based climate solutions?.md`
**Original source:** Project Drawdown, Christina Richardson PhD, 2 June 2026 — https://drawdown.org/insights/what-floats-and-what-sinks-when-it-comes-to-ocean-based-climate-solutions

**What was done:**
- Created source summary: `wiki/sources/drawdown-ocean-climate-solutions-2026.md`
- Created new wiki page: `wiki/biodiversity-land/ocean-based-climate-solutions.md`
- Updated `wiki/index.md`

**Key content added:**
- Offshore wind: 1.90–3.04 Gt CO₂-eq/year — top ocean climate solution
- Coastal wetlands + seaweed protection: 0.21–0.30 Gt CO₂-eq/year combined
- All other ocean actions: under 0.1 Gt CO₂-eq/year each
- Ocean biomass sinking, artificial upwelling, ocean fertilisation: not recommended
- Ocean protection funding: ~$1.2bn/year vs ~$16bn/year needed for 30x30
- Highest-impact climate actions are still mostly on land (solar, wind, diet, forests)

---

## 2026-06-11 ingest | Wealthy people with environmental ideals are the biggest emitters

**Source file:** `raw/papers/Wealthy people with environmental ideals are the biggest emitters.pdf`
**Original source:** New Scientist, Alec Luhn — research by Malte Dewies and Micha Kaiser, University of Cambridge

**What was done:**
- Created source summary: `wiki/sources/wealthy-biggest-emitters-newscientist.md`
- Created new wiki page: `wiki/concepts/behavior-change/high-income-carbon-paradox.md`
- Updated `wiki/index.md`

**Key content added:**
- Top 30% by socioeconomic status: high-income environmentalists emit more than high-income peers
- Main driver: frequent flying by people with international social networks
- BP popularised the term "carbon footprint" to shift responsibility from producers to consumers
- Conclusion: policy intervention beats attitude campaigns for reducing emissions

---

## 2026-06-11 ingest | Collapse of key ocean current may release billions of tonnes of carbon (New Scientist.pdf)

**Source file:** `raw/papers/New Scientist.pdf`
**Original source:** New Scientist, Alec Luhn, 13 April 2026 — Nature Communications Earth & Environment, DOI: 10.1038/s43247-026-03427-w

**What was done:**
- Created source summary: `wiki/sources/amoc-collapse-carbon-newscientist-2026.md`
- Created new wiki page: `wiki/climate-science/amoc-collapse-carbon.md`
- Updated `wiki/index.md`
- Note: New Scientist.pdf also contained the "Wealthy people" article (see entry above); that article was ingested from its standalone PDF.

**Key content added:**
- AMOC (includes Gulf Stream) has already declined ~15% due to Greenland meltwater
- Modelling: AMOC collapse would trigger Southern Ocean convection, releasing up to 640 billion tonnes of CO₂
- Additional warming from this carbon release: 0.2°C, over 1,000+ years
- AMOC collapse irreversible above 350 ppm CO₂ — current level is 430 ppm
- AMOC collapse would cool Arctic by 7°C and warm Antarctica by 6°C simultaneously
- East Antarctic Ice Sheet at risk, threatening metres of sea level rise
- Rockström: "The commitment time may be within the next 25 to 50 years. It's literally now."

---

## 2026-06-11 skip | Can you please translate the following in engllis....md

**Source file:** `raw/articles/Can you please translate the following in engllis....md`

**Decision:** Skipped. File contains only a Google Docs iframe with no substantive content. Not an article.

---

## 2026-06-06 ingest | Lab-Grown Meat — Revolution or Distant Promise?

**Source file:** `raw/own-research/Lab-Grown Meat -  Revolution or Distant Promise.md`
**Original source:** Own research by Fabien Mossière

**What was done:**
- Filed directly (own-research — no summarising): `wiki/sectors/agriculture-food/lab-grown-meat.md`
- Added standard frontmatter and linked to related wiki pages
- Updated `wiki/index.md` — added new page entry

**Key content:**
- Lab-grown meat science: bioreactor process, no slaughter required
- Livestock = 12% of global GHG, 75% of agricultural land, 500–700 L water per kg of beef
- 2023 University of California study: industrial cultured meat could emit 4–25× more than conventional beef due to energy-intensive purification
- Cost still ~€90/kg vs a future floor of €4–20/kg; investment fell 78% in 2023
- Only 4 territories have approved cultured meat: Singapore, US, Israel, UK (pet food only)
- Plant-based market now worth ~€10bn/year globally and more immediately scalable

---

## 2026-06-06 ingest | Why Everyone Keeps Talking About Bees

**Source file:** `raw/own-research/Why Everyone Keeps Talking About Bees.md`
**Original source:** Own research by Fabien Mossière

**What was done:**
- Filed directly (own-research — no summarising): `wiki/biodiversity-land/why-bees-matter.md`
- Added standard frontmatter and linked to related wiki pages
- Updated `wiki/index.md` — added new page entry

**Key content:**
- 1 in 3 bites of food depends on pollinators; bees are the most important
- 20,000+ bee species; 90%+ are solitary — not the managed honeybee at risk
- Corporate rooftop hives often harm wild bees by outcompeting them for scarce forage
- Focus on habitat (wildflower patches, bee hotels, reduced pesticide) rather than honey production
- EU Pollinators Initiative and Nature Restoration Regulation set legally binding 2030 targets

---

## 2026-06-06 ingest | Average person eats six times more chicken than in 1961, UN report finds

**Source file:** `raw/articles/Average person eats six times more chicken than in 1961, UN report finds.md`
**Original source:** The Guardian, Ajit Niranjan, 5 June 2026 — https://www.theguardian.com/environment/2026/jun/05/global-meat-supply-chicken-pork-fao-report

**What was done:**
- Created source summary: `wiki/sources/fao-global-meat-supply-2026.md`
- Updated existing page: `wiki/sectors/agriculture-food/agriculture-planetary-footprint.md` — added FAO 2026 data on global meat supply trends and expert criticism of FAO's failure to recommend reduction
- Updated `wiki/index.md`

**Key content added:**
- Global meat supply rose from 25 kg/person (1961) to 47 kg (2022) — a fourfold increase
- Poultry: 3 kg → 17 kg per person (6× increase); pork doubled; beef held steady at 9 kg
- Agricultural emissions forecast to rise 7.6% in the next decade; livestock = 80% of that increase
- ~14% of meat and milk is lost or wasted before consumption
- Scientists criticised FAO for not recommending meat reduction in wealthy countries

---

## 2026-06-06 ingest | Mangrove forests are healing after decades of human destruction

**Source file:** `raw/articles/Mangrove forests are healing after decades of human destruction.md`
**Original source:** BBC News, Matt McGrath and Esme Stallard, 5 June 2026 — https://www.bbc.com/news/articles/cn4pk07npvvo

**What was done:**
- Created source summary: `wiki/sources/mangrove-recovery-2026.md`
- Created new wiki page: `wiki/biodiversity-land/mangrove-forests-recovery.md`
- Updated `wiki/index.md`

**Key content added:**
- Since 2010, the world gains more mangroves than it loses — net historical loss reduced to ~849 sq km
- 1980s–2010: over 12,000 sq km cleared across Asia, Africa, the Americas (area of Jamaica)
- Natural regeneration — not active planting — is the main driver once clearing stops
- Closed-canopy (most carbon-dense) mangroves up 20% since 1980s
- Mangroves store 5× more carbon per hectare than land forests; protect coasts from storms
- Niger Delta a hotspot of ongoing destruction via oil pipeline pollution
- Indonesia and Myanmar leading recovery following tsunami/cyclone attitude shifts

---

## 2026-06-06 ingest | More than 100 UK datacentres plan to burn gas to generate electricity

**Source file:** `raw/articles/More than 100 UK datacentres plan to burn gas to generate electricity.md`
**Original source:** The Guardian, Aisha Down, 18 May 2026 — https://www.theguardian.com/business/2026/may/18/uk-datacentres-plan-to-burn-gas-to-generate-electricity

**What was done:**
- Created source summary: `wiki/sources/uk-datacentres-gas-2026.md`
- Created new wiki page: `wiki/sectors/digital/ai-data-centre-energy-crisis.md` (covers this article plus the 24 Apr and 28 May articles below)
- Updated `wiki/index.md`

**Key content added:**
- 100 GW of data centre projects queued for UK National Grid
- 100+ gas connection requests; total >15 TWh/year (power London for 4.5 months)
- Some operators requesting 100 MW+ of gas on permanent basis
- Threatens UK Clean Power 2030 target (< 5% unabated gas in electricity system)

---

## 2026-06-06 ingest | Officials hugely underestimated impact of AI datacentres on UK carbon emissions

**Source file:** `raw/articles/Officials hugely underestimated impact of AI datacentres on UK carbon emissions.md`
**Original source:** The Guardian, Damien Gayle, 24 April 2026 — https://www.theguardian.com/technology/2026/apr/24/officials-hugely-underestimated-impact-of-ai-datacentres-on-uk-carbon-emissions

**What was done:**
- Created source summary: `wiki/sources/uk-datacentres-underestimated-emissions-2026.md`
- Incorporated into wiki page: `wiki/sectors/digital/ai-data-centre-energy-crisis.md`
- Updated `wiki/index.md`

**Key content added:**
- UK government revised AI data centre emissions estimate from 0.142m to 34–123m tonnes CO₂ over 2025–35 (100× increase)
- Previous figure quietly deleted after Foxglove/Carbon Brief investigation
- Buildout "could double the electricity consumption of the entire country" if unchecked

---

## 2026-06-06 ingest | 'Hidden datacentre tax' costing Irish households millions, report says

**Source file:** `raw/articles/'Hidden datacentre tax' costing Irish households millions, report says.md`
**Original source:** The Guardian, Rory Carroll, 28 May 2026 — https://www.theguardian.com/technology/2026/may/28/irish-datacentres-household-bills-electricity

**What was done:**
- Created source summary: `wiki/sources/ireland-datacentre-hidden-tax-2026.md`
- Incorporated Ireland section into wiki page: `wiki/sectors/digital/ai-data-centre-energy-crisis.md`
- Updated existing page: `wiki/ireland-hub/IRELAND Datacentre Dilemna.md` — added hidden tax section with 2026 findings
- Updated `wiki/index.md`

**Key content added:**
- Ireland data centres used 22% of national electricity in 2025 — more than all urban homes
- Cumulative household cost: €360/household (2015–2023); projected €295–644 (2025–2034)
- €715m drained from Irish economy; mechanism: gas-set electricity prices pushed up by inflexible DC demand
- Ireland has strictest data centre energy rule in Europe: 80% from additional renewables

---

## 2026-06-06 ingest | World's first underwater data center powered by wind is now online

**Source file:** `raw/articles/World's first underwater data center powered by wind is now online.md`
**Original source:** New Atlas, Bronwyn Thompson, 1 June 2026 — https://newatlas.com/energy/china-underwater-data-center-opens/

**What was done:**
- Created source summary: `wiki/sources/china-underwater-data-centre-2026.md`
- Created new wiki page: `wiki/sectors/digital/underwater-data-centre-china-2026.md`
- Updated `wiki/index.md`

**Key content added:**
- World's first commercial underwater data centre, off Shanghai, operational May 2026
- Offshore wind provides 95% of electricity; seawater replaces freshwater cooling
- Land use reduced 90%+; cooling electricity reduced 22.8%
- Planned capacity 24 MW; potential 50 billion kWh/year saving if scaled
- Open questions on marine heat impact and long-term maintenance

---

## 2026-05-29 ingest | 'Historic breakthrough': Colombia climate talks end with hopes raised for fossil fuel phaseout

**Source file:** `raw/articles/'Historic breakthrough' Colombia climate talks end with hopes raised for fossil fuel phaseout.md`
**Original source:** The Guardian, 30 April 2026. Authors: Fiona Harvey and Jonathan Watts.

**What was done:**
- Created source summary: `wiki/sources/colombia-santa-marta-fossil-fuel-talks-2026.md`
- Created new wiki page: `wiki/solutions/energy-transition/santa-marta-fossil-fuel-conference-2026.md`
- Updated existing page: `wiki/legislation-policy/COP30.md` — added section confirming Santa Marta outcomes as follow-up to the COP30 roadmap announcement
- Created `wiki/index.md` — master catalog of all wiki pages (first creation)
- Created `wiki/log.md` — this file (first creation)
- Created `wiki/sources/` directory (first use)

**Key content added:**
- ~60-country coalition agreeing voluntary fossil fuel phaseout roadmaps
- France as first developed country with a national phaseout roadmap
- Second conference to be held in Tuvalu 2027, co-hosted by Ireland
- Major absentees: US, China, India, Russia, Saudi Arabia, Qatar, UAE

---

## 2026-06-01 ingest | Should I get air conditioning in the UK – and can it be green?

**Source file:** `raw/articles/Should I get air conditioning in the UK – and can it be green?.md`
**Original source:** The Guardian, 28 May 2026. Authors: Chris Baraniuk and Zoe Wood.

**What was done:**
- Created source summary: `wiki/sources/uk-air-conditioning-green-2026.md`
- Created new wiki page: `wiki/climate-adaptation/home-cooling-heatwaves.md`
- Updated `wiki/index.md` — added new source and new climate-adaptation page

**Key content added:**
- 4 million UK homes now have AC, double the figure from 3 years ago
- UK CCC estimate: 22% of homes will need active cooling at 2°C of warming
- Efficiency comparison: fans vs portable AC vs fixed split units vs air-to-air heat pumps
- Pairing AC with solar or home battery as a lower-carbon approach
- UK government £2,500 grant for air-to-air heat pump installation
- Passive cooling alternatives (shutters, night ventilation, green roofs)

---

## 2026-06-01 ingest | Wildlife experts call for 'misleading' timber industry book to be removed from schools

**Source file:** `raw/articles/Wildlife experts call for 'misleading' timber industry book to be removed from schools.md`
**Original source:** The Irish Times, 22 April 2026. Authors: Caroline O'Doherty and Órla Ryan.

**What was done:**
- Created source summary: `wiki/sources/sitka-spruce-greenwashing-ireland-2026.md`
- Updated existing page: `wiki/ireland-hub/IRELAND Land use, Soil and Forestry.md` — added section on the Sitka spruce children's book controversy
- Updated existing page: `wiki/concepts/key-ideas/Greenwashing.md` — added as a new greenwashing example
- Updated `wiki/index.md` — added new source entry

**Key content added:**
- Industry-funded book (*Sitka Spruce – the Amazing Timber Tree*) distributed to Irish primary schools
- Book depicts Sitka plantations as ecologically rich; in reality they are ecological dead zones
- Foreword by Michael Healy-Rae (then minister of state for forestry)
- Irish Wildlife Trust called for removal; Department of Education disclaimed responsibility
- Highlights systemic gap: no safeguard against commercial promotional material in Irish schools
- Raises the carbon sink claim dispute: Sitka planted on bogs is worse for carbon than leaving bogs intact

---

## 2026-06-04 ingest | How Food and Farming Will Determine the Fate of Planet Earth

**Source file:** `raw/articles/How food and farming will determine the fate of planet Earth.md`
**Original source:** Project Drawdown, Jonathan Foley PhD, 30 March 2024 — https://drawdown.org/insights/how-food-and-farming-will-determine-the-fate-of-planet-earth

**What was done:**
- Created source summary: `wiki/sources/foley-food-farming-fate-earth-2024.md`
- Created new wiki page: `wiki/sectors/agriculture-food/agriculture-planetary-footprint.md`
- Updated `wiki/index.md` — added new source and new agriculture page

**Key content added:**
- Agriculture covers 37% of Earth's land surface (cropland + pasture) — more than Asia and Europe combined
- 75% of all agricultural land supports livestock (grazing or animal feed)
- Agriculture uses 70% of global freshwater; Aral Sea and Colorado River as case studies
- Fertiliser runoff has more than doubled global nitrogen/phosphorus flows, creating coastal dead zones
- Direct agriculture and land use = ~22% of global GHG emissions; full food system = ~33%
- Deforestation for farming = ~10–11% of global emissions — equivalent to the entire US economy

---

## 2026-06-04 ingest | AI Emissions: A Practical Guide for Corporate Sustainability Leaders

**Source file:** `raw/papers/AI-emissions-guide-Watershed.pdf`
**Original source:** Watershed, Eric Nevalsky & Steven Watson, 2025 — https://watershed.com

**What was done:**
- Created source summary: `wiki/sources/watershed-ai-emissions-guide-2025.md`
- Created new wiki page: `wiki/sectors/digital/ai-emissions-corporate-guide.md`
- Updated `wiki/index.md` — added new source and new digital page

**Key content added:**
- Inference (running models) accounts for >90% of total AI lifecycle emissions; training <10%
- Single LLM query = ~0.1–0.3 g CO₂e; heavy user (100 queries/day) = ~3 kg CO₂e/year
- Jevons Paradox: AI energy demand projected to triple by 2030 despite per-query efficiency gains
- Goldman Sachs: 60% of new data centre power this decade expected from natural gas
- In 2025, 1,891 energy projects (266 GW) cancelled in the US, 93% clean energy
- Choosing lower-carbon data centre region can cut AI emissions by 30–80% instantly
- No global standard yet for measuring AI emissions; region and model ID are critical data points

---

## 2026-06-04 ingest | The Environmental Footprint of Data Centers in the United States

**Source file:** `raw/papers/The_environmental_footprint_of_data_centers_in_the.pdf`
**Original source:** Environmental Research Letters, Siddik MA, Shehabi A, Marston L, 21 May 2021 — https://doi.org/10.1088/1748-9326/abfba1

**What was done:**
- Created source summary: `wiki/sources/data-centers-environmental-footprint-us-2021.md`
- Created new wiki page: `wiki/sectors/digital/data-center-environmental-footprint.md`
- Updated `wiki/index.md` — added new source and new digital page

**Key content added:**
- US data centres = ~1.8% of US electricity, ~0.5% of US GHG emissions (2018 data)
- Total annual water footprint of US data centres: 5.13 × 10⁸ m³; 75% is indirect (via electricity)
- 70% of water scarcity footprint falls on water-stressed Western US watersheds
- Carbon intensity varies 50-fold by location (0.02–1 tonne CO₂-eq/MWh)
- Smart geographic placement could reduce water scarcity footprint by 90% and carbon by 55%
- Hyperscale data centres are ~6× more water-efficient per workload than internal centres

## 2026-06-13 ingest | Coffeeangel: Brewing a Better Future with Biodiversity

- Source: `raw/articles/Coffeeangel Brewing a Better Future with Biodiversity.md`
- Source summary created: `wiki/sources/coffeeangel-biodiversity-credits.md`
- Existing wiki page updated: `wiki/biodiversity-land/Coffeeangel - an example of Biodiversity restauration credits use.md` — frontmatter corrected (quoted tags, proper keyword summary, added sources and cover_image fields, updated title)
- `wiki/index.md` updated (sources section + biodiversity-land section)
