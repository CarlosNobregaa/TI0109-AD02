import questao03 as q

# Automated tests
def test_questao03():
  # Test health insurance values
  assert q.health_insurance_price(-1) == None
  for age in range(0, 11):
    assert q.health_insurance_price(age) == 30
  for age in range(11, 30):
    assert q.health_insurance_price(age) == 60
  for age in range(30, 46):
    assert q.health_insurance_price(age) == 120
  for age in range(46, 60):
    assert q.health_insurance_price(age) == 150
  for age in range(60, 66):
    assert q.health_insurance_price(age) == 250
  for age in range(66, 101):
    assert q.health_insurance_price(age) == 400
