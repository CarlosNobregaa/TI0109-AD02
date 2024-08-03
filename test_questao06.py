import questao06 as q

# Automated tests
def test_questao06():
  # Test valid dates
  assert q.is_valid_date(29, 2, 2020) == True
  assert q.is_valid_date(1, 1, 2023) == True
  assert q.is_valid_date(31, 12, 2023) == True
  assert q.is_valid_date(22, 4, 1500) == True
  assert q.is_valid_date(7, 9, 1822) == True
  assert q.is_valid_date(13, 5, 1888) == True
  assert q.is_valid_date(15, 11, 1889) == True
  assert q.is_valid_date(-1, 2, 2002) == False
  assert q.is_valid_date(1, -2, 2002) == False
  assert q.is_valid_date(1, 2, -2002) == False
  assert q.is_valid_date(30, 2, 2002) == False
  assert q.is_valid_date(31, 4, 1999) == False
