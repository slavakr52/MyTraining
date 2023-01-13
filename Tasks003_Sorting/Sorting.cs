
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
}


