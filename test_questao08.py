import questao08 as q

# Automated tests
def test_questao08():
  # Test day periods
  assert round(q.pmt(1000, 0.01, 12, 1), 4) == 88.8488
  assert round(q.balance(q.pmt(1000, 0.01, 12, 1), 0.01, 12, 1, 6), 4) == 514.9211
