
public static class Infrastructure
{

    public static int[] CreateArray(int n)
    {
        int[] array = new int[n];
        for (int i = 0; i < n; i++)
        {
            array[i] = new Random().Next(0, 10);
        }
        return array;
    }
}