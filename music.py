import musicpy as mp

# Create a melody.
melody = mp.Melody([
    mp.Note("C4"),
    mp.Note("D4"),
    mp.Note("E4"),
    mp.Note("F4"),
    mp.Note("G4"),
    mp.Note("A4"),
    mp.Note("B4"),
    mp.Note("C5")
])

# Create a chord progression.
chords = mp.ChordProgression([
    mp.Chord("C major"),
    mp.Chord("G major"),
    mp.Chord("F major"),
    mp.Chord("C major")
])

# Create a drum pattern.
drums = mp.DrumPattern([
    mp.Kick(),
    mp.Snare(),
    mp.HiHat()
])

# Create a synthesizer.
synth = mp.Synth()

# Play the melody, chords, and drums.
synth.play(melody, chords, drums)