using static Infrastructure;
using static Sorting;



Console.WriteLine("Введите размер массива:");
Console.Write("> ");
int n = int.Parse(Console.ReadLine()!);
int[] array = CreateArray(n);
Console.WriteLine($"Исходный массив: [{String.Join(", ", array)}]");
Annotation();
int sortNum = int.Parse(Console.ReadLine()!);

if (sortNum != 1 && sortNum != 2 && sortNum != 3 && sortNum != 4) Console.WriteLine("Такой сортировки не указано");
else
{
    if (sortNum == 1) ChooseSortArray(array);
    if (sortNum == 2) BubbleSortArray(array);
    if (sortNum == 3) { SortQuick(array, 0, array.Length - 1); Console.WriteLine($"Отсортированный массив: [{String.Join(", ", array)}]"); }
    if (sortNum == 4) { SortCounting(array); Console.WriteLine($"Отсортированный массив: [{String.Join(", ", array)}]"); }
}
