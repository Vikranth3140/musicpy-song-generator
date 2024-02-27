import musicpy as mp

# Create a more interesting melody.
melody = mp.Melody([
    mp.Note("C4", duration=0.5),
    mp.Note("D4", duration=0.5),
    mp.Note("E4", duration=0.5),
    mp.Note("F4", duration=0.5),
    mp.Note("G4", duration=0.5),
    mp.Note("A4", duration=0.5),
    mp.Note("B4", duration=0.5),
    mp.Note("C5", duration=0.5)
])

# Create a richer chord progression.
chords = mp.ChordProgression([
    mp.Chord("C major", duration=2),
    mp.Chord("G major", duration=2),
    mp.Chord("F major", duration=2),
    mp.Chord("C major", duration=2)
])

# Add more complexity to the drum pattern.
drums = mp.DrumPattern([
    mp.Kick(),
    mp.Snare(),
    mp.HiHat(),
    mp.HiHat(open=True, position=2),
    mp.Snare(position=3),
    mp.Kick(position=4)
])

# Create a more dynamic synthesizer.
synth = mp.Synth(
    waveform="sawtooth",
    attack=0.1,
    decay=0.2,
    sustain=0.6,
    release=0.3
)

# Play the enhanced composition.
synth.play(melody, chords, drums)
