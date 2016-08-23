#include <stdio.h>
#include <new>
#include <math.h>

unsigned long long primeSum(unsigned long n);

int main() {
  unsigned long long sum = primeSum(2000000);
  printf("\n Sum of primes less than 2,000,000: %llu\n\n", sum);
  return -1;
}

/**
 *
 * primeSum(N): returns the sum of primes less than N
 *
 **/
unsigned long long primeSum(unsigned long n) {
  unsigned long long sum = 0;

  //
  //create bitmap and init with zeroes
  //
  unsigned long * map;
  map = new unsigned long[(n / 32) + 1];
  for(unsigned long i = 0; i < ((n / 32) + 1); i++)
    map[i] = 0x00000000;

  //
  // perform prime sieve, using sqrt(n)
  // as an upper bound
  //
  unsigned long mapIndex = 0;
  int offset = 0;
  for(unsigned long i = 2; i <= 1414; i++) {
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
  // at 1414, but loop begins at 1414 + 1
  //
  mapIndex = 44;
  offset = 5;
  for(unsigned long i = 1415; i < n; i++) {
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
