namespace CYDM.Utils;

using YoutubeDLSharp;

public static class PathResolver
{
    private static readonly DirectoryInfo BasePath = new(Directory.GetCurrentDirectory());
    public static string TopLevelPath => BasePath.Parent?.Parent?.Parent?.FullName ?? BasePath.FullName;

    public static string YoutubeDlpBinaryPath =>
        Path.Combine(DependencyResolver.DependencyDir, Utils.YtDlpBinaryName);

    public static string FfmpegBinaryPath =>
        Path.Combine(DependencyResolver.DependencyDir, Utils.FfmpegBinaryName);

    public static string DownloadPath =>
        Path.Combine(TopLevelPath, "cydm-downloads");

    public static string DownloadArchivePath =>
        Path.Combine(TopLevelPath, "completed-download-archive.log");
}