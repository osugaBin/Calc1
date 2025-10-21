import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

def create_limit_animation():
    # Set up the figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # θ values (from large to small, showing approach to 0)
    theta_values = np.linspace(np.pi/2, 0.01, 100)
    
    # Calculate corresponding sin(θ)/θ values
    ratio_values = np.sin(theta_values) / theta_values
    
    def update(frame):
        ax1.clear()
        ax2.clear()
        
        theta = theta_values[frame]
        ratio = ratio_values[frame]
        
        # First subplot: Unit Circle Geometric Interpretation
        ax1.set_xlim(-1.2, 1.2)
        ax1.set_ylim(-1.2, 1.2)
        ax1.set_aspect('equal')
        ax1.grid(True, alpha=0.3)
        ax1.set_title(f'Unit Circle Geometric Interpretation\nθ = {theta:.4f} radians', fontsize=12, pad=20)
        
        # Draw unit circle
        circle = plt.Circle((0, 0), 1, fill=False, color='blue', linewidth=2)
        ax1.add_patch(circle)
        
        # Draw angle θ
        x_end = np.cos(theta)
        y_end = np.sin(theta)
        
        # Draw radius
        ax1.plot([0, x_end], [0, y_end], 'r-', linewidth=2, label='Radius = 1')
        
        # Draw arc
        arc_theta = np.linspace(0, theta, 100)
        arc_x = np.cos(arc_theta)
        arc_y = np.sin(arc_theta)
        ax1.plot(arc_x, arc_y, 'g-', linewidth=3, label=f'Arc length = {theta:.4f}')
        
        # Draw sin(θ) line
        ax1.plot([x_end, x_end], [0, y_end], 'purple', linewidth=2, 
                label=f'sin(θ) = {np.sin(theta):.4f}')
        
        # Draw tan(θ) line (tangent)
        if theta < np.pi/2:  # Avoid infinity at 90 degrees
            tan_x = 1
            tan_y = np.tan(theta)
            ax1.plot([1, tan_x], [0, tan_y], 'orange', linewidth=2, 
                    label=f'tan(θ) = {np.tan(theta):.4f}')
        
        # Add annotations
        ax1.text(0.1, 0.7, f'sin(θ) = {np.sin(theta):.6f}', fontsize=10)
        ax1.text(0.1, 0.6, f'Arc length θ = {theta:.6f}', fontsize=10)
        ax1.text(0.1, 0.5, f'sin(θ)/θ = {ratio:.6f}', fontsize=10, 
                bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))
        
        # Show geometric inequality
        if theta > 0.1:
            ax1.text(-1.1, -1.0, f'Geometric Inequality:\ncos(θ) ≤ sin(θ)/θ ≤ 1', 
                    fontsize=9, bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue"))
        
        ax1.legend(loc='upper left')
        
        # Second subplot: Function and Limit
        ax2.set_xlim(0, np.pi/2)
        ax2.set_ylim(0.75, 1.02)
        ax2.grid(True, alpha=0.3)
        ax2.set_xlabel('θ (radians)')
        ax2.set_ylabel('sin(θ)/θ')
        ax2.set_title('Limit of f(θ) = sin(θ)/θ as θ → 0', fontsize=12, pad=20)
        
        # Draw the complete function curve
        theta_curve = np.linspace(0.01, np.pi/2, 200)
        ratio_curve = np.sin(theta_curve) / theta_curve
        ax2.plot(theta_curve, ratio_curve, 'b-', linewidth=2, alpha=0.7, 
                label='f(θ) = sin(θ)/θ')
        
        # Mark current point
        ax2.plot(theta, ratio, 'ro', markersize=8, 
                label=f'Current: ({theta:.4f}, {ratio:.6f})')
        
        # Add limit line
        ax2.axhline(y=1, color='red', linestyle='--', alpha=0.7, linewidth=2, 
                   label='Limit = 1')
        
        # Add squeeze theorem bounds
        cos_curve = np.cos(theta_curve)
        ax2.plot(theta_curve, cos_curve, 'green', linestyle=':', alpha=0.7, 
                label='cos(θ)')
        
        # Add approach arrow
        if frame > 80:
            ax2.annotate('Approaching Limit', xy=(0.1, 0.99), xytext=(theta, ratio),
                        arrowprops=dict(arrowstyle='->', color='green', lw=2),
                        fontsize=10, ha='center')
        
        ax2.legend(loc='lower left')
        
        # Main title with mathematical notation
        fig.suptitle(f'Proof of $\\lim_{{θ\\to 0}} \\frac{{\\sin(θ)}}{{θ}} = 1$\n'
                    f'Current: $\\frac{{\\sin({theta:.4f})}}{{{theta:.4f}}} = {ratio:.6f}$', 
                    fontsize=16, y=0.95)
    
    # Create animation
    anim = FuncAnimation(fig, update, frames=len(theta_values), 
                        interval=100, repeat=True)
    
    # Save as GIF
    print("Generating GIF animation...")
    anim.save('sin_theta_limit_english.gif', writer='pillow', fps=10, dpi=120)
    print("GIF animation saved as 'sin_theta_limit_english.gif'")
    
    plt.tight_layout()
    plt.show()

def numerical_verification():
    """Numerical verification of the limit"""
    print("\nNumerical Verification of the Limit:")
    print("θ (radians)\t\tsin(θ)/θ")
    print("-" * 50)
    
    test_thetas = [1.0, 0.5, 0.2, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0001]
    for theta in test_thetas:
        ratio = np.sin(theta) / theta
        print(f"{theta:.6f}\t\t{ratio:.10f}")
    
    print("\nMathematical Proof Summary:")
    print("1. Geometric argument:")
    print("   - For small θ in unit circle: sin(θ) ≈ θ ≈ tan(θ)")
    print("   - Actually: sin(θ) < θ < tan(θ) for 0 < θ < π/2")
    print("2. Dividing by sin(θ): 1 < θ/sin(θ) < 1/cos(θ)")
    print("3. Taking reciprocals: cos(θ) < sin(θ)/θ < 1")
    print("4. By Squeeze Theorem: lim_{θ→0} cos(θ) = 1, so lim_{θ→0} sin(θ)/θ = 1")

def create_squeeze_theorem_visualization():
    """Create a separate visualization of the squeeze theorem"""
    theta_squeeze = np.linspace(0.01, np.pi/2, 100)
    sin_theta_over_theta = np.sin(theta_squeeze) / theta_squeeze
    cos_theta = np.cos(theta_squeeze)
    ones = np.ones_like(theta_squeeze)
    
    plt.figure(figsize=(10, 6))
    plt.plot(theta_squeeze, cos_theta, 'g--', linewidth=2, label='cos(θ)')
    plt.plot(theta_squeeze, sin_theta_over_theta, 'b-', linewidth=3, label='sin(θ)/θ')
    plt.plot(theta_squeeze, ones, 'r--', linewidth=2, label='1')
    plt.fill_between(theta_squeeze, cos_theta, ones, alpha=0.2, color='yellow')
    
    plt.xlim(0, 1)
    plt.ylim(0.5, 1.05)
    plt.xlabel('θ (radians)')
    plt.ylabel('Function Value')
    plt.title('Squeeze Theorem: cos(θ) ≤ sin(θ)/θ ≤ 1\n' + 
              'As θ → 0, cos(θ) → 1, so sin(θ)/θ → 1')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig('squeeze_theorem.png', dpi=150, bbox_inches='tight')
    print("Squeeze theorem visualization saved as 'squeeze_theorem.png'")

if __name__ == "__main__":
    print("Creating animation for: lim_{θ→0} sin(θ)/θ = 1")
    create_limit_animation()
    numerical_verification()
    create_squeeze_theorem_visualization()