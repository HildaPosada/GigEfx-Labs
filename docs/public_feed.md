# Public pricing feed

The deployed explorer fetches Little Bird Electronics through its documented, unauthenticated public API. The source supports browser CORS and permits 60 requests per minute per IP. Prices are AUD including GST.

Source: https://littlebirdelectronics.com.au/help/public-api

The live workflow validates prices, sorts and filters products, records an observation timestamp, compares consecutive browser-session observations, and exports a JSON snapshot. It is an Australian integration demonstration, not a replacement claim for African retailer coverage. Persistent historical collection and cross-retailer matching remain future work.
