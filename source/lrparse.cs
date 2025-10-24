static List<string> LR(string s, string left, string right, bool recursive)
{
    var output = new List<string>();

    try
    {
        if (s == null || left == null || right == null) return output;

        if (left.Length == 0 && right.Length == 0)
        {
            output.Add(s);
            return output;
        }

        if ((left.Length > 0 && s.IndexOf(left, StringComparison.Ordinal) < 0) ||
            (right.Length > 0 && s.IndexOf(right, StringComparison.Ordinal) < 0))
        {
            return output;
        }

        if (!recursive)
        {
            int startindex = (left.Length == 0) ? 0 : s.IndexOf(left, StringComparison.Ordinal);
                if (startindex < 0) return output;

                int from = startindex + left.Length;

                int endindex = (right.Length == 0) ? s.Length : s.IndexOf(right, from, StringComparison.Ordinal);
                if (endindex < 0) return output;

                output.Add(s.Substring(from, endindex - from));
                return output;
            
            
        }
        else
        {
            int pos = 0;
            while (pos < s.Length)
            {
                int startindex = (left.Length == 0) ? pos : s.IndexOf(left, pos, StringComparison.Ordinal);
                if (startindex < 0) break;

                int from = startindex + left.Length;

                int endindex = (right.Length == 0) ? s.Length : s.IndexOf(right, from, StringComparison.Ordinal);
                if (endindex < 0) break;

                output.Add(s.Substring(from, endindex - from));
                
                if (right.Length == 0) break; // avoid infinite loop
                pos = endindex + right.Length;
            }

            return output;
        }
    }
    catch (Exception)
    {
        return output;
    }
}






