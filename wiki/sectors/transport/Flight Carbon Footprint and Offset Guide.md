---
title: Flight Carbon Footprint and Offset Guide
category: sectors
tags: ["#aviation", "#carbon-offset", "#carbon", "#transport"]
created: 2026-06-01
updated: 2026-08-26
summary: flight carbon footprint calculation, jet fuel burn, great circle distance, aircraft and engine type, cargo vs passenger allocation, seat occupancy rate, passenger load factor, seat class multiplier, carbon calculators comparison, Google Flights, ICAO methodology, MyClimate, CarbonFootprint.com, contrails, radiative forcing, net cooling research, carbon offsetting, CORSIA, EU ETS, EasyJet, offset price, additionality
---

# Flight Carbon Footprint and Offset Guide

## What is it

Calculating the CO2 emissions of a flight is relatively straightforward in principle, since it is directly tied to how much jet fuel is burnt. Working out how much of that belongs to a single passenger is harder, and depends on several factors. This guide walks through how footprint calculators actually work, why different tools can give very different answers for the same flight, and what buying a carbon offset actually achieves.

Other related reading: [Carbon Offsets: How They Work and Why They Often Fall Short](../../concepts/key-ideas/Carbon%20Offsets.md)

## Why it matters

Two people can fly the identical route and be told wildly different numbers for their carbon footprint, depending on which calculator they use and what it accounts for. Understanding why helps travellers judge offset claims critically rather than taking a green tick at face value.

## How a flight's carbon footprint is calculated

Five factors matter most:

1. **Flight distance.** The further the distance, the more fuel is burnt overall, but take-off and landing use a disproportionate share of fuel on short routes, making short flights less efficient per kilometre. Calculators typically use the great circle distance (the shortest path between two airports) plus an allowance for real-world routing, weather diversions and air traffic delays.
2. **Aircraft and engine type.** Fuel consumption varies considerably between aircraft models and engines.
3. **Cargo versus passengers.** Most of a flight's weight is the aircraft and its fuel; the remaining "payload" is people and cargo. Passenger aircraft, especially wide-bodies on long-haul routes, often carry substantial freight and mail alongside passengers. Emissions are typically split by each group's share of total payload weight: if passengers are 80% of payload weight and cargo 20%, then 20% of the flight's emissions are attributed to cargo and subtracted before dividing the rest among passengers. Industry practice assumes 100 kg per passenger including luggage, plus another 50 kg per passenger for shared infrastructure such as toilets, galleys and crew. The passenger share of payload varies a lot by route: over 96% on intra-European flights, but only 64 to 80% on Europe-Asia flights ([ICAO, 2017](https://www.icao.int/environmental-protection/CarbonOffset/Documents/Methodology%20ICAO%20Carbon%20Calculator_v10-2017.pdf)).
4. **Seat occupancy rate**, also called the passenger load factor. Longer flights tend to use larger, more efficient aircraft, but a flight's actual emissions per passenger depend on how full it is: the same total emissions divided among fewer passengers means a higher footprint each. Occupancy is highest on Central America to Europe routes (83%) and lowest between Africa/Middle East and South America (60%) ([ICAO, 2017](https://www.icao.int/environmental-protection/CarbonOffset/Documents/Methodology%20ICAO%20Carbon%20Calculator_v10-2017.pdf)).
5. **Seat class.** Business and first-class seats take up more cabin space and carry fewer passengers per plane, so they are assigned a larger share of the aircraft's weight and emissions. A multiplier of around 1.5 is typically used for business class and 2 to 3 for first class.

## Typical fuel consumption by distance

