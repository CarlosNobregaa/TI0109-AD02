import questao10 as q

# Automated tests
def test_questao10():
  # Test day periods
  assert q.credit(-1) == None
  assert q.credit(0) == 0
  assert q.credit(250) == 0
  assert q.credit(500) == 0
  assert q.credit(501) == 0.3*501
  assert q.credit(750) == 0.3*750
  assert q.credit(1000) == 0.3*1000
  assert q.credit(1001) == 0.4*1001
  assert q.credit(2000) == 0.4*2000
  assert q.credit(3000) == 0.4*3000
  assert q.credit(3001) == 0.5*3001
