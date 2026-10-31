# StarGate

StarGate is a satellite ground station, for now focused on being portable downlink station.

Downlink ground stations work like this:

1. Pass prediction
- This part is purely focused on predicting when the satellite will pass overhead. This is needed so it can rotate the antenna to recieve the downlink from the satellite, since satellites are fast and there's only a small window daily where we can be able to recieve anything from them,

In detail:

A pass is the window when the satellite is above you. There's a rising period, a max elevation, then a dropping period. Elevation is the angle above my horizon (ex. 90 degrees elevation is right above me). Azimuth is the compass direction.

To predict a pass, we need to know three things: 1) where the satellite is at a specific time, where am I at a specific time, and where is the satellite from where I'm at in space. Let `t` = time. To know where the satellite is at a specific `t`, we use the TLE and SGP4. The TLE and SGP4 gives us the satellite's position in space. To know where we are in space, we need to take into account the Earth's rotation and movement. To know the direction of where to point out antenna, we take the vector from us to the satellite and turn it into azimuth and elevation values.

These three questions are answered every 10 seconds or so. When we notice elevation going from negative to positive, we know that the satellite is approaching.

Another note:
Using the ISS as an example and Reno, we first know that we can see the ISS from ground at around 2,000km in any direction, so a 4,000km range total. We know the Earth takes 24hrs to turn 360 degrees, and an ISS pass takes around 90 minutes, so 90 * 360/1440 = 22.5 degrees elevation, meaning every time the ISS passes, the next time it goes around it would have moved 22.5 degrees to the West of us. From Reno, 1 degree of longtitude is around 86km, so 22.5 * 86 = 1935km. This tells us that every time the ISS passes above us, it has moved 1935km to the West. This basically means, given our 4k range (2k in any direction), we can see the ISS only 2-3 times pass above us. Passes come in clusters, with about 90 minutes between each cluster.

As a test, I'll use the ISS and predict that we will see it 3 times in a given orbit. Assuming that the ISS travels in a straight line, we are likely to see only 2 orbit, and maybe 3 but more faintly, however we could see it orbit 3-4 times since it passes at a slant heading NE or SE. 

TLDR: We are answering when it will pass, and to do that we need to know where we are, where the satellite is, and how to point to it. There's no simple formula to know when it will come

2. Antenna
- This part takes in the radio waves from the satellite and uses SDR to turn it into digital samples, which a computer records.

3. Decode
- This part first turns the radio waves into bits, then sets the bits into fields based on the satellite's specified format

4. Telemetry
- This part is where we can use the decoded data for whatever we need. This lets us montior the satellite's status or do other things.
