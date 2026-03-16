---
name: ResearchLab
description: Multi-agent research lab. Takes questions → spawns 15 specialist agents → outputs paper-ready reports. Includes DataScientist for empirical grounding. USE WHEN research, investigate, study|analyze|explore deep.
---

# Peace-png Research Lab
**Author**: Peace-png
**License**: CC BY 4.0 © Peace-png 2026

---

## Quick Start

```
research "Your question here"
```

Spawns real specialist agents in parallel.

---

## ⚠️ PRE-FLIGHT CHECKLIST (MANDATORY)

**Before starting ANY research, the Director MUST print this checklist and track completion:**

```
╔═══════════════════════════════════════════════════════════════╗
║           RESEARCH LAB STACK - EXECUTION CHECKLIST            ║
╠═══════════════════════════════════════════════════════════════╣
║  WAVE 1: Core Analysis                                        ║
║  [ ] Scientist (ClaudeResearcher)                             ║
║  [ ] Skeptic (GrokResearcher)                                 ║
║  [ ] Historian (Research skill)                               ║
║                                                               ║
║  WAVE 1.5: Empirical Grounding                                ║
║  [ ] DataScientist (CodexResearcher) [skip if --no-data]      ║
║    - Pull datasets from World Bank, FRED, OWID                ║
║    - Run regression analysis                                  ║
║    - Output: coefficients, CIs, base rates                    ║
║    - Save: results/empirical_results.json                     ║
║                                                               ║
║  WAVE 2: Interpretation                                       ║
║  [ ] Experimenter (CodexResearcher)                           ║
║  [ ] Philosopher (Thinking skill)                             ║
║  [ ] Explainer (GeminiResearcher)                             ║
║                                                               ║
║  WAVE 2.5: Novel Hypotheses                                   ║
║  [ ] Ideologist (CodexResearcher)                             ║
║    - Uses DataScientist results as grounding                  ║
║    - Hypotheses must be consistent with empirical data        ║
║                                                               ║
║  WAVE 3: Validation                                           ║
║  [ ] Simulator/Brian2 (CodexResearcher)                       ║
║                                                               ║
║  WAVE 4: Visualisation                                        ║
║  [ ] Artist (Media skill) [skip if --no-images]               ║
║                                                               ║
║  WAVE 5: Memory                                               ║
║  [ ] Archivist (update lab_memory.json)                       ║
║                                                               ║
║  WAVE 6: Publication                                          ║
║  [ ] Publisher (ClaudeResearcher) → README.md + PAPER.md      ║
║                                                               ║
║  QUALITY GATES (MANDATORY)                                    ║
║  [ ] Gate 1: Empirical grounding - data shown for claims      ║
║  [ ] Gate 2: Post-hoc flexibility - counter-examples counted  ║
║  [ ] Gate 3: Endogeneity - causal claims match evidence       ║
║  [ ] Gate 4: Citations verified - no hallucinated refs        ║
║  [ ] Gate 5: DataScientist ran for quantitative claims        ║
║                                                               ║
║  FINAL: Git                                                   ║
║  [ ] Commit all outputs                                       ║
║  [ ] Push (if --push flag)                                    ║
║  [ ] Index to ClawMem                                         ║
╚═══════════════════════════════════════════════════════════════╝
```

**Failure Modes to Avoid:**

| What Happened | Why It's Wrong | Fix |
|---------------|----------------|-----|
| Skipped Waves 2.5-6 | "Had enough data" | NEVER skip - each wave has unique purpose |
| Didn't commit/push | Forgot final step | Checklist requires explicit completion |
| Web search rate-limited | External dependency | Continue with available data, don't skip waves |
| Made up citations | Publisher overstepped | Publisher FORMATS only, doesn't author |

**Director Responsibility:**

After each wave completes, mark `[x]` in checklist. If any wave fails:
1. Log the failure in lab_memory.json
2. Continue with remaining waves if possible
3. Report failure to user at end

**NEVER:**
- Skip a wave because "we have enough data"
- Skip the checklist printing
- Skip the final git commit
- Skip ClawMem indexing

---

## The Agent Stack

This skill wires 15 logical roles to your actual PAI researchers, mapped to brain regions:

| Role | Real Agent | Brain Region | Function |
|------|------------|--------------|----------|
| **Director** | Main session | Brainstem + Thalamus | Orchestrate, route signals |
| **Scientist** | `ClaudeResearcher` | Prefrontal | Final authority, truth claims |
| **DataScientist** | `CodexResearcher` | Parietal lobe | Statistical analysis, empirical grounding |
| **Skeptic** | `GrokResearcher` | Amygdala | Threat detection, MAJOR_FLAW |
| **Ideologist** | `CodexResearcher` | Right hemisphere | Novel hypothesis generation |
| **Experimenter** | `CodexResearcher` | Motor cortex | Design tests, action |
| **Historian** | `Research` skill | Temporal cortex | Literature, examples |
| **Philosopher** | `Thinking` skill | Limbic | Meaning, implications |
| **Explainer** | `GeminiResearcher` | Language areas | Simplification |
| **Artist** | `Media` skill | Visual cortex | Visualisations |
| **Archivist** | Direct file write | Hippocampus | Memory consolidation |
| **Synthesiser** | `PerplexityResearcher` | DMN | Cross-cycle integration |
| **Publisher** | `ClaudeResearcher` | Broca's area | Academic formatting |
| **Ground Truth** | `ClaudeResearcher` | Cerebellum | Validate against known data |
| **Simulator** | `CodexResearcher` | Basal Ganglia | Brian2 validation, rhythm extraction |

