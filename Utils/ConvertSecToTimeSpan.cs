namespace CYDM.Utils;

public static class ConvertSecToTimeSpan
{
    public static TimeSpan Convert(int seconds)
    {
        var minuteResult = Math.DivRem(seconds, 60, out var second);
        var hour = Math.DivRem(minuteResult, 60, out var minute);

        return new TimeSpan(hour, minute, second);
    }
}