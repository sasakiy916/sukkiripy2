player_hobbies = {"読書","ゲーム","漫画","ネカフェ","Youtube"}
player2_hobbies = {"ハイキング","ゲーム","サバゲ","漫画","レッドブル"}
input("心の準備ができたら Enterキーを押してください")

multi = (player_hobbies & player2_hobbies)
add = (player_hobbies | player2_hobbies)

compatibility_rate = len(multi) / len(add)
print(f"相性度:{compatibility_rate * 100}%")