### E/I Balance (Excitation/Inhibition)

**Excitatory agents** (generate ideas, expand scope):
- Scientist, Experimenter, Historian, Philosopher

**Inhibitory agents** (constrain, challenge):
- Skeptic (can HALT with MAJOR_FLAW)

This balance prevents runaway speculation while maintaining exploration.

### Publisher Agent (NEW)

The Publisher runs AFTER all research agents complete. It is a **formatter, not an author**:

| Capability | Automated | Human Required |
|------------|-----------|----------------|
| IMRaD structure | ✅ | - |
| Citation formatting | ✅ | Verification |
| Statistical notation | ✅ | Verification |
| Abstract generation | ✅ | Review |
| Novelty claims | - | ✅ |
| Interpretation | - | ✅ |
| Ethical judgment | - | ✅ |

**Publisher outputs:**
- `README.md` - Blog format (current style)
- `PAPER.md` - Academic format (IMRaD structure)
- `CITATION.bib` - BibTeX references

### Ground Truth Agent (Optional - Neuroscience Mode)

When running neuroscience research with `--grounding neuroscience`, an additional agent validates claims against known data:

| Capability | Automated | Source |
|------------|-----------|--------|
| Parameter validation | ✅ | Validated SNN parameters |
| PMID citation check | ✅ | PubMed lookup |
| Firing rate comparison | ✅ | NeuroElectro / literature |
| Mechanism verification | ✅ | Known neurophysiology |

**Ground Truth runs AFTER Scientist, BEFORE Skeptic** to provide factual constraints.

### DataScientist Agent - Empirical Grounding Engine

The DataScientist runs AFTER Scientist, BEFORE Ideologist. It **grounds hypotheses in real data**, transforming selective anecdotes into systematic evidence.

#### Why This Agent Exists

**The Problem:** Research Lab was generating hypotheses from cherry-picked historical examples. "Arab Spring had food inflation" → "Food inflation predicts unrest." This is selection bias, not evidence.

**The Solution:** DataScientist pulls actual datasets, runs real statistics, outputs:
- Sample sizes (N)
- Effect sizes with confidence intervals
- P-values (where appropriate)
- Base rates
- False positive/negative rates

#### Capabilities

| Capability | Method | Output |
|------------|--------|--------|
| **Data Retrieval** | World Bank API, FRED, OWID, IMF | Raw CSV/JSON datasets |
| **Data Merging** | Country-year matching, ISO codes | Merged panel data |
| **Missing Data Handling** | Listwise deletion, interpolation flags | Clean analysis dataset |
| **Descriptive Stats** | Mean, median, SD, quartiles | Summary tables |
| **Regression Analysis** | OLS, logistic, panel (FE/RE) | Coefficients, SEs, p-values |
| **Time Series** | Lagged variables, Granger causality | Lead/lag relationships |
| **Causal Inference** | IV, diff-in-diff (if natural experiments) | Causal estimates |
| **Cross-Validation** | Train/test split, k-fold | Out-of-sample performance |
| **Visualization Specs** | Plot specifications for Artist | Data-driven charts |

#### Data Sources (Priority Order)

1. **World Bank WDI** (api.worldbank.org)
   - Inflation, GDP, unemployment, trade
   - 217 countries, 1960-present
   - API: `api.worldbank.org/v2/country/all/indicator/FP.CPI.TOTL.ZG`

2. **FRED** (fred.stlouisfed.org)
   - US economic indicators
   - 816,000+ series
   - API: `api.stlouisfed.org/fred/series/observations`

3. **Our World in Data** (ourworldindata.org)
   - Pre-processed, documented datasets
   - Standardized country codes
   - Direct CSV: `ourworldindata.org/grapher/data.csv`

4. **IMF WEO/IFS**
   - International macroeconomic data
   - Quarterly + annual

5. **V-Dem** (v-dem.net)
   - Democracy indices, regime type
   - 202 countries, 1789-present

6. **ACLED** (acleddata.com)
   - Protest/event data (requires API key)
   - Geographic, temporal precision

7. **POLITY V**
   - Regime type, political stability
   - Annual country-level

#### Execution Protocol

