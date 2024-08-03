import questao07 as q

# Automated tests
def test_questao07():
  # Test day periods
  assert q.day_period(-1, 0, 0) == None
  assert q.day_period(0, -1, 0) == None
  assert q.day_period(0, 0, -1) == None
  assert q.day_period(24, 0, 0) == None
  assert q.day_period(0, 60, 0) == None
  assert q.day_period(0, 0, 60) == None
  assert q.day_period(0, 0, 0) == 0
  assert q.day_period(5, 59, 59) == 0
  assert q.day_period(6, 0, 0) == 1
  assert q.day_period(11, 59, 59) == 1
  assert q.day_period(11, 0, 0) == 2
  assert q.day_period(17, 59, 59) == 2
  assert q.day_period(17, 0, 0) == 3
  assert q.day_period(23, 59, 59) == 3
