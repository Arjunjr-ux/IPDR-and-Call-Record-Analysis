def generate(df):
    duration = df["Session Duration"]

    return {
        "Average Duration": round(float(duration.mean()), 2),
        "Maximum Duration": round(float(duration.max()), 2),
        "Minimum Duration": round(float(duration.min()), 2)
    }