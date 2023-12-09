using CYDM.Utils;
using CYDM.Views;
using YoutubeDLSharp;
using YoutubeDLSharp.Metadata;
using YoutubeDLSharp.Options;

namespace CYDM.Controllers;

public class VideoDownloadController
{
    private readonly string _url;
    private readonly YoutubeDL _youtubeDl;
    private readonly OptionSet _youtubeDlOptionSet;
    private RunResult<VideoData>? _runResult;

    public VideoDownloadController(string url)
    {
        _url = url;

        _youtubeDl = new YoutubeDL
        {
            YoutubeDLPath = PathResolver.YoutubeDlpBinaryPath,
            FFmpegPath = PathResolver.FfmpegBinaryPath,
            OutputFolder = PathResolver.DownloadPath,
            RestrictFilenames = true
        };

        _youtubeDlOptionSet = new OptionSet
        {
            NoContinue = false,
            NoPlaylist = true,
            Quiet = false,
            NoWarnings = true,
            WindowsFilenames = true,
            Format = "best",
            // DownloadArchive = PathResolver.DownloadArchivePath,
        };
    }

    private async Task InitiateVideoInfo()
    {
        _runResult ??= await _youtubeDl.RunVideoDataFetch(_url);
    }

    public async Task ShowVideoInfo()
    {
        await InitiateVideoInfo();
        VideoView.PrintVideoInfo(_runResult!.Data);
        // VideoView.ChooseVideoFormat(_runResult.Data);
    }


    public async Task Download()
    {
        
        var lastUpdateTime = DateTime.Now;
        var progress = new Progress<DownloadProgress>(p => VideoView.PrintDownloadProgressInfo(ref lastUpdateTime, p));
        var cts = new CancellationTokenSource();

        await InitiateVideoInfo();
        VideoView.PrintBeforeDownloadInfo(_runResult!.Data);
        await _youtubeDl.RunVideoDownload(_url, mergeFormat: DownloadMergeFormat.Mp4,
            overrideOptions: _youtubeDlOptionSet, progress: progress,
            ct: cts.Token);
    }
};