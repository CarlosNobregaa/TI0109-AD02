import questao01 as q
from math import pi, sqrt

# Automated tests
def test_questao01():
  # Test volume and area functions
  assert q.volume(1, 1) == pi/3
  assert q.area(1, 1) == pi*(1+sqrt(2))
  assert q.volume(0, 1) == None
  assert q.area(0, 1) == None
  assert q.volume(1, 0) == None
  assert q.area(1, 0) == None
  assert q.volume(-1, 1) == None
  assert q.area(-1, 1) == None
  assert q.volume(1, -1) == None
  assert q.area(1, -1) == None
