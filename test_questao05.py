import questao05 as q

# Automated tests
def test_questao05():
  # Test palindromes
  assert q.is_palindrome(1) == True
  assert q.is_palindrome(22) == True
  assert q.is_palindrome(121) == True
  assert q.is_palindrome(3993) == True
  assert q.is_palindrome(12) == False
  assert q.is_palindrome(123) == False
  assert q.is_palindrome(1231) == False
  assert q.is_palindrome(0) == None
  assert q.is_palindrome(19991) == None
