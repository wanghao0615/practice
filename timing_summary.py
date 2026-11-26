"""Summarize fictional timing data for Git practice."""


def main():
    endpoint_slacks_ps = [-18.0, 12.0, -6.5, 4.0]
    negative_slacks_ps = [slack for slack in endpoint_slacks_ps if slack < 0]

    wns_ps = min(negative_slacks_ps, default=0.0)
    tns_ps = sum(negative_slacks_ps)

    print(f"WNS: {wns_ps:.1f} ps")
    print(f"TNS: {tns_ps:.1f} ps")


if __name__ == "__main__":
    main()
