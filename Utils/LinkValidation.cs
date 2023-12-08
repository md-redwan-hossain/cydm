using System.Text.RegularExpressions;

namespace CYDM.Utils;

public static class LinkValidation
{
    private static readonly Regex PlaylistUrlRegex = new(@"^.*(youtu.be\/|list=)([^#\&\?]*).*", RegexOptions.Compiled);

    private static readonly Regex VideoUrlRegex =
        new(
            @"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$",
            RegexOptions.Compiled);

    public static bool ValidateVideoUrl(string url) =>
        VideoUrlRegex.IsMatch(url);

    public static bool ValidatePlaylistUrl(string url) =>
        PlaylistUrlRegex.IsMatch(url);
}