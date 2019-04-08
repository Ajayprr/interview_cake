def recursive_search(lst, term):
  """hello, this is a doc string"""
  def helper(count):
    if count == len(lst):
      return None
    elif lst[count] == term:
      return count 
    return helper(count+1)
  return helper(0)
 