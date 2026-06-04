---
title: "AI Emissions and Corporate Responsibility"
category: sectors
tags: ["#ai", "#digital", "#energy", "#esg", "#carbon"]
sources: ["Watershed, Eric Nevalsky & Steven Watson, 2025 — https://watershed.com"]
created: 2026-06-04
updated: 2026-06-04
cover_image:
summary: AI emissions, LLM carbon footprint, GPU electricity, inference vs training, data centers, Jevons paradox, AI procurement, vendor evaluation, renewable energy, PPA, REC, scope 2, carbon intensity, grid decarbonization, AI and sustainability, measuring AI emissions, token count, model ID, corporate sustainability, AI efficiency, right-sizing models, context stuffing, sustainability AI tools
---

# AI Emissions and Corporate Responsibility

## What it is

This page explains **where AI emissions actually come from, how large they are, and what companies can do about them.** The source is a 2025 guide by Watershed (a corporate sustainability platform), aimed at sustainability leaders trying to get ahead of AI's growing carbon footprint before it becomes a material issue in their reporting.

The central, non-obvious finding: **inference — the act of running a model — accounts for over 90% of total AI lifecycle emissions.** Training gets all the headlines, but because it happens once while inference happens millions of times a day, it is a rounding error by comparison.

## Where AI Emissions Actually Come From

AI emissions are almost entirely electricity: **~80.9% from powering GPUs** during inference, ~17.8% from other data centre infrastructure, and just 1.3% from GPU manufacturing. A single LLM query uses roughly 0.24 Wh of electricity — about **0.1–0.3 g CO₂e** on the average US grid. A heavy user running 100 queries/day generates around 3 kg CO₂e/year, less than the emissions from half a kilogram of beef.

The practical implication is that **AI emissions scale with usage, depend heavily on grid carbon intensity, and are therefore decarbonisable** — unlike cement or steel, AI does not require fossil fuels as a chemical input.

## The Jevons Paradox Problem

AI models are becoming more efficient per query — Google's Gemini saw a **33× energy reduction per query** from 2024 to 2025. But efficiency gains make AI cheaper, which drives adoption, which drives total electricity demand up. This is the **Jevons Paradox**: total AI energy demand is projected to **triple by 2030** even as per-query efficiency improves. The risk is not any single query; it is system-wide energy growth outpacing clean supply.

Making this worse: data centres are being built faster than renewable energy can come online. Goldman Sachs projects **60% of new data centre power this decade will come from natural gas**. In 2025 alone, 1,891 energy projects (266 GW) were cancelled in the US — 93% of them clean energy.

## Responsible Procurement as Climate Strategy

Most AI emissions are determined upstream — by where data centres are located, what electricity they use, and how efficiently they operate. **Companies cannot control model architecture, but they can control which vendors they choose.** Watershed frames procurement as the strongest lever sustainability leaders have.

When evaluating AI or cloud providers, the guide recommends assessing three things: (1) **infrastructure transparency** (can they disclose region-level emissions factors and methodology?); (2) **clean energy strategy** (hourly vs annual matching, PPAs vs unbundled RECs); (3) **long-term commitments** (carbon removal purchases, data centre efficiency roadmaps). Selecting a data centre region with cleaner grid electricity can **reduce operational AI emissions by 30–80% instantly**.

## Measuring AI Emissions

There is currently no globally accepted standard for measuring AI emissions. The most useful data points are **region/location** (critical — grid carbon intensity varies enormously by place), **model ID** (critical — different models have very different compute requirements), and **token count** (medium-high — a good proxy for compute, though converting to energy requires assumptions). Spend-based estimates are a fallback. Latency is a poor proxy.

## Summary findings

- **>90% of AI lifecycle emissions** come from inference (usage), not training or hardware.
- A single LLM query = ~0.1–0.3 g CO₂e; a heavy user generates ~3 kg CO₂e/year — less than half a kilo of beef.
- AI energy demand is projected to **triple by 2030** due to the Jevons Paradox, despite per-query efficiency gains.
- **60% of new data centre power** this decade is projected to come from natural gas, not renewables (Goldman Sachs).
- Choosing a lower-carbon data centre region can cut AI emissions by **30–80% immediately**.
- No global standard exists for measuring AI emissions; region and model ID are the most critical data points.
- Only **25% of sustainability teams** currently estimate or report AI emissions.

## Connected topics

- [FACTS about AI, Emissions Impacts and Mitigation Potential](../digital/facts-about-ai-emissions-impacts-and-mitigation-potential.md)
- [Data Centre Environmental Footprint](Data%20Centre%20environmental%20footprint.md)
- [What is Jevons Paradox](../digital/what-is-jevons-paradox.md)
- [IRELAND Data Centre Dilemma](../../ireland-hub/ireland-data-centre-dilemna.md)
- [FACTS about Electricity](../energy/facts-about-electricity.md)
- [Scope 3 GHG](../../concepts/key-ideas/scope-3-ghg.md)

## Sources

- Watershed, Eric Nevalsky & Steven Watson, 2025 — https://watershed.com
