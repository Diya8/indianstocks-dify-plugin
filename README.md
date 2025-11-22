## Indian Stock Values

**Author:** diya8

**Version:** 0.0.1

**Type:** tool

### Description

This plugin has the tool **Get Values** which helps you to get the OHLC values and volume for an Indian stock.

Note: OHLC stands for Open, High, Low and Close.

### Configuration

No configuration required, the plugin can be used readily without any authorisation.

### Usage

Following are the input parameters:

1. **Trade Type**: You can choose between "historical" and "intraday"

2. **Symbol**: Trading symbol e.g., RELIANCE, HDFCBANK

3. **Period**: Period for data. 
    - Minutes, hours and days in intraday mode
    - Minutes, hours, days, weeks and months in historical mode

4. **Interval**: Data interval with the following possible values: 
    - 1-300 for minutes 
    - 1-5 for hours
    - 1 for days, weeks, and months

5. **Start Date**: In historical trade type, start date for data retrieval in YYYY-MM-DD format. Leave as blank in case of intraday mode.

6. **End Date**: In historical trade type, end date for data retrieval in YYYY-MM-DD format. Leave as blank in case of intraday mode.

Input the above parameters as per your requirement.

### Output

Output is in the form of candle data in the following format:

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

The number of data points vary with respect to the input given.

If there is an error in the input format or with fetching the data, the error log will be returned instead of the data.

### Issues, Feedback and Suggestions

For issues, feedback and suggestions, please raise it in this GitHub repository. I would love to hear back from you!