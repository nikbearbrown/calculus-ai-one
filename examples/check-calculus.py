"""Check the switching-tank fixture with standard-library rational arithmetic."""
from csv import DictReader
from fractions import Fraction as F
from pathlib import Path
import unittest


def first(t):
    return 6-t*t


def after(t, zero=4):
    return 2*(t-zero)


def flow(t):
    if not 0 <= t <= 7:
        raise ValueError("outside modeled interval")
    return first(t) if t < 2 else after(t)


def volume(t, zero=4):
    if not 0 <= t <= 7:
        raise ValueError("outside modeled interval")
    if t <= 2:
        return 10+6*t-F(t**3,3)
    return F(58,3)+(t-zero)**2-(2-zero)**2


def midpoint(rate, start, count, step):
    return sum(step*rate(start+(F(1,2)+i)*step) for i in range(count))


def trapezoid(rate, start, count):
    return sum(F(rate(t)+rate(t+1),2) for t in range(start,start+count))


class SwitchingTank(unittest.TestCase):
    def test_samples(self):
        with Path(__file__).with_name("flow-samples.csv").open() as src:
            rows=[(int(x["minute"]),int(x["net_flow_l_per_min"])) for x in DictReader(src)]
        self.assertEqual(rows,[(t,flow(t)) for t in range(8)])

    def test_switch_and_domain(self):
        self.assertEqual((first(2),after(2),flow(2)),(2,-4,-4))
        with self.assertRaises(ValueError):
            flow(8)

    def test_derivative_and_tangent(self):
        for h in (F(1,10),F(-1,10),F(1,5)):
            self.assertEqual((flow(1+h)-flow(1))/h,-2-h)
            self.assertEqual((flow(3+h)-flow(3))/h,2)
        self.assertEqual(5-2*F(1,5)-flow(F(6,5)),F(1,25))

    def test_volume_and_extrema(self):
        self.assertEqual([volume(t) for t in (0,2,4,7)],[10,F(58,3),F(46,3),F(73,3)])
        self.assertEqual([flow(t)>0 for t in (1,3,5)],[True,False,True])
        self.assertEqual(volume(3),F(49,3))
        self.assertEqual(volume(2),volume(6))

    def test_one_sided_volume_secants(self):
        for h in (F(1,10),F(1,100)):
            self.assertEqual((volume(2)-volume(2-h))/h,2+2*h-h*h/3)
            self.assertEqual((volume(2+h)-volume(2))/h,-4+h)

    def test_exact_area_check(self):
        triangles=-F(2*4,2)+F(3*6,2)
        self.assertEqual(F(28,3)+triangles,F(43,3))
        self.assertEqual(volume(7)-volume(0),F(43,3))

    def test_midpoint(self):
        self.assertEqual(midpoint(flow,0,7,1),F(29,2))
        self.assertEqual(midpoint(flow,0,14,F(1,2)),F(115,8))
        self.assertEqual(midpoint(flow,0,7,1)-F(43,3),F(1,6))
        self.assertEqual(midpoint(flow,0,14,F(1,2))-F(43,3),F(1,24))

    def test_trapezoid(self):
        self.assertEqual(trapezoid(flow,0,7),11)
        self.assertEqual(trapezoid(first,0,2)+trapezoid(after,2,5),14)
        self.assertEqual(trapezoid(lambda t: 0 if t==2 else flow(t),0,7),15)

    def test_unseen_controller(self):
        candidates=(0,2,3,4)
        levels=[volume(t,3) for t in candidates]
        self.assertEqual(levels,[10,F(58,3),F(55,3),F(58,3)])
        self.assertEqual([t for t,v in zip(candidates,levels) if v==max(levels)],[2,4])
        self.assertEqual(F(after(2,3),2)+F(after(4,3),2),0)


if __name__=="__main__":
    unittest.main(verbosity=2)
