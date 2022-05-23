public class Solution1
{
  public static int Compress(char[] chars)
  {
    if (chars.Length < 2)
    {
      return chars.Length;
    }

    char last = chars[0];
    int count = 0;
    int update_index = 0;

    for (int i = 0; i < chars.Length; i++)
    {
      if (chars[i] == last)
      {
        count++;
      }
      else
      {
        chars[update_index] = last;
        if (count > 1)
        {
          string count_str = count.ToString();
          for (int k = 0; k < count_str.Length; k++)
          {
            chars[update_index + 1 + k] = count_str[k];
          }
          update_index += count_str.Length + 1;
        }
        else
        {
          update_index++;
        }
        last = chars[i];
        count = 1;
      }
    }

    chars[update_index] = last;
    if (count > 1)
    {
      string final_count_str = count.ToString();
      for (int k = 0; k < final_count_str.Length; k++)
      {
        chars[update_index + 1 + k] = final_count_str[k];
      }
      update_index += final_count_str.Length + 1;
    }
    else
    {
      update_index++;
    }

    return update_index;
  }
}
