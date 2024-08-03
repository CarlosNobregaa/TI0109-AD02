import questao02 as q
from math import sqrt

# Automated tests
def test_questao02():
  # Test volume and area functions
  assert q.volume(1) == sqrt(18)/36
  assert q.area(1) == sqrt(3)
  assert q.volume(0) == None
  assert q.area(0) == None
  assert q.volume(-1) == None
  assert q.area(-1) == None
