# Evaluation Methods

This document outlines how the system evaluates text using the analysis modules.

## 1. Emotional Tone Evaluation
- Identify sentiment direction (positive, negative, neutral)
- Measure intensity
- Detect emotional shifts across the text

## 2. Deception Evaluation
- Flag misleading or vague phrasing
- Identify hidden assumptions
- Detect persuasive framing
- Assign a risk level

## 3. Reasoning Drift Evaluation
- Detect topic drift
- Identify emotional drift
- Identify logic drift
- Compute a stability score

## 4. Combined Assessment
Each module returns structured data.
A combined evaluator can merge these signals to produce a unified interpretation.
