
LINE_First = "1 25544U 98067A   26302.56368278  .00005507  00000-0  10765-3 0  9997"
LINE_Second = "2 25544  51.6333 355.1294 0007050 324.3141  35.7375 15.49100842592585"            

print(len(LINE_First))
print(len(LINE_Second))

LINE_First_split = LINE_First.split()
LINE_Second_split = LINE_Second.split()

print(LINE_First_split)
print(LINE_Second_split)

line_1 = LINE_First[0] # Line number
sat_num = LINE_First[2:7] # Satellite number
classification = LINE_First[7] # Classification
intl_last_launch_yr = LINE_First[9:11] # Intl. designator, last 2 digits of launch year
intl_launch_num_yr = LINE_First[11:14] # Intl. designator, launch # of the year
intl_piece = LINE_First[14:17] # Intl. designator (piece of launch)
epoch_year = LINE_First[18:20] # Epoch year
epoch_day = LINE_First[20:32] # Epoch day
first_time_dv = LINE_First[33:43] # First Time Derivative of the Mean Motion
second_time_dv_d = LINE_First[44:52] # Second Time Derivative of the Mean Motion (decimal point assumed)
bstar = LINE_First[53:61] # B* (BSTAR) drag term
ephemris = LINE_First[62] # Ephemeris type
element_num = LINE_First[64:68] # Element number
checksum = LINE_First[68] # Checksum (mod 10) (Letters, blanks, periods, plus signs = 0; minus signs = 1)

line_2 = LINE_Second[0] # Line number 
sat_num_2 = LINE_Second[2:7] # Satellite number
inclination = LINE_Second[8:16] # Inclination (degrees)
raan = LINE_Second[17:25] # Right Ascension of the Ascending Node (degrees)
eccentricity = LINE_Second[26:33] # Eccentricity
arg_of_perigee = LINE_Second[34:42] # Argument of Perigee
mean_anomaly = LINE_Second[43:51] # Mean Anomaly
mean_motion = LINE_Second[52:63] # Mean Motion
rev_at_epoch = LINE_Second[63:68] # Revolution number at epoch
checksum_2 = LINE_Second[68] # Checksum (mod 10) (Letters, blanks, periods, plus signs = 0; minus signs = 1)

print(float(eccentricity))
print(float(bstar))

# Sanity check list
# 1. eccentricity must be between 0 and 1