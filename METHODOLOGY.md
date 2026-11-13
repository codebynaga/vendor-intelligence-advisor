# Methodology, provenance, and evaluation gaps

## Source
Amazon Reviews 2023, Clothing, Shoes & Jewelry, review and metadata JSONL. The supplied notebook and team presentation are the sources of the dashboard snapshot. Raw files are not distributed.

## Sampling
The saved notebook sampled 512 review blocks and 2,048 metadata blocks at 256 KiB each (128 + 512 MiB). Retained 280,295 usable sampled reviews and 215,640 metadata records; matched 8,535 analytical reviews from 5,221 parent products. Matching coverage was 3.05% of the retained sampled reviews. The byte-block design samples locations, not uniformly independent review rows; adjacent records may cluster.

## Pipeline
1. Deduplicate, join on parent ASIN, cap at 200 reviews per parent.
2. Attribute taxonomy and clause-level VADER sentiment; compute complaint shares and low-star lift.
3. TF-IDF retrieval against listing language and exploratory LDA topics.
4. Select uncertain reviews for GPT-4o mini semantic annotation and action drafts.
5. Validate structured outputs and cited review evidence; use lexical fallback when checks fail.

Low-star lift = P(attribute mentioned | 1–2-star review) / P(attribute mentioned). It is an association, not a causal effect.

## Evidence acceptance versus predictive quality
79 reviews selected for semantic review, 24 annotations accepted and 55 lexical fallbacks. 24/79 = 30.4% **evidence acceptance**, not classification accuracy. The notebook's manual evaluation output showed zero human-reviewed rows; therefore precision, recall and F1 remain unknown.

## Business output
The five demo products had 246 reviews. Four had repeated actionable signals; one required further evidence. The presentation reports 16 proposed changes (10 GPT, six evidence-derived). The dashboard intentionally summarizes the product-level findings rather than fabricating individual review quotes or detailed 16-action content not included as separate artifacts.

## Risks and limitations
- Sampling and metadata join are not representative of the category.
- Sample sizes for several products are 20–34 reviews; rare mentions may be unstable.
- Current listing content may differ from listing content when reviews were written.
- Additional semantic detections may include false positives; human validation is incomplete.
- No causal or financial-impact assessment; proposed actions must be tested.
- Historical static outputs; not an operational, live Amazon integration.
- Team contributions should be attributed accurately.


Dataset source: Amazon Reviews 2023, McAuley Lab, UC San Diego, https://amazon-reviews-2023.github.io/.
