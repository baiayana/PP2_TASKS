import json

FILE_NAME = "sample-data.json"

def main():
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("Interface Status")
    print("=" * 80)

    # exact formatted header
    print("{:<50} {:<20} {:>6}  {:>6}".format("DN", "Description", "Speed", "MTU"))
    print("{:<50} {:<20} {:>6}  {:>6}".format("-"*50, "-"*20, "-"*6, "-"*6))

    for item in data.get("imdata", []):
        attr = item.get("l1PhysIf", {}).get("attributes", {})

        dn = attr.get("dn", "")
        descr = attr.get("descr", "")
        speed = attr.get("fecMode", "inherit")
        mtu = attr.get("mtu", "")

        print("{:<50} {:<20} {:>6}  {:>6}".format(dn, descr, speed, mtu))

        if "eth1/35" in dn:
            break

if __name__ == "__main__":
    main()