```
DATASCIENTIST EXECUTION FLOW:
┌─────────────────────────────────────────────────────────────┐
│  INPUT: Research question + Scientist's initial findings    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 1: Identify Required Variables                        │
│  - What data would test the core hypothesis?                │
│  - What are the outcome variables? (unrest, regime change)  │
│  - What are the predictor variables? (inflation, food)      │
│  - What are the control variables? (GDP, unemployment)      │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 2: Identify Available Data Sources                    │
│  - Check which datasets have required variables             │
│  - Check temporal coverage (years available)                │
│  - Check geographic coverage (countries available)          │
│  - Document gaps and workarounds                            │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 3: Retrieve Data                                      │
│  - Use web_fetch for CSV/JSON APIs                          │
│  - Document exact API calls for reproducibility             │
│  - Save raw data to results/raw_data/                       │
│  - Log any access issues or missing data                    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 4: Merge & Clean                                      │
│  - Match on ISO country codes + year                        │
│  - Handle missing data (document method)                    │
│  - Create analysis dataset                                  │
│  - Save to results/analysis_dataset.csv                     │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 5: Descriptive Statistics                             │
│  - N observations, N countries, year range                  │
│  - Distribution of key variables (mean, SD, range)          │
│  - Correlation matrix for main variables                    │
│  - Base rates: P(outcome) overall, by predictor quintile    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 6: Main Analysis                                      │
│  - Regression: outcome ~ predictor + controls               │
│  - Report: coefficient, SE, 95% CI, p-value                 │
│  - Test alternative specifications (robustness)             │
│  - If time series: test lead/lag relationships              │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 7: Validation                                         │
│  - Cross-validation: train/test split                       │
│  - Sensitivity: does result hold with different specs?      │
│  - Counter-example check: how many cases contradict?        │
│  - Out-of-sample: predict next year, check accuracy         │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  OUTPUT: empirical_results.json                             │
│  {                                                          │
│    "n_observations": 2453,                                  │
│    "n_countries": 142,                                      │
│    "year_range": [1990, 2023],                              │
│    "main_result": {                                         │
│      "coefficient": 0.034,                                  │
│      "se": 0.012,                                           │
│      "ci_95": [0.010, 0.058],                               │
│      "p_value": 0.005,                                      │
│      "interpretation": "1pp inflation increase → 3.4% higher unrest probability" │
│    },                                                       │
│    "base_rate": 0.12,                                       │
│    "false_positives": 234,                                  │
│    "false_negatives": 89,                                   │
│    "out_of_sample_accuracy": 0.67,                          │
│    "counter_examples": ["Turkey 2022", "Argentina 2019"],   │
│    "data_sources": ["World Bank WDI", "ACLED"],             │
│    "limitations": ["Endogeneity unresolved", "Missing data for 23 countries"] │
│  }                                                          │
└─────────────────────────────────────────────────────────────┘
```

#### Output Interpretation Standards

| Statistical Result | Label | Confidence |
|--------------------|-------|------------|
| p < 0.01, CI excludes 0, replicated OOS | **SUPPORTED** | HIGH |
| p < 0.05, CI excludes 0 | **TENTATIVE** | MEDIUM |
| p < 0.10 or CI includes 0 | **INCONCLUSIVE** | LOW |
| p ≥ 0.10 or opposite sign | **REJECTED** | HIGH (negative) |
| N < 100 or major data gaps | **INSUFFICIENT DATA** | N/A |

#### When DataScientist Runs

**ALWAYS** for quantitative research questions involving:
- Thresholds, percentages, probabilities
- "X predicts Y" claims
- Comparative statements across countries/years
- Time-based predictions (lead times)

**OPTIONAL** (can skip with `--no-data`) for:
- Philosophical analysis
- Historical narrative
- Conceptual frameworks
- Qualitative research

#### Example: Inflation Predicting Unrest

```
DATASCIENTIST OUTPUT:
┌─────────────────────────────────────────────────────────────┐
│  EMPIRICAL ANALYSIS: Inflation → Civil Unrest               │
│                                                              │
│  DATA:                                                       │
│  - Source: World Bank WDI (inflation) + ACLED (protests)    │
│  - N: 2,847 country-years                                   │
│  - Countries: 142                                            │
│  - Years: 1997-2023                                          │
│                                                              │
│  MAIN RESULT: Inflation → Protest Count (Poisson)           │
│  - Coefficient: 0.018 (SE: 0.007)                           │
│  - 95% CI: [0.004, 0.032]                                   │
│  - p-value: 0.011                                            │
│  - Interpretation: 10pp inflation → 18% more protests       │
│                                                              │
│  THRESHOLD ANALYSIS:                                         │
│  - >15% inflation: 2.3x protest rate (p < 0.001)            │
│  - >30% inflation: 3.1x protest rate (p < 0.001)            │
│  - >50% inflation: 4.2x protest rate (p = 0.023)            │
│  - Hyperinflation: N=12, too few for inference              │
│                                                              │
│  BASE RATES:                                                 │
│  - Overall protest probability: 23%                          │
│  - Given inflation <10%: 18%                                 │
│  - Given inflation 10-30%: 29%                               │
│  - Given inflation >30%: 47%                                 │
│                                                              │
│  FALSE POSITIVES: 312 (high inflation, no unrest)           │
│  FALSE NEGATIVES: 89 (low inflation, unrest occurred)       │
│                                                              │
│  COUNTER-EXAMPLES (N=23):                                    │
│  - Turkey 2018-2023: 80%+ inflation, stable regime          │
│  - Argentina 2018-2023: 50%+ inflation, democracy persists  │
│  - Angola 2016: 42% inflation, no major unrest              │
│                                                              │
│  OUT-OF-SAMPLE: 2022 predictions → 64% accuracy              │
│                                                              │
│  LIMITATIONS:                                                │
│  - Endogeneity: unrest may cause inflation (capital flight) │
│  - Missing: N Korea, Somalia, Syria (no data)               │
│  - Protest definition varies by source                       │
│                                                              │
│  CONCLUSION: TENTATIVE SUPPORT for threshold effects,       │
│  but high false positive rate (44%) limits predictive use.  │
└─────────────────────────────────────────────────────────────┘
```

