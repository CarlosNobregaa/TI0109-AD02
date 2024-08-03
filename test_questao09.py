import questao09 as q

# Automated tests
def test_questao09():
  # Test day periods
  assert q.approve_loan(1000, 299.99) == True
  assert q.approve_loan(1000, 300.01) == False
  assert q.approve_loan(100, 29.99) == True
  assert q.approve_loan(100, 30.01) == False
