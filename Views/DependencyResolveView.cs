using CYDM.Utils;

namespace CYDM.Views;

public static class DependencyResolveView
{
    public static void PrintBeforeResolveInfo() =>
        EnhancedConsole.WriteColoredLine("\rResolving Dependency..", ConsoleColor.Yellow, newLine: false);


    public static void PrintAfterResolveInfo()
    {
        EnhancedConsole.WriteColoredLine("\rDependency Resolved..", ConsoleColor.Yellow, newLine: false);
        Console.Clear();
    }
}