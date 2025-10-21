import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 定义函数
def f(x):
    return x ** 2  # 可以换成其他函数，比如 np.sin(x) 或 np.exp(x)

# 固定点 a
a = 1.0

# 生成 x 数据
x_vals = np.linspace(-3, 5, 400)

# 创建图形
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-3, 5)
ax.set_ylim(-1, 10)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_title("Secant Line Approaching Tangent Line")
ax.set_xlabel("x")
ax.set_ylabel("y")

# 初始绘图元素
curve, = ax.plot(x_vals, f(x_vals), 'k-', label='f(x) = x²')
sec_line, = ax.plot([], [], 'r-', label='Secant Line')
tan_line, = ax.plot([], [], 'b-', label='Tangent Line')
point_A, = ax.plot([], [], 'go', label='A (fixed)')
point_B, = ax.plot([], [], 'mo', label='B (moving)')
text_sec = ax.text(2, 8, "", fontsize=10)
text_tan = ax.text(2, 7, "", fontsize=10)
text_diff = ax.text(2, 6, "", fontsize=10)

# 初始函数
def init():
    sec_line.set_data([], [])
    tan_line.set_data([], [])
    point_A.set_data([], [])
    point_B.set_data([], [])
    return sec_line, tan_line, point_A, point_B

# 更新函数
def update(frame):
    # 移动点 x 从 3 靠近 a
    x = a + (3 - a) * (1 - frame / 100)
    
    # 计算点
    A = (a, f(a))
    B = (x, f(x))
    
    # 割线（延长线）
    sec_x = np.linspace(-5, 5, 200)  # 贯穿整个绘图范围
    m_sec = (f(x) - f(a)) / (x - a) if x != a else 2 * a
    sec_y = f(a) + m_sec * (sec_x - a)
    sec_line.set_data(sec_x, sec_y)
    
    # 切线（延长线）
    m_tan = 2 * a  # f'(x) = 2x
    tan_x = np.linspace(-5, 5, 200)
    tan_y = f(a) + m_tan * (tan_x - a)
    tan_line.set_data(tan_x, tan_y)
    
    # 点
    point_A.set_data([A[0]], [A[1]])
    point_B.set_data([B[0]], [B[1]])
    
    # 斜率文本
    text_sec.set_text(f"Secant slope = {m_sec:.4f}")
    text_tan.set_text(f"Tangent slope = {m_tan:.4f}")
    text_diff.set_text(f"Difference = {abs(m_sec - m_tan):.4f}")
    
    return sec_line, tan_line, point_A, point_B

# 创建动画
ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True)

# 保存为 GIF（本地运行可直接写文件）
ani.save('secant_to_tangent.gif', writer='pillow', fps=15)
print("动画已保存为 secant_to_tangent.gif")

# 显示图形
plt.legend()
plt.show()