#### Integration with Other Agents

**Scientist → DataScientist:**
- Scientist provides: research question, initial hypotheses, relevant variables
- DataScientist uses this to design data retrieval strategy

**DataScientist → Ideologist:**
- DataScientist provides: empirical results, effect sizes, counter-examples
- Ideologist uses this to ground novel hypotheses in real patterns

**DataScientist → Skeptic:**
- DataScientist provides: base rates, false positives, limitations
- Skeptic uses this to constrain overclaiming

**DataScientist → Publisher:**
- DataScientist provides: statistical notation, table specifications
- Publisher formats according to journal style

#### Quality Checklist

Before DataScientist output is accepted:

- [ ] Sample size (N) reported
- [ ] Data sources documented with URLs/API calls
- [ ] Base rates calculated
- [ ] Confidence intervals (not just p-values)
- [ ] Counter-examples listed
- [ ] Limitations acknowledged
- [ ] Raw data saved for reproducibility

### Ideologist Agent - Novel Hypothesis Generator

The Ideologist runs AFTER initial analysis, BEFORE Simulator. It **generates novel hypotheses** to test:

| Capability | Description |
|------------|-------------|
| Divergent thinking | Proposes ideas outside current paradigm |
| Cross-domain mapping | "What works in X might work here" |
| Hypothesis formulation | Testable predictions with falsification criteria |
| Risk assessment | Flags which ideas are worth simulating |

**Example - "87 Toyota fuel efficiency":**
```
IDEOLOGIST OUTPUT:
┌─────────────────────────────────────────────────────────────┐
│ Hypothesis 1: Intake resonance tuning                        │
│   - Map: Air intake as acoustic resonator (ω = c/2L)        │
│   - Prediction: 42Hz resonance improves fuel mixing 3-5%    │
│   - Test: Brian2 models pressure waves as oscillators       │
│                                                              │
│ Hypothesis 2: Exhaust pulse timing                           │
│   - Map: Exhaust pulses as phase-coupled oscillators        │
│   - Prediction: Backpressure tuning at specific RPM         │
│   - Test: Brian2 CPG network with exhaust timing            │
│                                                              │
│ Hypothesis 3: Thermal cycling optimization                    │
│   - Map: Engine temp as relaxation oscillator                │
│   - Prediction: Optimal warmup rhythm reduces rich fuel     │
│   - Test: Brian2 tau relaxation model                       │
└─────────────────────────────────────────────────────────────┘
```

**Ideologist → Simulator loop:**
```
Ideologist proposes 3-5 novel hypotheses
        ↓
Director ranks by testability + impact
        ↓
Simulator runs Brian2 on top 2-3
        ↓
Results feed back to Ideologist (refine/reject/iterate)
```

### Simulator Agent (Brian2) - Universal Rhythm Engine

The Simulator runs AFTER Experimenter, validates ALL research claims against Brian2 oscillator dynamics:

| Domain | Brian2 Maps To | Validates |
|--------|----------------|-----------|
| Neuroscience | Direct SNN simulation | Firing rates, oscillation frequencies |
| Forensics | Timeline → phase array | Alibi gaps = phase desync |
| Governance | Policy → coupled oscillators | Stability exponents |
| Voynich/linguistics | Glyph frequency → rhythm | Periodicity significance |
| Physics | N-body → CPG network | Conservation laws |

**Universal oscillator template:**
```python
# Any domain → Brian2 rhythm extraction
master_eqs = Equations('''
    dphase/dt = omega : 1          # Domain-specific frequency
    drhythm/dt = -rhythm/tau + coupling*sum(sin(diff_phase)) : 1
''')
domain_groups = NeuronGroup(N_events, master_eqs, ...)
```

**When Simulator triggers:**
- Neuroscience research: ALWAYS (validates against 370M spike benchmarks)
- Other domains: When Experimenter proposes testable rhythm hypothesis
- Output: `simulation_results.json` with stability metrics

**Source of truth hierarchy:**
1. Running Brian2 simulation (highest)
2. Validated parameters file (`PARAMETER_VALIDATION_RESULTS.md`)
3. Literature citations (PMID sources)
4. Agent consensus (lowest)

**CRITICAL: Oscillator simulations prove mathematical consistency, NOT empirical validity.**
- Parameters are hand-tuned to produce desired behavior
- No fitting to actual data required
- Must label results as "HYPOTHESIS" not "CONFIRMED" unless:
  - Parameters fit to N > 100 observations
  - Cross-validated on holdout set
  - Beats simple baselines
  - Out-of-sample performance reported

---

## Quality Gates (MANDATORY)

**Before ANY report is published, these checks MUST PASS:**

### Gate 1: Empirical Grounding
For every threshold/percentage claim, MUST show:
- **Dataset**: N, countries, years, sources
- **Base rates**: How often outcome occurs WITHOUT trigger
- **False positives/negatives**: Raw counts
- **Statistical test**: Coefficient, p-value, CI

