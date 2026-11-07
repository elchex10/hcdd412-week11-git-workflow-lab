"""Late-fee calculation for the campus library desk."""


def late_fee(days_late: int, daily_rate: float, grace_days: int = 0) -> float:
    """Return the late fee in dollars for an item returned ``days_late`` days late.

    Items returned on time or early are never charged. The first ``grace_days``
    days late are free; only days beyond the grace period are charged.
    """
    if days_late <= 0:
        return 0.0
    chargeable_days = max(days_late - grace_days, 0)
    return round(chargeable_days * daily_rate, 2)
