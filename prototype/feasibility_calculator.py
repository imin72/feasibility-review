import json
import math
import sys
from typing import Dict, List, Optional


def npv(discount_rate: float, cashflows: List[float]) -> float:
    return sum(cf / ((1 + discount_rate) ** idx) for idx, cf in enumerate(cashflows))


def irr(cashflows: List[float], guess: float = 0.1) -> Optional[float]:
    rate = guess
    for _ in range(200):
        denom = [(1 + rate) ** i for i in range(len(cashflows))]
        f = sum(cf / d for cf, d in zip(cashflows, denom))
        df = sum(-i * cf / ((1 + rate) ** (i + 1)) for i, cf in enumerate(cashflows[1:], start=1))
        if abs(df) < 1e-12:
            return None
        new_rate = rate - f / df
        if not math.isfinite(new_rate):
            return None
        if abs(new_rate - rate) < 1e-8:
            return new_rate
        rate = new_rate
    return None


def payback_period(cashflows: List[float]) -> Optional[float]:
    cumulative = 0.0
    for i, cf in enumerate(cashflows):
        prev = cumulative
        cumulative += cf
        if cumulative >= 0:
            if i == 0:
                return 0.0
            if cf == 0:
                return float(i)
            fraction = (0 - prev) / cf
            return (i - 1) + fraction
    return None


def calculate(data: Dict) -> Dict:
    years = data["years"]
    revenue = data["revenue"]
    capex = data["capex"]
    opex = data["opex"]
    fixed_cost = data["fixed_cost"]
    variable_rate = data["variable_cost_rate"]
    discount_rate = data.get("discount_rate", 0.1)

    rows = []
    cashflows = []
    cumulative = 0.0

    for year in years:
        y = str(year)
        rev = float(revenue[y])
        inv = float(capex[y])
        opx = float(opex[y])
        op_profit = rev - inv - opx
        op_margin = (op_profit / rev) if rev else 0.0
        cumulative += op_profit

        vc = rev * float(variable_rate[y])
        contribution_margin_ratio = (rev - vc) / rev if rev else 0.0
        bep_sales = float("inf")
        if contribution_margin_ratio > 0:
            bep_sales = float(fixed_cost[y]) / contribution_margin_ratio

        rows.append(
            {
                "year": year,
                "revenue": rev,
                "capex": inv,
                "opex": opx,
                "operating_profit": op_profit,
                "operating_margin": op_margin,
                "cumulative_profit": cumulative,
                "bep_sales": bep_sales,
            }
        )
        cashflows.append(op_profit)

    project_npv = npv(discount_rate, cashflows)
    project_irr = irr(cashflows)
    project_payback = payback_period(cashflows)

    return {
        "rows": rows,
        "summary": {
            "total_revenue": sum(float(revenue[str(y)]) for y in years),
            "total_capex": sum(float(capex[str(y)]) for y in years),
            "total_opex": sum(float(opex[str(y)]) for y in years),
            "total_operating_profit": sum(cashflows),
            "npv": project_npv,
            "irr": project_irr,
            "payback_period_years": project_payback,
        },
    }


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python feasibility_calculator.py <input.json>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        data = json.load(f)

    result = calculate(data)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