**If missing → Label as "HYPOTHESIS" not "CONFIRMED"**

### Gate 2: Post-Hoc Flexibility Check
For counter-examples explained away:
- **Count**: How many counter-examples vs supporting cases?
- **Falsifiability**: Is ANY outcome that would prove threshold wrong?
- **If unfalsifiable → Mark "UNTESTABLE"**

### Gate 3: Endogeneity Acknowledgment
If causal direction unresolved:
- Cannot claim "X predicts Y" as causality
- Must frame as "X precedes Y" or "X correlates with Y"
- Label lead times as "association" not "prediction"

### Gate 4: Citation Verification
All citations must be:
- **Verifiable**: DOI/PMID/URL that resolves
- **Accurate**: Actually supports the claim
- **Not fabricated**: NO hallucinated papers

**If unverifiable → Remove or mark "UNVERIFIED"**

---

## Neuroscience Grounding Mode

```
research "question" --grounding neuroscience
```

Loads validated parameters from `grounding/validated_parameters.md`:
- tau_m values per brain region (PMID-cited)
- Oscillation frequencies (EEG/LFP validated)
- Connection delays (anatomically-based)
- Synaptic weights (PSP amplitude matched)
- Known constraints (tau_osc ≤ 10ms, A_osc scaling)

**Integration:**
1. Director loads grounding context
2. Ground Truth agent checks claims against validated parameters
3. Skeptic receives Ground Truth report as constraint
4. All neuroscience claims validated against PMID sources

---

## Execution Flow

```
┌─────────────────────────────────────────────────────────────┐
│  DIRECTOR (main session)                                    │
│  - Receives question                                        │
│  - Checks lab_memory.json for context                       │
│  - Spawns parallel researchers                              │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ SCIENTIST    │    │ SKEPTIC      │    │ HISTORIAN    │
│ ClaudeResearch│    │ GrokResearch │    │ Research     │
│              │    │              │    │              │
│ Truth claims │    │ Challenges   │    │ Citations    │
│ Confidence   │    │ Alternatives │    │ Examples     │
└──────────────┘    └──────────────┘    └──────────────┘
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  DATASCIENTIST (CodexResearcher) ← NEW WAVE 1.5             │
│  - Pulls datasets from World Bank, FRED, OWID               │
│  - Runs regression: outcome ~ predictor + controls          │
│  - Outputs: coefficients, CIs, base rates, counter-examples │
│  - Saves: results/empirical_results.json                    │
│  - Grounds hypotheses in REAL data, not anecdotes           │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  DIRECTOR checks for MAJOR_FLAW from Skeptic                │
│  - If found: HALT, report to user                           │
│  - If clear: continue                                       │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ EXPERIMENTER │    │ PHILOSOPHER  │    │ EXPLAINER    │
│ CodexResearch│    │ Thinking     │    │ GeminiResearch│
│              │    │              │    │              │
│ Concrete test│    │ Implications │    │ Simplified   │
│ designs      │    │ Thought exps │    │ explanation  │
└──────────────┘    └──────────────┘    └──────────────┘
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  IDEOLOGIST (CodexResearcher) - NOW GROUNDED IN DATA        │
│  - Uses DataScientist's empirical results                   │
│  - Novel hypotheses must be consistent with data            │
│  - If data contradicts hypothesis → reject or modify        │
│  - Cross-domain mapping based on REAL patterns              │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  SIMULATOR (Brian2) - CodexResearcher                        │
│  - Maps domain → oscillator network                          │
│  - Runs 10s simulation (or uses validated params)            │
│  - Outputs: stability metrics, rhythm validation             │
│  - Source of truth: simulation > docs > consensus            │
└─────────────────────────────────────────────────────────────┘
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  ARTIST (Media skill)                                        │
│  - Generates actual visualisations from specs               │
│  - Outputs: PNG files, mermaid, etc.                        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  ARCHIVIST (direct write)                                    │
│  - Updates lab_memory.json                                   │
│  - Tracks supported/rejected/unknown                        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼ (every 3rd cycle)
┌─────────────────────────────────────────────────────────────┐
│  SYNTHESISER (PerplexityResearcher)                         │
│  - Cross-cycle pattern detection                            │
│  - Meta-level insights                                      │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼ (FINAL - always runs)
┌─────────────────────────────────────────────────────────────┐
│  PUBLISHER (ClaudeResearcher)                                │
│  - Converts research to academic format                      │
│  - Formats citations (APA/IEEE/Chicago)                     │
│  - Structures IMRaD sections                                │
│  - Applies statistical notation standards                   │
│  - Generates:                                                │
│    ├── README.md (blog format - current)                    │
│    ├── PAPER.md (academic format - IMRaD)                   │
│    └── CITATION.bib (BibTeX references)                     │
│                                                              │
│  ⚠️ CANNOT: Claim novelty, judge merit, take responsibility │
│  ✅ CAN: Format, structure, apply templates                 │
└─────────────────────────────────────────────────────────────┘
```

---

## Spawn Commands

When Director runs, it spawns agents like this:

