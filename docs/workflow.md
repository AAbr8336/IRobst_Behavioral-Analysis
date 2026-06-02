# Workflow

This document describes how the system processes text from input to final evaluation.

## 1. Input
Raw text is provided to the system.

## 2. Preprocessing
- Clean the text
- Normalize casing
- Remove unnecessary whitespace

## 3. Module Analysis
Each module runs independently:
- Emotional analysis
- Deception analysis
- Reasoning drift analysis

## 4. Aggregation
Outputs from each module are combined into a unified structure.

## 5. Interpretation
A higher-level evaluator can interpret the combined signals to produce:
- summaries
- risk assessments
- reasoning stability insights
