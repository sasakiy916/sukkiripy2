matuda_scores = {"netowork":60,"database":80,"security":50}
asagi_scores = {"netowork":80,"database":75,"security":92}

member_scores = {
    "松田":matuda_scores,
    "浅木":asagi_scores
}
print(member_scores["松田"]["security"])