```python
# Parallel spawn for core analysis
agents = [
    Agent("ClaudeResearcher", prompt=f"SCIENTIST role: Analyze {question}"),
    Agent("GrokResearcher", prompt=f"SKEPTIC role: Challenge assumptions about {question}"),
    Agent(subagent_type="Research", prompt=f"HISTORIAN role: Find literature on {question}")
]

# Wait for all, then check Skeptic for MAJOR_FLAW
results = parallel_execute(agents)

if results["GrokResearcher"].major_flaw:
    HALT("Skeptic found breaking flaw")

# Wave 1.5: DataScientist (NEW - empirical grounding)
if not args.no_data and is_quantitative_question(question):
    Agent("CodexResearcher", prompt=f"""
DATASCIENTIST role: Ground hypotheses in real data

Research question: {question}
Scientist's initial findings: {results["Scientist"].findings}

Your task: Pull REAL datasets and run ACTUAL statistics.

STEP 1 - Identify variables:
- What outcome variables measure the phenomenon?
- What predictor variables test the hypothesis?
- What control variables are needed?

STEP 2 - Find data sources:
- World Bank WDI: api.worldbank.org (inflation, GDP, unemployment)
- FRED: api.stlouisfed.org (US economic indicators)
- Our World in Data: ourworldindata.org/grapher/data.csv
- V-Dem: v-dem.net (democracy indices)
- ACLED: acleddata.com (protest data)

STEP 3 - Retrieve data:
- Use web_fetch to get CSV/JSON from APIs
- Save raw data to results/raw_data/
- Document exact API calls for reproducibility

STEP 4 - Merge & clean:
- Match on ISO country codes + year
- Handle missing data (document method)
- Save to results/analysis_dataset.csv

STEP 5 - Analysis:
- Run regression: outcome ~ predictor + controls
- Calculate: coefficient, SE, 95% CI, p-value
- Report base rates and false positive/negative counts
- List counter-examples explicitly

STEP 6 - Output:
Save to results/empirical_results.json:
{{
  "n_observations": <number>,
  "n_countries": <number>,
  "year_range": [<start>, <end>],
  "main_result": {{
    "coefficient": <value>,
    "se": <value>,
    "ci_95": [<lower>, <upper>],
    "p_value": <value>,
    "interpretation": "<plain language>"
  }},
  "base_rate": <value>,
  "false_positives": <count>,
  "false_negatives": <count>,
  "counter_examples": ["<country year>", ...],
  "data_sources": ["<source>", ...],
  "limitations": ["<limitation>", ...]
}}

CRITICAL:
- Use REAL data, not hypothetical numbers
- Every statistic must be calculable from retrieved data
- If data unavailable, report "INSUFFICIENT DATA" with explanation
- Do NOT fabricate or estimate statistics
""")

# Second wave (after DataScientist)
agents_wave_2 = [
    Agent("CodexResearcher", prompt=f"EXPERIMENTER role: Design tests for {question}"),
    Agent(subagent_type="Thinking", prompt=f"PHILOSOPHER role: Implications of {findings}"),
    Agent("GeminiResearcher", prompt=f"EXPLAINER role: Simplify {findings}")
]

# Wave 2.5: Ideologist (NOW GROUNDED IN DATA)
Agent("CodexResearcher", prompt=f"""
IDEOLOGIST role: Generate novel hypotheses GROUNDED in empirical data

Research question: {question}
DataScientist's empirical results: {empirical_results}

CRITICAL: Your hypotheses must be CONSISTENT with the data above.
If the data shows no effect, do not hypothesize a strong effect.
If the data shows counter-examples, your hypothesis must explain them.

Generate 3-5 novel hypotheses by cross-domain mapping:
1. Identify pattern in data (e.g., nonlinear threshold, habituation)
2. Find analogous pattern in other domain (ecology, medicine, physics)
3. Formulate testable prediction
4. Specify falsification criteria

For each hypothesis, provide:
- Name: Descriptive title
- Source Domain: Where the pattern comes from
- Prediction: What should happen if hypothesis is true
- Data Consistency: How this fits with DataScientist's results
- Falsification: What evidence would prove it wrong

OUTPUT FORMAT:
```
HYPOTHESIS N: [Name]
- Map: [Domain pattern applied to this problem]
- Prediction: [Testable claim]
- Data Fit: [Consistent with empirical results because...]
- Falsification: [Would be disproven if...]
```
""")

# Third wave: SIMULATOR (Brian2 validation)
Agent("CodexResearcher", prompt=f"""
SIMULATOR role: Validate claims via Brian2 oscillator dynamics

Domain: {detected_domain}
Claims to validate: {experimenter_claims}
Hypotheses from Ideologist: {ideologist_hypotheses}
Empirical constraints from DataScientist: {empirical_results}

CRITICAL: Parameters must be CONSISTENT with empirical data.
If DataScientist found coefficient = 0.034, your coupling strength
should produce similar effect sizes, not arbitrary values.

Map domain → oscillator network:
- Neuroscience → Direct SNN (run 10s sim, check firing rates)
- Forensics → Timeline phases (check alibi rhythm desync)
- Governance → Policy CPG (check stability exponent)
- Linguistics → Glyph frequency (check periodicity significance)
- Physics → Coupled oscillators (check conservation)
- Automotive → Intake/exhaust as resonators (check phase alignment)

For EACH Ideologist hypothesis:
1. Map to Brian2 oscillator model
2. Set parameters consistent with empirical data
3. Run 10s simulation
4. Extract stability metrics (Lyapunov exponent, phase coherence)
5. Report: STABLE / UNSTABLE / INCONCLUSIVE

IMPORTANT: Label results as "MATHEMATICALLY CONSISTENT" not "CONFIRMED"
unless parameters were fit to N > 100 observations with cross-validation.

Output: simulation_results.json with stability metrics + hypothesis validation
""")

# Fourth wave: Artist (if images enabled)
if not args.no_images:
    Agent(subagent_type="Media", prompt=f"ARTIST role: Generate visualisations for {findings}")

# Fourth wave: Archivist
write_file("lab_memory.json", update_memory(all_results))

# Fifth wave: Synthesiser (every 3rd cycle)
if cycle % 3 == 0:
    Agent("PerplexityResearcher", prompt=f"SYNTHESISER role: Cross-cycle patterns for {all_cycles}")

# FINAL wave: Publisher (always runs)
Agent("ClaudeResearcher", prompt=f"""
PUBLISHER role: Convert research to academic format

Research findings: {all_results}
Empirical results: {empirical_results}
Target style: {style or 'apa'}
Target journal: {journal or 'general'}

Generate TWO outputs:
1. README.md - Blog format (current style)
2. PAPER.md - Academic format (IMRaD structure)

CRITICAL CONSTRAINTS:
- You are a FORMATTER, not an AUTHOR
- DO NOT claim novelty or judge merit
- DO NOT fabricate citations
- All statistics must come from DataScientist's empirical_results.json
- If no empirical data, label claims as "HYPOTHESIS" not "CONFIRMED"
- Use templates from specification
- Human verification required before submission
""")
```

