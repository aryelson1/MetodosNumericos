def bracket_minimum(f, x=0, s=1e-2, k=2.0):
    a, ya = x, f(x)
    b, yb = a + s, f(a + s)
    if yb > ya:
        a, b = b, a
        ya, yb = yb, ya
        s = -s
    while True:
        c, yc = b + s, f(b + s)
        if yc > yb:
            return (a, c) if a < c else (c, a)
        a, ya, b, yb = b, yb, c, yc
        s *= k


from collections import namedtuple

Pt = namedtuple('Pt', ['x', 'y'])

def _get_sp_intersection(A, B, l):
    t = ((A.y - B.y) - l*(A.x - B.x)) / (2*l)
    return Pt(A.x + t, A.y - t*l)

def shubert_piyavskii(f, a, b, l, ϵ, δ=0.01):
    m = (a+b)/2
    A, M, B = Pt(a, f(a)), Pt(m, f(m)), Pt(b, f(b))
    pts = [A, _get_sp_intersection(A, M, l), M, _get_sp_intersection(M, B, l), B]
    Δ = float('inf')
    while Δ > ϵ:
        i = min(range(len(pts)), key=lambda i: pts[i].y)
        P = Pt(pts[i].x, f(pts[i].x))
        Δ = P.y - pts[i].y
        P_prev = _get_sp_intersection(pts[i-1], P, l)
        P_next = _get_sp_intersection(P, pts[i+1], l)
        del pts[i]
        pts.insert(i, P_next)
        pts.insert(i, P)
        pts.insert(i, P_prev)
    intervals = []
    i = 2*(np.argmin([P.y for P in pts[1:2:-1]])) - 1
    for j in range(1, len(pts), 2):
        if pts[j].y < pts[i].y:
            dy = pts[i].y - pts[j].y
            x_lo = max(a, pts[j].x - dy/l)
            x_hi = min(b, pts[j].x + dy/l)
            if intervals and intervals[-1][1] + δ >= x_lo:
                intervals[-1] = (intervals[-1][0], x_hi)
            else:
                intervals.append((x_lo, x_hi))
    return (pts[i], intervals)


def bisection(f_prime, a, b, eps):
    if a > b:
        a, b = b, a
    ya, yb = f_prime(a), f_prime(b)
    if ya == 0:
        b = a
    if yb == 0:
        a = b
    while b - a > eps:
        x = (a + b) / 2
        y = f_prime(x)
        if y == 0:
            a, b = x, x
        elif y * ya > 0:
            a = x
        else:
            b = x
    return (a, b)


def bracket_sign_change(f_prime, a, b, k=2):
    if a > b:
        a, b = b, a
    center, half_width = (b + a) / 2, (b - a) / 2
    while f_prime(a) * f_prime(b) > 0:
        half_width *= k
        a = center - half_width
        b = center + half_width
    return (a, b)

import math

def fibonacci_search(f, a, b, n, ϵ=0.01):
    s = (1-math.sqrt(5))/(1+math.sqrt(5))
    ρ = 1 / (phi*(1-s**(n+1))/(1-s**n))
    d = ρ*b + (1-ρ)*a
    yd = f(d)
    for i in range(1, n):
        if i == n-1:
            c = ϵ*a + (1-ϵ)*d
        else:
            c = ρ*a + (1-ρ)*b
        yc = f(c)
        if yc < yd:
            b, d, yd = d, c, yc
        else:
            a, b = b, c
        ρ = 1 / (phi*(1-s**(n-i+1))/(1-s**(n-i)))
    return (a, b) if a < b else (b, a)

def golden_section_search(f, a, b, n):
    ρ = phi-1
    d = ρ * b + (1 - ρ)*a
    yd = f(d)
    for i in range(1, n):
        c = ρ*a + (1 - ρ)*b
        yc = f(c)
        if yc < yd:
            b, d, yd = d, c, yc
        else:
            a, b = b, c
    return (a, b) if a < b else (b, a)
	
def quadratic_fit_search(f, a, b, c, n):
    ya, yb, yc = f(a), f(b), f(c)
    for i in range(n-3):
        x = 0.5*(ya*(b**2-c**2)+yb*(c**2-a**2)+yc*(a**2-b**2)) / \
            (ya*(b-c) + yb*(c-a) + yc*(a-b))
        yx = f(x)
        if x > b:
            if yx > yb:
                c, yc = x, yx
            else:
                a, ya, b, yb = b, yb, x, yx
        elif x < b:
            if yx > yb:
                a, ya = x, yx
            else:
                c, yc, b, yb = b, yb, x, yx
    return (a, b, c)
