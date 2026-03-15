def classify_risk(probability: float, threshold: float = 0.35) -> str:
    """
    Convert model probability into a cardiac risk category.
    """

    if probability < 0 or probability > 1:
        raise ValueError("Probability must be between 0 and 1")

    if probability < threshold:
        return "Low Risk"

    elif probability < 0.60:
        return "Medium Risk"

    else:
        return "High Risk"


if __name__ == "__main__":
    test_probs = [0.2, 0.38, 0.75]

    for p in test_probs:
        print(p, "->", classify_risk(p))