---

## Output Format

After all agents complete, Director assembles TWO outputs:

### README.md (Blog Format - Current Style)

```markdown
# Research Report: [Question]

## Quick Summary
[From Explainer]

## What The Data Shows
[From Scientist - ClaudeResearcher]

## Why This Might Be Wrong
[From Skeptic - GrokResearcher]

## What To Test Next
[From Experimenter - CodexResearcher]

## Real-World Context
[From Historian - Research skill]

## What It Means
[From Philosopher - Thinking skill]

## The Simple Version
[From Explainer - GeminiResearcher]

## Visualisations
[Generated by Media skill]

## Confidence Assessment
- ✅ Supported: [claims]
- ❌ Rejected: [claims]
- ❓ Unknown: [claims]

## Validation Hooks
[What would falsify this]
```

### PAPER.md (Academic Format - IMRaD Structure)

Generated by Publisher agent:

```markdown
# [Title]

## Abstract
[200-300 words: Background 15-20%, Methods 15-25%, Results 40-50%, Conclusion 10-15%]

## 1. Introduction
### 1.1 Background and Context
### 1.2 Literature Review
### 1.3 Research Gap
### 1.4 Research Questions / Hypotheses
### 1.5 Study Objectives

## 2. Methods
### 2.1 Research Design
### 2.2 Data Sources
### 2.3 AI System Documentation (if applicable)
- Model: [e.g., GPT-4o]
- Version: [e.g., 2024-05-13]
- Parameters: temperature, max_tokens, etc.
- Prompts: [Full text in Appendix A]
### 2.4 Analysis Techniques
### 2.5 Ethical Considerations

## 3. Results
### 3.1 Descriptive Statistics
### 3.2 Primary Outcomes
### 3.3 Secondary Outcomes
### 3.4 Figures and Tables

## 4. Discussion
### 4.1 Summary of Key Findings
### 4.2 Interpretation
### 4.3 Comparison to Prior Work
### 4.4 Implications
### 4.5 Limitations
### 4.6 Future Directions
### 4.7 Conclusion

## References
[Formatted per target journal style]

## Appendix A: Complete Prompt Documentation
[If prompts > 500 words]

## Data Availability Statement
[Template-based]

## Code Availability Statement
[Template-based]

## Author Contributions
[CRediT taxonomy format]

## Conflicts of Interest
[Declaration]
```

### CITATION.bib (BibTeX References)

Generated by Publisher agent from all cited sources.

---

## Hard Rules

0. **PRE-FLIGHT CHECKLIST IS MANDATORY** - Print checklist, track all waves, never skip
1. **ClaudeResearcher has FINAL AUTHORITY on conclusions**
2. **GrokResearcher can HALT workflow with MAJOR_FLAW**
3. **All agents run in PARALLEL where possible**
4. **Media skill generates actual images, not just specs**
5. **lab_memory.json updates after every cycle**
6. **PerplexityResearcher runs every 3rd cycle**
7. **Publisher ALWAYS runs last, outputs both README.md and PAPER.md**
8. **Publisher CANNOT claim novelty or judge merit - human verification required**
9. **All citations must be verified against real databases before final output**
10. **ALWAYS commit outputs to git - push if --push flag**

---

## Memory Schema

`lab_memory.json`:

