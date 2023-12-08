using Spectre.Console;

namespace CYDM.Views;

public static class SelectionView
{
    public static string TopLevelSelection() =>
        AnsiConsole.Prompt(new SelectionPrompt<string>()
            .Title("[green]Enter your choice:[/]")
            .PageSize(5)
            .MoreChoicesText("[grey](Move up and down to reveal more options)[/]")
            .AddChoices("Download Video", "Download Playlist", "Exit"));


    public static string YesNoSelection() =>
        AnsiConsole.Prompt(new SelectionPrompt<string>()
            .Title("[green]Enter your choice:[/]")
            .PageSize(5)
            .MoreChoicesText("[grey](Move up and down to reveal more options)[/]")
            .AddChoices("Yes", "No"));

    public static string YesNoSelection(string promptText) =>
        AnsiConsole.Prompt(new SelectionPrompt<string>()
            .Title($"[green]{promptText}[/]")
            .PageSize(5)
            .MoreChoicesText("[grey](Move up and down to reveal more options)[/]")
            .AddChoices("Yes", "No"));


    public static string GenericSelection(string promptText, IEnumerable<string> choices, byte pageSize = 5) =>
        AnsiConsole.Prompt(new SelectionPrompt<string>()
            .Title($"[green]{promptText}[/]")
            .PageSize(pageSize)
            .MoreChoicesText("[grey](Move up and down to reveal more options)[/]")
            .AddChoices(choices));
}