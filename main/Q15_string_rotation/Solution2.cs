public class Solution2
{
  public static bool RotateString(string s1, string s2)
  {
    if (s1.Length != s2.Length) return false;
    if (s1 == "") return true;
    return (s1 + s1).Contains(s2);
  }

  public static bool RotateString2(string s1, string s2)
  {
    if (s1.Length != s2.Length) return false;
    if (s1 == "") return true;

    string s1s1 = s1 + s1;

    for (int i = 0; i <= s1.Length; i++)
    {
      int k = 0;
      for (; k < s1.Length; k++)
      {
        if (s1[(i + k) % s1.Length] != s2[k]) break;
      }

      if (k == s1.Length) return true;
    }

    return false;
  }
}
