from sys import argv, exit
from csv import DictReader


def main():
    # Check for correct number of command-line arguments
    if len(argv) != 3:
        print("Usage: python dna.py DATABASE.CSV_File SEQ.TXT_File")
        exit(1)

    # List to store dictionaries containing DNA subsequences count data
    STRs_all_data = []

    # Read data from the DNA database file and store it in a list of dictionaries
    with open(argv[1]) as dna_database_file:
        reader = DictReader(dna_database_file)
        for STRs_data in reader:
            STRs_all_data.append(STRs_data)

    # Read the DNA sequence file
    with open(argv[2]) as dna_seq_file:
        dna_seq = dna_seq_file.read()

    # List to store DNA subsequences data collected from the DNA sequence
    STRs_current_seq = []

    # Extract DNA sequence data and store it in STRs_current_seq list
    for key, value in STRs_all_data[0].items():
        if key == "name":
            continue
        else:
            STRs_current_seq.append(str(longest_match(dna_seq, key)))

    # Compare the extracted DNA sequence data with the DNA database, print if match
    for STRs_subseq in STRs_all_data:
        current_subseq = list(STRs_subseq.values())[1:]

        # Check for a match between the current subsequence and the extracted DNA sequence data
        if current_subseq == STRs_current_seq:
            print(STRs_subseq["name"])
            exit(0)

    # If no match is found
    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in the sequence for the longest consecutive runs of the subsequence
    for i in range(sequence_length):
        count = 0  # Initialize count of consecutive runs

        # Check for a subsequence match in a substring within the sequence
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break  # If no match in the substring

        # Update the longest consecutive matches found
        longest_run = max(longest_run, count)

    # Return the length of the longest run
    return longest_run


main()
