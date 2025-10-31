# q1_crm_cleanup.py
import re
import csv
from pathlib import Path

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")


def validate_email(raw):
    if not raw:
        return None
    email = raw.strip()
    if EMAIL_RE.fullmatch(email):
        return email
    return None


def normalize_phone(raw):
    if not raw:
        return ""
    digits = re.sub(r"\D", "", raw)
    if len(digits) < 10:
        return ""
    return digits[-10:]


def parse_contacts_from_string(text):
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    rows = []
    for line in lines:
        parts = [p.strip() for p in line.split(",")]
        if len(parts) < 2:
            continue
        name = parts[0]
        email = validate_email(parts[1])
        if not email:
            continue
        phone = normalize_phone(parts[2]) if len(parts) > 2 else ""
        rows.append({"name": name, "email": email, "phone": phone})
    return deduplicate_contacts(rows)


def deduplicate_contacts(rows):
    seen = set()
    result = []
    for row in rows:
        key = row["email"].lower()
        if key in seen:
            continue
        seen.add(key)
        result.append(row)
    return result




def parse_contacts_from_file(path_str: str):
    path = Path(path_str)
    try:
        with path.open("r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    return parse_contacts_from_string(text)


def write_contacts_csv(rows, path_str: str):
    path = Path(path_str)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "email", "phone"])
        for row in rows:
            writer.writerow([row["name"], row["email"], row["phone"]])


if __name__ == "__main__":
    cleaned = parse_contacts_from_file("contacts_raw.txt")
    write_contacts_csv(cleaned, "contacts_clean.csv")
    print(f"do not crush ")
