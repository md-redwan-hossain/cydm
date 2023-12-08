using CYDM.Utils;
using YoutubeDLSharp;
using YoutubeDLSharp.Metadata;

namespace CYDM.Views;

public static class VideoView
{
    public static void PrintVideoInfo(VideoData data)
    {
        EnhancedConsole.WriteColoredLine("Title: ", ConsoleColor.Green, newLine: false);
        Console.WriteLine(data.Title);

        if (data.Duration != null)
        {
            EnhancedConsole.WriteColoredLine("Duration: ", ConsoleColor.Green, newLine: false);
            Console.WriteLine(ConvertSecToTimeSpan.Convert(Convert.ToInt32(data.Duration)));
        }

        EnhancedConsole.WriteColoredLine("Uploader: ", ConsoleColor.Green, newLine: false);
        Console.WriteLine(data.Uploader);

        if (!string.IsNullOrEmpty(data.Description))
        {
            var selection = SelectionView.YesNoSelection("Do you want to see the video description?");
            if (selection == "Yes")
            {
                EnhancedConsole.WriteColoredLine("Description: ", ConsoleColor.Green, newLine: false);
                Console.WriteLine(data.Description);
            }
        }
    }

    public static string ChooseVideoFormat(VideoData data)
    {
        var storage = new[]
        {
            "1080p", "720p", "480p", "360p"
        };

        return SelectionView.GenericSelection("Choose format:", storage, 5);
    }

    public static void PrintBeforeDownloadInfo(VideoData data)
    {
        EnhancedConsole.WriteEmptyLine();
        EnhancedConsole.WriteColoredLine("Downloading..", ConsoleColor.Yellow);
        Console.WriteLine(data.Title);
    }

    public static void PrintDownloadProgressInfo(ref DateTime time, DownloadProgress p)
    {
        if (p.Progress > 0)
        {
            if ((DateTime.Now - time).Milliseconds >= 500)
            {
                time = DateTime.Now;
                EnhancedConsole.ClearLine();
                Console.Write($"\r[progress] {p.Progress * 100:F2}% of {p.TotalDownloadSize} at {p.DownloadSpeed}");
            }
        }

        if (p.State == DownloadState.Success)
        {
            EnhancedConsole.ClearLine();
            EnhancedConsole.WriteColoredLine("\rDownload Complete", ConsoleColor.Yellow);
        }
    }

    public static string InputVideoLink()
    {
        while (true)
        {
            EnhancedConsole.WriteColoredLine("Enter the youtube video link: ", ConsoleColor.Cyan, newLine: false);
            var url = Console.ReadLine();
            if (!string.IsNullOrWhiteSpace(url))
            {
                var status = LinkValidation.ValidateVideoUrl(url);
                if (status) return url;
                EnhancedConsole.WriteColoredLine("Invalid Input", ConsoleColor.Red);
                var selection = SelectionView.YesNoSelection("Try Again?");
                if (selection == "Yes") continue;
            }

            break;
        }

        return string.Empty;
    }
}