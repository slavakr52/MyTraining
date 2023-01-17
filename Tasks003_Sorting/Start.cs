using static Infrastructure;
using static Sorting;


Console.WriteLine("Введите размер массива:");
int n = int.Parse(Console.ReadLine()!);
int[] array = CreateArray(n);
Console.WriteLine($"Исходный массив: [{String.Join(", ", array)}]");
Console.WriteLine();
Console.WriteLine("Выберите вид сортировки:");
Console.WriteLine("1. Сортировка выбором");
Console.WriteLine("2. Пузырьковая сортировка");
Console.WriteLine("3. Быстрая сортировка");
int sortNum = int.Parse(Console.ReadLine()!);

if (sortNum != 1 && sortNum != 2 && sortNum != 3) Console.WriteLine("Такой сортировки не указано");
else
{
    if (sortNum == 1) ChooseSortArray(array);
    if (sortNum == 2) BubbleSortArray(array);
    if (sortNum == 3) {SortQuick(array, 0, array.Length - 1); Console.WriteLine($"Отсортированный массив: [{String.Join(", ", array)}]");}
}
