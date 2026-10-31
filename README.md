# StarGate

StarGate is a satellite ground station, for now focused on being portable downlink station.

Downlink ground stations work like this:

1. Pass prediction
- This part is purely focused on predicting when the satellite will pass overhead. This is needed so it can rotate the antenna to recieve the downlink from the satellite, since satellites are fast and there's only a small window daily where we can be able to recieve anything from them,

2. Antenna
- This part takes in the radio waves from the satellite and uses SDR to turn it into digital samples, which a computer records.

3. Decode
- This part first turns the radio waves into bits, then sets the bits into fields based on the satellite's specified format

4. Telemetry
- This part is where we can use the decoded data for whatever we need. This lets us montior the satellite's status or do other things.
