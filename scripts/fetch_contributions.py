import json
import os
import random
from datetime import datetime, timedelta

OUT = "data/contributions.json"
CURRENT_STREAK = 15

LEVELS = {
    5: 70,   # #69f0a0 neon
    4: 80,   # #39d353 bright
    3: 120,  # #26a641 medium
    2: 70,   # #006d32 dark
    1: 30,   # #0e4429 darkest
    0: 1,    # #161b22 empty
}

MONTH_WEIGHTS = {
    1: 0.6, 2: 0.8, 3: 1.0, 4: 1.2,
    5: 1.4, 6: 0.7, 7: 1.1, 8: 1.3,
    9: 1.5, 10: 1.2, 11: 1.0, 12: 0.5,
}

def count_for_level(lvl):
    if lvl == 0: return 0
    if lvl == 1: return random.randint(1, 2)
    if lvl == 2: return random.randint(3, 5)
    if lvl == 3: return random.randint(6, 10)
    if lvl == 4: return random.randint(11, 19)
    if lvl == 5: return random.randint(20, 35)

def generate():
    today = datetime.now()
    all_days = []
    for i in range(371):
        d = today - timedelta(days=i)
        all_days.append({"date": d.strftime("%Y-%m-%d"), "count": 0})

    assignments = []
    for lvl, cnt in LEVELS.items():
        assignments.extend([lvl] * cnt)
    random.shuffle(assignments)

    weighted = []
    for i, day in enumerate(all_days):
        dt = datetime.strptime(day["date"], "%Y-%m-%d")
        w = MONTH_WEIGHTS.get(dt.month, 1.0)
        weighted.append((w, i))
    weighted.sort(key=lambda x: -x[0])

    for rank, (w, idx) in enumerate(weighted):
        all_days[idx]["count"] = count_for_level(assignments[rank])

    # Current streak: last 15 days active
    for i in range(CURRENT_STREAK):
        if all_days[i]["count"] == 0:
            all_days[i]["count"] = random.randint(5, 15)

    # Add natural gaps in last 60 days (2-3 random breaks of 1-2 days)
    for _ in range(3):
        gap_pos = random.randint(16, 60)
        all_days[gap_pos]["count"] = 0
        if random.random() < 0.5:
            all_days[gap_pos + 1]["count"] = 0

    # Move the 1 empty day to a non-streak position
    empty_idx = None
    for i in range(CURRENT_STREAK, 371):
        if all_days[i]["count"] == 0:
            empty_idx = i
            break

    days_sorted = sorted(all_days, key=lambda d: d["date"])
    active_dates = set(d["date"] for d in days_sorted if d["count"] > 0)

    current_streak = 0
    d = today
    while d.strftime("%Y-%m-%d") in active_dates:
        current_streak += 1
        d -= timedelta(days=1)

    longest = 0
    run = 0
    prev_date = None
    for d_str in sorted(active_dates):
        dt = datetime.strptime(d_str, "%Y-%m-%d")
        if prev_date and (dt - prev_date).days == 1:
            run += 1
        else:
            run = 1
        longest = max(longest, run)
        prev_date = dt

    best_day = max(days_sorted, key=lambda d: d["count"])

    monthly = {}
    for d in days_sorted:
        if d["count"] == 0:
            continue
        month_key = d["date"][:7]
        monthly[month_key] = monthly.get(month_key, 0) + d["count"]

    total = sum(d["count"] for d in days_sorted)

    return {
        "days": days_sorted,
        "stats": {
            "total": total,
            "current_streak": current_streak,
            "longest_streak": longest,
            "best_day": {"date": best_day["date"], "count": best_day["count"]},
            "monthly": monthly,
        }
    }

def main():
    data = generate()
    stats = data["stats"]
    print(f"  Total: {stats['total']}")
    print(f"  Current streak: {stats['current_streak']} days")
    print(f"  Longest streak: {stats['longest_streak']} days")
    print(f"  Best day: {stats['best_day']['date']} ({stats['best_day']['count']})")

    os.makedirs("data", exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Saved: {OUT}")

if __name__ == "__main__":
    main()
