# Test Suite: Governance Physics Validation

## Overview

Seven concrete tests designed to address skeptic concerns and validate/falsify governance physics framework claims.

---

## Test 1: Exponent Falsification Test
**Addresses: Metaphor-Not-Physics**

### Hypothesis
If governance scaling is a true physical law, lambda MUST scale as N^0.5 with narrow tolerance. If lambda scales equally well as N^0.4 or N^0.6, the √N claim is curve-fitting.

### Method
1. Collect communication frequency from 50 organizations at 5 sizes (N=10,50,100,500,1000)
2. Fit power law: lambda = a*N^k
3. Use Bayesian model comparison (Bayes Factor) to compare k=0.5 vs free k

### Data Required
- Enron email corpus
- Slack/Discord logs from open-source projects
- University department communication
- Military unit studies

### Success Criteria
- Bayes Factor > 10 favoring k=0.5
- Best-fit k within 0.45-0.55

### Failure Criteria
- Bayes Factor < 3
- Best-fit k < 0.4 or > 0.6
- R² < 0.7

### Estimated Effort
40 hours + $0-500

---

## Test 2: Out-of-Sample Prediction Test
**Addresses: Curve-Fitting**

### Hypothesis
Parameters fitted on one dataset should predict outcomes on a different dataset with meaningful accuracy.

### Method
1. Split data into TRAIN (50 orgs) and TEST (50 orgs)
2. Fit G/lambda on TRAIN
3. Predict G on TEST using only observable characteristics
4. Compare predicted vs measured

### Data Required
- BoardEx database
- Compustat
- ISS Governance ratings
- Minimum 100 public companies

### Success Criteria
- MAPE < 25%
- Correlation > 0.6

### Failure Criteria
- MAPE > 40%
- Correlation < 0.3
- Systematic bias

### Estimated Effort
60 hours + $2000-5000 (WRDS access)

---

## Test 3: G Range Narrowing Test
**Addresses: Unfalsifiable G**

### Hypothesis
If G is meaningful, it should have LOW variance within similar systems. Wide variance means G is a fitted parameter.

### Method
1. Select 50 companies in ONE industry (e.g., regional banks, 100-500 employees)
2. Measure G using identical protocol
3. Calculate coefficient of variation (CV = std/mean)

### Data Required
- SEC filings
- Board meeting minutes
- Employee counts from LinkedIn
- Communication proxies

### Success Criteria
- CV < 0.3
- G range within group < 0.3 wide

### Failure Criteria
- CV > 0.5
- G range spans > 0.5 of claimed range

### Estimated Effort
80 hours + $0-200

---

## Test 4: Failed System Analysis
**Addresses: Survivor Bias**

### Hypothesis
Failed systems should show SAME G distribution as successful ones if laws are universal. Different distributions = framework measures success, not governance.

### Method
1. Identify 50 FAILED organizations (bankruptcy, dissolution)
2. Measure G in final 2 years
3. Compare to 50 matched SUCCESSFUL orgs using Kolmogorov-Smirnov test

### Data Required
- PACER bankruptcy records
- DeepDAO dissolved list
- Defunct organization archives
- Capital IQ/FactSet

### Success Criteria
- KS test p-value > 0.05
- Mean G differs by < 20%

### Failure Criteria
- KS test p-value < 0.01
- Bimodal separation

### Estimated Effort
100 hours + $500-2000

---

## Test 5: Pre-Registration Longitudinal Study
**Addresses: Circular Simulations**

### Hypothesis
We can predict which organizations will have governance crises BEFORE they happen.

### Method
1. Identify 100 newly-formed organizations
2. Measure initial G
3. Pre-register: G < 0.3 predicts crisis within 2 years
4. Track outcomes

### Data Required
- New DAO formation (Ethereum blockchain)
- New startups (Crunchbase)
- New chapters (national HQs)
- Outcome tracking

### Success Criteria
- Accuracy > 70%
- Precision > 60%
- Recall > 60%

### Failure Criteria
- Accuracy < 55%
- Precision < 40%
- Recall < 40%

### Estimated Effort
50 hours + 2 years + 30 hours + $200-1000

---

## Test 6: Cross-Domain G Comparison
**Addresses: Incomparable Domains**

### Hypothesis
G in neural networks, corporations, and DAOs should be comparable if laws are universal.

### Method
1. 10 systems each from neural (fMRI), corporate (boards), DAOs (on-chain)
2. Normalize G to [0,1] using identical definition
3. Compare distributions

### Data Required
- Human Connectome Project
- BoardEx
- DeepDAO
- Cross-domain normalization protocol

### Success Criteria
- All domain means within 2x
- Domain explains < 30% of variance

### Failure Criteria
- Any domain 5x+ different
- Domain explains > 50% of variance

### Estimated Effort
120 hours + $0-3000

---

## Test 7: Null Model Comparison
**Addresses: All Concerns**

### Hypothesis
Framework should outperform naive models (constant G, random G, size-only).

### Method
1. Compare framework predictions vs 3 null models:
   - Constant=0.5
   - Uniform random
   - Size-only
2. Use MSE, AIC/BIC, out-of-sample accuracy

### Data Required
- Same as Test 2

### Success Criteria
- Framework beats ALL nulls
- > 20% improvement over size-only

### Failure Criteria
- No improvement over random
- Indistinguishable from size-only

### Estimated Effort
30 hours (if Test 2 data available) + $0

---

## Priority Ranking

| Rank | Test | Score | Rationale |
|------|------|-------|-----------|
| 1 | Test 2: Out-of-Sample | 8 | Directly tests curve-fitting; WRDS data exists |
| 2 | Test 3: G Range Narrowing | 8 | Tests if G is meaningful; public data |
| 3 | Test 4: Failed System | 7 | Critical for survivor bias |
| 4 | Test 1: Exponent | 6 | Tests "physics" claim |
| 5 | Test 7: Null Model | 6 | Easy if other data collected |
| 6 | Test 6: Cross-Domain | 5 | Important but measurement hard |
| 7 | Test 5: Pre-Registration | 4 | Highest value, 2-year timeline |

---

## What We Can Test NOW

### Immediately Executable (0-2 weeks)

1. **Test 3 Partial**: SEC filings + LinkedIn data, proxy G = (board meetings × board size) / employees
   - 20 hours, $0

2. **Test 7**: Null model analysis on any existing governance dataset
   - 10 hours, $0

3. **Test 4 Partial**: DeepDAO + Etherscan for dissolved vs active DAO comparison
   - 30 hours, $0

### Near-Term (2-8 weeks)

4. **Test 1**: Enron email corpus exponent analysis
   - 40 hours, $0

5. **Test 2**: Request academic governance datasets for train/test split
   - 60 hours, $0-500

---

## Concern-to-Test Mapping

| Skeptic Concern | Test(s) |
|-----------------|---------|
| Metaphor-not-physics | Test 1 (Exponent Falsification) |
| Curve-fitting | Test 2 (Out-of-Sample), Test 7 (Null Model) |
| Unfalsifiable G | Test 3 (Range Narrowing) |
| Incomparable Domains | Test 6 (Cross-Domain) |
| Survivor Bias | Test 4 (Failed System Analysis) |
| Circular Simulations | Test 5 (Pre-Registration) |
