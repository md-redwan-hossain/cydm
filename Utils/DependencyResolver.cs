using CYDM.Views;

namespace CYDM.Utils;

public static class DependencyResolver
{
    public static readonly string DependencyDir = Path.Combine(PathResolver.TopLevelPath, "cydm-dependency");

    private static void CreateNonExistingDir()
    {
        if (!Path.Exists(DependencyDir))
            Directory.CreateDirectory(DependencyDir);
    }

    public static async Task Resolve()
    {
        DependencyResolveView.PrintBeforeResolveInfo();
        CreateNonExistingDir();
        await YoutubeDLSharp.Utils.DownloadBinaries(skipExisting: true, directoryPath: DependencyDir);
        DependencyResolveView.PrintAfterResolveInfo();
    }
}