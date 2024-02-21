def ioufunc(a, b):
    # a, bは矩形を表すリストで、a=[xmin,ymin,xmax, ymax]
    ax_mn, ay_mn, ax_mx, ay_mx = a[0], a[1], a[2], a[3]
    bx_mn, by_mn, bx_mx, by_mx = b[0], b[1], b[2], b[3]

    a_area = (ax_mx - ax_mn + 1.0) * (ay_mx - ay_mn + 1.0)
    b_area = (bx_mx - bx_mn + 1.0) * (by_mx - by_mn + 1.0)

    abx_mn = max(ax_mn, bx_mn)
    aby_mn = max(ay_mn, by_mn)
    abx_mx = min(ax_mx, bx_mx)
    aby_mx = min(ay_mx, by_mx)
    w = max(0.0, abx_mx - abx_mn + 1.0)
    h = max(0.0, aby_mx - aby_mn + 1.0)
    intersect = w*h

    iou = intersect / (a_area + b_area - intersect)
    return iou
