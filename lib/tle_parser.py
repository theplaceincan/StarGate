
# Checksum validation
# Both lines
def validate_checksum(line, checksum):
  res = 0

  for char in line[:68]:
    if char.isdigit():
      res = res + int(char)
    elif char == '-':
      res = res + 1

  s = str(res)
  end_chr = s[-1]

  if int(end_chr) == checksum:
    return True

  raise ValueError(f"Sum calculated: {res}, is not equal to checksum {checksum}.")

# Eccentricity value
# Must be between 0 and 1
def validate_eccentricity(eccentricity):
  if eccentricity >= 0 and eccentricity < 1:
    return True
  raise ValueError(f"Eccentricity out of range: {eccentricity}")

# Parse & return parsed TLE
def tle_parse(first_line, second_line):

  first_line = first_line.strip()
  second_line = second_line.strip()

  if len(first_line) != 69:
    raise ValueError(f"Line 1 has invalid length: {len(first_line)}")
  elif len(second_line) != 69:
    raise ValueError(f"Line 2 has invalid length: {len(second_line)}")

  validate_checksum(first_line, int(first_line[68]))
  validate_checksum(second_line, int(second_line[68]))

  line_1 = first_line[0] # Line number
  sat_num_1 = int(first_line[2:7]) # Satellite number
  classification = first_line[7] # Classification
  intl_last_launch_yr = first_line[9:11] # Intl. designator, last 2 digits of launch year
  intl_launch_num_yr = first_line[11:14] # Intl. designator, launch # of the year
  intl_piece = first_line[14:17].strip() # Intl. designator (piece of launch)
  epoch_year = int(first_line[18:20]) # Epoch year
  epoch_day = float(first_line[20:32]) # Epoch day
  first_time_dv = float(first_line[33:43]) # First Time Derivative of the Mean Motion
  second_time_dv_d_1 = float(int(first_line[44:50])/1e5) # Second Time Derivative of the Mean Motion (decimal point assumed)
  second_time_dv_d_ex = int(first_line[50:52])
  second_time_dv_d = second_time_dv_d_1* 10 ** second_time_dv_d_ex
  bstar_1 = float(int(first_line[53:59])/1e5) # B* (BSTAR) drag term
  bstar_ex = int(first_line[59:61])
  bstar = bstar_1* 10 ** bstar_ex
  ephemeris = int(first_line[62]) # Ephemeris type
  element_num = int(first_line[64:68]) # Element number
  checksum_1 = int(first_line[68]) # Checksum (mod 10) (Letters, blanks, periods, plus signs = 0; minus signs = 1)

  line_2 = int(second_line[0]) # Line number 
  sat_num_2 = int(second_line[2:7]) # Satellite number
  inclination_deg = float(second_line[8:16]) # inclination (degrees)
  raan = float(second_line[17:25]) # Right Ascension of the Ascending Node (degrees)
  eccentricity = float(int(second_line[26:33])/1e7) # Eccentricity
  arg_of_perigee = float(second_line[34:42]) # Argument of Perigee
  mean_anomaly = float(second_line[43:51]) # Mean Anomaly
  mean_motion_rev_per_day = float(second_line[52:63]) # Mean Motion
  rev_at_epoch = int(second_line[63:68]) # Revolution number at epoch
  checksum_2 = int(second_line[68]) # Checksum (mod 10) (Letters, blanks, periods, plus signs = 0; minus signs = 1)

  validate_eccentricity(eccentricity)
  
  if sat_num_1 != sat_num_2:
    raise ValueError(f"Incorrect satellite IDs. Line 1: {sat_num_1}, Line 2: {sat_num_2}")

  tle = {
      "line_1": line_1,
      "sat_num_1": sat_num_1,
      "classification": classification,
      "intl_last_launch_yr": intl_last_launch_yr,
      "intl_launch_num_yr": intl_launch_num_yr,
      "intl_piece": intl_piece,
      "epoch_year": epoch_year,
      "epoch_day": epoch_day,
      "first_time_dv": first_time_dv,
      "second_time_dv_d_1": second_time_dv_d_1,
      "second_time_dv_d_ex": second_time_dv_d_ex,
      "second_time_dv_d": second_time_dv_d,
      # "bstar_1": bstar_1,
      # "bstar_ex": bstar_ex,
      "bstar": bstar,
      "ephemeris": ephemeris,
      "element_num": element_num,
      "checksum_1": checksum_1,
      "line_2": line_2,
      "sat_num_2": sat_num_2,
      "inclination_deg": inclination_deg,
      "raan": raan,
      "eccentricity": eccentricity,
      "arg_of_perigee": arg_of_perigee,
      "mean_anomaly": mean_anomaly,
      "mean_motion_rev_per_day": mean_motion_rev_per_day,
      "rev_at_epoch": rev_at_epoch,
      "checksum_2": checksum_2
    }
  
  return tle

if __name__ == "__main__":

  # ISS (ZARYA)
  line_1 = "1 25544U 98067A   26302.56368278  .00005507  00000-0  10765-3 0  9997"
  line_2 = "2 25544  51.6333 355.1294 0007050 324.3141  35.7375 15.49100842592585"
  tle_parse(line_1, line_2)

  # METEOR-M2 3           
  line_1 = "1 57166U 23091A   26305.25001294 -.00000024  00000+0  82011-5 0  9992"
  line_2 = "2 57166  98.5918 357.3037 0004889 124.0054 236.1590 14.24055351174020"
  tle_parse(line_1, line_2)