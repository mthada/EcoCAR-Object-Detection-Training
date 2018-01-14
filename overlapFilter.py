import cv2

def overlapFilter(Objects, frame, boxColorB, boxColorG, boxColorR):
    i = 1
    class Point(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y
    class Rect(object):
        def __init__(self, p1, p2):
            '''Store the top, bottom, left and right values for points
                   p1 and p2 are the (corners) in either order
            '''
            self.left = min(p1.x, p2.x)
            self.right = max(p1.x, p2.x)
            self.bottom = min(p1.y, p2.y)
            self.top = max(p1.y, p2.y)

    def overlap(r1, r2):

        h_overlaps = (r1.left <= r2.right) and (r1.right >= r2.left)
        v_overlaps = (r1.bottom <= r2.top) and (r1.top >= r2.bottom)
        inside = r1.left >= r2.left and r1.right <= r2. right and r1.top >= r2.top and r1.bottom <= r2.bottom
        return (h_overlaps and v_overlaps) or inside

    for (X, Y, W, H) in Objects:
        c = 1
        if (i == 1):
            # print "***area: " + str(rearW*rearH) + "  with y axis=" + str(rearY)#TODO
            # print the very first rectangle because no overlap is possible with just one image
            cv2.rectangle(frame, (X, Y), (X + W, Y + H), (boxColorB, boxColorG, boxColorR), 2)
        else:
            # for the remaining rectangles, ensure that each is unique and not overlapping previous rectangles
            rr1 = Rect(Point(X, Y), Point(X + W, Y + 2 * H))
            overlapDetected = False
            for (X2, Y2, W2, H2) in Objects:
                if (c != i):
                    # for all rectangles(rr2), check that rr1 doesnt overlap with any
                    rr2 = Rect(Point(X2, Y2), Point(X2 + W2, Y2 + H2))
                    if (overlap(rr1, rr2)): # or overlap(rr2, rr1)):
                        overlapDetected = True
                c = c + 1
            if (not overlapDetected):
                # print "***area: " + str(rearW * rearH) + "  with y axis=" + str(rearY)
                cv2.rectangle(frame, (X, Y), (X + W, Y + H), (boxColorB, boxColorG, boxColorR), 2)
        i = i + 1
    return frame