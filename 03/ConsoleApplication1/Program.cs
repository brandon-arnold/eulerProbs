using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            UInt64 bigNum = 600851475143,
                   maxRange = bigNum / 3,
                   counterPercent = maxRange / 100,
                   counter = 1;
            for (UInt64 divisor = maxRange; divisor > 3; divisor--)
            {
                if(counter % counterPercent == 0) 
                    Console.WriteLine(String.Format("{0:0.0}%. . .", (double)counterPercent / (double)maxRange));
                if(bigNum % divisor == 0)
                {
                    Console.WriteLine("Factor found; testing " + divisor.ToString());
                    if(IsPrime(divisor))
                        Console.WriteLine(divisor.ToString() + " is prime!");
                }
                counter++;
            }
        }

        private static bool IsPrime(ulong number)
        {
            ulong maxDivisor = (ulong)Math.Sqrt((double)number);
            if (number % 2 == 0 || number % 3 == 0)
            {
                Console.WriteLine(number.ToString() + " is not prime; divisible by 2 or 3.");
                return false;
            }
            for (ulong k = 1; k <= maxDivisor / 6; k++)
            {
                if (number % (6 * k - 1) == 0 ||
                    number % (6 * k + 1) == 0)
                {
                    Console.WriteLine(number.ToString() + " is not prime; divisible by " + (6 * k - 1).ToString() + " or "+ (6 * k + 1).ToString() + ".");
                    return false;
                }
            }
            return true;
        }
    }
}