Average jet fuel consumption per passenger, according to [BDL (2015)](https://www.bdl.aero/wp-content/uploads/2015/07/energieeffizienz_klimaschutz_2015_de.pdf):

- 2 to 6.8 litres per 100 passenger-km on short flights (under 800 km)
- 4.2 to 6 litres per 100 passenger-km on medium flights (800 to 3,000 km)
- 3.5 to 9 litres per 100 passenger-km on long flights (over 3,000 km)

## Why calculators disagree: a real comparison

Testing several popular calculators on the same direct Dublin to Geneva flight produced results that varied by up to 2x:

- Google Flights: 230 kg CO2e
- ICAO Environment calculator: around 230 kg
- MyClimate: around 500 kg, roughly double the above
- CarbonFootprint.com: around 320 kg, with the option to add or exclude radiative forcing from contrails

Google and ICAO are the most transparent about their methodology, and Google is notably upfront about the unresolved challenge of estimating contrails' real climate impact.

## Contrails: the piece most calculators leave out

Most carbon calculators do not account for contrails, the feathery ice clouds that form when hot jet exhaust meets cold, humid air at altitude. Most contrails dissipate quickly, but a small share persist and spread, trapping outgoing heat.

According to [Google's Travel Impact Model documentation](https://support.google.com/travel/answer/11116147), once contrails are factored in, the warming impact of flying can be up to 60% higher than estimates based on fuel burn alone ([Lee et al., 2021](https://www.sciencedirect.com/science/article/pii/S1352231020305689)). Roughly 10% of flights are responsible for the majority of persistent, warming contrails, but predicting exactly which flights will form them, and quantifying the impact per flight, remains scientifically unresolved, which is why most calculators leave contrails out entirely. Separate research published in the [2022 IPCC report](https://www.ipcc.ch/report/ar6/wg3/downloads/report/IPCC_AR6_WGIII_Chapter10.pdf) estimated that contrail-induced cloud cover accounts for roughly 35% of aviation's total global warming impact, over half as much as the warming from burning the jet fuel itself. A separate 2019 study on contrail cirrus radiative forcing projected this effect would grow significantly as air traffic increases.

Contrail science has also moved recently. A newer AI-assisted analysis of 700,000 contrails over Europe and North Africa during winter 2023 and 2024, reported by [New Scientist](https://www.newscientist.com/article/2449212-jet-contrails-may-cool-the-planet-by-day-and-warm-it-by-night/), found the picture is more complex than "contrails always warm." Contrails both reflect incoming sunlight (a cooling effect) and trap outgoing heat (a warming effect). Some 62% of the contrails observed formed at night, when only the warming effect applies, but most daytime contrails were found to have a net cooling effect because the reflection and trapping effects partially cancel out. The average contrail lasts 2.5 to 3.5 hours, though some persist for 14 hours or more, meaning a contrail formed late in the day can still carry into the night and add warming. This suggests day flights may have a smaller climate impact than night flights on the same route, though it does not offset the CO2 emissions of the flight itself. The more promising fix under active research is rerouting aircraft around the supersaturated air where persistent contrails form, though this can add around 30 minutes to a long-haul flight. For the AI-driven trial now under way to test this at scale, see [Operation Blue Skies](FACTS%20about%20Air%20Travel.md#contrails).

## Carbon offsetting for the aviation industry

Prospective offset buyers sometimes assume airlines already offset their emissions under regulation. That is only partly true, and coverage is patchy. Within the EU, the Emissions Trading System (ETS) covers flights, but international flights are excluded. The Kyoto Protocol asked wealthier countries to limit international aviation emissions through the International Civil Aviation Organization (ICAO). In 2008, with progress stalling under ICAO, the EU added both domestic and international flights to and from the EU to its ETS, but the international aviation industry objected, and in 2012 the EU exempted international flights to give ICAO time to develop its own scheme. That scheme, the [Carbon Offsetting and Reduction Scheme for International Aviation (CORSIA)](https://www.icao.int/environmental-protection/pages/climate-change.aspx), was adopted by ICAO in 2016. Both the EU ETS and CORSIA are steps in the right direction, but their combined impact remains very limited, particularly outside the EU.

In response, many airlines now offer passengers the option to buy a carbon offset when booking. Almost all companies and organisations with net-zero pledges are purchasing or otherwise engaging in offset projects, yet the sector remains highly controversial. In September 2022, the British budget airline EasyJet said it would stop using most carbon credits to reach its mid-century net-zero goal, [citing its own net zero roadmap](https://corporate.easyjet.com/files/doc_downloads/easyjet-nz-roadmap.pdf).

Offset prices vary enormously, from just a few euros on some budget airlines to far higher on carriers that price offsets more realistically. One widely cited example: a passenger flying roughly 34,000 km from London to Tahiti paid an extra £27 to offset 1.7 tonnes of CO2, despite their actual footprint for the journey being closer to 6 tonnes. At a more realistic carbon price of around $80 a tonne, which many economists consider still undervalued, 1.7 tonnes should cost far more than £27. Airline offset schemes are voluntary and often opaque about how much money actually funds permanent, additional emissions reductions rather than projects that would have happened anyway. As the [New Scientist has argued](https://www.newscientist.com), the offset market remains a drop in the ocean of what is needed, and risks distracting from the real solution: decarbonising aviation itself.

## Key facts

- The same Dublin-Geneva flight produced footprint estimates from 230 kg to 500 kg CO2e depending on the calculator used.
- Contrails can push aviation's real warming impact up to 60% above fuel-burn-only estimates (Lee et al., 2021, via Google).
- Contrail-induced cloud cover is estimated to cause around 35% of aviation's total warming, more than half as much as CO2 from the fuel itself (IPCC AR6).
- Around 10% of flights cause the majority of persistent, warming contrails.
- A 2024 study of 700,000 contrails found most daytime contrails have a net cooling effect, while night-forming contrails (62% of those studied) warm.
- Rerouting to avoid contrail-forming air can add roughly 30 minutes to a long-haul flight.
- One documented case: an offset of 1.7 tonnes CO2 cost £27, against an actual footprint of around 6 tonnes for the trip.

## Connected topics

- [Facts about Air Travel](FACTS%20about%20Air%20Travel.md)
- [Carbon Offsets: How They Work and Why They Often Fall Short](../../concepts/key-ideas/Carbon%20Offsets.md)
- [Carbon Footprint Calculator](../../concepts/Carbon%20Footprint%20Calculator.md)

## Sources

- Offset Guide, "Passenger climate footprints" — https://www.offsetguide.org/understanding-carbon-offsets/air-travel-climate/passenger-climate-footprints/
- ICAO, "Carbon Calculator Methodology" (2017/2018) — https://www.icao.int/environmental-protection/CarbonOffset/Documents/Methodology%20ICAO%20Carbon%20Calculator_v10-2017.pdf
- BDL, "Energieeffizienz und Klimaschutz" (2015) — https://www.bdl.aero/wp-content/uploads/2015/07/energieeffizienz_klimaschutz_2015_de.pdf
- Google Travel Help Centre, "Other warming effects of flying" — https://support.google.com/travel/answer/11116147
- Lee et al., "The contribution of global aviation to anthropogenic climate forcing", Atmospheric Environment, 2021 — https://www.sciencedirect.com/science/article/pii/S1352231020305689
- IPCC AR6 Working Group III, Chapter 10 — https://www.ipcc.ch/report/ar6/wg3/downloads/report/IPCC_AR6_WGIII_Chapter10.pdf
- New Scientist, "Jet contrails may cool the planet by day and warm it by night" — https://www.newscientist.com/article/2449212-jet-contrails-may-cool-the-planet-by-day-and-warm-it-by-night/
- EasyJet, Net Zero Roadmap (2022) — https://corporate.easyjet.com/files/doc_downloads/easyjet-nz-roadmap.pdf
- The Guardian, "Private jets are awful for the climate. It's time to tax the rich who fly in them", 10 August 2023 — https://www.theguardian.com/commentisfree/2023/aug/10/private-jets-are-awful-for-the-climate-its-time-to-tax-the-rich-who-fly-in-them
