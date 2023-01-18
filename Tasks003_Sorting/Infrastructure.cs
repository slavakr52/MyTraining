
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

    public static void Annotation()
    {
        Console.WriteLine();
        Console.WriteLine("Выберите вид сортировки:");
        Console.WriteLine("1. Сортировка выбором");
        Console.WriteLine("2. Пузырьковая сортировка");
        Console.WriteLine("3. Быстрая сортировка");
        Console.WriteLine("4. Сортировка подсчётом");
        Console.Write("> ");
    }

    
}