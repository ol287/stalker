import string
from itertools import product
from time import time


class BruteForce:
    def __init__(self, password, digit_lengths=[4, 6]):
        """
        Initialize the BruteForce object.

        Parameters
        ----------
        password : str
            The password to be brute-forced.
        digit_lengths : list
            List of digit lengths to consider for brute-forcing.
        """
        self.password = password
        self.digit_lengths = digit_lengths

    def _generate_combinations(self, length):
        """
        Generate all possible numeric combinations of a given length.

        Parameters
        ----------
        length : int
            The length of the numeric combinations to generate.

        Returns
        -------
        generator
            A generator yielding each possible numeric combination.
        """
        return product(string.digits, repeat=length)

    def _attempt_bruteforce(self, length):
        """
        Attempt to brute-force the password with a given digit length.

        Parameters
        ----------
        length : int
            The length of the numeric combinations to attempt.

        Returns
        -------
        str or None
            The brute-forced password if found, otherwise None.
        """
        print(f"\t..Trying {length}-digit combinations")
        generator = self._generate_combinations(length)
        for combination in generator:
            candidate = ''.join(combination)
            if candidate == self.password:
                print(f'\nPassword found: {candidate}')
                return candidate
        return None

    def run(self):
        """
        Run the brute-force algorithm over the specified digit lengths.

        Returns
        -------
        str or None
            The brute-forced password if found, otherwise None.
        """
        print('Starting brute-force attack...')
        for length in self.digit_lengths:
            result = self._attempt_bruteforce(length)
            if result:
                return result

        print('Password not found within the specified digit lengths.')
        return None


# EXAMPLE USAGE
if __name__ == "__main__":
    password_to_crack = '1234'  # Example: Try with '1234' or '123456' or any 4 or 6 digit combination
    brute_force = BruteForce(password_to_crack)

    start_time = time()
    brute_force.run()
    end_time = time()

    print('Total time: %.2f seconds' % (end_time - start_time))
