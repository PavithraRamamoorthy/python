def atm_mbar(pressure):
  return pressure * 1013.25
def mbar_mmhg(pressure):
  return pressure * 0.75006

pressure = 1.2 # in atmospheres
pressure = atm_mbar(pressure)
pressure = mbar_mmhg(pressure)
print(pressure)