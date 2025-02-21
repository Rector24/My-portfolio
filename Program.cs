using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace project222222
{
    using System;
    using System.Collections.Generic;
    using System.Linq;

    public class Student
    {
        public string Name { get; set; }
        public bool IsResidenceStudent { get; set; }
        public int YearsOnCampus { get; set; }
        public int YearsAtCurrentResidence { get; set; }
        public decimal MonthlyAllowance { get; set; }
        public double AverageMark { get; set; }

        public bool QualifiesForDiscount()
        {
            return IsResidenceStudent && YearsOnCampus > 1 && AverageMark > 85 && MonthlyAllowance <= 1000;
        }
    }

    public enum Menu
    {
        CaptureDetails,
        CheckDiscountQualification,
        ShowQualificationStats,
        Exit
    }

    class Program
    {
        static List<Student> students = new List<Student>();
        static List<Student> qualifiedStudents = new List<Student>();

        static void Main(string[] args)
        {
            while (true)
            {
                Console.WriteLine("Choose an option:");
                Console.WriteLine("1. Capture Details");
                Console.WriteLine("2. Check discount qualification");
                Console.WriteLine("3. Show qualification stats");
                Console.WriteLine("4. Exit");

                Menu option = (Menu)Enum.Parse(typeof(Menu), Console.ReadLine());

                switch (option)
                {
                    case Menu.CaptureDetails:
                        CaptureDetails();
                        break;
                    case Menu.CheckDiscountQualification:
                        CheckDiscountQualification();
                        break;
                    case Menu.ShowQualificationStats:
                        ShowQualificationStats();
                        break;
                    case Menu.Exit:
                        Environment.Exit(0);
                        break;
                    default:
                        Console.WriteLine("Invalid option.");
                        break;
                }
            }
        }

        static void CaptureDetails()
        {
            while (true)
            {
                Student student = new Student();

                Console.Write("Enter student's full name: ");
                student.Name = Console.ReadLine();

                Console.Write("Is the student a residence student? (Y/N): ");
                string input = Console.ReadLine();
                student.IsResidenceStudent = input.ToLower() == "y";

                Console.Write("How many years has the student been on campus? ");
                student.YearsOnCampus = int.Parse(Console.ReadLine());

                if (student.IsResidenceStudent)
                {
                    Console.Write("How many years has the student been at the current residence? ");
                    student.YearsAtCurrentResidence = int.Parse(Console.ReadLine());
                }

                Console.Write("What is the student's monthly allowance/salary? ");
                student.MonthlyAllowance = decimal.Parse(Console.ReadLine());

                Console.Write("What is the student's average mark across all subjects? ");
                student.AverageMark = double.Parse(Console.ReadLine());

                students.Add(student);

                Console.Write("Do you want to capture more applicants? (Y/N): ");
                string captureMore = Console.ReadLine();
                if (captureMore.ToLower() == "n")
                {
                    break;
                }
            }
        }

        static void CheckDiscountQualification()
        {
            foreach (Student student in students)
            {
                if (student.QualifiesForDiscount())
                {
                    qualifiedStudents.Add(student);
                }
            }

            Console.WriteLine($"{qualifiedStudents.Count} students qualified for the discount.");
            Console.WriteLine($"{students.Count - qualifiedStudents.Count} students did not qualify for the discount.");
        }

        static void ShowQualificationStats()
        {
            var stats = qualifiedStudents.GroupBy(s => s.IsResidenceStudent)
                .Select(g => new { IsResidenceStudent = g.Key, Count = g.Count() })
                .ToList();

            Console.WriteLine("Qualification Stats:");
            Console.WriteLine($"Number of residence students who qualified: {stats.FirstOrDefault(s => s.IsResidenceStudent).Count}");
            Console.WriteLine($"Number of non-residence students who qualified: {stats.LastOrDefault(s => s.IsResidenceStudent).Count}");
        }
    }
}
