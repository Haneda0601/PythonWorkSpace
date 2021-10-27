import math
input_angle = float(input('角度を入力してください（度）：'))
print(f"{input_angle:.1f}度->{math.radians(input_angle)}ラジアン")
print(f"sin({input_angle:.1f})=>{math.sin(math.radians(input_angle))}")