# [GigEfx Pricing Explorer](https://gigefx-demo.vercel.app/)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white)](https://www.chartjs.org/)
[![Vercel](https://img.shields.io/badge/Vercel-171717?style=for-the-badge&logo=vercel&logoColor=white)](https://vercel.com/)

Explore real electronics prices from a documented public retailer API.

## Features

- Product search, stock filtering, price sorting, and retailer links.
- Collection timestamps and JSON exports.
- Validated, versioned price snapshots and comparison baselines.
- Missing and zero-price records are excluded rather than presented as free products.

This integration uses Little Bird Electronics in Australia. Prices are AUD including GST and may describe starting variants. It demonstrates public-feed collection; it does not establish African-market coverage.

## Collect a saved snapshot

```bash
python scripts/collect_prices.py
```

The collector appends observations to `web/history.json`. Publish the updated file to refresh the saved comparison baseline. [Source and collection details](docs/public_feed.md). Scheduled collection and cross-retailer matching remain open.
