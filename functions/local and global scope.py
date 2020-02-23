def normal_pressure(pressure):
  result = pressure-pressure_at_sea_level
  return result
pressure_at_sea_level = 7
print(normal_pressure(16))