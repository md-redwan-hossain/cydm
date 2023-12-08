using CYDM.Controllers;
using CYDM.Utils;
using CYDM.Views;


await DependencyResolver.Resolve();
var selection = SelectionView.TopLevelSelection();

switch (selection)
{
    case "Download Video":
        EnhancedConsole.WriteColoredLine("YouTube Video Downloader", ConsoleColor.Yellow);
        EnhancedConsole.WriteEmptyLine();

        var url = VideoView.InputVideoLink();
        if (!string.IsNullOrEmpty(url))
        {
            EnhancedConsole.WriteColoredLine("Processing...", ConsoleColor.Yellow);
            EnhancedConsole.WriteEmptyLine();

            var vid = new VideoDownloadController(url);
            await vid.ShowVideoInfo();
            await vid.Download();
        }

        break;

    case "Exit":
        EnhancedConsole.WriteColoredLine("Bye!", ConsoleColor.Yellow);
        EnhancedConsole.WriteEmptyLine();
        break;
}