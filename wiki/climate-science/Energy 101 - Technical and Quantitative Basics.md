---
title: "Energy 101: Technical and Quantitative Basics"
category: climate-science
tags: ["#science", "#energy"]
created: 2026-06-01
updated: 2026-08-26
summary: energy versus power, watts, watt-hours, energy content of fuels, carbon intensity of fuels, unit conversions, efficiency, capacity factor, load curve, load duration curve, duck curve, solar generation midday, grid capacity planning, 100% renewable studies, levelized cost of energy, LCOE, capital costs, fixed and variable operation costs, fuel costs, transmission costs
---

# Energy 101: Technical and Quantitative Basics

A grounding in a handful of core energy concepts, energy versus power, efficiency, load curves, and how electricity is actually costed, makes it much easier to evaluate claims about energy technologies rather than taking headline numbers on faith.

## Energy vs Power

**Energy** is the capacity to do work, measured in joules, kilowatt-hours (kWh), Btu, or calories. **Power** is the rate at which energy is used or generated, i.e. energy over time, measured in watts, horsepower, or Btu per hour. The relationship is simple: Power (W) = Energy (Wh) / Time (h). A 7W light bulb left on for 4 hours consumes 7 x 4 = 28Wh of energy.

Beyond this core distinction, energy analysis generally draws on a few related ideas: **energy content of fuels** (energy per unit mass or volume of a given fuel), **carbon intensity of fuels** (CO2 emitted per unit of energy produced), and a great deal of **unit conversion** between these different measures.

## Efficiency and Capacity Factor

**Efficiency** is simply what a system gets out relative to what goes in. A typical coal power plant, for example, converts only around 36% of the fuel's energy content into usable electricity, with the rest lost mostly as waste heat.

**Capacity factor** is a related but distinct concept: the share of a power plant's theoretical maximum output it actually generates over a given period. It captures real-world downtime, maintenance, and, for wind and solar in particular, the variability of the resource itself (a plant might have a high nameplate capacity but a much lower capacity factor once weather and daylight hours are accounted for).

## Load Curves and the "Duck Curve"

A **load curve** plots actual electricity demand chronologically, hour by hour, across a day or season; summing it up gives total energy demand for that period. Load curves vary by country and by season. A **load duration curve (LDC)** shows the same demand data, but sorted in descending order of magnitude rather than chronologically, which is useful for planning how much capacity needs to be available for peak demand versus typical demand.

Solar power has visibly reshaped load curves in grids with high solar penetration: when solar generation peaks around midday, it reduces net demand on the rest of the system, which then climbs again as the sun sets and solar output drops off just as evening demand rises. The resulting shape, a dip followed by a steep evening ramp, is widely known in the power sector as the **"duck curve."**

Planning a grid with high levels of variable renewable generation requires a newer generation of capacity planning models, which now underpin well over a thousand published studies showing that grids can run reliably and economically at very high renewable energy shares. Some of the most influential regional studies include:

- **Europe:** SolarPower Europe and LUT University's [100% Renewable Europe study](https://www.solarpowereurope.org/insights/market-outlooks/100-renewable-europe-study)
- **USA:** Columbia University's [Electrification on the Path to Net Zero](https://www.energypolicy.columbia.edu/research/report/electrification-path-net-zero-comparison-studies-examining-opportunities-and-barriers-united-states), and UC Berkeley's [2035 Report](https://www.2035report.com/)
- **Philippines:** a [2021 study](https://www.sciencedirect.com/science/article/pii/S1364032121002264) finding a 100% renewable energy system achievable by 2050 at a cost comparable to the 2015 system
- **India:** a [2021 report](https://www.wartsila.com/docs/default-source/power-plants-documents/downloads/white-papers/asia-australia-middle-east/a-100-renewable-power-system-across-india-by-2050-whitepaper.pdf) finding India could reach net-zero electricity by 2050 while halving overall electricity costs
- **Australia:** a 2021 [Rewiring Australia study](https://www.rewiringaustralia.org/castles-and-cars) by Saul Griffith arguing the country's exceptional solar and wind resources make it "the luckiest country" for electrification

## The Cost of Producing Electricity

Building and running any power generation facility involves five distinct types of cost:

1. **Capital costs**: fixed costs of building the facility itself, including land, materials, labour, and regulatory costs like siting permits and environmental approvals
2. **Fixed operation and maintenance costs**: costs to keep a plant running regardless of output, such as labour that must always be present and routine maintenance
3. **Variable operation and maintenance costs**: costs that scale with actual power output, including additional labour, maintenance, wastewater management, chemicals and spare parts, but excluding fuel
4. **Fuel costs**: the cost of the fuel itself, which scales with output for conventional fossil-fuel generators
5. **Transmission costs**: highly context-specific costs, including grid upgrades a new facility might require, and the added complexity of two-way power flow as distributed rooftop solar feeds electricity back into a grid originally designed to send power only one way

Because comparing five different cost categories across technologies is unwieldy, the industry combines them into a single metric: the **levelized cost of energy** or **levelized cost of electricity (LCOE)**, a facility's cost to generate one unit of electricity averaged over its entire lifetime. Whenever electricity costs are quoted in the media as $/kWh or similar, this is almost always LCOE.

On an unsubsidised basis, wind, solar PV and geothermal are now competitive with, and often cheaper than, fossil fuel generation. Solar paired with storage is cheaper than most coal, gas peaking plants and nuclear power, and highly competitive with gas combined-cycle plants, even before any subsidies or tax incentives are factored in.

## Connected topics

- [Clean Electricity: Why It Has to Come First](../sectors/energy/Clean%20Electricity%20-%20Why%20It%20Has%20to%20Come%20First.md)
- [FACTS about Solar Energy](../solutions/renewables/FACTS%20about%20Solar%20Energy.md)
- [FACTS about Wind Energy](../solutions/renewables/FACTS%20about%20Wind%20Energy.md)

## Sources


- SolarPower Europe and LUT University, 100% Renewable Europe study — https://www.solarpowereurope.org/insights/market-outlooks/100-renewable-europe-study
- Columbia University Center on Global Energy Policy, Electrification on the Path to Net Zero — https://www.energypolicy.columbia.edu/research/report/electrification-path-net-zero-comparison-studies-examining-opportunities-and-barriers-united-states
- UC Berkeley Goldman School of Public Policy, 2035 Report — https://www.2035report.com/
- Science of the Total Environment (2021), 100% renewable energy system for the Philippines — https://www.sciencedirect.com/science/article/pii/S1364032121002264
- Wärtsilä (2021), a 100% renewable power system across India by 2050 — https://www.wartsila.com/docs/default-source/power-plants-documents/downloads/white-papers/asia-australia-middle-east/a-100-renewable-power-system-across-india-by-2050-whitepaper.pdf
- Rewiring Australia, Castles and Cars (2021) — https://www.rewiringaustralia.org/castles-and-cars
