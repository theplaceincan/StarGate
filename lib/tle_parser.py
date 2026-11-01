
LINE_First = "1 25544U 98067A   26302.56368278  .00005507  00000-0  10765-3 0  9997"
LINE_Second = "2 25544  51.6333 355.1294 0007050 324.3141  35.7375 15.49100842592585"            

LENGTH = 69

print(len(LINE_First))
print(len(LINE_Second))

LINE_First_split = LINE_First.split()
LINE_Second_split = LINE_Second.split()

print(LINE_First_split)
print(LINE_Second_split)

line_1 = LINE_First[0] # Line number
sat_num_1 = int(LINE_First[2:7]) # Satellite number
classification = LINE_First[7] # Classification
intl_last_launch_yr = LINE_First[9:11] # Intl. designator, last 2 digits of launch year
intl_launch_num_yr = LINE_First[11:14] # Intl. designator, launch # of the year
intl_piece = LINE_First[14:17].strip() # Intl. designator (piece of launch)
epoch_year = int(LINE_First[18:20]) # Epoch year
epoch_day = float(LINE_First[20:32]) # Epoch day
first_time_dv = float(LINE_First[33:43]) # First Time Derivative of the Mean Motion
second_time_dv_d_1 = float(int(LINE_First[44:50])/1e5) # Second Time Derivative of the Mean Motion (decimal point assumed)
second_time_dv_d_ex = int(LINE_First[50:52])
second_time_dv_d = second_time_dv_d_1* 10 ** second_time_dv_d_ex
bstar_1 = float(int(LINE_First[53:59])/1e5) # B* (BSTAR) drag term
bstar_ex = int(LINE_First[59:61])
bstar = bstar_1* 10 ** bstar_ex
ephemris = int(LINE_First[62]) # Ephemeris type
element_num = int(LINE_First[64:68]) # Element number
checksum_1 = int(LINE_First[68]) # Checksum (mod 10) (Letters, blanks, periods, plus signs = 0; minus signs = 1)

line_2 = int(LINE_Second[0]) # Line number 
sat_num_2 = int(LINE_Second[2:7]) # Satellite number
inclination = float(LINE_Second[8:16]) # Inclination (degrees)
raan = float(LINE_Second[17:25]) # Right Ascension of the Ascending Node (degrees)
eccentricity = float(int(LINE_Second[26:33])/1e7) # Eccentricity
arg_of_perigee = float(LINE_Second[34:42]) # Argument of Perigee
mean_anomaly = float(LINE_Second[43:51]) # Mean Anomaly
mean_motion = float(LINE_Second[52:63]) # Mean Motion
rev_at_epoch = int(LINE_Second[63:68]) # Revolution number at epoch
checksum_2 = int(LINE_Second[68]) # Checksum (mod 10) (Letters, blanks, periods, plus signs = 0; minus signs = 1)

# Sanity check list
# 1. eccentricity must be between 0 and 1

if eccentricity < 0 or eccentricity >= 1:
  raise ValueError(f"eccentricity out of range: {eccentricity}")


# Checksum validation
# Both lines
def validate_checksum(line, checksum):
  sum = 0
  count = 0
  for char in line:
    if char.isdigit():
      sum = sum + int(char)
      count = count + 1
      if count+1 >= LENGTH:
        break

  if sum == checksum:
    return True

  return False

print(validate_checksum(LINE_First, checksum_1))
print(validate_checksum(LINE_Second, checksum_2))