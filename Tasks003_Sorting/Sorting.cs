
public static class Sorting
{

    public static int[] ChooseSortArray(int[] array) // Сортировка выбором
    {
        int temp;
        int count = 1;
        for (int i = 0; i < array.Length; i++)
        {
            for (int j = 0; j < array.Length; j++)
            {
                if (array[i] < array[j])
                {
                    temp = array[i];
                    array[i] = array[j];
                    array[j] = temp;
                }
            }
            Console.WriteLine($"Итерация {count}: [{String.Join(", ", array)}]");
            count++;
        }
        return array;
    }

    public static int[] BubbleSortArray(int[] array) // Пузырьковая сортировка
    {
        int temp;
        int count = 1;
        for (int i = 0; i < array.Length; i++)
        {
            for (int j = 0; j < array.Length - 1; j++)
            {
                if (array[j] > array[j + 1])
                {
                    temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
            Console.WriteLine($"Итерация {count}: [{String.Join(", ", array)}]");
            count++;
        }
        return array;
    }

    public static int[] SortQuick(int[] array, int left, int right)
    {
        int i = left;
        int j = right;

        int pivot = array[Random.Shared.Next(left, right)];
        while (i <= j)
        {
            while (array[i] < pivot) i++;
            while (array[j] > pivot) j--;

            if (i <= j)
            {
                int t = array[i];
                array[i] = array[j];
                array[j] = t;
                i++;
                j--;
            }
        }
        if (i < right) SortQuick(array, i, right);
        if (left < j) SortQuick(array, left, j);
        return array;
    }

    public static int[] SortCounting(int[] array)
    {
        int max = array.Max();
        int size = array.Length;

        int[] counter = new int[max + 1];

        for (int i = 0; i < size; i++) counter[array[i]]++;

        int index = 0;
        for (int i = 0; i < max + 1; i++)
        {
            for (int j = 0; j < counter[i]; j++)
            {
                array[index++] = i;
            }
        }
        return array;
    }
}



