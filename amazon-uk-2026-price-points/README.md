# Amazon UK price endings, round-number thresholds and price bands (Sept 2026)

How Amazon UK prices end, how far products crowd under round-pound thresholds, which seller groups use .99 pricing, and how often each price band shows a 'bought in past month' sales label.

- **Rows:** 38
- **File:** `amazon-uk-2026-price-points.csv`
- **Marketplace:** amazon.co.uk
- **Snapshot:** 2026-09-23/2026-09-24
- **Licence:** CC BY 4.0
- **Attribution:** Scrapewise, snapshot of amazon.co.uk 23-24 Sep 2026

## Columns

| Column | What it holds |
|---|---|
| `dataset` | Dataset slug, the same on every row of this file. |
| `row_id` | Stable id for the row. Derived from dataset + grain + key + metric, so it does not move when rows are added. |
| `grain` | What the row is about: a country, a category, a price band, a rating band, a search keyword, and so on. |
| `key` | The name of that thing, for example `China` or `Health and Supplements`. |
| `metric` | What was measured. |
| `value_num` | The number. Always a number, never text, and never carries its unit. |
| `unit` | `percent`, `count`, `gbp`, `ratio`, `stars`, `reviews` or `ratings`. |
| `basis_n` | How many products or sellers the figure rests on. Empty when the post did not print a denominator. |
| `qualifier` | `exact`, `approx` (rounded in the post), `minimum` (a floor, not a count) or `excerpt_top_n` (the post printed only part of a longer list). |
| `coverage` | What the figure covers and what it leaves out. |
| `source_url` | The post this row was published in. |
| `snapshot_date` | When the data was collected. |

## Metrics in this file

- `amazon_is_a_seller_share`
- `below_vs_at_ratio`
- `label_1k_plus_share`
- `median_price`
- `price_ends_99_share`
- `priced_product_share`
- `product_count`
- `product_count_at`
- `product_count_below`
- `sales_label_share`

## Source posts

- [amazon-uk-charm-pricing-99-endings-2026](https://scrapewise.ai/blogs/amazon-uk-charm-pricing-99-endings-2026)
- [price-threshold-psychology-amazon-uk-2026](https://scrapewise.ai/blogs/price-threshold-psychology-amazon-uk-2026)
- [best-price-point-to-sell-on-amazon-uk-2026](https://scrapewise.ai/blogs/best-price-point-to-sell-on-amazon-uk-2026)

Method: [how the data was collected](https://scrapewise.ai/blogs/how-we-scraped-amazon-uk-search-results-2026). Full report: [Amazon UK Marketplace Report 2026](https://scrapewise.ai/blogs/amazon-uk-marketplace-report-2026).

## Read this before using the numbers

- Every figure is an aggregate. There are no seller names, addresses, contact details, product
  titles or ASINs in this file, and no Amazon page content is redistributed.
- The sample is keyword-driven and taken at one moment, so it is not every product or every seller
  on amazon.co.uk. Read `coverage` on each row.
- Rows marked `minimum` come from Amazon's rounded "bought in past month" labels. They are floors.
- A figure whose `basis_n` is empty was published without a denominator. It is still the published
  figure; it just cannot be re-based.
- Medians, not means. The method post explains why.
