from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.vals import GetValues

class IndianstockTool(Tool):
    def _to_py(self, value):
        if hasattr(value, "item"):
            return value.item()
        return value
    def _get_values(self) -> GetValues:
        g = GetValues()
        s = g.get_readings(instrument=self.instrument, period=self.period, interval=self.interval, trade_type=self.trading_type, start_date=self.start_date, end_date=self.end_date)

        if "status" in s:
            return s
        for i in range(len(s)):
            for var, val in s[i].items():
                s[i][var] = self._to_py(val)
        return s
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        
        self.trading_type = tool_parameters.get("trade_type")
        symbol = tool_parameters.get("trading_symbol")
        isin = GetValues().get_isin(symbol.upper())
        self.instrument = isin if isin != "Instrument not found" else "NULL"
        self.period = tool_parameters.get("period")
        self.interval = tool_parameters.get("interval")
        self.start_date = tool_parameters.get("start_date")
        self.end_date = tool_parameters.get("end_date")
        if self.start_date == "":
            self.start_date = "YYYY-MM-DD"
        if self.end_date == "":
            self.end_date = "YYYY-MM-DD"

        yield self.create_json_message({
            "result": self._get_values()
        })