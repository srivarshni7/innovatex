def calculate_score(project):

    score = 50

    # Tech stack
    if len(project["tech_stack"]) >= 3:
        score += 15

    # Description
    if len(project["description"]) > 150:
        score += 10

    # Problem statement
    if len(project["problem"]) > 100:
        score += 10

    # Skill level
    if project["skill"] == "Advanced":
        score += 10
    elif project["skill"] == "Intermediate":
        score += 5

    score = min(score, 100)

    return {
        "innovation": score,
        "feasibility": max(score - 5, 0),
        "market": max(score - 2, 0),
        "overall": round((score + (score - 5) + (score - 2)) / 3)
    }