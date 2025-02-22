using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Programming_project
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter your name:");
            string Fname = Console.ReadLine();

            bool residenceStudent = true;
            bool NotResidenceStudent = false;
            Console.WriteLine("Are you a Residence student?");
            bool residenceStudentOrNot = Convert.ToBoolean(Console.ReadLine());

            Console.WriteLine("How many years have you been at campus?");
            int YearsAtCampus = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("How many years have you been a residence?");
            int YearsAtCurrentResidence = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("What is your monthly allowance/salary?");
            decimal MonthlySalary = Convert.ToDecimal(Console.ReadLine());

            Console.WriteLine("what is your average mark across all subjects(%)?");
            double percentage = Convert.ToDouble(Console.ReadLine());
            Console.ReadLine();



        }
    }
}
