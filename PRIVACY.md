## Privacy Policy for Indian Stock Dify Plugin

### Overview

This privacy policy explains how the **Indian Stock Plugin** ("the plugin") handles, stores, and processes data when used within a Dify workflow.  
The plugin provides one tool — **Get Values** — used to fetch OHLC (Open, High, Low, Close) and volume data for Indian stocks.

The plugin does **not** collect, store, share, or transmit any personal data of the user.

### Data Handling

#### 1. User Inputs

The plugin accepts the following inputs:

- Trade Type (historical/intraday)  
- Symbol (e.g., `RELIANCE`, `HDFCBANK`)  
- Period  
- Interval  
- Start Date (for historical data)  
- End Date (for historical data)

**None of these inputs contain or require personal information.** They are used strictly for retrieving financial market data.

#### 2. External API Calls (Third-Party Data Providers)

To fetch market data, the plugin sends the user-provided parameters to a third-party market data provider.

**Third-party service used**

- **Upstox Market Data API**  
  - Privacy Policy: https://upstox.com/privacy-policy/  

**What is sent**

- Only stock-related parameters (symbol, trade type, period, interval, optional start and end dates).  
- No user personal information, account details, API tokens, or device identifiers are transmitted.

**What is received**

- OHLC candle data and volume, for example: timestamp, open, high, low, close, volume, open interest.

The plugin is an independent utility and is **not affiliated with, endorsed by, or certified by Upstox**.

#### 3. Data Storage

- The plugin does **not** store any data locally or externally.  
- All data is handled in-memory for the duration of a request.  
- No logs, caches, or historical records are retained by the plugin.

### Security

- All communication with third-party APIs occurs over HTTPS.  
- The plugin does not request, store, or handle authentication tokens, passwords, or credentials.  
- No sensitive data is logged or persisted.

### Permissions

The plugin does not request any system-level permissions.  
It only receives stock query parameters required to fetch market data.

### Output

The plugin returns only market-related data for the requested symbol. Example:

```json
{
  "close": 182.24,
  "high": 185.17,
  "low": 182.1,
  "open": 182.4,
  "open_interest": 0,
  "timestamp": "2025-09-30T00:00:00+05:30",
  "volume": 4038
}
```

This output contains **no user-identifiable information**.

### Error Handling

If input parameters are invalid or the third-party API returns an error, the plugin returns the error message.  
These messages contain only technical information — never personal data.

### Third-Party Disclosure & Links

By using this plugin, users should be aware that the plugin sends stock query parameters to Upstox to retrieve market data.

Relevant Upstox links:

- Privacy Policy: https://upstox.com/privacy-policy/  
- API Documentation: https://upstox.com/developer/api-documentation/

### Summary

- No personal data is collected.  
- No personal data is stored or transmitted.  
- Only stock symbols and request parameters are sent to Upstox.  
- The plugin uses no cookies, analytics, or tracking.  
- The plugin is independent and not affiliated with Upstox.

### Contact

For questions about this privacy policy, please contact the plugin author via the plugin’s [GitHub repository](https://github.com/Diya8/indianstocks-dify-plugin).
