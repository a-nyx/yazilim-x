namespace Q13_string_compression
{
  class Program
  {
    public static void Main(string[] args)
    {
      const string input = "abbccccccde";

      Solution2 solution = new Solution2();
      string compressed = solution.Compress();

      Console.WriteLine(compressed);
    }
  }
}