```json
{
  "project": "slug-from-question",
  "created": "YYYY-MM-DD",
  "runs": [
    {
      "cycle": 1,
      "date": "YYYY-MM-DD HH:MM",
      "question": "...",
      "result": "...",
      "supported": ["..."],
      "rejected": ["..."],
      "unknown": ["..."],
      "next_tests": ["..."],
      "agents_used": ["ClaudeResearcher", "GrokResearcher", "..."],
      "status": "needs_validation|complete|blocked"
    }
  ],
  "dead_ends": [],
  "open_questions": [],
  "key_insights": []
}
```

---

## Invocation

```
research "Your question here"
```

With options:

```
research "question" --mode kid --cycles 5 --no-images
```

| Flag | Effect |
|------|--------|
| `--mode journalist` | Explainer uses punchy style (default) |
| `--mode storyteller` | Explainer uses narrative style |
| `--mode kid` | Explainer uses simple analogies |
| `--cycles N` | Run N cycles |
| `--no-images` | Skip Media skill (faster) |
| `--no-data` | Skip DataScientist wave (qualitative only) |
| `--deep` | Use extensive research mode |
| `--grounding neuroscience` | Load validated SNN parameters |

---

## Research Frequencies (Oscillation Modes)

Like brain oscillations, research has different "frequencies":

| Mode | Brain Analog | Behavior |
|------|--------------|----------|
| **alpha** (default) | 8-12 Hz | Standard research, balanced exploration |
| **gamma** | 30-100 Hz | `--deep` flag - intense focus, exhaustive analysis |
| **theta** | 4-8 Hz | Philosophical reflection, meaning-seeking |
| **beta** | 13-30 Hz | Experimental design, test-focused |

Usage:
```
research "question" --gamma    # deep analysis
research "question" --theta    # philosophical
research "question" --beta     # experiment-focused
```

---

## Git Output Structure

Every research project creates:

```
research-project/
├── README.md                 # Blog format report (current style)
├── PAPER.md                  # Academic format (IMRaD structure) ← NEW
├── LICENSE                   # MIT © Andrew Hagan 2026
├── CITATION.bib              # BibTeX references ← NEW
├── header_image.png          # Generated header
├── simulation.py             # If applicable
├── results/
│   ├── data.csv
│   └── plots/
│       ├── cascade_distribution.png
│       └── timeline.png
├── docs/
│   ├── RESEARCH_REPORT.md
│   ├── LITERATURE_REVIEW.md
│   └── VALIDATION_PLAN.md
├── lab_memory.json
└── tests/                    # If applicable
    └── validation_tests.py
```

---

## Git Configuration (MANDATORY for Push)

**Before pushing to GitHub, ALWAYS configure git with correct identity:**

```bash
git config user.name "Peace-png"
git config user.email "peaceful0369@gmail.com"
```

This ensures commits are attributed to Peace-png on GitHub. Do NOT use:
- `peace@users.noreply.github.com` (links to wrong account)
- Any other email (will show wrong contributor)

---

## License

All Research Lab outputs are licensed under:

**Creative Commons Attribution 4.0 International (CC BY 4.0)**

Copyright 2026 Peace-png

You are free to:
- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material for any purpose

Under the following terms:
- **Attribution** — You must give appropriate credit to Peace-png

**Citation format:**
```
Peace-png. (2026). [Research Title].
Retrieved from https://github.com/Peace-png/[repo-name]
```

---

## The Promise

You ask the question.
Real specialist agents research in parallel.
Output is publication-ready.

Same structure every time. Consistent across all repos.

*"I can run the data but I don't know what it means."* → **Solved.**

---

## The Cave Wall Principle

> The cave wall already exists. Everything is already on it. The research question is the spike that illuminates what was always encoded. You don't paint the wall — you reveal it.

**Research doesn't create new knowledge. It reveals patterns that already exist in the data.**

The agents don't manufacture findings—they illuminate what's already there:
- Scientist reveals the structure
- Skeptic reveals the gaps
- Philosopher reveals the meaning
- Historian reveals the context

Your question is the light. The patterns were always encoded.

---

## Cross-Session Memory (ClawMem)

Research Lab outputs are indexed by ClawMem for true session persistence:

### How It Works

1. **Pre-research:** Hooks auto-surface relevant prior research from indexed collections
2. **During research:** Lab agents can access MCP tools for targeted retrieval
3. **Post-research:** `decision-extractor` captures findings
4. **Cross-session:** Next session auto-surfaces relevant prior research

### Indexed Collections

| Collection | Path | Contents |
|------------|------|----------|
| research-lab | `~/.claude/skills/ResearchLab/memory/` | Research Lab memory files |
| pai-memory | `~/.claude/projects/-home-peace/memory/` | PAI cross-session memory |
| conscious-snn | `~/conscious_snn/docs/` | Conscious SNN research |
| governance-physics | `~/research-governance-physics/` | Governance physics research |

### MCP Tools Available

When escalated to Tier 3 retrieval:
- `memory_retrieve(query)` — Auto-routing retrieval
- `query(query)` — Full hybrid search (BM25 + vector + rerank)
- `intent_search(query)` — Causal/entity chains with graph traversal
- `search(query)` — BM25 only (fast, keyword matching)
- `timeline(docid)` — Temporal neighborhood

### Integration Details

See: `memory/CLAWMEM_INTEGRATION.md`
