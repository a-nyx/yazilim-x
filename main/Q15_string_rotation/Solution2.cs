public class Solution2
{
  public static bool RotateString(string s1, string s2)
  {
    if (s1.Length != s2.Length) return false;
    if (s1 == "") return true;
    return (s1 + s1).Contains(s2);
  }
}
