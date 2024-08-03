import questao04 as q

# Automated tests
def test_questao04():
  # Test weights
  assert q.equiv_weight(100, 1) == 37
  assert q.equiv_weight(100, 2) == 88
  assert q.equiv_weight(100, 3) == 38
  assert q.equiv_weight(100, 4) == 264
  assert q.equiv_weight(100, 5) == 115
  assert q.equiv_weight(100, 6) == 117
