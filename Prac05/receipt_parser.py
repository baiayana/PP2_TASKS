import re
import json
from pathlib import Path


def parse_money_to_float(s: str) -> float:
    """
    Converts money like '1 200,00' or '308,00' to float 1200.00 / 308.00
    """
    s = s.strip().replace(" ", "").replace("\xa0", "")
    s = s.replace(",", ".")
    return float(s)


def parse_receipt(text: str) -> dict:
    # 1) Extract all prices (money-like values)
    # matches: 308,00  1 200,00  18 009,00  0,00 etc.
    money_pattern = r"\d{1,3}(?:[ \xa0]\d{3})*,\d{2}"
    all_prices_str = re.findall(money_pattern, text)
    all_prices = [parse_money_to_float(x) for x in all_prices_str]

    # 2) Find all product names + item totals
    # Structure in your raw:
    # N.
    # <name line>
    # <qty> x <unit_price>
    # <line_total>
    # Стоимость
    # <line_total_again>
    item_block_pattern = re.compile(
        r"(?m)^\s*(\d+)\.\s*\n"           # item number
        r"(.+?)\n"                        # product name (one line)
        r"([0-9]+,[0-9]{3})\s*x\s*(" + money_pattern + r")\s*\n"  # qty x unit
        r"(" + money_pattern + r")",      # line total
        re.DOTALL
    )

    items = []
    for m in item_block_pattern.finditer(text):
        idx = int(m.group(1))
        name = m.group(2).strip()
        qty_str = m.group(3)
        unit_price_str = m.group(4)
        line_total_str = m.group(5)

        qty = float(qty_str.replace(",", "."))
        unit_price = parse_money_to_float(unit_price_str)
        line_total = parse_money_to_float(line_total_str)

        items.append({
            "index": idx,
            "name": name,
            "quantity": qty,
            "unit_price": unit_price,
            "line_total": line_total
        })

    # 3) Calculate total amount (prefer "ИТОГО", else sum of line totals)
    total_match = re.search(r"(?m)^ИТОГО:\s*\n(" + money_pattern + r")\s*$", text)
    if total_match:
        total_amount = parse_money_to_float(total_match.group(1))
        total_source = "receipt_total"
    else:
        total_amount = round(sum(i["line_total"] for i in items), 2)
        total_source = "sum_items"

    # 4) Extract date and time
    dt_match = re.search(r"Время:\s*(\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2})", text)
    date_time = dt_match.group(1) if dt_match else None

    # 5) Find payment method (simple rules)
    payment_method = None
    if re.search(r"(?im)Банковская\s+карта", text):
        payment_method = "Банковская карта"
    elif re.search(r"(?im)Наличные", text):
        payment_method = "Наличные"

    # Optional: payment amount near payment method
    payment_amount = None
    pay_match = re.search(r"(?m)^Банковская\s+карта:\s*\n(" + money_pattern + r")\s*$", text)
    if pay_match:
        payment_amount = parse_money_to_float(pay_match.group(1))

    # Extra: store meta (optional)
    branch = re.search(r"(?m)^Филиал\s+(.+)$", text)
    bin_m = re.search(r"(?m)^БИН\s+(\d+)$", text)
    receipt_no = re.search(r"(?m)^Чек\s*№\s*(\d+)$", text)

    data = {
        "meta": {
            "branch": branch.group(1).strip() if branch else None,
            "bin": bin_m.group(1) if bin_m else None,
            "receipt_number": receipt_no.group(1) if receipt_no else None,
        },
        "date_time": date_time,
        "payment_method": payment_method,
        "payment_amount": payment_amount,
        "items": items,
        "all_prices_raw": all_prices_str,      # task 1 (raw strings)
        "all_prices": all_prices,              # task 1 (as numbers)
        "total_amount": total_amount,
        "total_source": total_source
    }

    return data


def main():
    raw_path = Path(__file__).with_name("raw.txt")
    text = raw_path.read_text(encoding="utf-8")

    parsed = parse_receipt(text)

    # 6) Output structured JSON (pretty)
    print(json.dumps(parsed, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()