# Scrapewise sample datasets

Small, aggregated, dated datasets built from public e-commerce pages by
[Scrapewise](https://scrapewise.ai). Free to use with attribution.

This set covers one snapshot of **amazon.co.uk**, taken **2026-09-23/2026-09-24**:
180 aggregate figures across 3 files.

| Dataset | Rows | What it covers |
|---|---|---|
| [`amazon-uk-2026-seller-geography`](amazon-uk-2026-seller-geography/) | 91 | Amazon UK sellers by declared country, UK postcode area and VAT status (Sept 2026) |
| [`amazon-uk-2026-price-points`](amazon-uk-2026-price-points/) | 38 | Amazon UK price endings, round-number thresholds and price bands (Sept 2026) |
| [`amazon-uk-2026-ratings-and-feedback`](amazon-uk-2026-ratings-and-feedback/) | 51 | Amazon UK product star ratings and seller feedback scores (Sept 2026) |

## Licence and attribution

- **Licence:** CC BY 4.0
- **Attribution:** Scrapewise, snapshot of amazon.co.uk 23-24 Sep 2026

The figures are aggregates computed by Scrapewise from public amazon.co.uk pages. No Amazon
page content is redistributed and Scrapewise is not affiliated with Amazon. Product and company
names belong to their owners.

## What the sample is

A keyword-driven sample of amazon.co.uk, collected 2026-09-23/2026-09-24:
197,022 products, 55,660 public
seller profiles and 394,727 seller-product links.
Method: [how the data was collected](https://scrapewise.ai/blogs/how-we-scraped-amazon-uk-search-results-2026).

Base counts used by the figures:

- `products`: 197,022
- `products_priced`: 193,782
- `products_rated`: 182,700
- `products_single_seller`: 141,582
- `products_with_offer_data`: 196,376
- `seller_product_links`: 394,727
- `sellers`: 55,660
- `sellers_rated`: 51,374

## How these files are built

Every row is a figure already published in a post on https://scrapewise.ai, hand-transcribed into one shape
and checked back against the post. Nothing is recomputed. Each row names the post it came from, so a
correction to a post is a correction to the dataset.

Build: `node scripts/build-datasets.mjs` in the Scrapewise site repo. The CSV writer is shared with
the Scrapewise data export, so cells that a spreadsheet would run as a formula are written as text.

Areas, keywords or groups resting on fewer than 10 sellers or products are left out, which is
also what the posts do.

## Verifying a download

`checksums.txt` holds a SHA-256 for every file.

```sh
shasum -a 256 -c checksums.txt
```

## Dates

These files are a snapshot, not a feed. There is no "latest" version: 2026-09-23/2026-09-24 is what
they describe, and they are not updated in place.
