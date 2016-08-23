#include <stdio.h>
#include <new>
#include <math.h>

// returns the sum of primes less than N
unsigned long long primeSum(unsigned long n);

int main(int argc, char *argv[]) {
  if(argc != 2) {
    printf("\n Usage: primeSum <N>\n\n Calculates the sum of primes less than an integer N.\n\n");
    return 0;
  }
  
  unsigned long n = atoi(argv[1]);
  if(n == 0) {
    printf("\n N must be greater than 0.\n\n");
    return 0;
  }
  
  unsigned long long sum = primeSum(n);
  printf("\n Sum of primes less than %lu: %llu\n\n", n, sum);
  return -1;
}

/**
 *
 * getZeroBitmap(N): returns a zeroed bitmap of size N
 *
 **/
unsigned long * getBitmap(unsigned long n) {
  // create a bitmap with N bits
  unsigned long * intMap;
  intMap = new unsigned long[(n / 32) + 1];
  
  //initialize bitmap with zeroes
  for(unsigned long i = 0; i < ((n / 32) + 1); i++)
    intMap[i] = 0x00000000;

  return intMap;
}

/**
 *
 * primeSum(N): returns the sum of primes less than N
 *
 **/
unsigned long long primeSum(unsigned long n) {
  unsigned long long sum = 0;
  unsigned long * map = getBitmap(n);

  //
  // perform prime sieve, using square root of N
  // as an upper bound
  //
  unsigned long floorSqrtN = (int)sqrt(n);
  unsigned long mapIndex = 0;
  int offset = 0;
  for(unsigned long i = 2; i <= floorSqrtN; i++) {
    mapIndex = (i - 1) / 32;
    offset = (i - 1) % 32;

    //if the nth bit is 0, it is prime; accumulate into sum and mark
    // its multiples as non-prime (else do nothing)
    if((map[mapIndex] & (0x00000001 << offset)) == 0) {
      sum += i;
      unsigned long multiple = i * i;
      while(multiple < n) {
        mapIndex = (multiple - 1) / 32;
        offset = (multiple - 1) % 32;
        map[mapIndex] |= (0x00000001 << offset);
        multiple = multiple + i;
      }
    }
  }

  //
  // sum the remaining primes greater than sqrt(n)
  //
  // note that mapIndex and offset are initialized
  // at floorSqrtN, but loop begins at floorSqrtN + 1
  //
  mapIndex = (floorSqrtN - 1) / 32;
  offset = (floorSqrtN - 1) % 32;
  for(unsigned long i = floorSqrtN + 1; i < n; i++) {
    //increment offset and mapIndex appropriately
    offset++;
    if(offset > 31) {
      offset = 0;
      mapIndex++;
    }

    //if bit at current location is 0, it is prime; accumulate it
    if((map[mapIndex] & (0x00000001 << offset)) == 0)
      sum += i;
  }
  return sum;
}
