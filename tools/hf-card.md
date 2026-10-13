---
license: cc-by-4.0
language:
- en
tags:
- e-commerce
- amazon
- retail
- pricing
- marketplace
- united-kingdom
pretty_name: Amazon UK marketplace snapshot (September 2026)
size_categories:
- n<1K
---

# Amazon UK marketplace snapshot, September 2026

180 aggregate figures describing one snapshot of **amazon.co.uk**, taken **23-24 September 2026**,
built from public pages by [Scrapewise](https://scrapewise.ai). Free to use with attribution.

Nothing here is row-level. Every value is a count, a share or an average over a group of sellers or
products, so there are no seller names, addresses, emails or ASINs in these files.

| File | Rows | What it covers |
|---|---|---|
| `amazon-uk-2026-seller-geography.csv` | 91 | Sellers by declared country, UK postcode area and VAT status |
| `amazon-uk-2026-price-points.csv` | 38 | Price endings, round-number thresholds and price bands |
| `amazon-uk-2026-ratings-and-feedback.csv` | 51 | Product star ratings and seller feedback scores |

## Columns

All three files share one shape, so they stack.

| Column | What it is |
|---|---|
| `dataset` | Which of the three files the row belongs to |
| `row_id` | Stable 10-character id for the row, so you can join across versions |
| `grain` | What one row is about: a country, a UK postcode area, a price band, a rating bucket |
| `key` | The specific thing at that grain, e.g. `CN`, `LONDON_E`, `9.99` |
| `metric` | What is being measured, e.g. `seller_share_pct`, `product_count` |
| `value_num` | The number. Always a number, never text, never carrying a unit |
| `unit` | What `value_num` is in: `pct`, `count`, `gbp`, `stars`, `ratio` |
| `basis_n` | How many sellers or products the figure rests on. Blank where it does not apply |
| `qualifier` | How to read the number: `exact`, `approx`, `median`, `mean`, `min`, `max` |
| `coverage` | Which part of the sample the figure covers, e.g. `all_sellers`, `priced_products` |
| `source_url` | The published post the figure comes from |
| `snapshot_date` | `2026-09-23/2026-09-24` on every row |

## What the sample is

A keyword-driven sample of amazon.co.uk, collected 2026-09-23/2026-09-24: 197,022 products,
55,660 public seller profiles and 394,727 seller-product links.
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

Areas, keywords or groups resting on fewer than 10 sellers or products are left out, which is also
what the posts do.

## How these files are built

Every row is a figure already published in a post on https://scrapewise.ai, hand-transcribed into one
shape and checked back against the post. Nothing is recomputed. Each row names the post it came from,
so a correction to a post is a correction to the dataset.

Cells that a spreadsheet would run as a formula are written as text, using the same CSV writer as the
Scrapewise data export.

## Verifying a download

`checksums.txt` holds a SHA-256 for every data file.

```sh
shasum -a 256 -c checksums.txt
```

## Dates

These files are a snapshot, not a feed. There is no "latest" version: 23-24 September 2026 is what
they describe, and they are not updated in place.

## Licence and attribution

- **Licence:** CC BY 4.0
- **Attribution:** Scrapewise, snapshot of amazon.co.uk 23-24 Sep 2026

The figures are aggregates computed by Scrapewise from public amazon.co.uk pages. No Amazon page
content is redistributed and Scrapewise is not affiliated with Amazon. Product and company names
belong to their owners.

## Where else to get this

The same figures, from the same build:

- [GitHub](https://github.com/BEBOTECH-OU/scrapewise-datasets)
- [Kaggle](https://www.kaggle.com/datasets/siimbrazier/amazon-uk-marketplace-snapshot-september-2026)
