fn letter_counts(s: &[u8]) -> HashMap<u8, u16> {
    let mut counts = HashMap::new();
    for &c in s {
        counts.entry(c).and_modify(|x| *x += 1).or_insert(1);
    }
    counts
}

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        letter_counts(s.as_bytes()) == letter_counts(t.as_bytes())
    }
}
