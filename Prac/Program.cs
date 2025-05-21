// See https://aka.ms/new-console-template for more information

class Program
{
    static void Main()
    {
        Console.WriteLine("Input the string: ");
        string? input = Console.ReadLine();

        if (string.IsNullOrEmpty(input))
        {
            Console.WriteLine("No input provided.");
            return;
        }

        Dictionary<char, int> charFrequency = new Dictionary<char, int>();

        foreach (char c in input)
        {
            if (charFrequency.ContainsKey(c))
            {
                charFrequency[c]++;
            }
            else
            {
                charFrequency.Add(c, 1);
            }
        }

        // Display results
        Console.WriteLine("The frequency of the characters are:");
        foreach (var pair in charFrequency)
        {
            Console.WriteLine($"Character {pair.Key}: {pair.Value} times");
        }
    }
}
