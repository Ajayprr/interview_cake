def json_ish(d):
  stringified = "{"
  count = 0
  for key, value in d.items():
    if type(value) == dict:
      value = json_ish(value)
    if count >= 1:
      stringified += ","
    stringified += key + ":" + value
    
    count += 1
  stringified += "}"
  return stringified

