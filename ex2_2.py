scores = []
kamoku = ("国語","算数","理科","社会","英語")
for k in kamoku:
    scores.append(int(input(f"{k} >> ")))

print(f"合計点:{sum(scores)}")
print(f"平均点:{sum(scores)/len(scores)}")