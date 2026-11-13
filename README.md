# Vendor Intelligence Advisor

**From customer reviews to evidence-grounded vendor decisions.**

[**Launch the interactive dashboard**](https://codebynaga.github.io/vendor-intelligence-advisor/dashboard/) · [Methodology](docs/METHODOLOGY.md) · [Team presentation](docs/team_presentation.pdf)

> **Research demonstration, not a live Amazon service.** The dashboard uses fixed outputs from the supplied team presentation and notebook. It does not query Amazon or generate recommendations on demand.

## Why this matters

A star rating says customers are unhappy, but not **what to fix**. Vendors need to distinguish product-quality issues (durability, fit, support) from expectation gaps (listing descriptions, sizing claims), then verify the evidence before changing products or listings. This project turns unstructured review text into **testable improvement hypotheses**, rather than generic sentiment scores.

## What the tool does

1. **Sample and join** historical Amazon Reviews 2023 *Clothing, Shoes & Jewelry* reviews and product metadata by parent ASIN.
2. **Detect complaints** using attribute-level lexical rules, clause-level VADER sentiment and low-star lift.
3. **Retrieve context** with TF-IDF comparisons to listing text and exploratory LDA topics.
4. **Use an LLM selectively** to interpret ambiguous reviews and draft actions, under cost limits.
5. **Verify evidence** against review IDs and source text; reject unsupported semantic annotations and retain lexical fallback.
6. **Recommend a check**: proposed product test, listing clarification or additional evidence gathering.

## Demonstrated results (historical sample)

| Metric | Saved result | Interpretation |
|---|---:|---|
| Matched analytical reviews | 8,535 | Not a representative population estimate |
| Matched parent products | 5,221 | Sampled metadata/review overlap |
| Eligible demonstration parents | 9 | At least 20 reviews and 3 low-star reviews |
| Selected demo products | 5 | 246 reviews total |
| Semantic reviews selected | 79 | Candidate reviews for LLM interpretation |
| Accepted semantic annotations | 24 | 30.4% evidence acceptance, **not model accuracy** |
| Lexical fallbacks | 55 | Retained when semantic evidence did not pass checks |
| Generated change proposals | 16 | 10 GPT-generated; 6 evidence-derived fallbacks |
| API cost in saved session | ~$0.009 | Historical run only; not a pricing guarantee |

**Example:** For SHAPERMINT (23 sampled reviews), the hybrid pipeline found 3 negative listing-mismatch mentions versus 1 lexical detection, and 6 fit/sizing mentions versus 3. These are **additional detections, not validated improvements in precision or recall**. Proposed next step: check fit and listing claims before making changes.

## Business applications

- **Product quality:** prioritize durability, support, material and stitching investigations.
- **E-commerce content:** test clearer sizing, limitations and product-description claims.
- **Vendor operations:** create an auditable backlog of issues, supporting evidence and verification steps.
- **Continuous improvement:** test one change, then monitor independent complaint, return and rating data.

The project does **not** estimate financial ROI, prove causality, or establish defect rates.

## Dashboard

Five views: **Overview**, **Diagnostics**, **Recommendations**, **Business Insights**, and **Methodology**. The dashboard uses the **Midnight Violet** dark palette with a complementary lavender-tinted light mode. Includes theme toggle, product selection, action filtering and CSV export. All data is embedded for reliable static hosting.

## Reproduce the notebook

```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook notebooks/vendor_review_advisor.ipynb
```

Download the original Amazon Reviews 2023 category review and metadata JSONL files from the [Amazon Reviews 2023 dataset (McAuley Lab, UC San Diego)](https://amazon-reviews-2023.github.io/) under the dataset's license and terms. The notebook expects `Clothing_Shoes_and_Jewelry.jsonl` and `meta_Clothing_Shoes_and_Jewelry.jsonl` in its configured project directory. **Edit `PROJECT_DIR` in the notebook** to point to the folder containing these files; the saved notebook originally used a local working directory. Run cells in order. Large source files are **not included**. A new run may require a network connection and an OpenAI API key; costs and output may differ.

**Reproducibility note:** This release includes the original analysis logic with outputs cleared to avoid embedding local file paths and unreviewed customer excerpts. The interactive dashboard is a *historical snapshot* of the reported findings, not regenerated automatically from the notebook. Reproducing the saved run requires the source dataset and the same sampling/configuration.

## Methodological limitations and evidence safeguards

Do not report precision, recall, F1, or model superiority. The random byte-block sample is reproducible but clustered; reviews and metadata were independently sampled, resulting in about **3.05% join coverage**. The source reviews may not align with the current listing version. Some recommendations have very small support. See [Methodology & limitations](docs/METHODOLOGY.md).

## Team attribution

Developed as an **MSBA 2026 Analytics for Unstructured Data team project** by **Evelyn Chis, Dhilan Vivek, Elena Reyes, Kosam Ganjoo, and Naga Thiyagarajan**. The dashboard and repository packaging were prepared as a portfolio presentation layer for the team project. No affiliation with or endorsement by Amazon.

## Future outlook

Human-labeled evaluation and inter-annotator agreement; representative/stratified sampling; product-variant and listing-version reconciliation; stronger confidence intervals; prospective experiments on product and listing changes; privacy and content-usage review; and operational monitoring before any production use.

## Dataset citation

**Amazon Reviews 2023**, McAuley Lab, UC San Diego: https://amazon-reviews-2023.github.io/. The source site requests citation of Hou et al., *Bridging Language and Items for Retrieval and Recommendation* (2024). This project uses the **Clothing, Shoes & Jewelry** subset; full-source dataset counts should not be confused with the sampled analytical cohort.
