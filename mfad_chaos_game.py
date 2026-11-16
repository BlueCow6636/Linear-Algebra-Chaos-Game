
import numpy as np
import matplotlib.pyplot as plt

def polygon(n):
    """Vertices of a regular n-gon on the unit circle, first one on the x-axis. Shape (2, n)."""
    t = np.linspace(0, 2 * np.pi, n + 1)[:-1]                                    
    return np.array([np.cos(t), np.sin(t)])

def rotation(theta):
    return np.array([[np.cos(theta), -np.sin(theta)],
                    [np.sin(theta),  np.cos(theta)]])

def chaos_game(v, T, num=10000, rule="any"):
    """
    v    : (2, n) vertices
    T    : (2, 2) matrix
    rule : "any"          -> any vertex each step
        "not_same"     -> new vertex != previous vertex
        "not_opposite" -> new vertex is not opposite the previous (n must be even)
    """
    n = v.shape[1]
    pts = np.zeros((2, num + 1))
    pts[:, 0] = np.random.rand(2) - 0.5                          
    prev = np.random.randint(n)
    for j in range(num):
        while True:
            k = np.random.randint(n)
            if rule == "any":
                break
            if rule == "not_same" and k != prev:
                break
            if rule == "not_opposite" and k != (prev + n // 2) % n:
                break
        w = v[:, k]
        pts[:, j + 1] = T @ (pts[:, j] - w) + w
        prev = k
    return pts

def show(pts, v, title):
    plt.figure()
    plt.plot(pts[0], pts[1], "b.", markersize=1)
    plt.plot(v[0], v[1], "k*")
    plt.axis("equal")
    plt.title(title)
    plt.show(block=False)
    plt.pause(0.75)

def barnsley_fern(num=15000):
    Ts = [np.array([[0.85, 0.04], [-0.04, 0.85]]),
        np.array([[-0.15, 0.28], [0.26, 0.24]]),
        np.array([[0.2, -0.26], [0.23, 0.22]]),
        np.array([[0, 0], [0, 0.16]])]
    Qs = [np.array([0, 1.64]), np.array([-0.028, 1.05]),
        np.array([0, 1.6]), np.array([0, 0])]
    P = np.cumsum([0.85, 0.07, 0.07, 0.01])                                  
    x = np.zeros((2, num + 1))
    x[:, 0] = np.random.rand(2)
    for j in range(num):
        i = np.searchsorted(P, np.random.rand())                      
        i = min(i, 3)
        x[:, j + 1] = Ts[i] @ x[:, j] + Qs[i]
    plt.figure()
    plt.plot(x[0], x[1], "g.", markersize=1)
    plt.axis("equal")
    plt.title("Barnsley fern")
    plt.show(block=False)
    plt.pause(0.75)

if __name__ == "__main__":
    half = 0.5 * np.eye(2)
    third = np.eye(2) / 3
    '''
    v3 = polygon(3)
    show(chaos_game(v3, half), v3, "Shape: Sierpinski triangle (r = 1/2)")

    show(chaos_game(v3, third), v3, "Shape: triangle, r = 1/3")

    show(chaos_game(v3, 0.5 * rotation(np.pi / 18)), v3, "Shape: triangle with rotation")

    v4 = polygon(4)
    show(chaos_game(v4, half), v4, "Shape: square, r = 1/2 (no fractal)")
    show(chaos_game(v4, third), v4, "Shape: square, r = 1/3")

    show(chaos_game(v4, half, 5000, "not_same"), v4, "Shape: square, no repeat vertex")
    show(chaos_game(v4, half, 5000, "not_opposite"), v4, "Shape: square, not opposite")

    barnsley_fern()

    v6 = polygon(6)
    show(chaos_game(v6, third, 15000), v6, "Shape: hexagon, r = 1/3")

    v5 = polygon(5)
    show(chaos_game(v5, 0.4 * np.eye(2), 10000, "not_same"), v5, "Shape: pentagon, r = 2/5")'''
    
    vnew = polygon(4)
    show(chaos_game(vnew, 0.4 * np.eye(2), 10000, "not_same"), vnew, "Shape: square, r = 2/5")

    plt.show()
